import sys

digits = "0123456789"
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

T_INTEGER       = 'INTEGER'
T_FLOAT         = 'FLOAT'
T_CHAR          = 'CHAR'
T_BOOLEAN       = 'BOOL'
T_PLUS          = 'PLUS'
T_MINUS         = 'MINUS'
T_STAR          = 'STAR'
T_DIV           = 'DIV'
T_BSLASH        = 'BSLASH'
T_MOD           = 'MOD'
T_LPAREN        = 'LPAREN'
T_RPAREN        = 'RPAREN'
T_LBRACE        = 'LBRACE'
T_RBRACE        = 'RBRACE'
T_SEMICOLON     = 'SEMICOLON'
T_STRING        = 'STRING'
T_EQUAL         = 'EQUALS'
T_ASSIGN        = 'ASSIGNMENT'
T_LTHAN         = 'LTHAN'
T_GTHAN         = 'GTHAN'
T_AND           = 'AND'
T_OR            = 'OR'
T_QUOTE         = 'QUOTE'
T_ID            = 'ID'
T_COMMA         = 'COMMA'
T_DOT           = 'DOT'
T_EOF           = 'EOF'
T_COMMENT       = 'COMMENT'
T_ARROW         = 'ARROW'
T_BANG          = 'BANG'
T_NOTEQ         = 'NOTEQUAL'

# reserved words
T_BEGIN         = 'BEGIN'
T_FUNC          = 'FUNC'
T_RETURN        = 'RETURN'
T_WHILE         = 'WHILE'
DT_INT           = 'DT_INT'
DT_FLOAT         = 'DT_FLOAT'
DT_STRING        = 'DT_STRING'
DT_BOOL          = 'DT_BOOL'
DT_CHAR          = 'DT_CHAR'
DT_VOID          = 'DT_VOID'


class Token:
    def __init__(self, ttype, value=None):
        self.type = ttype
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'

class Lexer:
    # State Map
    # 0 - Default state
    # 1 - Beginning of string
    # 2 - Beginning of comment
    # 3 - Beginning of assignment ( := )

    def __init__(self, text):
        self.text = text
        self.position = -1
        self.curr_char = None
        self.state = 0
        self.advance()

    def advance(self):
        self.position += 1

        if self.position < len(self.text):
            self.curr_char = self.text[self.position]
        else:
            self.curr_char = None

    def make_tokens(self):
        tokens = []

        while self.curr_char != None:
            # print(self.get_status())
            # ignore spaces and tabs for now
            if self.curr_char in ' \t\n':
                self.advance()

            elif self.curr_char in digits:
                tokens.append(self.make_num())

            elif self.curr_char == '\"':
                if self.state == 0:     # if state is default
                    self.advance()
                    tokens.append(self.make_string())
                    
            elif self.curr_char in alpha:
                tokens.append(self.make_id())

            elif self.curr_char == '+':
                tokens.append(Token(T_PLUS))
                self.advance()
            elif self.curr_char == '-':
                if self.state == 0:
                    self.state = 11
                    tokens.append(self.minus_or_arrow())
                self.advance()
            elif self.curr_char == '*':
                tokens.append(Token(T_STAR))
                self.advance()
            elif self.curr_char == '/':
                if self.state == 0:
                    self.state = 7
                    self.process_comment()
                elif self.state == 8:
                    tokens.append(Token(T_DIV))
                self.advance()
            elif self.curr_char == '\\':
                tokens.append(Token(T_BSLASH))
                self.advance()
            elif self.curr_char == '%':
                tokens.append(Token(T_MOD))
                self.advance()
            elif self.curr_char == '(':
                tokens.append(Token(T_LPAREN))
                self.advance()
            elif self.curr_char == ')':
                tokens.append(Token(T_RPAREN))
                self.advance()
            elif self.curr_char == '{':
                tokens.append(Token(T_LBRACE))
                self.advance()
            elif self.curr_char == '}':
                tokens.append(Token(T_RBRACE))
                self.advance()
            elif self.curr_char == ';':
                tokens.append(Token(T_SEMICOLON))
                self.advance()
            elif self.curr_char == ':':
                self.state = 3
                tokens.append(self.make_assign())
                self.advance()
            elif self.curr_char == '=':
                self.state = 5
                tokens.append(self.make_equiv())
                self.advance()
            elif self.curr_char == ',':
                tokens.append(Token(T_COMMA))
                self.advance()
            elif self.curr_char == '.':
                tokens.append(Token(T_DOT))
                self.advance()
            elif self.curr_char == '!':
                if self.state == 0:
                    self.state = 13
                    tokens.append(self.bang_or_not_eq())
                self.advance()
            elif self.curr_char == '>':
                tokens.append(Token(T_GTHAN))
                self.advance()
            elif self.curr_char == '<':
                tokens.append(Token(T_LTHAN))
                self.advance()
            elif self.curr_char == '|':
                tokens.append(self.make_or())
                self.advance()
            elif self.curr_char == '&':
                tokens.append(self.make_and())
                self.advance
            else:
                self.advance()
                char = self.curr_char
                return self.show_error('Illegal Character Exception: {0}'.format(char))

        tokens.append(Token(T_EOF))


        # check for reserved words
        for i in range(len(tokens)):
            
            if tokens[i].type == T_ID:
                if tokens[i].value == 'int':
                    tokens[i] = Token(DT_INT)    
                elif tokens[i].value == 'float':
                    tokens[i] = Token(DT_FLOAT)
                elif tokens[i].value == 'string':
                    tokens[i] = Token(DT_STRING)
                elif tokens[i].value == 'bool':
                    tokens[i] = Token(DT_BOOL)
                elif tokens[i].value == 'char':
                    tokens[i] = Token(DT_CHAR)
                elif tokens[i].value == 'void':
                    tokens[i] = Token(DT_VOID)
                elif tokens[i].value == 'begin':
                    tokens[i] = Token(T_BEGIN)
                elif tokens[i].value == 'func':
                    tokens[i] = Token(T_FUNC)
                elif tokens[i].value == 'return':
                    tokens[i] = Token(T_RETURN)
                elif tokens[i].value == 'while':
                    tokens[i] = Token(T_WHILE)


        return tokens

