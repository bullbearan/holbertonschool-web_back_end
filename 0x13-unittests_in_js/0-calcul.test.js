const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
	it("test", () => {
		assert.strictEqual(calculateNumber(2, 2), 4);
		assert.strictEqual(calculateNumber(1, 5.5), 7);
		assert.strictEqual(calculateNumber(1.5, 2.5), 5);
		assert.strictEqual(calculateNumber(1.5, 2), 4);
		assert.strictEqual(calculateNumber(-2, -2), -4);
		assert.strictEqual(calculateNumber(-1, -5.5), -6);
		assert.strictEqual(isNaN(calculateNumber("one", 1)), true);
		assert.strictEqual(isNaN(calculateNumber(2, "two")), true);
		assert.strictEqual(isNaN(calculateNumber(5.5)), true);
		assert.strictEqual(isNaN(calculateNumber()), true);
	});
});
