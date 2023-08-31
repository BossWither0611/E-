from pathlib import Path
import colorama
from colorama import Fore, Back, Style
import time
from pynput.keyboard import Key, Controller
import os

colorama.init()

path = input("E§> ")

#Var

hasMainVoid = False
functionIsRunned = False
hasMainClass = False
classIsRunned = False

class PLVar:
    keyBoardIsImported = False
    STDSystemIsImported = False
    dontRun = False

###############################
# Error
###############################

class Error:
    def __init__(self, error):
        self.error = error
        if (self.error == "calculation"):
            self.calculation()
        elif (self.error == "unknownCalculation"):
            self.unknowCalculation()
        elif (self.error == "testError"):
            self.testError()
        elif (self.error == "unknownError"):
            self.unknownError()
        elif (self.error.__contains__("!importedSTDLib")):
            self.unImportedSTDLibrary()
        elif (self.error == "ifDataType"):
            self.unknownIfStatement()

    def calculation(self):
        print(f"{Fore.RED}CalculationError(): Calculation failed due to unknown mathematical characters.{Fore.YELLOW}\n")
    
    def unknowCalculation(self):
        print(f"{Fore.RED}UnkownCalculationError(): Something went wrong when calculating an integer.{Fore.YELLOW}\n")

    def testError(self):
        print(f"{Fore.RED}This Error is just a test, you shouldn't run into it, if you aren't testing the error msg.{Fore.YELLOW}\n")

    def unknownError(self):
        print(f"{Fore.RED}UnknownError(): A unknown Error was tried to be recreated.\n  This Error is always found in an @error-command when the error isn't exsting. It can also probably be in other commands.{Fore.YELLOW}\n")

    def unImportedSTDLibrary(self):
        print(f"{Fore.RED}STD::{self.error[self.error.find('(') + 1 : self.error.find(');')]} is missing.\n  To prevend this error from happening again, you need to import the right Module/Library.\n  {'{'}#import <Library/Module>{'}'}{Fore.YELLOW}\n")

    def unknownIfStatement(self):
        print(f"{Fore.RED}Error.typeNotFoundInIf-Statement(): An unsupported data-type was found in an if statement!{Fore.YELLOW}")

class AtError:
    def __init__(self, ln):
        self.ln = ln
        type = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
        Error(type)

###############################
# import (#import <module>)
###############################

class Import:
    def __init__(self, ln):
        self.ln = ln
        if (self.ln == "#import <keyBoard>"):
            PLVar.keyBoardIsImported = True
        elif (self.ln == "#import <STD/System>"):
            PLVar.STDSystemIsImported = True

###############################
# Math
###############################

class Math:
    result = 0
    def __init__(self, expression):
        self.expression = expression

    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Fore.YELLOW}")
            return None
        
    def printMath(self, expression):
        self.expression = expression
        try:
            result = eval(self.expression)
            print(result, end = "")
            return result
        except Exception:
            Error("calculation")

################################
# String
################################

class String:
    def __init__(self, value=""):
        self.value = value

    def __repr__(self):
        return f'String("{self.value}")'

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, String):
            return String(self.value + other.value)
        elif isinstance(other, str):
            return String(self.value + other)
        else:
            raise TypeError(f"{Fore.RED}Unsupported operand type for +{Fore.YELLOW}")

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, String):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def interpret_command(command):
    tokens = command.split("+")
    result = String()

    for token in tokens:
        token = token.strip()
        if token.startswith('"') and token.endswith('"'):
            result += token.strip('"')
        elif token.startswith("'") and token.endswith("'"):
            result += token.strip("'")
        else:
            raise ValueError(f"{Fore.RED}Invalid token:{Fore.YELLOW}" + token)

    return result

################################
# Libraries
################################

class Libraries:
    def __init__(self, ln):
        self.ln = ln
        self.name = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        lib = open(self.name, "rb")
        lines = lib.readlines()
        self.rln = 0
        self.libln = lines[self.rln]
        if (self.libln.__contains__("rc = ")):
            self.runCommand()
        lib.close()

    def runCommmand(self):
        self.cmd = self.ln[self.ln.find("(") + 1 : self.ln.find(")")]
        if (self.cmd.__contains__("line[") and self.cmd.__contains__("]")):
            p = interpret_command(self.cmd[self.cmd.find("[") + 1 : self.cmd.find("]")])
            print(p)

