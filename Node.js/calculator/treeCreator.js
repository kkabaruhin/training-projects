class Node {
    result = 0;
    body = "";
    parent = null;
    priority = -1;
    operands = [];
    leftOperand = null;
    rightOperand = null;
    
    constructor(body, priority) {
        this.body = body;
        this.priority = priority;
    }

    add_operand(new_operand) {
        this.operands.push(new_operand);
    }
}

const priority_table = { "(": 0, "-": 1, "+": 1, "*": 3, "/": 3, "//": 3, "^": 4, "()": 150 };
const unary_operations = ["-", "+"];
const binary_operations = ["*", "/", "//", "^"];

function calcPriority(lexem){
    if (Object.keys(priority_table).includes(lexem)) {
        return priority_table[lexem];
    }
    if (!isNaN(lexem)){
        return 100;
    }
    if (lexem[0] >= "a" && lexem[0] <= "z") {
        return 75;
    }
    return 50;
}

function insertLexemInTree(curr_node, lexem){
    let new_node = new Node(lexem, calcPriority(lexem));
    if (curr_node.body === "") {
        return new_node;
    }
    if ((unary_operations.includes(curr_node.body)) && ((unary_operations.includes(new_node.body)))) { //solution +-+ problem
        if (new_node.body === "-") {
            if (curr_node.body === "+") {
                curr_node.body = "-";
            }
            else {
                curr_node.body = "+";
            }
        }
        return curr_node;
    }
    if ((binary_operations.includes(curr_node.body)) && ((unary_operations.includes(new_node.body)))) { //solution *-+ problem
        curr_node.rightOperand = new_node;
        new_node.parent = curr_node;
        return new_node;
    }
    if (new_node.body === "(") {
        curr_node.rightOperand = new_node;
        new_node.parent = curr_node;
        return new_node;
    }
    if (new_node.body === ")") {
        while (curr_node.body !== "(") {
            curr_node = curr_node.parent;
            if (curr_node === null) throw new SyntaxError("Expected (");
        }
        curr_node.body = "()";
        curr_node.priority = calcPriority("()");
        return curr_node;
    }
    while (true) {
        if (curr_node.priority < new_node.priority) {
            curr_node.rightOperand = new_node;
            new_node.parent = curr_node;
            return new_node;
        }
        if (curr_node.priority >= new_node.priority) {
            if (curr_node.parent !== null) {
                if (curr_node.parent.priority >= new_node.priority) {
                    curr_node = curr_node.parent;
                    continue;
                }
                else {
                    curr_node.parent.rightOperand = new_node;

                    new_node.parent = curr_node.parent;
                    curr_node.parent = new_node;
                    new_node.leftOperand = curr_node;
                    return new_node;
                }
            }
            else {
                curr_node.parent = new_node;
                new_node.leftOperand = curr_node;
                return new_node;
            }
        }
        else {
            new_node.parent = curr_node;
            curr_node.rightOperand = new_node;
            return new_node;
        }
    }
}
exports.createSyntaxTree = function(lexemes){
    if (!lexemes) {
        return new Node();
    }
    let curr_node = new Node("", -1);

    for (let i = 0; i < lexemes.length; i++) {
        curr_node = insertLexemInTree(curr_node, lexemes[i]);
    }

    while (curr_node.parent != null) {
        curr_node = curr_node.parent;
    }
    return curr_node;
}