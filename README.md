# essentials-of-compilation

Following along with the [Essentials of compilation book](https://mitpress.mit.edu/9780262048248/essentials-of-compilation/)


## Chapter 1: Preliminaries

- This chapter introduces the basics of AST and uses the python module `ast`.
- Programming language can be thought of a set of all possible programs. Since we cannot list all possible programs (infinite set) we define a context free grammer
- Context free grammer for L_int (the simple language in this chapter):
```
exp   ::= Constant(int) | Call(Name('input_int'), []) | UnaryOp(USub(), exp) | BinOp(exp, Add(), exp) | BinOp(exp, Sub(), exp)
stmt  ::= Expr(Call(Name('print'), [exp])) | Expr(exp)
L_int ::= Module(stmt*)
```

- The [exp] in print means that the value of the expression not the expression is printed

