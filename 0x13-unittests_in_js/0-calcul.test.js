const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
	it("test1", () => {
		assert.strictEqual(calculateNumber(2, 2), 4);
		assert.strictEqual(calculateNumber(1, 5.5), 7);
		assert.strictEqual(calculateNumber(1.5, 2.5), 5);
		assert.strictEqual(calculateNumber(1.5, 2), 4);
		assert.strictEqual(calculateNumber(-2, -2), -4);
		assert.strictEqual(calculateNumber(-1, -5.5), -6);
	});
	it("test2", () => {
		assert.strictEqual(calculateNumber(2, 2), 4);
		assert.strictEqual(calculateNumber(1, 5.5), 7);
		assert.strictEqual(calculateNumber(1.5, 2.5), 5);
		assert.strictEqual(calculateNumber(1.5, 2), 4);
		assert.strictEqual(calculateNumber(-2, -2), -4);
		assert.strictEqual(calculateNumber(-1, -5.5), -6);
	});
});
