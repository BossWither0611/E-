from pathlib import Path
import colorama
from colorama import Fore, Back, Style
import time

colorama.init()

path = input("E§> ")

#Var

hasMainVoid = False
functionIsRunned = False
hasMainClass = False
classIsRunned = False

###############################
# Error
###############################

class Error:
    def __init__(self, error):
        if (error == "calculation"):
            self.calculation()
        elif (error == "unknownCalculation"):
            self.unknowCalculation()
        elif (error == "testError"):
            self.testError()

    def calculation(self):
        print(f"{Fore.RED}CalculationError(): Calculation failed due to unknown mathematical characters.{Fore.YELLOW}\n")
    
    def unknowCalculation(self):
        print(f"{Fore.RED}UnkownCalculationError(): Something went wrong when calculating an integer.{Fore.YELLOW}\n")

    def testError(self):
        print(f"{Fore.RED}This Error is just a test, you shouldn't run into it, if you aren't testing the error msg.{Fore.YELLOW}\n")

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
            print(f"Error: {str(e)}")
            return None
        
    def printMath(self, expression):
        self.expression = expression
        try:
            result = eval(self.expression)
            print(result),
            return result
        except Exception:
            Error("calculation")

################################
# String
################################

class String:
    def __init__(self):
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
        if (self.type == "int" and new == True):
            self.newInt()
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

    def out(self):
        if (self.ln.__contains__("System.out.println(") and self.ln.__contains__(");")):
            text = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            txt = text
            print(txt)
        elif (self.ln.__contains__("System.out.print(") and self.ln.__contains__(");")):
            text = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            txt = text
            print(txt),
        elif (self.ln.__contains__(".out.math.")):
            self.outMath()
        elif (self.ln.__contains__("System.out.var.print(") and self.ln.__contains__(");")):
            printVar = self.ln[self.ln.find("(") + 1 : self.ln.__contains__(");")]
            if (printVar == "tests"):
                print(SystemVariables.tests),
        elif (self.ln.__contains__("System.out.\\n();")):
            print("\n"),

    def outMath(self):
        if (self.ln.__contains__("System.out.math.print(") and self.ln.__contains__(");")):
            cal = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            Math.printMath(self, cal)

    def in_(self):
        if (self.ln.__contains__("System.in.input(") and self.ln.__contains__(");")):
            input(self.ln[self.ln.find("(") + 1 : self.ln.find(");")])
        elif (self.ln.__contains__("System.in.outInput(")):
            i = input(self.ln[self.ln.find("(") + 1 : self.ln.find(");")])
            print(i)

    def test(self):
        print(f"Test {self.tests} done...")
        SystemVariables.tests += 1

#################################################
# Code reading
#################################################

def main():
    with open(path, "r") as f:
        lines = f.readlines()
        rln = 0
        ln = lines[rln]
        linesInFile = sum(1 for _ in open("main.ep", "rbU"))
        print("\n\n")

        #This line here is to check if the Code works properly
            #print(linesInFile)
        while (True):
            #code reader:
            if (ln != ""):
                if (ln.__contains__("§System.")):
                    System(ln)
                if (ln.__contains__("§int")):
                    Var("int", ln, True)
                elif (ln.__contains__("$int")):
                    Var("int", ln, True)
                if (ln == "§@error(test);"):
                    Error("testError")

            
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
