from pathlib import Path
import colorama
from colorama import Fore, Back, Style
import time

colorama.init()

path = input("E§.Compile> ")
app = open("app.py", "w")

print("Compiling...")

###############################
# Error
###############################

print(f"{Fore.RED}Loading Errors...")

class Error:
    def __init__(self, error):
        if (error == "calculation"):
            self.calculation()
        elif (error == "unknownCalculation"):
            self.unknowCalculation()
        elif (error == "testError"):
            self.testError()

    def calculation(self):
        print(f"{Fore.RED}CalculationError(): Calculation failed due to unknown mathematical characters.\n")
    
    def unknowCalculation(self):
        print(f"{Fore.RED}UnkownCalculationError(): Something went wrong when calculating an integer.\n")

    def testError(self):
        print(f"{Fore.RED}This Error is just a test, you shouldn't run into it, if you aren't testing the error msg.\n")

#######################
# Compiling
#######################

print(f"{Fore.LIGHTMAGENTA_EX}Loading Math...")

class Math:
    result = 0
    def __init__(self, expression):
        self.expression = expression

    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            Error("calculation")
            return None
        
    def printMath(self, expression):
        self.expression = expression
        try:
            result = eval(self.expression)
            #print(result),
            return result
        except Exception:
            Error("calculation")

class SystemVariables:
    tests = 1

print(f"{Fore.BLUE}Loading class::System...")

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
            app.write(f"print(\"{text}\")\n")
        elif (self.ln.__contains__("System.out.print(") and self.ln.__contains__(");}\n")):
            text = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            app.write(f"print(\"{text}\"),\n")
        elif (self.ln.__contains__(".out.math.")):
            self.outMath()
        elif (self.ln.__contains__("System.out.var.print(") and self.ln.__contains__(");")):
            printVar = self.ln[self.ln.find("(") + 1 : self.ln.__contains__(");")]
            if (printVar == "tests"):
                app.write(f"print(\"{SystemVariables.tests}\")\n")
        elif (self.ln.__contains__("System.out.\\n();")):
            app.write(f"print(\"\\n\"),\n")

    def outMath(self):
        if (self.ln.__contains__("System.out.math.print(") and self.ln.__contains__(");")):
            math = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            Math.calculate(self, math)
            app.write(f"print({math}),\n")

    def in_(self):
        if (self.ln.__contains__("System.in.input(") and self.ln.__contains__(");")):
            cursor = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            app.write(f"input(\"{cursor}\")\n")
        elif (self.ln.__contains__("System.in.outInput(")):
            cursor = self.ln[self.ln.find("(") + 1 : self.ln.find(");")]
            app.write(f"NULL = input(\"{cursor}\")\nprint(NULL)\n")

    def test(self):
        SystemVariables.tests += 1
    
print(f"{Fore.WHITE}Compiling Started...")

def main():
    print("Compiling (Reading File)...")
    with open(path, "r") as f:
        lines = f.readlines()
        rln = 0
        ln = lines[rln]
        linesInFile = sum(1 for _ in open("main.ep", "rb"))
        print("\n\n")

        #This line here is to check if the Code works properly
            #print(linesInFile)
        print("Compiling (Writing File [app.py])...")
        while (True):
            #code reader:
            if (ln != ""):
                if (ln.__contains__("§System.")):
                    System(ln)
                if (ln == "§@error(test);"):
                    Error("testError")

            
            #Checking if line there
            if (rln == linesInFile - 1):
                break;
            else:
                rln += 1;
                ln = lines[rln]
main()

print(f"{Fore.GREEN}Compiling finished...")
input()