from tkinter import *
from tkinter import ttk
import tkinter as tk
import math
import ast
import operator as op
import re
menu_s_sum_ativo = False
menu_s_var_ativo = False
mplus = [2, 4, 6, 8]  # Lista de valores para testes mudar para quando fizeram o mplus(e de outro grupo por isso valores testes)
#DISPLAY QUER DIZER O NOME DO SEU DISPLAY.
#NUMBER1 É UMA VARIAVEL QUE VAI GUARDAR A EQUACAO QUE ESTA SENDO FEITA, EXPLICANDO MELHOR O DISPLAY MOSTRA O VALOR DE NUMBER1
def ativar_menu_s_var():
    limpar()  # Limpa a entrada atual
    global menu_s_var_ativo
    menu_s_var_ativo = True  # Ativa flag indicando que o menu S-VAR está ativo
    Display.set("1-x̅   2-xσn   3-xσn-1")  # Mostra as opções no display

def ativar_menu_s_sum():
    limpar()
    global menu_s_sum_ativo
    menu_s_sum_ativo = True
    Display.set("1-Σx    2-Σx²   3-n")

def ativar_menu_drg():
    """Ativa o menu DRG quando Shift + Ans é pressionado"""
    global menu_drg_ativo, shift
    menu_drg_ativo = True  # Ativa flag indicando que o menu DRG está ativo
    shift = not shift  # Alterna o estado de shift
    Display.set("D-1 R-2 G-3")  # Mostra as opções de ângulos: Degree, Radian, Gradian
    
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
    
def media_x():
    return sum(mplus)/len(mplus) if mplus else 0

def desvio_populacional():
    n = len(mplus)
    if n == 0:
        return 0
    mean = media_x()
    return (sum((x - mean)**2 for x in mplus)/n)**0.5

def desvio_amostral():
    n = len(mplus)
    if n <= 1:
        return 0
    mean = media_x()
    return (sum((x - mean)**2 for x in mplus)/(n-1))**0.5

def fnSoma_x():
    return sum(mplus)

def fnSoma_x2():
    return sum(x**2 for x in mplus)

def fnQuantidade_n():
    return len(mplus)

def fnSIN(valor):
    valor_em_graus = converter_para_graus(valor)
    resultado = math.sin(math.radians(valor_em_graus))
    return str(resultado)

def fnCOS(valor):
    resultado = math.cos(math.radians(float(valor)))
    return str(resultado)

def fnTAN(valor):
    resultado = math.tan(math.radians(float(valor)))
    return str(resultado)

#SIN_INV SENO INVERSO
def fnSIN_INV(valor):
    """Arco seno (sin⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.asin(float(valor)))
    except:
        return "Erro"
    
#COS_INV COSSENO INVERSO
def fnCOS_INV(valor):
    """Arco cosseno (cos⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.acos(float(valor)))
    except:
        return "Erro"
    
#TAN_INV TANGENTE INVERSA
def fnTAN_INV(valor):
    """Arco tangente (tan⁻¹) - retorna em graus"""
    try:
        return math.degrees(math.atan(float(valor)))
    except:
        return "Erro"
def fnExp(valor):
    try:
        resultado = 10 ** float(valor)
        return str(resultado)
    except:
        return "Erro"
    
def fnPi():
    return str(math.pi)

def inserir_ans():
    global Number1
    if (shift):
        ativar_menu_drg()
    else:
        Number1 += "Ans"
        Display.set((Number1))

#NAO É ASSOCIADO A NENHUM BOTAO
def inserir_pi():
    global Number1
    Number1 += "π"  
    Display.set(Number1)
    
#ASSOCIADO AO BOTAO hyp
def inserir_H():
    global Number1
    Number1 += "h"
    Display.set((Number1))

#ASSOCIADO AO BOTAO EXP
def inserir_exp():
    global Number1
    if (shift):
        inserir_pi()
    else:
        Number1 += "exp("
        Display.set(Number1)

#ASSOCIADO AO BOTAO sin
def inserir_sin():
    global shift, Number1
    if shift:
        Number1 += "sin⁻¹("
        shift = False 
    else:
        Number1 += "sin("
    Display.set((Number1))

#ASSOCIADO AO BOTAO cos
def inserir_cos():
    global shift, Number1
    if shift:
        Number1 += "cos⁻¹("
        shift = False
    else:
        Number1 += "cos("
    Display.set((Number1))

#ASSOCIADO AO BOTAO tan
def inserir_tan():
    global shift, Number1
    if shift:
        Number1 += "tan⁻¹("
        shift = False
    else:
        Number1 += "tan("
    Display.set((Number1))

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
#Essa função a seguir repara a expressão para cálculo, convertendo unidades, funções trigonométricas, notação inversa, e substituindo variáveis como Ans e π
def processar_completo(conta):
    conta = converter_notacao_inversa(conta)
    conta = converter_notacao_hiperbolica_inversa(conta)
    
    # Funções trigonométricas inversas e hiperbólicas
    conta = processar_funcoes_inversas(conta)
    conta = processar_funcoes_hiperbolicas(conta)
    
    # Unidades angulares
    conta = processar_expressao_com_unidades(conta)
    
    # Substitui Ans e variáveis
    conta = conta.replace("Ans", str(ans))
    for var, valor in memory_slots.items():
        conta = conta.replace(var, str(valor))
    
    # Símbolos matemáticos
    conta = conta.replace("π", str(math.pi))
    conta = conta.replace("X", "*").replace("÷", "/").replace(",", ".")
    
    conta = remover_zeros_esquerda(conta)
    
    # Processa símbolos angulares dentro de funções trig
    conta = processar_simbolos_angulares(conta)
    
    return conta

# PARA DEIXAR BEM CLARO ESSE TRECHO DE CODIGO DEVE SER COLOCADO NO JEITO QUE VOCE USOU PARA ADICIONAR O NUMERO, PQ TEM VERIFICAR SE OS PRECIONADOS
#  SAO 1 ou 2 ou 3 ENTAO QUANDO O VALUE FOR 1 FAZER NO LOCAL QUE VOCE ADICIONA O NUMERO 1 O MEU GRUPO FEZ UMA FUNCAO INTEIRA SO DE ADICIONAR NUMERO
#  ENTAOVERIFICAR ISSO
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
#O TRECHO A SEGUIR SERVE APENAS PARA ILUSTRAR ONDE O PROCESSAR_COMPLETO DEVE SER CHAMADO E QUANDO O VALOR DA VARIAVEL ans DEVE SER ALTERADO
def calcular_cientifica(conta):
    global ans, memory_slots
    try:
        conta = processar_completo(conta)
        # Corrige parênteses
        abertos = conta.count('(')
        fechados = conta.count(')')
        conta += ')' * (abertos - fechados)
        # ====================================================
        #         METODO QUE VCS USAM PRA CALCULAR
        #=====================================================
        ans = resultado
        return resultado
    except Exception as e:
        return f"Erro em calcular_cientifica: {e}"





        # ====================================================
        #         QUALQUER DUVIDA SO CHAMAR MATHEUS
        #=====================================================