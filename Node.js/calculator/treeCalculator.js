let function_names = ["abs", "sqr", 'sqrt'];

function calculateTree(curr_node) {
    if (curr_node === null) {
        throw new SyntaxError("Node is null");
    }
    if (!isNaN(curr_node.body)) {
        try {
            curr_node.result = parseFloat(curr_node.body);
            return curr_node.result;
        }
        catch (err) {
            throw new SyntaxError("Number cast error");
        }
    }
    if (curr_node.body === "(") {
        throw new SyntaxError("Expected )");
    }
    if (curr_node.body === ")") {
        throw new SyntaxError("Expected (");
    }
    if (curr_node.body === "()") {
        return calculateTree(curr_node.rightOperand);
    }
    if (curr_node.body === "-" || curr_node.body === "+") {
        let left_ress = 0, right_ress = 0;
        if (curr_node.leftOperand !== null) 
            left_ress = calculateTree(curr_node.leftOperand);

        try {
            right_ress = calculateTree(curr_node.rightOperand);
            if (curr_node.body === "-") {
                curr_node.result = left_ress - right_ress;
            }
            else {
                curr_node.result = left_ress + right_ress;
            }
            return curr_node.result;
        }
        catch (err) {
            if (err.message === "Node is null") {
                throw new SyntaxError("Expected expression after " + curr_node.body)
            }
            else throw err;
        }
    }
    if (curr_node.body === "*" || curr_node.body === "/" || curr_node.body === "//" || curr_node.body === "^") {
        let left_ress = 0, right_ress = 0;
        try {
            left_ress = calculateTree(curr_node.leftOperand);
        }
        catch (err) {
            if (err.message == "Node is null") {
                throw new SyntaxError("Expected expression before " + curr_node.body)
            }
            else throw err;
        }
        try {
            right_ress = calculateTree(curr_node.rightOperand);
        }
        catch (err) {
            if (err.message == "Node is null") {
                throw new SyntaxError("Expected expression after " + curr_node.body)
            }
            else throw err;
        }


        if (curr_node.body === "*") {
            curr_node.result = left_ress * right_ress;
        }
        if (curr_node.body === "/") {
            curr_node.result = left_ress / right_ress;
        }
        if (curr_node.body === "//") {
            curr_node.result = Math.floor(left_ress / right_ress);
        }
        if (curr_node.body === "^") {
            curr_node.result = left_ress ** right_ress;
        }
        return curr_node.result;
    }
    if (function_names.includes(curr_node.body)) {
        if (!curr_node.rightOperand || curr_node.rightOperand.body !== "()") {
            throw new SyntaxError("Expected ( after " + curr_node.body)
        } 
        if (curr_node.body === "abs") {
            let right_ress = calculateTree(curr_node.rightOperand);
            return Math.abs(right_ress);
        }
        if (curr_node.body === "sqr") {
            let right_ress = calculateTree(curr_node.rightOperand);
            return right_ress * right_ress;
        }
        if (curr_node.body === "sqrt") {
            let right_ress = calculateTree(curr_node.rightOperand);
            return Math.sqrt(right_ress);
        }
    }
    return 0;
}
module.exports.calculateTree =  calculateTree;