################################
# Classes
################################

class Classes:
    pass

################################
# Variables
################################

floats = {}
ints = {}
strings = {}
booleans = {}

class Var:
    def __init__(self, type, ln, new):
        self.type = type
        self.ln = ln
        if (new):
            if (self.type == "int"):
                self.newInt()
            elif (self.type == "string"):
                self.newString()
            elif (self.type == "boolean"):
                self.newBoolean()
        if (new == False):
            if (self.type == "int" and self.ln.__contains__("+=") or self.type == "int" and self.ln.__contains__("-=") or self.type == "int" and self.ln.__contains__("*=") or self.ln.__contains__("/=") and self.type == "int"):
                self.useInt()

    def newInt(self):
        name = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        declaration = "0"
        if (self.ln.__contains__("§int <" + name + "> = {") and self.ln.__contains__("}")):
            declaration = self.ln[self.ln.find("{") + 1 : self.ln.find("}")]
        math = Math(declaration)
        num = math.calculate(declaration)
        ints[name] = num
        print(ints)
    
    #Unfinished
    def useInt(self):
        name = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        changeType = None
        if (self.ln.__contains__("+=")):
            changeType = "+"
        elif (self.ln.__contains__("-=")):
            changeType = "-"
        elif (self.ln.__contains__("*=")):
            changeType = "*"
        elif (self.ln.__contains__("/=")):
            changeType = "/"
        else:
            changeType = "+"
        change = self.ln[self.ln.find("{") + 1 : self.ln.find("}")]
        math = Math(change)
        num = math.calculate(change)
        if (num is not None):
            if (changeType == "+"):
                ints[name] += num
            elif (changeType == "-"):
                ints[name] -= num
            elif (changeType == "*"):
                ints[name] *= num
            elif (changeType == "/"):
                ints[name] /= num
            else:
                Error.unkownCalculation()
            print(ints)
        else:
            Error.calculation()

    def newString(self):
        name = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        declaration = "\"NULL\""
        if (self.ln.__contains__(f"§string <{name}> = " + "{") and self.ln.__contains__("};")):
            declaration = self.ln[self.ln.find("{") + 1 : self.ln.find("};")]
        true_declaration = interpret_command(declaration)
        strings[name] = true_declaration
        print(strings)
        print(f"{Fore.YELLOW}This command isn't finished.{Fore.WHITE}")

    def newBoolean(self):
        name = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        declaration = False
        if (self.ln.__contains__(f"§bool <{name}> = " + "{") and self.ln.__contains__("};")):
            declaration = self.ln[self.ln.find("{") + 1 : self.ln.find("};")]
            if (declaration == "true"):
                declaration = True
            elif (declaration == "false"):
                declaration = False
        else:
            declaration = False
        booleans[name] = declaration


################################
# Time
################################

class Time:
    def __init__(self, ln):
        self.ln = ln
        if (self.ln.__contains__("Time::sleep")):
            self.sleep()

    def sleep(self):
        wait = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
        waiting = int(wait)
        time.sleep(waiting / 1000)

################################
# System
################################

class SystemVariables:
    tests = 1

