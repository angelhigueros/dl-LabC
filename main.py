# Angel Higueros - 20460
# Laboratorio C

from yalex.yalex import Yalex
from tools.graph import display_expression_tree
from tools.tools import infix_postfix
from tree.tree import get_tree

import sys


analizador = Yalex(sys.argv[1])
regex = analizador.get_regex()
display_expression_tree(get_tree(infix_postfix(regex)), regex)




