from tkinter import *
from tkinter import ttk
import tkinter as tk
import math
import ast
import operator as op
import re
ans = 0
yaux = 45
xaux = 18
xauxoffset = 11
yauxoffset = 10
windowX = 210
windowY = 310
ciencia = False
shift = False
alpha = False
menu_s_sum_ativo = False
menu_s_var_ativo = False
values = ["#"]          # Lista de dígitos digitados
operation = [0, "#", 0] # [valor1, operador, valor2]
aIndex = 0              # Índice para operação
memory_slots = {
  "A": "4",
  "B": "5",
  "C": "0",
  "D": "0",
  "E": "8",
  "F": "0",
  "G": "0",
  "X": "0",
  "Y": "0",
  "M": "0"
}








################# CODIGO ADICIONADO GRUPO CAIKE ####################
def processar_operador_basico(operador):
    global operation, Number1
    
    operador_simples = operador.strip().replace("X", "*").replace("÷", "/")
    
    if operation[1] == "#":  
        operation[0] = float(Number1.replace(",", "."))
        operation[1] = operador_simples
        Number1 = "0"
        Display.set(Number1)
    else:  
        operation[2] = float(Number1.replace(",", "."))
        resultado = res()
        operation[0] = resultado
        operation[1] = operador_simples
        operation[2] = 0
        Number1 = str(resultado)
        Display.set(Number1)

def res():
    try:
        a = operation[0]
        b = operation[2]
        op = operation[1]

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return "Erro" if b == 0 else a / b
        else:
            return b
    except:
        return "Erro"

def reset_values(result):
    global values, operation, aIndex, Number1
    values = ["#"]
    operation = [result, "#", 0]
    aIndex = 0
    Number1 = str(result)
    Display.set(Number1)

def calc_raiz():
    global Number1, values
    try:
        n = float(Number1.replace(",", "."))
        res = math.sqrt(n)
        reset_values(res)
    except:
        Display.set("Erro")

def calc_raiz_cubica():
    global Number1, values
    try:
        n = float(Number1.replace(",", "."))
        res = n ** (1/3)
        reset_values(res)
    except:
        Display.set("Erro")

def calc_radiciacao():
    global values, operation, aIndex, Number1
    try:
        if operation[1] == "rad":
            radicando = float(Number1.replace(",", "."))
            indice = operation[0]
            if indice == 0:
                Display.set("Erro")
            else:
                res = radicando ** (1/indice)
                reset_values(res)
        else:
            indice = float(Number1.replace(",", "."))
            operation[0] = indice
            operation[1] = "rad"
            values = ["#"]
            Number1 = str(indice) + "√"
            Display.set(Number1)
    except:
        Display.set("Erro")
        
def calc_inverso():
    global Number1, shift
    
    if shift:
        calc_fatorial()
        shift = False  
        return
    try:
        n = float(Number1.replace(",", "."))
        if n == 0:
            Display.set("Erro")
        else:
            res = 1 / n
            reset_values(res)
    except:
        Display.set("Erro")
def calc_fatorial():
    global Number1
    try:
        n = int(float(Number1.replace(",", ".")))
        if n < 0:
            Display.set("Erro")
        else:
            res = math.factorial(n)
            reset_values(res)
    except:
        Display.set("Erro")

def calc_quadrado():
    global Number1
    try:
        n = float(Number1.replace(",", "."))
        res = n**2
        reset_values(res)
    except:
        Display.set("Erro")

def calc_cubo():
    global Number1,shift
    if (shift):
            res = calc_raiz_cubica()
            shift = not shift
    else:
        try:
           n = float(Number1.replace(",", "."))
           res = n**3
           reset_values(res)
        
        except:
            Display.set("Erro")

def calc_exponenciacao():
    global values, operation, aIndex, Number1, shift
    
  
    if shift:
        calc_raiz_cubica()
        shift = False 
        return
    
    try:
        if operation[1] == "^":
            expoente = float(Number1.replace(",", "."))
            base = operation[0]
            res = base ** expoente
            reset_values(res)
            
        else:
            base = float(Number1.replace(",", "."))
            operation[0] = base
            operation[1] = "^"
            values = ["#"]
            Number1 = str(base) + "^"
            Display.set(Number1)
    except:
        Display.set("Erro")
################# FIM DO CODIGO ADICIONADO GRUPO CAIKE ####################
def  fnPi():
    pi = math.pi
menu_drg_ativo = False

def ativar_menu_s_var():
    limpar()
    global menu_s_var_ativo
    menu_s_var_ativo = True
    Display.set("1-x̅   2-xσn   3-xσn-1") 

def ativar_menu_s_sum():
    limpar()
    global menu_s_sum_ativo
    menu_s_sum_ativo = True
    Display.set("1-Σx    2-Σx²   3-n")

def ativar_menu_drg():
    """Ativa o menu DRG quando Shift + Ans é pressionado"""
    global menu_drg_ativo
    menu_drg_ativo = True
    Display.set("D-1 R-2 G-3")

def inserir_simbolo_angular(opcao):
    """Insere o símbolo angular baseado na opção escolhida"""
    global menu_drg_ativo, Number1
    
    simbolos = {
        1: "°",
        2: "r", 
        3: "g"
    }
    
    if opcao in simbolos:
        Number1 += simbolos[opcao]
        Display.set(formatarcontaessao(Number1))
    
    menu_drg_ativo = False

def fnExp(valor):
    try:
       
        resultado = math.pow(10,float(valor))
        return (resultado)
    except:
        return "Erro"
def get_slotValues():
    return [float(v) for v in memory_slots.values()]

def media_x():
    valores = get_slotValues()
    return sum(valores) / len(valores) if valores else 0

def desvio_populacional():
    valores = get_slotValues()
    n = len(valores)
    if n == 0:
        return 0
    mean = media_x()
    return (sum((x - mean) ** 2 for x in valores) / n) ** 0.5

def desvio_amostral():
    valores = get_slotValues()
    n = len(valores)
    if n <= 1:
        return 0
    mean = media_x()
    return (sum((x - mean) ** 2 for x in valores) / (n - 1)) ** 0.5

def fnSoma_x():
    return sum(get_slotValues())

def fnSoma_x2():
    return sum(x ** 2 for x in get_slotValues())

def fnQuantidade_n():
    valores = get_slotValues()
    return sum(1 for v in valores if v != 0)
def fnHSIN(valor):
    """Seno hiperbólico"""
    try:
        return math.sinh(float(valor))
    except:
        return "Erro"

def fnHCOS(valor):
    """Cosseno hiperbólico"""
    try:
        return math.cosh(float(valor))
    except:
        return "Erro"

def fnHTAN(valor):
    """Tangente hiperbólica"""
    try:
        return math.tanh(float(valor))
    except:
        return "Erro"

def fnHSIN_INV(valor):
    """Arco seno hiperbólico (hsin⁻¹)"""
    try:
        return math.asinh(float(valor))
    except:
        return "Erro"

def fnHCOS_INV(valor):
    """Arco cosseno hiperbólico (hcos⁻¹)"""
    try:
        return math.acosh(float(valor))
    except:
        return "Erro"

def fnHTAN_INV(valor):
    """Arco tangente hiperbólica (htan⁻¹)"""
    try:
        return math.atanh(float(valor))
    except:
        return "Erro"
def fnSIN_INV(valor):
    """Arco seno (sin⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.asin(float(valor)))
    except:
        return "Erro"

def fnCOS_INV(valor):
    """Arco cosseno (cos⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.acos(float(valor)))
    except:
        return "Erro"

