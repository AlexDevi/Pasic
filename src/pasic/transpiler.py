'''
Created on Apr 17, 2012

@author: alex
'''
#from locale import str
from .lexer import BasicLexer

class PasicTranspiler(object):
    '''
    The main PASIC transpiler, taking care of lexing, parsing and transforming
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def process(self, file_name: str) -> bool:
        '''Transforms source files to C++ source files'''
        
        # TODO support of filename extensions may include .asp, .vbs, .wsh, etc.
        if not file_name.lower().endswith('.bas'):
            print('PASIC expects "bas" filename extension')
            return False
        
        # TODO error handling if file does not exist 
        source_file = open(file_name, 'r')
        basic_code = source_file.read()
        
        lexer = BasicLexer()
        tokens = lexer.lex(basic_code)
            
        