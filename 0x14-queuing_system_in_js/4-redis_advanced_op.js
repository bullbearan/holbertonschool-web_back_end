import { createClient } from "redis";
import redis from "redis";
const client = createClient();
client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (error) =>
	console.log(`Redis client not connected to the server: ${error.message}`),
);
const values = {
	Portland: 50,
	Seattle: 80,
	"New York": 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};
for (const value in values) client.hset("HolbertonSchools", value, values[value], redis.print);
client.hgetall("HolbertonSchools", (err, value) => console.log(value));
