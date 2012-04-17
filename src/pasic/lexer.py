'''
Created on Apr 17, 2012

@author: alex
'''

import string

class Token(object):
    token_type = ''
    value = ''

class BasicLexer(object):
    '''
    A lexer for the BASIC language
    '''
    
    tokens = []
    
    position = 0
    
    # TODO move this to a central basic language class
    operators = [
                '^',        # Exponentiation
                '-',        # Negation or Subtraction
                '*',        # Multiplication
                '/', '\\',  # Division, Integer division
                'mod',      # modulo
                '+',        # Addition
                '&',        # String Concatenation
                '=',        # Equality or Assignment
                '<>',       # Inequality
                '<', '>' ,  # Less than, greater than
                '<=', '>=', # Less than or equal, greater than or equal
                'is',       # Object equivalence
                'not', 'and', 'or', 'xor', 'eqv', 'imp'
                ]
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def lex(self, source_code):
        '''starts lexing the source_code, returns found tokens'''
        
        while self.position < len(source_code):
            character = source_code[self.position]
            lchar = character.lower()
            self.position = self.position + 1
            
            if lchar in string.whitespace:
                continue
                
            if lchar in self.operators:
                self.add_token(character)
                continue
            
            # TODO add is identifier
            
            # TODO add is digit
            
            
        
        return self.tokens
    
    
    def add_token(self, token_type, value=''):
        ''' adds a Token object to the list of tokens '''
        
        t = Token()
        t.token_type = token_type
        t.value = value
        
        self.tokens.append(t)
    
    