##################
# STATE MACHINES #
##################

    def make_num(self):
        num_str = ''
        num_dots = 0

        while self.curr_char != None and self.curr_char in digits + '.':
            if self.curr_char == '.':
                if num_dots == 1: break
                num_dots += 1
                num_str += '.'
            else:
                num_str += self.curr_char
            self.advance()

        if num_dots == 0:
            return Token(T_INTEGER, int(num_str))
        else:
            return Token(T_FLOAT, float(num_str))

    def make_string(self):
        string_str = ''
        # while current char is not end of string
        while self.curr_char != None:
            if self.state == 0:     # we are starting the string
                string_str += self.curr_char    # append curr_char
                self.state = 1      # we are now inside the string
            elif self.state == 1 and self.curr_char == '\"': 
                self.advance()
                break # we are inside the string and have come to the end 
            elif self.state == 1 and self.curr_char != '\"':
                string_str += self.curr_char
           
            self.advance()

        self.state = 0
        return Token(T_STRING, string_str)

    def make_assign(self):
        token_str = ''

        while self.curr_char != None:
            if self.state == 3 and self.curr_char == ':':     # we have a colon and are starting a :=
                token_str += self.curr_char
                self.state = 4
            if self.state == 4 and self.curr_char == "=":
                token_str += self.curr_char
                self.state = 0
                break

            self.advance()

        return Token(T_ASSIGN)

    def make_equiv(self):
        token_str = ''

        while self.curr_char != None:
            if self.state == 5 and self.curr_char == "=":   # we have a = and are starting a ==
                token_str += self.curr_char
                self.state = 6
                self.advance()
            if self.state == 6 and self.curr_char == "=":
                token_str += self.curr_char
                self.state = 0
                break
            
            self.advance()
        return Token(T_EQUAL)

    def make_id(self):
        id_str = ''

        while self.curr_char != None and (self.curr_char in alpha or self.curr_char in digits):
            id_str += self.curr_char
            
            self.advance()

        return Token(T_ID, id_str)

    def process_comment(self):

        while self.curr_char != None:
            if self.state == 7 and self.curr_char == '/':   # we might have found a comment
                self.state = 8
            elif self.state == 8 and self.curr_char == '*': # yes, this is the beginning of a comment
                self.state = 9                              # now we must look for the end of comment marker
            elif self.state == 8 and self.curr_char != '*': # this is probably a divide symbol instead
               return                                       # so we pop out of the function
            elif self.state == 9 and self.curr_char == '*': # we might have the end of comment marker
                self.state = 10
            elif self.state == 10 and self.curr_char == '/':# we found the end of the comment, so we discard all that we saw
                self.state = 0
                return
            

            self.advance()


    def minus_or_arrow(self):
        
        while self.curr_char != None:
            if self.state == 11 and self.curr_char == '-':  # we may have an arrow
                self.state = 12
            elif self.state == 12 and self.curr_char == '>':
                self.state = 0
                return Token(T_ARROW)
            else:
                break
            
            self.advance()
        self.state = 0
        return Token(T_MINUS)

    def bang_or_not_eq(self):

        while self.curr_char != None:
            if self.state == 13 and self.curr_char == '!':  # we may have a not equal
                self.state = 14
            elif self.state == 14 and self.curr_char == '=':
                return Token(T_NOTEQ)
            elif self.state == 14 and self.curr_char != '=':
                return Token(T_BANG)
            
            self.advance()
            
    def make_and(self):
        temp = ''
        while self.curr_char != None:
            if temp == '&&':
                return Token(T_AND)

            if self.curr_char == '&':
                temp += self.curr_char
            
            self.advance()

    def make_or(self):
        temp = ''
        while self.curr_char != None:
            if temp == '||':
                return Token(T_OR)
            

            if self.curr_char == '|':
                temp += self.curr_char
            
            self.advance()

#########################
# END OF STATE MACHINES #
#########################

    def get_status(self):
        status = 'text:{0}\nlen:{1}position:{2}\ncurr_char:{3}\n'.format(
            self.text, len(self.text), self.position, self.curr_char
        )

        return status

    def show_error(self, error_type):
        print(error_type)
        print(self.text)
        
        print((self.position-1)*' ', end="")
        print('^')



def run(text):
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
   
    return tokens

def main():
    program = ''

    with open (sys.argv[1], 'r') as f:
        for line in f:
            program += line

    print(run(program))
    
if __name__ == '__main__':
    main()