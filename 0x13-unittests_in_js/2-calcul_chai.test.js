const chai = require("chai");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", () => {
	it("test", () => {
		chai.expect(calculateNumber("SUM", 2, 2)).to.equal(4);
		chai.expect(calculateNumber("SUM", 1, 5.5)).to.equal(7);
		chai.expect(calculateNumber("SUM", 1.5, 2.5)).to.equal(5);
		chai.expect(calculateNumber("SUM", 1.5, 2)).to.equal(4);
		chai.expect(calculateNumber("SUM", -2, -2)).to.equal(-4);
		chai.expect(calculateNumber("SUM", -1, -5.5)).to.equal(-6);
		chai.expect(calculateNumber("SUBTRACT", 2, 2)).to.equal(0);
		chai.expect(calculateNumber("SUBTRACT", 1, 5.5)).to.equal(-5);
		chai.expect(calculateNumber("SUBTRACT", 1.5, 2.5)).to.equal(-1);
		chai.expect(calculateNumber("SUBTRACT", 1.5, 2)).to.equal(0);
		chai.expect(calculateNumber("SUBTRACT", -2, -2)).to.equal(0);
		chai.expect(calculateNumber("SUBTRACT", -1, -5.5)).to.equal(4);
		chai.expect(calculateNumber("DIVIDE", 6.2, 2)).to.equal(3);
		chai.expect(calculateNumber("DIVIDE", 10, 2)).to.equal(5);
		chai.expect(calculateNumber("DIVIDE", 10, 0)).to.equal("Error");
	});
});