class System:
    def __init__(self, ln):
        self.ln = ln
        self.tests = SystemVariables.tests

        if (self.ln.__contains__(".out.")):
            self.out()
        elif (self.ln.__contains__(".in.")):
            self.in_()
        elif (self.ln.__contains__("System.test();")):
            self.test()
        elif (self.ln.__contains__("System.changeColor(") and self.ln.__contains__(");")):
            self.changeColor();

    def out(self):
        if (self.ln.__contains__("System.out.println(") and self.ln.__contains__(");")):
            text = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            result = interpret_command(text)
            print(result)
        elif (self.ln.__contains__("System.out.print(") and self.ln.__contains__(");")):
            text = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            result = interpret_command(text)
            print(result, end = "")
        elif (self.ln.__contains__(".out.math.")):
            self.outMath()
        elif (self.ln.__contains__("System.out.var.print(") and self.ln.__contains__(");")):
            printVar = self.ln[self.ln.find("(") + 1 : self.ln.__contains__(");")]
            if (printVar == "tests"):
                print(SystemVariables.tests, end = "")
        elif (self.ln.__contains__("System.out.\\n();")):
            print("\n"),

    def outMath(self):
        if (self.ln.__contains__("System.out.math.print(") and self.ln.__contains__(");")):
            cal = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            Math.printMath(self, cal)
        elif (self.ln.__contains__("System.out.math.printVar(") and self.ln.__contains__(");")):
            cal = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            fVar = cal.find[cal.find("<") + 1 : cal.find(">")]
            sVar = cal.find[cal.find("{") + 1 : cal.find("}")]
            true_cal = ''
            for char in cal:
                if (char != '<' and char != '>' and char != '{' and char != '}'):
                    true_cal += char
            print("This command is unfinished.")
            

    def in_(self):
        if (self.ln.__contains__("System.in.input(") and self.ln.__contains__(");")):
            input(self.ln[self.ln.find("(") + 1 : self.ln.find(");")])
        elif (self.ln.__contains__("System.in.outInput(")):
            i = input(self.ln[self.ln.find("(") + 1 : self.ln.find(");")])
            print(i)

    def test(self):
        print(f"Test {self.tests} done...")
        SystemVariables.tests += 1

    def changeColor(self):
        color = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
        if (color == "white"):
            print(f"{Fore.WHITE}"),
        elif (color == "yellow"):
            print(f"{Fore.YELLOW}"),
        elif (color == "blue"):
            print(f"{Fore.BLUE}"),
        elif (color == "green"):
            print(f"{Fore.GREEN}"),
        elif (color == "cyan"):
            print(f"{Fore.CYAN}"),
        elif (color == "lightblueEX"):
            print(f"{Fore.LIGHTBLUE_EX}"),
        elif (color == "red"):
            print(f"{Fore.RED}"),
        elif (color == "lightcyanEX"):
            print(f"{Fore.LIGHTCYAN_EX}"),
        elif (color == "lightgreenEX"):
            print(f"{Fore.LIGHTGREEN_EX}"),
        elif (color == "magenta"):
            print(f"{Fore.MAGENTA}"),
        elif (color == "lightmagentEX"):
            print(f"{Fore.LIGHTMAGENTA_EX}"),
        elif (color == "lightredEX"):
            print(f"{Fore.LIGHTRED_EX}"),
        elif (color == "lightyellowEX"):
            print(f"{Fore.LIGHTYELLOW_EX}"),
        elif (color == "lightblackEX" or color == "grey"):
            print(f"{Fore.LIGHTBLACK_EX}"),
        elif (color == "reset"):
            print(f"{Fore.RESET}"),
        elif (color == "black"):
            print(f"{Fore.BLACK}"),

#################################################
# std
#################################################

class std:
    def __init__(self, ln):
        self.ln = ln
        if (self.ln.__contains__("std::pressKey")):
            self.pressKey()
        elif (self.ln.__contains__("std::System32.cmd")):
            self.system()

    def pressKey(self):
        if (PLVar.keyBoardIsImported):
            kb = Controller()
            key = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            if (key == "key.down"):
                kb.press(Key.down)
                kb.release(Key.down)
            elif (key == "key.up"):
                kb.press(Key.up)
                kb.release(Key.down)
            elif (key == "key.left"):
                kb.press(Key.left)
                kb.release(Key.left)
            elif (key == "key.right"):
                kb.press(Key.right)
                kb.release(Key.right)
            elif (key == "alt"):
                kb.press(Key.alt)
                kb.release(Key.alt)
            elif (Key == "alt_gr"):
                kb.press(Key.alt_gr)
                kb.release(Key.alt_gr)
            else:
                kb.press(key)
                kb.release(key)
        else:
            print(f"{Fore.RED}Error: Missing modules/libraries when using: \"std::pressKey()\".\n  Module/Library missing: <keyBoard>{Fore.YELLOW}")

    def system(self):
        if (PLVar.STDSystemIsImported):
            cmd = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            true_cmd = interpret_command(cmd)
            os.system(true_cmd)
        
