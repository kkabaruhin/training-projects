const assert = require("assert")
const { calculator } = require("../calculator");

describe("calculation tests with only +-*/^", function() {
    it("should successfully calc the expression 1", function() {
        let result = calculator("123");
        assert.equal(result, 123);
    })
    it("should successfully calc the expression 1.5", function () {
        let result = calculator("-+2");
        assert.equal(result, -2);
    })
    it("should successfully calc the expression 1.75", function () {
        let result = calculator("-+2");
        assert.equal(result, -2);
    })
    it("should successfully calc the expression 1.875", function () {
        let result = calculator("-+2+1");
        assert.equal(result, -1);
    })
    it("should successfully calc the expression 1.9", function () {
        let result = calculator("-1+2");
        assert.equal(result, 1);
    })
    it("should successfully calc the expression 2", function () {
        let result = calculator("2+3");
        assert.equal(result, 5);
    })
    it("should successfully calc the expression 3", function () {
        let result = calculator("3-2");
        assert.equal(result, 1);
    })
    it("should successfully calc the expression 4", function () {
        let result = calculator("41 * 10");
        assert.equal(result, 410);
    })
    it("should successfully calc the expression 5", function () {
        let result = calculator("57/3");
        assert.equal(result, 19);
    })
    it("should successfully calc the expression 6", function () {
        let result = calculator("1000//3");
        assert.equal(result, 333);
    })
    it("should successfully calc the expression 7", function () {
        let result = calculator("1+5-20");
        assert.equal(result, -14);
    })
    it("should successfully calc the expression 8", function () {
        let result = calculator("2+2*2");
        assert.equal(result, 6);
    })
    it("should successfully calc the expression 9", function () {
        let result = calculator(" -+2 +- 20");
        assert.equal(result, -22);
    })
    it("should successfully calc the expression 10", function () {
        let result = calculator("10*5-10");
        assert.equal(result, 40);
    })
    it("should successfully calc the expression 11", function () {
        let result = calculator(" 11 // 4 * 4 + 18-2*7");
        assert.equal(result, 12);
    })
    it("should successfully calc the expression 12", function () {
        let result = calculator(" 12 / 6 + 120/10");
        assert.equal(result, 14);
    })
    it("should successfully calc the expression 13", function () {
        let result = calculator(" 13 * -10");
        assert.equal(result, -130);
    })
    it("should successfully calc the expression 14", function () {
        let result = calculator(" 2^3");
        assert.equal(result, 8);
    })
    it("should successfully calc the expression 15", function () {
        let result = calculator(" 15^2-10");
        assert.equal(result, 215);
    })
    it("should successfully calc the expression 16", function () {
        let result = calculator(" 1-6^3*2");
        assert.equal(result, -431);
    })
    it("should successfully calc the expression 17", function () {
        let result = calculator("7+10*2^5/5*3");
        assert.equal(result, 199);
    })
    it("should successfully calc the expression 18", function () {
        let result = calculator("8^5/8^4*8^6");
        assert.equal(result, 2097152);
    })
    it("should successfully calc the expression 19", function () {
        let result = calculator("4^0.5");
        assert.equal(result, 2);
    })
    it("should successfully calc the expression 20", function () {
        let result = calculator("4^0.5 + 27^(1/3)");
        assert.equal(result, 5);
    })
})

describe("calculation tests ()", function () {
    it("should successfully calc the () expression 1", function () {
        let result = calculator("(1)");
        assert.equal(result, 1);
    })
    it("should successfully calc the () expression 2", function () {
        let result = calculator("(2+3)");
        assert.equal(result, 5);
    })
    it("should successfully calc the () expression 3", function () {
        let result = calculator("3+(2)");
        assert.equal(result, 5);
    })
    it("should successfully calc the () expression 4", function () {
        let result = calculator("(2)*2");
        assert.equal(result, 4);
    })
    it("should successfully calc the () expression 5", function () {
        let result = calculator("(2+2)*2");
        assert.equal(result, 8);
    })
    it("should successfully calc the () expression 6", function () {
        let result = calculator("(6*4+1) - (20//7-2*3)");
        assert.equal(result, 29);
    })
    it("should successfully calc the () expression 7", function () {
        let result = calculator("77*(1+1) - 36/(18-(3*(3-1) + 2))");
        assert.equal(result, 150.4);
    })
    it("should successfully calc the () expression 8", function () {
        let result = calculator("18+(-10)");
        assert.equal(result, 8);
    })
})

describe("calculation functions tests", function () {
    it("should successfully calc the func expression 1", function () {
        let result = calculator("abs(1)");
        assert.equal(result, 1);
    })
    it("should successfully calc the func expression 2", function () {
        let result = calculator("abs(-21)");
        assert.equal(result, 21);
    })
    it("should successfully calc the func expression 3", function () {
        let result = calculator("sqr(3)");
        assert.equal(result, 9);
    })
    it("should successfully calc the func expression 4", function () {
        let result = calculator("sqr(-4)");
        assert.equal(result, 16);
    })
    it("should successfully calc the func expression 5", function () {
        let result = calculator("sqrt(25)");
        assert.equal(result, 5);
    })
    it("should successfully calc the func expression 6", function () {
        let result = calculator("sqrt(36)");
        assert.equal(result, 6);
    })
    it("should successfully calc the func expression 7", function () {
        let result = calculator("sqrt(sqr(3) + sqr(4))");
        assert.equal(result, 5);
    })
    it("should successfully calc the func expression 8", function () {
        let result = calculator("abs(10) - abs(-8) * sqrt(sqr(4))");
        assert.equal(result, -22);
    })
    it("should successfully calc the func expression 9", function () {
        let result = calculator("abs((1+2) * abs(sqr(10)))");
        assert.equal(result, 300);
    })
   
})

describe("calculation exceptions tests", function () {
    it("should throw exception 1", function () {
        let x = 0;
        try {let result = calculator(" 1*/2");}
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected expression after *");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 2", function () {
        let x = 0;
        try {let result = calculator("/2");}
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected expression before /");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 3", function () {
        let x = 0;
        try { let result = calculator("333 +");}
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected expression after +");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 4", function () {
        let x = 0;
        try { let result = calculator("4*+-89//7-"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected expression after -");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 5", function () {
        let x = 0;
        try { let result = calculator("("); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected )");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 6", function () {
        let x = 0;
        try { let result = calculator(")"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected (");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 7", function () {
        let x = 0;
        try { let result = calculator("(1+2))"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected (");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 8", function () {
        let x = 0;
        try { let result = calculator("8*(99-14"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected )");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 9", function () {
        let x = 0;
        try { let result = calculator("91/8+15-(1-55*5-1*(11+5)"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected )");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 10", function () {
        let x = 0;
        try { let result = calculator("abs"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected ( after abs");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 11", function () {
        let x = 0;
        try { let result = calculator("sqr"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected ( after sqr");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 12", function () {
        let x = 0;
        try { let result = calculator("sqrt"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Expected ( after sqrt");
        }
        assert.equal(x, 1);
    })
})