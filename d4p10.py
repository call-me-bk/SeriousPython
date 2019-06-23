# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:59:58 2019

@author: user
"""

# This is not heavy duty compiler
# parsing, lexing and certainly not everything about
# AST
# Abstract Sytax Tree
# This is just programtically inspecting your source
#
import ast

code = ast.parse("print('Hello world!')")
print(code)
#exec( excute normal code)
exec(compile(code, filename="", mode="exec"))


import ast
a=6
expression = '6 + 8 + a'
code = ast.parse(expression, mode='eval')

print(eval(compile(code, '', mode='eval')))
print(ast.dump(code))

# Let us look at a multiline AST



tree = ast.parse('''
fruits = ['grapes', 'mango']
name = 'peter'

for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
''')

print(ast.dump(tree))


import ast

class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        print('{}'.format(tree_node.s))


class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str('String: ' + tree_node.s)


tree_node = ast.parse('''
fruits = ['grapes', 'mango']
name = 'peter'

for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
''')

NodeTransformer().visit(tree_node)
NodeVisitor().visit(tree_node)

tree_node = ast.fix_missing_locations(tree_node)
exec(compile(tree_node, '', 'exec'))



    
    