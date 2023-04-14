import redis from "redis";
import { promisify } from "util";
import express from "express";

const client = redis.createClient();
const get = promisify(client.get).bind(client);
const set = promisify(client.set).bind(client);
const app = express();

const listProducts = [
	{
		id: 1,
		name: "Suitcase 250",
		price: 50,
		stock: 4,
	},
	{
		id: 2,
		name: "Suitcase 450",
		price: 100,
		stock: 10,
	},
	{
		id: 3,
		name: "Suitcase 650",
		price: 350,
		stock: 0,
	},
	{
		id: 4,
		name: "Suitcase 1050",
		price: 550,
		stock: 2,
	},
];
const getItemById = (id) => {
	for (let idx = 0; idx < listProducts.length; idx++) {
		if (listProducts[idx].id === id) return listProducts[idx];
	}
};
const reserveStockById = async (itemId, stock) => await set(itemId, stock);
const getCurrentReservedStockById = async (itemId) => await get(itemId);

app.get("/list_products", (req, res) => res.send(JSON.stringify(listProducts)));

app.get("/list_products/:itemId", async (req, res) => {
	const id = parseInt(req.params.itemId);
	const item = getItemById(id);
	const reservedStock = parseInt(await getCurrentReservedStockById(id));

	if (!item) return res.status(404).json({ status: "Product not found" });
	item.currentQuantity = !isNaN(reservedStock) ? reservedStock : 0;
	res.json(item);
});

app.get("/reserve_product/:itemId", async (req, res) => {
	const id = parseInt(req.params.itemId);
	const item = getItemById(id);
	if (!item) return res.status(403).json({ status: "Product not found" });

	const reservedStock = parseInt(await getCurrentReservedStockById(id));
	item.currentQuantity = !isNaN(reservedStock) ? reservedStock : 0;
	if (item.stock - item.currentQuantity < 1) {
		res.status(403).json({ status: "Not enough stock available", id });
		return;
	}
	await reserveStockById(id, item.currentQuantity + 1);
	res.json({ status: "Reservation confirmed", id });
});

app.listen(1245);
