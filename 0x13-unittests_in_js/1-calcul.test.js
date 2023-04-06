const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", () => {
	it("test", () => {
		assert.strictEqual(calculateNumber("SUM", 2, 2), 4);
		assert.strictEqual(calculateNumber("SUM", 1, 5.5), 7);
		assert.strictEqual(calculateNumber("SUM", 1.5, 2.5), 5);
		assert.strictEqual(calculateNumber("SUM", 1.5, 2), 4);
		assert.strictEqual(calculateNumber("SUM", -2, -2), -4);
		assert.strictEqual(calculateNumber("SUM", -1, -5.5), -6);
		assert.strictEqual(calculateNumber("SUBTRACT", 2, 2), 0);
		assert.strictEqual(calculateNumber("SUBTRACT", 1, 5.5), -5);
		assert.strictEqual(calculateNumber("SUBTRACT", 1.5, 2.5), -1);
		assert.strictEqual(calculateNumber("SUBTRACT", 1.5, 2), 0);
		assert.strictEqual(calculateNumber("SUBTRACT", -2, -2), 0);
		assert.strictEqual(calculateNumber("SUBTRACT", -1, -5.5), 4);
		assert.strictEqual(calculateNumber("DIVIDE", 6.2, 2), 3);
		assert.strictEqual(calculateNumber("DIVIDE", 10, 2), 5);
		assert.strictEqual(calculateNumber("DIVIDE", 10, 0), "Error");
	});
});
