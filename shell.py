# Shell for executing statements
import lexer


while True:
    statement = input("L >> ")
    result = lexer.run(statement)
    print(result)