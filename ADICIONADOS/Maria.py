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