def fnTAN_INV(valor):
    """Arco tangente (tan⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.atan(float(valor)))
    except:
        return "Erro"
def fnSIN(valor):
    try:
        valor_em_graus = converter_para_graus(valor)
        resultado = math.sin(math.radians(valor_em_graus))
        return str(resultado)
    except Exception as e:
        print(f"Erro em fnSIN: {e}")
        return "Erro"

def fnCOS(valor):
    try:
        valor_em_graus = converter_para_graus(valor)
        resultado = math.cos(math.radians(valor_em_graus))
        return str(resultado)
    except Exception as e:
        print(f"Erro em fnCOS: {e}")
        return "Erro"

def fnTAN(valor):
    try:
        valor_em_graus = converter_para_graus(valor)
        resultado = math.tan(math.radians(valor_em_graus))
        return str(resultado)
    except Exception as e:
        print(f"Erro em fnTAN: {e}")
        return "Erro"
def converter_para_graus(valor_str):
  
    try:
        
        valor_str = str(valor_str).strip().lower()
        
        if '°' in valor_str:
            numero = valor_str.replace('°', '')
            return float(numero)
        
        elif 'r' in valor_str:
            numero = valor_str.replace('r', '')
            if 'π' in numero:
                if numero == 'π':
                    return math.degrees(math.pi)
                else:
                    multiplicador = numero.replace('π', '')
                    if multiplicador == '':
                        multiplicador = 1
                    else:
                        multiplicador = float(multiplicador)
                    return math.degrees(multiplicador * math.pi)
            else:
                return math.degrees(float(numero))
        
        elif 'g' in valor_str:
            numero = valor_str.replace('g', '')
            return float(numero) * 0.9
        
        else:
            return float(valor_str)
            
    except ValueError as e:
        print(f"Erro ao converter {valor_str}: {e}")
        return float(valor_str)  
    except Exception as e:
        print(f"Erro inesperado com {valor_str}: {e}")
        return 0.0

OPERADORES = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}
def converter_notacao_inversa(conta):
    """
    Converte notação matemática sin⁻¹, cos⁻¹, tan⁻¹ para asin, acos, atan
    """
    conta = conta.replace('sin⁻¹', 'asin')
    conta = conta.replace('cos⁻¹', 'acos') 
    conta = conta.replace('tan⁻¹', 'atan')
    return conta

def converter_notacao_hiperbolica_inversa(conta):
    """
    Converte notação matemática hsin⁻¹, hcos⁻¹, htan⁻¹ para hasin, hacos, hatan
    """
    conta = conta.replace('hsin⁻¹', 'hasin')
    conta = conta.replace('hcos⁻¹', 'hacos')
    conta = conta.replace('htan⁻¹', 'hatan')
    return conta

FUNCOES = {
    'sin': fnSIN,
    'cos': fnCOS,
    'tan': fnTAN,
    'asin': fnSIN_INV,   
    'acos': fnCOS_INV,  
    'atan': fnTAN_INV,  
    'sqrt': math.sqrt,
    'log': math.log10, 
    'exp': fnExp,
    'pi': fnPi,

    'hsin': fnHSIN,
    'hcos': fnHCOS,
    'htan': fnHTAN,

    'hasin': fnHSIN_INV, 
    'hacos': fnHCOS_INV,  
    'hatan': fnHTAN_INV,
    
    # ADICIONE ESTAS NOVAS FUNÇÕES:
    'raiz': math.sqrt,           # raiz(x) - raiz quadrada
    'cbrt': lambda x: x ** (1/3), # cbrt(x) - raiz cúbica
    'quad': lambda x: x ** 2,     # quad(x) - quadrado
    'cubo': lambda x: x ** 3,     # cubo(x) - cubo
    'inv': lambda x: 1/x,         # inv(x) - inverso
    'fat': math.factorial,        # fat(x) - fatorial
}
virgulas = True  
operadores = [" + ", " - ", " X ", " ÷ ","sin("]
oper_dict = {" X ": "*", " ÷ ": "/"}

root = Tk()
root.resizable(width=False, height=False)
root.title("Calculadora")
root.geometry(f"{windowX}x{windowY}")

frm = ttk.Frame(root, width=windowX, height=windowY)
frm.grid()

Display = StringVar(value="0")
Number1 = "0"


def paudrao():
    global windowX
    global windowY
    global xauxoffset
    global yauxoffset
    global xaux
    global yaux
    global ciencia
    windowX = 210
    windowY = 310
    root.geometry(f"{windowX}x{windowY}")
    frm.config(width=windowX, height=windowY)
    xauxoffset = 11
    yauxoffset = 10
    yaux = 45
    xaux = 18
    ciencia = False
    limpar()
    socorro_me_ajuda(True)
    
def ciess():
    global windowX
    global windowY
    global xauxoffset
    global yauxoffset
    global xaux
    global yaux
    global ciencia
    windowX = 300
    windowY = 510
    root.geometry(f"{windowX}x{windowY}")
    frm.config(width=windowX, height=windowY)
    xauxoffset = -2
    yauxoffset = 10
    yaux= 60
    xaux= 18
    ciencia = True
    limpar()
    socorro_me_ajuda(False)

def socorro_me_ajuda(oi):
    if(oi):
        but11.config(command= lambda: inserir_porcentagem(), background="#f0f0f0", text="%", height=2, width=5)
        but12.config(command= lambda: inserir_1barranum(), text="1/X", background="#f0f0f0")
        but13.config(command= lambda: inserir_numero(7), background="#f0f0f0")
        but14.config(command= lambda: inserir_numero(4), background="#f0f0f0")
        but15.config(command= lambda: inserir_numero(1), background="#f0f0f0")
        but16.config(command= lambda: inserir_numero(0), background="#f0f0f0")

        but21.config(command= lambda: limpar_entrada(), background="#f0f0f0", text="CE", height=2, width=5)
        but22.config(command= lambda: inserir_quadrado(), background="#f0f0f0", text="X²", height=2, width=5)
        but23.config(command= lambda: inserir_numero(8), background="#f0f0f0")
        but24.config(command= lambda: inserir_numero(5), background="#f0f0f0")
        but25.config(command= lambda: inserir_numero(2), background="#f0f0f0")
        but26.config(command= lambda: inserir_virgula(), text=",", background="#f0f0f0")

        but31.config(command= limpar ,text="C", background="#f0f0f0")
        but32.config(command= lambda: inserir_raiz(), text="²√X", background="#f0f0f0")
        but33.config(command= lambda: inserir_numero(9), background="#f0f0f0")
        but34.config(command= lambda: inserir_numero(6), background="#f0f0f0")
        but35.config(command= lambda: inserir_numero(3), background="#f0f0f0")
        but36.config(command= resultado, width=12, background="#f0f0f0")

        but41.config(command= backspace, text="⌫", background="#f0f0f0")
        but42.config(command= lambda: inserir_operador(" ÷ "), background="#f0f0f0")
        but43.config(command= lambda: inserir_operador(" X "), background="#f0f0f0")
        but44.config(command= lambda: inserir_operador(" - "), background="#f0f0f0")
        but45.config(command= lambda: inserir_operador(" + "), background="#f0f0f0")
                         
                           ### COLUNA 1

        but11.place(x=xaux - xauxoffset, y=yaux * 1 - yauxoffset)
        but12.place(x=xaux - xauxoffset, y=yaux * 2 - yauxoffset)
        but13.place(x=xaux - xauxoffset, y=yaux * 3 - yauxoffset)
        but14.place(x=xaux - xauxoffset, y=yaux * 4 - yauxoffset)
        but15.place(x=xaux - xauxoffset, y=yaux * 5- yauxoffset)
        but16.place(x=xaux - xauxoffset, y=yaux * 6 - yauxoffset)
                           
                            ### COLUNA 2

        but21.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 1 - yauxoffset)
        but22.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 2 - yauxoffset)
        but23.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 3 - yauxoffset)
        but24.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 4 - yauxoffset)
        but25.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 5- yauxoffset)
        but26.place(x=(xaux * (3.7)) - xauxoffset, y=yaux * 6 - yauxoffset)
                         
                           ### COLUNA 3

        but31.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 1 - yauxoffset)
        but32.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 2 - yauxoffset)
        but33.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 3 - yauxoffset)
        but34.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 4 - yauxoffset)
        but35.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 5- yauxoffset)
        but36.place(x=(xaux * (3.7 * 1.72)) - xauxoffset, y=yaux * 6 - yauxoffset)
                       
                           ### COLUNA 4

        but41.place(x=(xaux * (3.7 * 2.46)) - xauxoffset, y=yaux * 1 - yauxoffset)
        but42.place(x=(xaux * (3.7 * 2.46)) - xauxoffset, y=yaux * 2 - yauxoffset)
        but43.place(x=(xaux * (3.7 * 2.46)) - xauxoffset, y=yaux * 3 - yauxoffset)
        but44.place(x=(xaux * (3.7 * 2.46)) - xauxoffset, y=yaux * 4 - yauxoffset)
        but45.place(x=(xaux * (3.7 * 2.46)) - xauxoffset, y=yaux * 5- yauxoffset)
        
        output.place(x = 19 - xauxoffset, y = 14 - yauxoffset)
        output.config(width= 17)
        
        butCrep1.place(x=9999)
        butCrep2.place(x=9999)
        butCrep3.place(x=9999)
        butCrep4.place(x=9999)
        butC15.place(x=9999)
        butC16.place(x=9999)
        butC21.place(x=9999)
        butC22.place(x=9999)
        butC23.place(x=9999)
        butC24.place(x=9999)
        butC25.place(x=9999)
        butC33.place(x=9999)
        butC34.place(x=9999)
        butC35.place(x=9999)
        butC43.place(x=9999)
        butC44.place(x=9999)
        butC45.place(x=9999)
        butC51.place(x=9999)
        butC52.place(x=9999)
        butC53.place(x=9999)
        butC54.place(x=9999)
        butC55.place(x=9999)
        butC61.place(x=9999)
        butC62.place(x=9999)
        butC63.place(x=9999)
        butC64.place(x=9999)
        butC65.place(x=9999)
        text1.place(x=9999)
        text2.place(x=9999)
        text3.place(x=9999)
        text4.place(x=9999)
        text5.place(x=9999)
        text6.place(x=9999)
        text7.place(x=9999)
        text8.place(x=9999)
        text9.place(x=9999)
        text10.place(x=9999)
        text11.place(x=9999)
        text12.place(x=9999)
        text13.place(x=9999)
        text14.place(x=9999)
        text15.place(x=9999)
        text16.place(x=9999)
        text17.place(x=9999)
        text18.place(x=9999)
        text19.place(x=9999)
        text20.place(x=9999)
        text21.place(x=9999)
        text22.place(x=9999)
        text23.place(x=9999)
        text24.place(x=9999)
        text25.place(x=9999)
        text26.place(x=9999)
        text27.place(x=9999)
        text28.place(x=9999)
        text29.place(x=9999)
        text30.place(x=9999)
        text31.place(x=9999)
        text32.place(x=9999)
        text33.place(x=9999)
        text34.place(x=9999)
        text35.place(x=9999)
        text36.place(x=9999)
        text37.place(x=9999)
        text38.place(x=9999)
        text39.place(x=9999)
        text40.place(x=9999)
        text41.place(x=9999)
                
    else:

        but11.config(command=lambda: inserir_raiz(), background="#f0f0f0")
        but12.config(command= lambda: inserir_exp(), text="EXP", background="#f0f0f0")
        but13.config(command= lambda: inserir_numero(7), background="#f0f0f0")
        but14.config(command= lambda: inserir_numero(4), background="#f0f0f0")
        but15.config(command= lambda: inserir_numero(1), background="#f0f0f0")
        but16.config(command= lambda: inserir_numero(0), background="#f0f0f0")

        but21.config(command= lambda: limpar_entrada(), background="#f0f0f0")
        but22.config(command= lambda: inserir_quadrado(), background="#f0f0f0")
        but23.config(command= lambda: inserir_numero(8), background="#f0f0f0")
        but24.config(command= lambda: inserir_numero(5), background="#f0f0f0")
        but25.config(command= lambda: inserir_numero(2), background="#f0f0f0")
        but26.config(command=lambda:inserir_virgula() , text=".", background="#f0f0f0")

        but31.config(command= limpar ,text="AC", background="red")
        but32.config(command= lambda:inserir_ans(), text="Ans", background="#f0f0f0")
        but33.config(command= lambda: inserir_numero(9), background="#f0f0f0")
        but34.config(command= lambda: inserir_numero(6), background="#f0f0f0")
        but35.config(command= lambda: inserir_numero(3), background="#f0f0f0")
        but36.config(command=resultado, width=5, background="#f0f0f0")

        but41.config(command= backspace, text="DEL", background="red")
        but42.config(command= lambda: inserir_operador(" ÷ "), background="#f0f0f0")
        but43.config(command= lambda: inserir_operador(" X "), background="#f0f0f0")
        but44.config(command= lambda: inserir_operador(" - "), background="#f0f0f0")
        but45.config(command= lambda: inserir_operador(" + "), background="#f0f0f0")
                        
                           ### COLUNA 1

        but13.place(x=xaux - xauxoffset, y=yaux * 1 - yauxoffset + 225)
        but14.place(x=xaux - xauxoffset, y=yaux * 2 - yauxoffset + 225)
        but15.place(x=xaux - xauxoffset, y=yaux * 3- yauxoffset + 225)
        text34.place(x=xaux - xauxoffset + 5, y=yaux * 3 - yauxoffset + 210)
        but16.place(x=xaux - xauxoffset, y=yaux * 4 - yauxoffset + 225)
        text35.place(x=xaux - xauxoffset + 5, y=yaux * 4 - yauxoffset + 210)
                        
                           ### COLUNA 2

        but23.place(x=(xaux * (4)) - xauxoffset, y=yaux * 1 - yauxoffset + 225)
        but24.place(x=(xaux * (4)) - xauxoffset, y=yaux * 2 - yauxoffset + 225)
        but25.place(x=(xaux * (4)) - xauxoffset, y=yaux * 3- yauxoffset + 225)
        text36.place(x=(xaux * (4)) - xauxoffset + 5, y=yaux * 3 - yauxoffset + 210)
        but26.place(x=(xaux * (4)) - xauxoffset, y=yaux * 4 - yauxoffset + 225)
        text37.place(x=(xaux * (4)) - xauxoffset + 5, y=yaux * 4 - yauxoffset + 210)

                           ### COLUNA 3

        but33.place(x=(xaux * (4 * 1.72)) - xauxoffset, y=yaux * 1 - yauxoffset + 225)
        but34.place(x=(xaux * (4 * 1.72)) - xauxoffset, y=yaux * 2 - yauxoffset + 225)
        but35.place(x=(xaux * (4 * 1.72)) - xauxoffset, y=yaux * 3- yauxoffset + 225)
        but12.place(x=(xaux * (4 * 1.72)) - xauxoffset, y=yaux * 4 - yauxoffset + 225)
        text38.place(x=(xaux * (4 * 1.72)) - xauxoffset + 5, y=yaux * 4 - yauxoffset + 210)
     
                           ### COLUNA 4

        text39.place(x=(xaux * (4 * 2.46)) - xauxoffset + 10, y=yaux * 1 - yauxoffset + 208)
        but41.place(x=(xaux * (4 * 2.46)) - xauxoffset, y=yaux * 1 - yauxoffset + 225)
        but43.place(x=(xaux * (4 * 2.46)) - xauxoffset, y=yaux * 2 - yauxoffset + 225)
        but45.place(x=(xaux * (4 * 2.46)) - xauxoffset, y=yaux * 3- yauxoffset + 225)
        but32.place(x=(xaux * (4 * 2.46)) - xauxoffset, y=yaux * 4 - yauxoffset + 225)
        text40.place(x=(xaux * (4 * 2.46)) - xauxoffset + 10, y=yaux * 4 - yauxoffset + 210)
        
                           ### COLUNA 5

        but31.place(x=(xaux * (4 * 3.19)) - xauxoffset, y=yaux * 1 - yauxoffset + 225)
        but42.place(x=(xaux * (4 * 3.19)) - xauxoffset, y=yaux * 2 - yauxoffset + 225)
        but44.place(x=(xaux * (4 * 3.19)) - xauxoffset, y=yaux * 3 - yauxoffset + 225)
        but36.place(x=(xaux * (4 * 3.19)) - xauxoffset, y=yaux * 4 - yauxoffset + 225)
        text41.place(x=(xaux * (4 * 3.19)) - xauxoffset + 10, y=yaux * 4 - yauxoffset + 210)

                        ### COLUNA CIENTIFICA 1

        text1.place(x=xaux - xauxoffset + 1, y=yaux * (0.85) - yauxoffset + 11)
        but21.config(height=1, width=3, text="", command=lambda:mudarShift())
        but21.place(x=(xaux) - xauxoffset, y=yaux * (0.85) - yauxoffset + 25)
        text6.place(x=(xaux) - xauxoffset + 10, y=yaux * (1.5) - yauxoffset + 12)
        but11.config(height=1, width=3, text="X⁻¹", command=calc_inverso)
        but11.place(x=(xaux) - xauxoffset, y=yaux * (1.5) - yauxoffset + 25)
        text7.place(x=(xaux) - xauxoffset + 10, y=yaux * (2.175) - yauxoffset + 11)
        but22.config(height=1, width=3, text="ab/c", command= "")
        but22.place(x=(xaux) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        text8.place(x=(xaux) - xauxoffset + 10, y=yaux * (2.85) - yauxoffset + 11)
        butC15.place(x=(xaux) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC15.config(height=1, width=3)
        text9.place(x=(xaux) - xauxoffset + 5, y=yaux * (3.55) - yauxoffset + 10)
        butC16.place(x=(xaux) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC16.config(height=1, width=3)
        
                        ### COLUNA CIENTIFICA 2
                      
        text2.place(x=(xaux * 3.5) - xauxoffset + 1, y=yaux * (0.85) - yauxoffset + 11)
        butC21.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (0.85) - yauxoffset + 25)
        butC21.config(height=1, width=3)
        text10.place(x=(xaux * 3.5) - xauxoffset + 3, y=yaux * (1.5) - yauxoffset + 12)
        butC22.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (1.5) - yauxoffset + 25)
        butC22.config(height=1, width=3)
        butC23.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        butC23.config(height=1, width=3,command=calc_raiz)
        text11.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 12)
        text12.place(x=(xaux * 3.5) - xauxoffset + 20, y=yaux * (2.85) - yauxoffset + 12)
        butC24.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC24.config(height=1, width=3)
        text13.place(x=(xaux * 3.5) - xauxoffset + 10, y=yaux * (3.55) - yauxoffset + 12)
        butC25.place(x=(xaux * 3.5) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC25.config(height=1, width=3)
        
                        ### COLUNA CIENTIFICA 3
                        
        butCrep1.place(x=(xaux * 7.2) - xauxoffset, y=yaux * (0.85) - yauxoffset + 25)
        butCrep4.place(x=(xaux * 5.9) - xauxoffset, y=yaux * (1.175) - yauxoffset + 25)
        butCrep3.place(x=(xaux * 7.2) - xauxoffset, y=yaux * (1.5) - yauxoffset + 25)
        butCrep2.place(x=(xaux * 8.5) - xauxoffset, y=yaux * (1.175) - yauxoffset + 25)
        butC33.place(x=(xaux * 5.9) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        butC33.config(height=1, width=3,command=calc_quadrado)
        text14.place(x=(xaux * 5.9) - xauxoffset + 20, y=yaux * (2.85) - yauxoffset + 12)
        butC34.place(x=(xaux * 5.9) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC34.config(height=1, width=3, command=lambda:inserir_H())
        butC35.place(x=(xaux * 5.9) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC35.config(height=1, width=3)
        
                        ### COLUNA CIENTIFICA 4
        
        text15.place(x=(xaux * 8.5) - xauxoffset + 10, y=yaux * (2.175) - yauxoffset + 12)
        butC43.place(x=(xaux * 8.5) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        butC43.config(height=1, width=3,command=calc_exponenciacao)
        text16.place(x=(xaux * 8.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 12)
        text17.place(x=(xaux * 8.5) - xauxoffset + 20, y=yaux * (2.85) - yauxoffset + 12)
        butC44.place(x=(xaux * 8.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC44.config(height=1, width=3, command=lambda:(inserir_sin()))
        text18.place(x=(xaux * 8.5) - xauxoffset + 10, y=yaux * (3.55) - yauxoffset + 12)
        butC45.place(x=(xaux * 8.5) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC45.config(height=1, width=3)
        
                        ### COLUNA CIENTIFICA 5

        text3.place(x=(xaux * 11) - xauxoffset - 2, y=yaux * (0.85) - yauxoffset + 11)
        butC51.place(x=(xaux * 11) - xauxoffset, y=yaux * (0.85) - yauxoffset + 25)
        butC51.config(height=1, width=3)
        text19.place(x=(xaux * 11) - xauxoffset, y=yaux * (1.5) - yauxoffset + 12)
        text20.place(x=(xaux * 11) - xauxoffset + 25, y=yaux * (1.5) - yauxoffset + 12)
        butC52.place(x=(xaux * 11) - xauxoffset, y=yaux * (1.5) - yauxoffset + 25)
        butC52.config(height=1, width=3)
        text21.place(x=(xaux * 11) - xauxoffset + 10, y=yaux * (2.175) - yauxoffset + 12)
        butC53.place(x=(xaux * 11) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        butC53.config(height=1, width=3)
        text22.place(x=(xaux * 11) - xauxoffset, y=yaux * (2.85) - yauxoffset + 12)
        text23.place(x=(xaux * 11) - xauxoffset + 20, y=yaux * (2.85) - yauxoffset + 12)
        butC54.place(x=(xaux * 11) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC54.config(height=1, width=3, command=lambda:(inserir_cos()))
        text24.place(x=(xaux * 11) - xauxoffset, y=yaux * (3.55) - yauxoffset + 12)
        text25.place(x=(xaux * 11) - xauxoffset + 20, y=yaux * (3.55) - yauxoffset + 12)
        butC55.place(x=(xaux * 11) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC55.config(height=1, width=3)
        
                        ### COLUNA CIENTIFICA 6
        
        text4.place(x=(xaux * 13.5) - xauxoffset - 12, y=yaux * (0.85) - yauxoffset + 13)
        text5.place(x=(xaux * 13.5) - xauxoffset + 15, y=yaux * (0.85) - yauxoffset + 11)
        butC61.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (0.85) - yauxoffset + 25)
        butC61.config(height=1, width=3)
        text26.place(x=(xaux * 13.5) - xauxoffset + 5, y=yaux * (1.5) - yauxoffset + 12)
        butC62.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (1.5) - yauxoffset + 25)
        butC62.config(height=1, width=3,command=calc_cubo)
        text27.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (2.175) - yauxoffset + 12)
        text28.place(x=(xaux * 13.5) - xauxoffset + 20, y=yaux * (2.175) - yauxoffset + 12)
        butC63.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (2.175) - yauxoffset + 25)
        butC63.config(height=1, width=3)
        text29.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 12)
        text30.place(x=(xaux * 13.5) - xauxoffset + 20, y=yaux * (2.85) - yauxoffset + 12)
        butC64.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (2.85) - yauxoffset + 25)
        butC64.config(height=1, width=3, command=lambda:(inserir_tan()))
        text31.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (3.55) - yauxoffset + 12)
        text32.place(x=(xaux * 13.5) - xauxoffset + 20, y=yaux * (3.55) - yauxoffset + 12)
        text33.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (4.175) - yauxoffset + 12)
        butC65.place(x=(xaux * 13.5) - xauxoffset, y=yaux * (3.55) - yauxoffset + 25)
        butC65.config(height=1, width=3)
        
        output.place(x = 19 - xauxoffset, y = 35 - yauxoffset)
        output.config(width= 23)

def inserir_ans():
    global Number1
    if (shift):
        ativar_menu_drg()
    else:
        Number1 += "Ans"
        Display.set(formatarcontaessao(Number1))
def armazenar_em_variavel(variavel, valor=None):
    global ans, memory_slots
    
    if valor is None:
        valor = ans
    
    if variavel.upper() in memory_slots:
        memory_slots[variavel.upper()] = valor
        return True
    else:
        return False
def mudarShift():
    global shift
    shift = not shift
def mudarAlpha():
    global alpha
    shift = not alpha
def inserir_pi():
    global Number1
    Number1 += "π"  
    Display.set(Number1)
def inserir_H():
    global Number1
    Number1 += "h"
    Display.set(formatarcontaessao(Number1))
def inserir_funcao_hiperbolica(funcao_base):
    global Number1
    Number1 += f"h{funcao_base}("
    Display.set(formatarcontaessao(Number1))
def inserir_exp():
    global Number1
    if (shift):
        inserir_pi()
    else:
        Number1 += "exp("
        Display.set(Number1)
    
        
def inserir_sin():
    global shift, Number1
    if shift:
        Number1 += "sin⁻¹("
        shift = False 
    else:
        Number1 += "sin("
    Display.set(formatarcontaessao(Number1))

def inserir_cos():
    global shift, Number1
    if shift:
        Number1 += "cos⁻¹("
        shift = False
    else:
        Number1 += "cos("
    Display.set(formatarcontaessao(Number1))

def inserir_tan():
    global shift, Number1
    if shift:
        Number1 += "tan⁻¹("
        shift = False
    else:
        Number1 += "tan("
    Display.set(formatarcontaessao(Number1))
    
def remover_zeros_esquerda(expr):

    return re.sub(r'\b0+(\d+)\b', r'\1', expr)

def substituir_sin(expr):
    i = 0
    while i < len(expr):
        if expr[i:i+4] == "sin(":
            count = 1
            j = i + 4
            while j < len(expr) and count > 0:
                if expr[j] == "(":
                    count += 1
                elif expr[j] == ")":
                    count -= 1
                j += 1
            parte_sin = expr[i:j] 
            resultado = fnSIN(parte_sin)
            expr = expr[:i] + resultado + expr[j:]
            i += len(resultado)  
        else:
            i += 1
    return expr


def formatarMilhares(valor):
    if "," in valor:
        parte_inteira, parte_decimal = valor.split(",")
    else:
        parte_inteira, parte_decimal = valor, False

    parte_inteira = parte_inteira.replace(".", "")
    partes = []
    while len(parte_inteira) > 3:
        partes.insert(0, parte_inteira[-3:])
        parte_inteira = parte_inteira[:-3]
    if parte_inteira:
        partes.insert(0, parte_inteira)
    parte_formatada = ".".join(partes)

    if parte_decimal is not False:
        return parte_formatada + "," + parte_decimal
    else:
        return parte_formatada

def calcular(conta):
    try:
        conta = conta.replace(".", "")
        operador_encontrado = None
        for oper in operadores:
            if oper in conta:
                operador_encontrado = oper
                break
        if operador_encontrado is None:
            valor = conta.replace(",", ".")
            resultado = float(valor)
        else:
            partes = conta.split(operador_encontrado)
            if len(partes) < 2 or partes[1].strip() == "":
                partes = [partes[0], partes[0]]
            num1 = float(partes[0].replace(",", "."))
            num2 = float(partes[1].replace(",", "."))
            if operador_encontrado == " + ":
                resultado = num1 + num2
            elif operador_encontrado == " - ":
                resultado = num1 - num2
            elif operador_encontrado == " X ":
                resultado = num1 * num2
            elif operador_encontrado == " ÷ ":
                if num2 == 0:
                    return "Não é possível dividir por zero"
                resultado = num1 / num2
            else:
                return "Erro"

        resultado_str = str(resultado).replace(".", ",")
        if resultado_str.endswith(",0"):
            resultado_str = resultado_str[:-2]
        return resultado_str

    except ZeroDivisionError:
        return "Não é possível dividir por zero"
    except Exception:
        return "Erro"

def limpar():
    global Number1, virgulas
    if ciencia:
        Number1 = ""
    else:
        Number1 = "0"
    virgulas = True  
    Display.set(Number1)

def inserir_numero(value):
    global Number1, virgulas, menu_drg_ativo, menu_s_sum_ativo,shift,menu_s_var_ativo
    
    
    
    if shift and value == 1:
        ativar_menu_s_sum()
        shift = False 
        return

    if shift and value == 2:
            ativar_menu_s_var()
            shift = False
            return
    if menu_s_sum_ativo:
        if value == 1:
            Number1 = str(fnSoma_x())   
        elif value == 2:
            Number1 = str(fnSoma_x2())
        elif value == 3:
            Number1 = str(fnQuantidade_n())
        else:
            menu_s_sum_ativo = False
            return
        Display.set(Number1)
        menu_s_sum_ativo = False
        return
    
    if menu_s_var_ativo:
        if value == 1:
            Number1 = str(media_x())
        elif value == 2:
            Number1 = str(desvio_populacional())
        elif value == 3:
            Number1 = str(desvio_amostral())
        else:
            menu_s_var_ativo = False
            return
        Display.set(Number1)
        menu_s_var_ativo = False
        return
    if menu_drg_ativo:
        if value in (1, 2, 3):
            inserir_simbolo_angular(value)
            return
        else:
            menu_drg_ativo = False

    if ciencia:
        raw = Number1
    else:
        raw = Number1.replace(".", "")
    
    for oper in operadores:
        if oper in raw:
            partes = Number1.split(oper)
            if partes[-1] == "0" or partes[-1] == "0," or partes[-1] == "0.":
                partes[-1] = str(value)
            else:
                partes[-1] += str(value)
            Number1 = oper.join(partes)
            Display.set(formatarcontaessao(Number1))
            virgulas = True
            return
    
    if raw == "0":
        Number1 = str(value)
    else:
        Number1 += str(value)
    
    Display.set(formatarcontaessao(Number1))
    virgulas = True
    
def inserir_virgula():
    global Number1, virgulas
    if not virgulas:
        return
    
    separador = "." if ciencia else ","
    
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
            if partes[-1] == "":
                partes[-1] = "0" + separador
            else:
                partes[-1] += separador
            Number1 = oper.join(partes)
            virgulas = False  
            Display.set(formatarcontaessao(Number1))
            return
    
    if Number1 == "":
        Number1 = "0" + separador
    else:
        Number1 += separador
    
    virgulas = False  
    Display.set(formatarcontaessao(Number1))

def backspace():
    global Number1, virgulas
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
            ultimo = partes[-1]
            ultimo = ultimo[:-1]
            if ultimo == "":
                partes = partes[:-1]
                if (len(partes) == 0):
                    Number1 = "0"
                    virgulas = True
                    Display.set(Number1)
                    return
                Number1 = oper.join(partes)
                virgulas = True 
            else:
                partes[-1] = ultimo
                Number1 = oper.join(partes)
                virgulas = True
            Display.set(formatarcontaessao(Number1))
            return
    Number1 = Number1[:-1]
    if Number1 == "":
        Number1 = "0"
        virgulas = True
    else:
        virgulas = True
    Display.set(formatarcontaessao(Number1))
def inserir_operador(value):
    global Number1, virgulas, ciencia

    Number1 = str(Number1)

    # --- Modo científica ---
    if ciencia:
        if value in ["sin(", "cos(", "tan("]:
            Number1 += value
            virgulas = True
            Display.set(formatarcontaessao(Number1))
            return

 
        if Number1.strip() == "" and value != "-":
            return

        Number1 += value
        virgulas = True
        Display.set(formatarcontaessao(Number1))
        return

    # --- Modo padrão ---

    if Number1.replace(".", "", 1).isdigit() and value in operadores:
        Number1 += value
        virgulas = False  
        Display.set(formatarcontaessao(Number1))
        return


    if Number1 == "0" and value != "-":
        Number1 = value
        virgulas = False if value.isdigit() else True
        Display.set(formatarcontaessao(Number1))
        return

 
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
         
            if len(partes) == 2 and partes[1].strip() != "":
                resultado_val = calcular(Number1)
                if resultado_val == "Não é possível dividir por zero":
                    limpar()
                    Display.set("Não é possível dividir por zero")
                    return
               
                Number1 = str(resultado_val) + value
                virgulas = False  
                Display.set(formatarcontaessao(Number1))
                return
            else:
               
                Number1 = partes[0] + value
                virgulas = False
                Display.set(formatarcontaessao(Number1))
                return

  
    if len(Number1) >= 1 and Number1[-1] in operadores and value in operadores:
        return

  
    Number1 += value


    if value == ".":
        if virgulas: 
            return
        virgulas = True

    Display.set(formatarcontaessao(Number1))
def resultado():
    global Number1, virgulas, ciencia
    
    if ciencia:
        resultado = calcular_cientifica(Number1)
    else:
        resultado = calcular(Number1)
    
    if resultado == "Não é possível dividir por zero" or resultado == "Erro":
        limpar()
        Display.set("Erro")
    else:
        Number1 = str(resultado)
        Display.set(formatarcontaessao(Number1))
        virgulas = True
def formatarcontaessao(conta):
    global ciencia
    if ciencia:
    
        return conta
    else:
        for oper in operadores:
            if oper in conta:
                partes = conta.split(oper)
                parte1 = formatarMilhares(partes[0])
                parte2 = formatarMilhares(partes[1]) if len(partes) > 1 else ""
                return parte1 + oper + parte2
        return formatarMilhares(conta)




def fnSIN(valor):
    try:
        print(f"fnSIN recebeu: {valor}")
      
        valor_em_graus = converter_para_graus(valor)
        print(f"fnSIN convertido: {valor} -> {valor_em_graus} graus")
        resultado = math.sin(math.radians(valor_em_graus))
        return str(resultado)
    except Exception as e:
        print(f"Erro em fnSIN: {e}")
        return "Erro"
def fnCOS(valor):
    try:
        resultado = math.cos(math.radians(float(valor)))
        return str(resultado)
    except:
        return "Erro"

def fnTAN(valor):
    try:
        resultado = math.tan(math.radians(float(valor)))
        return str(resultado)
    except:
        return "Erro"

def processar_expressao_com_unidades(expressao):
    """
    Processa expressões com unidades angulares como: 3r + 45° * 2g
    """
   
    padrao = r'(\d*\.?\d+)(°|r|g)'
    
 
    matches = re.finditer(padrao, expressao)
    
    for match in matches:
        numero = match.group(1)      
        unidade = match.group(2)    
        valor_original = match.group(0) 
        
       
        if unidade == '°':
            valor_convertido = float(numero)  
        elif unidade == 'r':
            valor_convertido = math.degrees(float(numero))
        elif unidade == 'g':
            valor_convertido = float(numero) * 0.9 
        
    
        expressao = expressao.replace(valor_original, str(valor_convertido))
    
    return expressao
def processar_funcoes_hiperbolicas(conta):
    """
    Processa TODAS as funções hiperbólicas: normais e inversas
    """

    funcoes_hiperbolicas = [
     
        'hsin(', 'hcos(', 'htan(',
  
        'hsin⁻¹(', 'hcos⁻¹(', 'htan⁻¹('
    ]
    
   
    for func_hiper in funcoes_hiperbolicas:
        if func_hiper in conta:
          
            pass
    
    return conta
def processar_funcoes_inversas(conta):
    """
    Processa funções trigonométricas inversas: sin⁻¹, cos⁻¹, tan⁻¹
    """
    funcoes_inversas = ['sin⁻¹(', 'cos⁻¹(', 'tan⁻¹(']
    
    for func_inversa in funcoes_inversas:
        if func_inversa in conta:
       
            pass
    
    return conta
def calcular_cientifica(conta):
    global ans, memory_slots
    
    try:
        conta = converter_notacao_inversa(conta)
        conta = converter_notacao_hiperbolica_inversa(conta)
        conta = processar_funcoes_inversas(conta)
        conta = processar_funcoes_hiperbolicas(conta)
        conta = processar_expressao_com_unidades(conta)
        
        # Resto do processamento normal...
        conta = conta.replace("Ans", str(ans))

        conta = conta.replace("^", "**")
        conta = conta.replace("π", str(math.pi))
        conta = conta.replace("X", "*").replace("÷", "/").replace(",", ".")
        conta = remover_zeros_esquerda(conta)
        conta = processar_simbolos_angulares(conta)
        for var, valor in memory_slots.items():
            conta = conta.replace(var, str(valor))

        abertos = conta.count('(')
        fechados = conta.count(')')
        conta += ')' * (abertos - fechados)
        
        tree = ast.parse(conta, mode='eval')

        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                return OPERADORES[type(node.op)](_eval(node.left), _eval(node.right))
            elif isinstance(node, ast.UnaryOp):
                return OPERADORES[type(node.op)](_eval(node.operand))
            elif isinstance(node, ast.Call):
                func = node.func.id
                if func in FUNCOES:
                    args = [_eval(arg) for arg in node.args]
                    return FUNCOES[func](*args)
                else:
                    raise ValueError(f"Função não permitida: {func}")
            else:
                raise TypeError(node)

        resultado = _eval(tree.body)
        ans = resultado
        return resultado

    except Exception as e:
        return f"Erro em calcular_cientifica: {e}"

def botaooperacao(texto, x, y, comando):
    Button(frm, text=texto, height=2, width=4, command=comando).place(x=x, y=y)

def obter_numeros():
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
            num1 = partes[0].replace(".", "")
            num2 = partes[1].replace(".", "") if len(partes) > 1 else None
            return (num1, oper, num2)
    return (Number1.strip().replace(".", ""), None, None)

def inserir_1barranum():
    global Number1, virgulas
    separado1, oper, separado2 = obter_numeros()

    if separado2 == "0" or (separado2 is None and separado1 == "0"):
        Number1 = "0"
        virgulas = True
        Display.set("Não é possível dividir por zero")
        return

    try:
        if separado2 is not None:
            invertido = 1 / float(separado2.replace(",", "."))
            invertido_str = f"{invertido:.10f}".rstrip("0").rstrip(".")
            invertido_str = invertido_str.replace(".", ",")
            Number1 = f"{separado1}{oper}{invertido_str}"
        else:
            invertido = 1 / float(separado1.replace(",", "."))
            invertido_str = f"{invertido:.10f}".rstrip("0").rstrip(".")
            invertido_str = invertido_str.replace(".", ",")
            Number1 = invertido_str

        Display.set(formatarcontaessao(Number1))
        virgulas = True
    except ZeroDivisionError:
        limpar()
        Display.set("Não é possível dividir por zero")

def inserir_raiz():
    global Number1, virgulas
    separado1, oper, separado2 = obter_numeros()

    if separado2 == "0" or (separado2 is None and separado1 == "0"):
        Number1 = "0"
        virgulas = True
        Display.set("Não é possível dividir por zero")
        return

    try:
        if separado2 is not None:
            invertido = math.sqrt(float(separado2.replace(",", ".")))
            invertido_str = f"{invertido:.10f}".rstrip("0").rstrip(".")
            invertido_str = invertido_str.replace(".", ",")
            Number1 = f"{separado1}{oper}{invertido_str}"
        else:
            invertido = math.sqrt(float(separado1.replace(",", ".")))
            invertido_str = f"{invertido:.10f}".rstrip("0").rstrip(".")
            invertido_str = invertido_str.replace(".", ",")
            Number1 = invertido_str

        Display.set(formatarcontaessao(Number1))
        virgulas = True
    except ZeroDivisionError:
        limpar()
        Display.set("Não é possível dividir por zero")



def processar_simbolos_angulares(conta):
    """
    Processa símbolos angulares em funções trigonométricas
    Ex: sin(45°) -> sin(45), cos(πr) -> cos(180), tan(100g) -> tan(90)
    """
    try:
        # Padrões para encontrar funções trigonométricas com símbolos angulares
        padroes = [
            r'(sin|cos|tan)\(([^)]+)(°|r|g)\)',
            r'(sin|cos|tan)\(([^)]+)(°|r|g)',
        ]
        
        for padrao in padroes:
            matches = re.finditer(padrao, conta, re.IGNORECASE)
            for match in matches:
                funcao = match.group(1) 
                valor = match.group(2)  
                simbolo = match.group(3) 
                print(f"Processando: {funcao}({valor}{simbolo})")
                
               
                valor_com_simbolo = valor + simbolo
                valor_em_graus = converter_para_graus(valor_com_simbolo)
                
                print(f"Convertido: {valor_com_simbolo} -> {valor_em_graus} graus")
                
               
                conta_original = f"{funcao}({valor}{simbolo})"
                conta_nova = f"{funcao}({valor_em_graus})"
                conta = conta.replace(conta_original, conta_nova)
                
                conta_original2 = f"{funcao}({valor}{simbolo}"
                conta_nova2 = f"{funcao}({valor_em_graus}"
                conta = conta.replace(conta_original2, conta_nova2)
    
    except Exception as e:
        print(f"Erro em processar_simbolos_angulares: {e}")
    
    return conta

def inserir_quadrado():
    global Number1, virgulas
    separado1, oper, separado2 = obter_numeros()
    try:
        if separado2 is not None:
            quadrado = (float(separado2.replace(",", "."))) * (float(separado2.replace(",", ".")))
            quadrado_str = f"{quadrado:.10f}".rstrip("0").rstrip(".")
            quadrado_str = quadrado_str.replace(".", ",")
            Number1 = f"{separado1}{oper}{quadrado_str}"
        else:
            quadrado = (float(separado1.replace(",", "."))) * (float(separado1.replace(",", ".")))
            quadrado_str = f"{quadrado:.10f}".rstrip("0").rstrip(".")
            quadrado_str = quadrado_str.replace(".", ",")
            Number1 = quadrado_str

        Display.set(formatarcontaessao(Number1))
        virgulas = True
    except ZeroDivisionError:
        limpar()
        Display.set("Não é possível dividir por zero")

def inserir_porcentagem():
    global Number1, virgulas
    separado1, oper, separado2 = obter_numeros()

    if separado2 == "0" or (separado2 is None and separado1 == "0"):
        Number1 = "0"
        virgulas = True
        Display.set("Não é possível dividir por zero")
        return
    try:
        if separado2 is not None:
            resultado = ((float(separado2.replace(",", "."))) / 100) * (float(separado1.replace(",", ".")))
            resultado_str = f"{resultado:.10f}".rstrip("0").rstrip(".")
            resultado_str = resultado_str.replace(".", ",")
            Number1 = f"{separado1}{oper}{resultado_str}"
        else:
            resultado = ((float(separado1.replace(",", "."))) / 100) * (float(separado1.replace(",", ".")))
            resultado_str = f"{resultado:.10f}".rstrip("0").rstrip(".")
            resultado_str = resultado_str.replace(".", ",")
            Number1 = resultado_str


        Display.set(formatarcontaessao(Number1))
        virgulas = True
    except ZeroDivisionError:
        limpar()
        Display.set("Não é possível dividir por zero")

def limpar_entrada():
    global Number1, virgulas
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
            if len(partes) == 2:
                Number1 = partes[0] + oper
                virgulas = True 
                Display.set(formatarcontaessao(Number1))
                return
    Number1 = "0"
    virgulas = True
    Display.set(Number1)

def atualizar_display():
    global Number1
    Display.set(formatarcontaessao(Number1))
    output.icursor(tk.END)

def on_key_press(event):
    global Number1, virgulas

    key = event.keysym
    char = event.char

    numeros = "0123456789"
    operadores_teclado = {"+": " + ", "-": " - ", "*": " X ", "/": " ÷ "}

    if key in ("BackSpace", "Delete"):
        return 

    if key in ("Left", "Right", "Home", "End"):
        return

    if char in numeros:
        if Number1 == "0":
            Number1 = char
        else:
            for oper in operadores:
                if oper in Number1:
                    partes = Number1.split(oper)
                    partes[-1] += char
                    Number1 = oper.join(partes)
                    break
            else:
                Number1 += char
        virgulas = True 
        atualizar_display()
        return "break"

    if char == ",":
        if not virgulas:
            return "break"
        for oper in operadores:
            if oper in Number1:
                partes = Number1.split(oper)
                if partes[-1] == "":
                    partes[-1] = "0,"
                else:
                    partes[-1] += ","
                Number1 = oper.join(partes)
                virgulas = False 
                atualizar_display()
                return "break"
        else:
            if Number1 == "":
                Number1 = "0,"
            else:
                Number1 += ","
            virgulas = False
            atualizar_display()
        return "break"

    if char in operadores_teclado:
        oper_formatado = operadores_teclado[char]

        if Number1 == "0" and char == "-":
            Number1 = "-"
        for oper in operadores:
            if oper in Number1:
                partes = Number1.split(oper)
                if len(partes) == 2 and partes[1].strip() != "":
                    res = calcular(Number1)
                    if res == "Não é possível dividir por zero":
                        limpar()
                        Display.set(res)
                        return "break"
                    Number1 = res + oper_formatado
                else:
                    Number1 = partes[0] + oper_formatado
                virgulas = True 
                atualizar_display()
                return "break"
        if len(Number1) >= 3 and Number1[-3:] in operadores:
            return "break"
        Number1 += oper_formatado
        virgulas = True 
        atualizar_display()
        return "break"
    return "break"

def on_key_release(event):
    global Number1, virgulas

    texto = output.get()

    for oper in operadores:
        texto = texto.replace(oper, oper.strip())

    texto = texto.replace(".", "")

    for simb, oper in {"+": " + ", "-": " - ", "X": " X ", "÷": " ÷ "}.items():
        texto = texto.replace(simb, oper)

    Number1 = texto
    virgulas = True
    for oper in operadores:
        if oper in Number1:
            partes = Number1.split(oper)
            virgulas = "," not in partes[-1]
            break
    else:
        virgulas = "," not in Number1

    atualizar_display()

output = tk.Entry(frm, width= 17, font=("Arial", 15), justify="right", textvariable=Display)
output.place(x = 19 - xauxoffset, y = 14 - yauxoffset)
output.focus()
output.bind("<Key>", on_key_press)
output.bind("<KeyRelease>", on_key_release)
output.bind("<Return>", lambda event: resultado())


# coluna 1


but11 = Button(frm, text="%", height=2, width=5, command= lambda: inserir_porcentagem())
but12 = Button(frm, text="1/X", height=2, width=5, command= lambda: inserir_1barranum())
but13 = Button(frm, text="7", height=2, width=5, command= lambda: inserir_numero(7))
but14 = Button(frm, text="4", height=2, width=5, command= lambda: inserir_numero(4))
but15 = Button(frm, text="1", height=2, width=5, command= lambda: inserir_numero(1))
but16 = Button(frm, text="0", height=2, width=5, command= lambda: inserir_numero(0))


# coluna 2


but21 = Button(frm, text="CE", height=2, width=5, command= lambda: limpar_entrada())
but22 = Button(frm, text="X²", height=2, width=5, command= lambda: inserir_quadrado())
but23 = Button(frm, text="8", height=2, width=5, command= lambda: inserir_numero(8))
but24 = Button(frm, text="5", height=2, width=5, command= lambda: inserir_numero(5))
but25 = Button(frm, text="2", height=2, width=5, command= lambda: inserir_numero(2))
but26 = Button(frm, text=",", height=2, width=5, command= lambda: inserir_virgula())


# coluna 3


but31 = Button(frm, text="C", height=2, width=5, command= limpar)
but32 = Button(frm, text="²√X", height=2, width=5, command= lambda: inserir_raiz())
but33 = Button(frm, text="9", height=2, width=5, command= lambda: inserir_numero(9))
but34 = Button(frm, text="6", height=2, width=5, command= lambda: inserir_numero(6))
but35 = Button(frm, text="3", height=2, width=5, command= lambda: inserir_numero(3))
but36 = Button(frm, text="=", height=2, width=12, command=resultado)


# coluna 4


but41 = Button(frm, text="⌫", height=2, width=5, command= backspace)
but42 = Button(frm, text="÷", height=2, width=5, command= lambda: inserir_operador(" ÷ "))
but43 = Button(frm, text="x", height=2, width=5, command= lambda: inserir_operador(" X "))
but44 = Button(frm, text="-", height=2, width=5, command= lambda: inserir_operador(" - "))
but45 = Button(frm, text="+", height=2, width=5, command= lambda: inserir_operador(" + "))


# ciencia:

butC15 = Button(frm, text="(-)", height=1, width=3, command="", background="#f0f0f0")
butC16 = Button(frm, text="RCL", height=1, width=3, command="", background="#f0f0f0")


butC21 = Button(frm, text="", height=1, width=3, command="", background="#f0f0f0")
butC22 = Button(frm, text="nCr", height=1, width=3, command="", background="#f0f0f0")
butC23 = Button(frm, text="√", height=1, width=3, command="", background="#f0f0f0")
butC24 = Button(frm, text="., ,,", height=1, width=3, command="", background="#f0f0f0")
butC25 = Button(frm, text="ENG", height=1, width=3, command="", background="#f0f0f0")

butCrep1 = Button(frm, text="↑", height=1, width=3, command="", background="#f0f0f0")
butCrep2 = Button(frm, text="→", height=1, width=3, command="", background="#f0f0f0")
butCrep3 = Button(frm, text="↓", height=1, width=3, command="", background="#f0f0f0")
butCrep4 = Button(frm, text="←", height=1, width=3, command="", background="#f0f0f0")
butC33 = Button(frm, text="X²", height=1, width=3, command="", background="#f0f0f0")
butC34 = Button(frm, text="hyp", height=1, width=3, command="", background="#f0f0f0")
butC35 = Button(frm, text="(", height=1, width=3, command="", background="#f0f0f0")

butC43 = Button(frm, text="^", height=1, width=3, command="", background="#f0f0f0")
butC44 = Button(frm, text="sin", height=1, width=3, command="", background="#f0f0f0")
butC45 = Button(frm, text=")", height=1, width=3, command="", background="#f0f0f0")

butC51 = Button(frm, text="", height=1, width=3, command="", background="#f0f0f0")
butC52 = Button(frm, text="Pol(", height=1, width=3, command="", background="#f0f0f0")
butC53 = Button(frm, text="log", height=1, width=3, command="", background="#f0f0f0")
butC54 = Button(frm, text="cos", height=1, width=3, command="", background="#f0f0f0")
butC55 = Button(frm, text=",", height=1, width=3, command="", background="#f0f0f0")

butC61 = Button(frm, text="", height=1, width=3, command="", background="#f0f0f0")
butC62 = Button(frm, text="X³", height=1, width=3, command="", background="#f0f0f0")
butC63 = Button(frm, text="ln", height=1, width=3, command="", background="#f0f0f0")
butC64 = Button(frm, text="tan", height=1, width=3, command="", background="#f0f0f0")
butC65 = Button(frm, text="M+", height=1, width=3, command="", background="#f0f0f0")

text1 = Label(frm, text="SHIFT", height=0, font=("Arial", 7), fg="#ff9500")
text2 = Label(frm, text="ALPHA", height=0, font=("Arial", 7), fg="#ff3300")
text3 = Label(frm, text="MODE", height=0, font=("Arial", 6), fg="#ff9500")
text4 = Label(frm, text="CLR", height=0, font=("Arial", 6), fg="#ff3300")
text5 = Label(frm, text="ON", height=0, font=("Arial", 7), fg="#ff9500")
text6 = Label(frm, text="X!", height=0, font=("Arial", 7), fg="#ff9500")
text7 = Label(frm, text="d/c", height=0, font=("Arial", 7), fg="#ff9500")
text8= Label(frm, text="A", height=0, font=("Arial", 7), fg="#ff3300")
text9 = Label(frm, text="STO", height=0, font=("Arial", 7), fg="#ff9500")
text10 = Label(frm, text="nPr", height=0, font=("Arial", 7), fg="#ff9500")
text11 = Label(frm, text="←", height=0, font=("Arial", 7), fg="#ff9500")
text12 = Label(frm, text="B", height=0, font=("Arial", 7), fg="#ff3300")
text13 = Label(frm, text="←", height=0, font=("Arial", 7), fg="#ff9500")
text14 = Label(frm, text="C", height=0, font=("Arial", 7), fg="#ff3300")
text15= Label(frm, text="ˣ√", height=0, font=("Arial", 7), fg="#ff9500")
text16 = Label(frm, text="sin⁻¹", height=0, font=("Arial", 8), fg="#ff9500")
text17 = Label(frm, text="D", height=0, font=("Arial", 7), fg="#ff3300")
text18 = Label(frm, text="X", height=0, font=("Arial", 7), fg="#ff3300")
text19 = Label(frm, text="Rec(", height=0, font=("Arial", 7), fg="#ff9500")
text20 = Label(frm, text=":", height=0, font=("Arial", 7), fg="#ff3300")
text21= Label(frm, text="10ˣ", height=0, font=("Arial", 7), fg="#ff9500")
text22 = Label(frm, text="cos⁻¹", height=0, font=("Arial", 8), fg="#ff9500")
text23 = Label(frm, text="E", height=0, font=("Arial", 7), fg="#ff3300")
text24 = Label(frm, text=":", height=0, font=("Arial", 7), fg="#ff3300")
text25 = Label(frm, text="Y", height=0, font=("Arial", 7), fg="#ff3300")
text26 = Label(frm, text="³√", height=0, font=("Arial", 7), fg="#ff9500")
text27 = Label(frm, text="cˣ", height=0, font=("Arial", 7), fg="#ff9500")
text28 = Label(frm, text="c", height=0, font=("Arial", 7), fg="#ff3300")
text29 = Label(frm, text="tan⁻¹", height=0, font=("Arial", 8), fg="#ff9500")
text30 = Label(frm, text="F", height=0, font=("Arial", 7), fg="#ff3300")
text31 = Label(frm, text="M-", height=0, font=("Arial", 7), fg="#ff9500")
text32 = Label(frm, text="M", height=0, font=("Arial", 7), fg="#ff3300")
text33 = Label(frm, text="DT CL\nOFF", height=0, font=("Arial", 5), fg="#ff9500")
text34 = Label(frm, text="S-SUM", height=0, font=("Arial", 7), fg="#ff9500")
text35 = Label(frm, text="RND", height=0, font=("Arial", 7), fg="#ff9500")
text36 = Label(frm, text="S-VAR", height=0, font=("Arial", 7), fg="#ff9500")
text37 = Label(frm, text="Ran#", height=0, font=("Arial", 7), fg="#ff9500")
text38 = Label(frm, text="π", height=0, font=("Arial", 7), fg="#ff9500")
text39 = Label(frm, text="INS", height=0, font=("Arial", 7), fg="#ff9500")
text40 = Label(frm, text="DRG+", height=0, font=("Arial", 7), fg="#ff9500")
text41 = Label(frm, text="%", height=0, font=("Arial", 7), fg="#ff9500")
socorro_me_ajuda(True)

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)



menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Menu", menu=menu_arquivo)
menu_arquivo.add_command(label='Padrao', command= paudrao)
menu_arquivo.add_command(label='Cientifica', command= ciess)

root.mainloop()