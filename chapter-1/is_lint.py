import ast

# This helps check if a program is a valid L_int program 
# Notes for Chapter 1 in README has the context free grammer for L_int

def is_exp(exp):
    match exp:
        case ast.Constant(x):
            return True
        case ast.Call(ast.Name("input_int"), []):
            return True
        case ast.UnaryOp(ast.USub(), e):
            return is_exp(e)
        case ast.BinOp(e1, ast.Add(), e2):
            return is_exp(e1) and is_exp(e2)
        case ast.BinOp(e1, ast.Sub(), e2):
            return is_exp(e1) and is_exp(e2)
        case _:
            return False


def is_stmt(s):
    match s:
        case ast.Expr(ast.Call(ast.Name("print"), [exp])):
            return is_exp(exp)
        case ast.Expr(exp):
            return is_exp(exp)
        case _:
            return False


def is_lint(program):
    match program:
        case ast.Module(list_of_stmt):
            return all([is_stmt(s) for s in list_of_stmt])
        case _:
            return False
