This is a training project on Node.js using Express for client-server interaction. 
The application is a simple calculator with a graphical interface. 
It supports the operations + - * / //, brackets and abs, sqr, sqrt functions. 
You can enter expressions of any length with operations in any order, if they are mathematically correct. 
To run, write in the "npm install" and after "node app" in PowerShell and go to http://localhost:3000/ in your browser. 
To run tests, you can enter "npm test".

Ejs is used as views. The motcha module is used for testing. 
For those interested in how everything is implemented, here's how.

1) The string entered by the user is parsed into components (lexemes), which are numbers, arithmetic operations, brackets and function calls. 
The implementation is presented in the lexicalParser.js file.
2) A syntax tree is formed from the resulting list of lexemes. Implementation is in treeCreator.js.
3) And finally, the value of the expression is calculated using depth-first traversal of the resulting tree. Implementation in treeCalculator.js.