#################################################
# if
#################################################

class If:
    def __init__(self, ln):
        self.ln = ln
        self.isTrue = False
        if (self.ln.__contains__("(bool")):
            self.bool()
        elif (self.ln.__contains__("(int")):
            self.int()
        else:
            Error("ifDataType")

        if (self.isTrue == False and self.ln.__contains__(") {")):
            PLVar.dontRun = True
        else:
            PLVar.dontRun = False

    def bool(self):
        boolean = self.ln[self.ln.find("<") + 1 : self.ln.find(">")]
        if (self.ln.__contains__(" == true")):
            if (booleans[boolean] == True):
                self.isTrue = True
            else:
                self.isTrue = False
        else:
            if (booleans[boolean] == False):
                self.isTrue = True
            else:
                self.isTrue = False

    def int(self):
        integer = self.ln[self.ln.find(".<") + 2 : self.ln.find(">.")]
        if (self.ln.__contains__(" == [")):
            compare = self.ln[self.ln.find("[") + 1 : self.ln.find("]")]
            trueCompare = int(compare)
            if (ints[integer] == trueCompare):
                self.isTrue = True
            else:
                self.isTrue = False
        elif (self.ln.__contains__(" <= [")):
            compare = self.ln[self.ln.find("[") + 1 : self.ln.find("]")]
            trueCompare = int(compare)
            if (ints[integer] <= trueCompare):
                self.isTrue = True
            else:
                self.isTrue = False
        elif (self.ln.__contains__(" >= [")):
            compare = self.ln[self.ln.find("[") + 1 : self.ln.find("]")]
            trueCompare = int(compare)
            if (ints[integer] >= trueCompare):
                self.isTrue = True
            else:
                self.isTrue = False
        elif (self.ln.__contains__(" < [")):
            compare = self.ln[self.ln.find("[") + 1 : self.ln.find("]")]
            trueCompare = int(compare)
            if (ints[integer] < trueCompare):
                self.isTrue = True
            else:
                self.isTrue = False
        elif (self.ln.__contains__(" > [")):
            compare = self.ln[self.ln.find("[") + 1 : self.ln.find("]")]
            trueCompare = int(compare)
            if (ints[integer] > trueCompare):
                self.isTrue = True
            else:
                self.isTrue = False
        else:
            self.isTrue = False

#################################################
# Code reading
#################################################

def main():
    with open(path, "r") as f:
        lines = f.readlines()
        rln = 0
        ln = lines[rln]
        linesInFile = sum(1 for _ in open("main.ep", "rb"))
        #print("\n\n")
        #This line here is to check if the Code works properly
            #print(linesInFile)
        while (True):
            #code reader:
            if (ln != ""):
                if (PLVar.dontRun == False):
                    if (ln.__contains__("§System.")):
                        System(ln)
                    if (ln.__contains__("§int")):
                        Var("int", ln, True)
                    elif (ln.__contains__("$int")):
                        Var("int", ln, False)
                    if (ln.__contains__("@error")):
                        AtError(ln)
                    if (ln.__contains__("§string")):
                        Var("string", ln, True)
                    if (ln.__contains__("§boolean")):
                        Var("boolean", ln, True)
                    if (ln.__contains__("goto")):
                        line = ln[ln.find("(") + 1 : ln.find(");")]
                        intline = int(line)
                        rln = intline - 2
                    if (ln.__contains__("§Time")):
                        Time(ln)
                    if (ln.__contains__("std::")):
                        std(ln)
                    if (ln.__contains__("§if")):
                        If(ln)
                    if (ln.__contains__("skipline();")):
                        rln += 1
                    if (ln.__contains__("§install(EOS);")):
                        eos = open("EOS", "w")
                        eos.close()
                if (ln.__contains__("}") and PLVar.dontRun == True):
                    PLVar.dontRun = False
            
            #Checking if line there
            if (rln == linesInFile - 1):
                break;
            else:
                rln += 1;
                ln = lines[rln]
main()

#only to remember for me
#print(int("1000"))
#text1 = "!aO"
#text2 = text1[text1.find("!")+1:text1.find("O")]
