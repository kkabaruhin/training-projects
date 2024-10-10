const { lexicalParser } = require("./lexicalParser");
const { createSyntaxTree } = require("./treeCreator");
const { calculateTree } = require("./treeCalculator");

exports.calculator = function(in_string){
    let lexems = lexicalParser(in_string);
    let root = createSyntaxTree(lexems);
    let answer = calculateTree(root);
    return answer;
}