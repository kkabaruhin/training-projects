const assert  = require("assert");
const { lexicalParser } = require("../lexicalParser");


describe("lexicalParser tests with only +-*/", function () {
    it("should pars simple example 1", function(){
        const result = lexicalParser("1");
        assert.deepEqual(result, ["1"]);
    })
    it("should pars simple example 2", function () {
        const result = lexicalParser("2345");
        assert.deepEqual(result, ["2345"]);
    })
    it("should pars simple example 3", function () {
        const result = lexicalParser("+3+   4 + 8");
        assert.deepEqual(result, ["+","3", "+", "4", "+", "8"]);
    })
    it("should pars simple example 4", function () {
        const result = lexicalParser("    -4 * 1 /   -5 ");
        assert.deepEqual(result, ["-", "4", "*", "1", "/", "-", "5"]);
    })
    it("should pars simple example 5", function () {
        const result = lexicalParser("555-    1230    -5090");
        assert.deepEqual(result, ["555", "-", "1230", "-", "5090"]);
    })
    it("should pars simple example 6", function () {
        const result = lexicalParser("     6 - + 7 + - - - + / 8     ");
        assert.deepEqual(result, ["6", "-", "+", "7", "+", "-", "-", "-", "+", "/", "8"]);
    })
    it("should pars simple example 7", function () {
        const result = lexicalParser("--123  /  / /   - +-4567++ + / // /* * +9876");
        assert.deepEqual(result, ["-", "-", "123", "//", "/", "-", "+", "-", "4567", "+", "+", "+", "//", "//", "*", "*", "+", "9876"]);
    })
})

describe("lexicalParser tests with only +-*/^()", function () {
    it("should pars example 1", function () {
        const result = lexicalParser("()");
        assert.deepEqual(result, ["(", ")"]);
    })
    it("should pars example 2", function () {
        const result = lexicalParser("-1*(+2^4)");
        assert.deepEqual(result, ["-", "1", "*", "(", "+", "2", "^", "4", ")"]);
    })
    it("should pars example 3", function () {
        const result = lexicalParser("(+-33^18 * 2 / 4) -99");
        assert.deepEqual(result, ["(", "+", "-", "33", "^", "18", "*", "2", "/", "4", ")", "-", "99"]);
    })
    it("should pars example 4", function () {
        const result = lexicalParser("(44 - 2.15) ^ (99 * 10 + 5)");
        assert.deepEqual(result, ["(", "44", "-", "2.15", ")", "^", "(", "99", "*", "10", "+", "5", ")"]);
    })
    it("should pars example 5", function () {
        const result = lexicalParser("-(55 + 77 * (1.2 ^ (3 + 1)))");
        assert.deepEqual(result, ["-", "(", "55", "+", "77", "*", "(", "1.2", "^", "(", "3", "+", "1", ")", ")", ")"]);
    })
})

describe("lexicalParser tests with words", function () {
    it("should pars word example 1", function () {
        const result = lexicalParser("abs");
        assert.deepEqual(result, ["abs"]);
    })
    it("should pars word example 2", function () {
        const result = lexicalParser("sqr");
        assert.deepEqual(result, ["sqr"]);
    })
    it("should pars word example 3", function () {
        const result = lexicalParser("sqrt");
        assert.deepEqual(result, ["sqrt"]);
    })
    it("should pars word example 4", function () {
        const result = lexicalParser("4-abs(2)");
        assert.deepEqual(result, ["4", "-", "abs", "(", "2", ")"]);
    })
    it("should pars word example 5", function () {
        const result = lexicalParser("sqr(5*4)");
        assert.deepEqual(result, ["sqr", "(", "5", "*", "4", ")"]);
    })
    it("should pars word example 6", function () {
        const result = lexicalParser("66/sqrt(2+5*4) - abs(1234)");
        assert.deepEqual(result, ["66", "/", "sqrt", "(", "2", "+", "5", "*", "4", ")", "-", "abs", "(", "1234", ")"]);
    })
    it("should pars word example 7", function () {
        const result = lexicalParser("sqr(7+sqrt(19-5*abs(99) - sqrt(54/1)))");
        assert.deepEqual(result, ["sqr", "(", "7", "+", "sqrt", "(", "19", "-", "5", "*", "abs", "(", "99", ")", "-", "sqrt", "(", "54", "/", "1", ")", ")", ")"]);
    })

})


describe("lexicalParser exception tests", function () {
    it("should throw exception 1", function () {
        let x = 0;
        try { let result = lexicalParser("5.6.7"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token 5.6.7");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 2", function () {
        let x = 0;
        try { let result = lexicalParser("2."); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token 2.");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 3", function () {
        let x = 0;
        try { let result = lexicalParser(".3"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token .3");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 4", function () {
        let x = 0;
        try { let result = lexicalParser("4+8562.23456//.1"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token .1");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 5", function () {
        let x = 0;
        try { let result = lexicalParser("5*8562.23456//1.+34636"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token 1.");
        }
        assert.equal(x, 1);
    })
    it("should throw exception 6", function () {
        let x = 0;
        try { let result = lexicalParser("6.8966*8562.23456//1.12.+34636"); }
        catch (err) {
            x += 1;
            assert.deepEqual(err.message, "Unexpected token 1.12.");
        }
        assert.equal(x, 1);
    })
})

