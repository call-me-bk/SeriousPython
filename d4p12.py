# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:33:48 2019

@author: user
"""

"""import ast
class ReplaceBinOp(ast.NodeTransformer):
    def visit_BinOp(self,node):
        return ast.BoolOp(left=node.left,
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
    print(x)"""
class IntegerWrapper(ast.NodeTransformer):
    """Wraps all integers in a call to Integer()"""
    def visit_Num(self, node):
        if isinstance(node.n, int):
            return ast.Call(func=ast.Name(id='Integer', ctx=ast.Load()),
                            args=[node], keywords=[])
        return node

tree = ast.parse("1/3")
tree = IntegerWrapper().visit(tree)
# Add lineno & col_offset to the nodes we created
ast.fix_missing_locations(tree)