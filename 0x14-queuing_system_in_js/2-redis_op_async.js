import { createClient } from "redis";
import redis from "redis";
const { promisify } = require("util");

const client = createClient();
const change = promisify(client.get).bind(client);
client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (error) =>
	console.log(`Redis client not connected to the server: ${error.message}`),
);
const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
	console.log(await change(schoolName));
};

const a = async () => {
	await displaySchoolValue("Holberton");
	setNewSchool("HolbertonSanFrancisco", "100");
	await displaySchoolValue("HolbertonSanFrancisco");
};
a();
