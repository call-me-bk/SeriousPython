# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:48:08 2019

@author: user
"""

import ast
ast.parse
ast.parse("x=42")
# This String gets parsed into token
ast.dump(ast.parse("x=42"))
# the dump function shows you
# there is an assignment
# the target is some guy called x
# filled with a numeric value 42
tree=ast.parse("x=42")
# Now this parsed ast is compiled into a byte
# object for execution
compile(tree,'a','exec')
#we can then evaluate the execcution of this
eval(compile(tree,'a','exec'))
print(x)
# visit the site for walking thru the tree for:
# 1. List and list iteration
# 2. List comprehensions
# 3. Tuple addition and display the out put to check this out
# using ast.walk or by using a
# NodeTransformer class
for node in ast.walk(tree):
    # we had an assign so let us check
    if isinstance(node,ast.Assign):
        name=node.targets[0].id
        print(name)
# in this trivial example we found 
# that this was an assignment and the 
# label is x
# a beautiful tool
# https://vpyast.appspot.com/ lets see this
import ast
class ReplaceBinOp(ast.NodeTransformer):
    def visit_BinOp(self,node):
        return ast.BinOp(left=node.left,
                          op=ast.Add(),
                          right=node.right)
tree=ast.parse("x=1/3")
ast.fix_missing_locations(tree)
eval(compile(tree,'','exec'))
print(ast.dump(tree))
print(x)
tree=ReplaceBinOp().visit(tree)
ast.fix_missing_locations(tree)
eval(compile(tree,'','exec'))
print(ast.dump(tree))
print(x)


def show_info(functionNode):
    print("Function name:", functionNode.name)
    print("Args:")
    for arg in functionNode.args.args:
        #import pdb; pdb.set_trace()
        print("\tParameter name:", arg.arg)

# code example for stackoverflow Credit: Kevin
filename = "untrusted.py"
with open(filename) as file:
    node = ast.parse(file.read())

functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
calleds = [ n for n in node.body if isinstance(n,ast.Call)]
for function in functions:
    show_info(function)

for class_ in classes:
    print("Class name:", class_.name)
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        show_info(method)
"""
for called in calleds:
    show_info(called) """ 
# Sometimes you need to find dead code - this is done using vulture
# pip install vulture
# pip install flake8
#called = [ n for n in node.body if isinstance(n,ast.Call)]


