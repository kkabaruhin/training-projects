function countOf(str, char) {
    let ans = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === char) ans++;
    }
    return ans;
}

function isLetter(chr) {
    return (chr >= "a" && chr <= "z" || chr >= "A" && chr <= "Z");
}

let spec_symbols = ["+", "-", "*", "/", "^", "(", ")"];
let spec_words = ["abs", "sqr", "sqrt"]
exports.lexicalParser = function (in_string) {
    if (!in_string) {
        return [];
    }
    in_string = String(in_string);
    in_string = in_string.replace(/\s/g, ""); //delete all spaces
    in_string = in_string.replace(/,/g, "."); //replace "," on "."
    in_string = in_string.toLowerCase();

    let answer = [];
    let lexem = ""; //lexem - is a buffer. If it's not empty in the start of iteration, then value of it must be pushed in answer or supplemented. If it's empty, then each previous symbol was pushed in answer
    for (let i = 0; i < in_string.length; i++) {
        if (!isNaN(in_string[i]) || in_string[i] === ".") { //collecting the number
            if (lexem === "" || !isNaN(lexem[0]) || lexem[0] === ".") {
                lexem += in_string[i];
            }
            else {
                answer.push(lexem);
                lexem = in_string[i];
            }
            continue;
        }
        if (spec_symbols.includes(in_string[i])) { //collecting spec symbols
            if (lexem) {
                answer.push(lexem);
                lexem = "";
            }
            if (answer) {
                if (answer[answer.length - 1] === "/" && in_string[i] === "/") {
                    answer[answer.length - 1] = "//";
                    lexem = "";
                }
                else {
                    lexem = in_string[i];
                }
            }
            else {
                lexem = in_string[i];
            }
            answer.push(lexem);
            lexem = "";
            continue;
        }
        if (isLetter(in_string[i])) {           //collecting word
            if (lexem === "" || isLetter(lexem[0])) {
                lexem += in_string[i];
            }
            else {
                answer.push(lexem);
                lexem = in_string[i];
            }
            continue;
        }

        throw new SyntaxError("Unknown symbol " + in_string[i]);
    }
    answer.push(lexem);
    for (let i = 0; i < answer.length; i++) {
        if (countOf(answer[i], ".") > 1 || answer[i][0] === "." || answer[i][answer[i].length - 1] === ".") {
            throw new SyntaxError("Unexpected token " + answer[i]);
        }
        if (isLetter(answer[i][0]) && !spec_words.includes(answer[i])) {
            throw new SyntaxError("Unknown function " + answer[i]);
        }
    }
    return answer.filter(x => x !== "");
}