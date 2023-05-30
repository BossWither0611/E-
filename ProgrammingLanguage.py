import time
import turtle

#########################################################
# ERRORS
#########################################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name} : {self.details}'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return  result
    
class IllegalCharError(Error):
    def __init__(self, details, pos_start, pos_end):
        super().__init__(pos_start, pos_end, 'Illegeral Character', details)

class UnknownSystemFunction(Error):
    def __init__():
        super().__init__(-1, -1, 'System function not found! \n', "")

#########################################################
# POSITION
#########################################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1;
        self.col += 1

        if (current_char == '\n'):
            self.ln += 1
            self.col = 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#########################################################
# Booleans
#########################################################
#I like programming in java and these bools make me comfortable
false = False;
true = True;
#########################################################
# Code Reding Variables
#########################################################
line = "NONE"
hasMain = false;
hasMainVoid = false;
cIsRun = false;
vIsRun = false;
KeyWords = ["while", "for", "if", ""]

#########################################################
# TOKENS
#########################################################

DIGITS = '0123456789'

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if (self.value): return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                #ERROR
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None
    
    def make_number(self):
        num_str = ""
        dot_count = 0
        while (self.current_char != None and self.current_char in DIGITS + '.'):
            if (self.current_char == "."):
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            self.advance()

        if (dot_count == 0):
            return Token(TT_INT, int (num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
        
def mRun(text):
    fn = 'main.ep'
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error

###################################################################
# System
###################################################################

class System:
    def __init__(self, ln):
        self.ln = ln
        if (self.ln.__contains__("System.out")):
            if (self.ln.__contains__("System.out.math.print")):
                cal = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
                result, error = mRun(cal)
                if error: print(error.as_string)
                else: print(result)
            #if (ln.__contains__("System."))
        elif (self.ln.__contains__("System.in")):
            if (self.ln.__contains__("System.in.out.input(") and line.__contains__(");")):
                cursor = self.ln[self.ln.find("(") + 1:self.ln.find(")")]
                string = input(cursor)
                pstring = string;
                print(pstring)
            if (self.ln.__contains__("System.in.input(") and self.ln.__contains__(");")):
                string = self.ln[self.ln.find("(")+1:self.ln.find(")")]
                pstring = string;
                input(pstring)
        #elif (self.ln.__contains__("System.print")):
            #print("Sys")
        elif (self.ln.__contains__("System.print(")):
            ''' and line.__contains__(");")'''
            string = self.ln[ln.find("(")+1:ln.find(")")]
            pstring = string
            print(pstring),
        elif (self.ln.__contains__("System.println(")):
            string = self.ln[self.ln.find("(")+1:self.ln.find(");")]
            #if (string.__contains__("[Enter]") or string.__contains__("\\n")):el
            pstring = string
            print(pstring)
        elif (self.ln.__contains__("System.advanced")):
            if (self.ln.__contains__("System.advanced.print(") and line.__contains__(");")):
                pstring = "Null"
                print("Error -1:(Code might not work like expected): This command isn't finished."),
        else:
            UnknownSystemFunction()

#########################################################
# KeyWords
######################################################### 

class KeyWord:
    def __init__(self, keyWord, line):
        self.line = line
        self.keyWord = keyWord
        if (keyWord == "if"):
            self.IF()
        elif (keyWord == "new"):
            self.NEW()
    def IF(self):
        #Math if statement
        if (self.line.__contains__("$") and self.line.__contains__("§")):
            result = self.line[self.line.find("$") + 1 : self.line.find("§")]
    def NEW(self):
        pass

#########################################################
# Code reding
#########################################################
def wait(i):
    time.sleep(i)
def main():
    with open(r"C:\Users\erens\OneDrive\Dokumente\ProgrammingLanguage\MainPythonFile\main.ep", "r") as f:
        rline = 0;
        hasMainClass = false;
        hasMainVoid = false;
        #fcontent = f.read();
        #if (fcontent.__contains__("public class Main {") and fcontent.__contains__("}")):
        #    cIsRun = true;
        #if (fcontent.__contains__("public main(Compiler) {") and fcontent.__contains__("}")):
        #    if (cIsRun):
        #        vIsRun = true;
        #if (vIsRun):
        for i in range(50):
            line = f.readline(1000)
            if (line.__contains__("public class Main {")):
                hasMainClass = true;
            if (hasMainClass and line.__contains__("public main(Compiler) {")):
                hasMainVoid = true;
            if (hasMainVoid):
                if (line.__contains__("System")):
                    System(line)
                if (line.__contains__("Test.test;")):
                    print("test")
                if (line.__contains__("Time.sleep(") and line.__contains__(");")):
                    integer = line[line.find("(") + 1:line.find(")")]
                    i = integer;
                    sinteger = int(i);
                    time.sleep(sinteger)
                if (line.__contains__("Time.msleep(") and line.__contains__(");")):
                    integer = line[line.find("(") + 1:line.find(")")]
                    i = (integer);
                    sinteger = int(i);
                    time.sleep(sinteger)
                    print("Error -1 (Code might not work like expected): This command isnt finished.")
                if (line.__contains__("bat.pause();")):
                    turtle.listen()
                    turtle.onkeypress(wait(0.1))
                    print("Error -1: (Code might not work like expected): This command isn't finished.")
                if (line.__contains__("§if")):
                    print("Error -1: (Code might not work like expected) :: This command isn't finished.")
                if (line.__contains__("for")):
                    number = line[line.find("(") + 1:line.find(")")]
                    #print(number)
                    integer = number;
                    sinteger = int(integer)
                    n = sinteger
                    for i in range(n):
                        cmd = line[line.find("{") + 1 : line.find("}")]
                        if (cmd.__contains__("print")):
                            string = line[line.find("print\"") + 6 : line.find("'")]
                            pstring = string
                            print(pstring)
                if (line.__contains__("goto")):
                    goto = line[line.find("(") + 1 : line.find(");")]
                    lineToGo = int(goto)
                    rline = lineToGo - 1
                    line = f.readline(rline)
                    print("Error -1: COMMAND not finished.")
                if (line.__contains__("file.readPrint")):
                    fpath = line[line.find("(") + 1 : line.find(");")]
                    path = fpath;
                    file = open(fpath, 'r')            
                    print(file.readlines())
                if (line.__contains__("while.1Cmd")):
                    c = line[line.find("(") + 1 : line.find(")")]
                    co = line[line.find("{") + 1 : line.find("};")]
                    if (c == "true"):
                        if (co.__contains__("print")):
                            text = line[line.find("\"") + 1 : line.find("'")]
                            print(text),
                if (line.__contains__("}")):
                    hasMainVoid = false;
                rline += 1
            if (line == "}" and hasMainVoid == false and hasMainClass == true):
                hasMainClass = false;
        #print(f"CHECK {rline}")
        #print(line)
main()

#only to remember for me
#print(int("1000"))
#text1 = "!aO"
#text2 = text1[text1.find("!")+1:text1.find("O")]