########################################### GRUPO Nathan ####################################
from fractions import Fraction
def Abc(x: float) -> str:
    """
    Converte número em fração.
      Ab/c normal -> fração imprópria
      SHIFT + Ab/c -> número misto
    """
    frac = Fraction(x).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"
    

# print(Abc(eval("25÷85+12÷25")))

#DC
from fractions import Fraction
def Dc(x: float) -> str:
    frac = Fraction(x).limit_denominator()
    
    inteiro, resto = divmod(frac.numerator, frac.denominator)
    if inteiro == 0:
        return f"{resto}/{frac.denominator}"
    elif resto == 0:
        return str(inteiro)
    else:
        return f"{inteiro} {resto}/{frac.denominator}"

print(Dc(20.5))

# print(Abc(eval("25÷85+12÷25")))

#ENG
import math
def ENG(x: float) -> str:
    """
    Converte número para notação de engenharia.
    SHIFT + ENG -> volta para decimal.
    """
    if x == 0:
        return "0"
    exp = int((math.log10(abs(x)) / 3) * 3)
    mantissa = x / (10 ** exp)
    return f"{mantissa}×10^{exp}"

#ln
from math import log
def fnLn(s: str) -> float:
    """ln(x). SHIFT -> e^x. ALPHA -> constante e."""
    formula = s
    if "ln" in formula:
        formula = formula.strip()
        value = float(formula.removeprefix("ln"))
    else:
        raise ValueError("log não está definido")
    if value <= 0:
        raise ValueError("ln indefinido para x <= 0")
    return log(value)

#LOG10
from math import log10
def fnLog10(s: str) -> float:
    """log10(x). SHIFT -> 10^x."""
    formula = s
    if "log" in formula:
        formula = formula.strip()
        value = float(formula.removeprefix("log"))
    if value <= 0:
        raise ValueError("log indefinido para x <= 0")
    return log10(value)

#POL

from math import radians, cos;

def Pol(s) -> float:
    s = s.replace("Pol(", "")
    if ")" in s: 
        s = s.replace(")", "")
    print(s)
    if "," not in s:
        raise ValueError("Faltando argumento em Pol(x, y)")
    n, k = s.split(",")
    if not n or not k:
        raise ValueError("Argumentos inválidos em Pol(x, y)")
    print(n, k)
    return ((float(n) ** 2 + float(k) ** 2) ** (1/2))

#Rec

from math import radians, cos;
def Rec(s):    
    s = s.replace("Rec(", "");
    s = s.replace(")", "");
    n, k = s.split(",")
    return (float(n) * cos(radians(float(k))))

#nCR
from math import factorial;
def nCr(s):
    if "C" in s:
        n,k= s.split("C")
        return factorial(int(n)) // (factorial(int(k)) * factorial(int(n) - int(k)))

#nPr
from math import factorial;
def nPr(s):
    if "P" in s:
        n,k = s.split("P")
        return factorial(int(n)) // factorial(int(n) - int(k))

#TwoPoint
def twoPoints(s):
    if("Ans" in s):
        s = s.replace("Ans", "")
        s = s.replace("x","*")
        expressions = s.split(":");

        for i in range(len(expressions)):
            if i==0:
                expressions[i] = eval(expressions[i])
            else:
                expression = str(expressions[i-1])+""+str(expressions[i])
                expressions[i] = eval(expression)
        return expressions
    else:
        return ValueError("Sintax Error: Ans não informado")
    ################################### FIM GRUPO Nathan ########################
