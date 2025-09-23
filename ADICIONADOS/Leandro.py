########################################### GRUPO LEANDRO ####################################

def vld_slots():
    """Return list of valid slot keys."""
    return list(memory_slots.keys())

def is_valid_slot(slot: str) -> bool:
    if not slot or not isinstance(slot, str):
        return False
    return slot.strip().upper() in memory_slots

def set_memory(slot: str, value: str) -> bool:
    if not isinstance(slot, str):
        return False
    s = slot.strip().upper()
    if s in memory_slots:
        memory_slots[s] = value
        return True
    return False

def get_memory(slot: str):
    if not isinstance(slot, str):
        return None
    return memory_slots.get(slot.strip().upper(), None)

# functions/degrees.py
"""
Aqui é a conversão de decimais para graus, minutos e segundos.
Funciona com números negativos e positivos.
Essa função está dentro da função formatDegree, tenha a certeza de importá-la para o arquivo que formatDegree estiver.
Usar assim:
  from functions.fnNew import degrees as deg
  deg.convertDecimal(value)
"""


degreeSign = "°"
minuteSign = "'"
secondSign = '"'

def convertDecimal(value):
  if isinstance(value, str):
    vnorm = value.strip().replace(",", ".")
  else:
    vnorm = str(value)

  try:
    num = float(vnorm)
  except Exception:
    raise ValueError(f"Valor inválido para conversão: {value!r}")

  sign = "-" if num < 0 else ""
  a = abs(num)
  degrees = int(a)
  rem_minutes = (a - degrees) * 60.0
  minutes = int(rem_minutes)
  seconds = (rem_minutes - minutes) * 60.0
  precision_seconds = 2
  seconds = round(seconds, precision_seconds)

  if seconds >= 60.0:
    seconds -= 60.0
    minutes += 1
  if minutes >= 60:
    minutes -= 60
    degrees += 1

  if float(seconds).is_integer():
    sec_str = str(int(round(seconds)))
  else:
    raw = f"{seconds:.{precision_seconds}f}"
    raw = raw.rstrip("0").rstrip(".")
    sec_str = raw

  formatted = f"{sign}{degrees}{degreeSign}{minutes}{minuteSign}{sec_str}{secondSign}"

  return formatted

'''
Funções de memória: STO, RCL e gerenciamento de slots.
Coloque as duas funções em um botão.
O arquivo auxiliar.py também será necessário, pois ele contém o dicionário de slots e funções auxiliares.
Usar assim:
  from functions.fnNew import memoryFx as mem
  mem._sto(display, app)  # Para armazenar
  mem._rcl(display, app)  # Para recuperar
  Display é o campo de entrada (Entry) do tkinter
  app é a instância da classe App (main)
'''

def valid_slots():
    return var.valid_slots()

def _ask_slot(parent, title):
    prompt = "Escolha um slot de memória (ex: A, B, C, ...):"
    slot = simpledialog.askstring(title, prompt, parent=parent)
    if not slot:
        return None
    slot = slot.strip().upper()
    if not var.is_valid_slot(slot):
        messagebox.showerror("Slot inválido", f"Slot '{slot}' inválido.\nUse: {', '.join(var.valid_slots())}", parent=parent)
        return None
    return slot

def _sto(display, parent):
    slot = _ask_slot(parent, "STO (armazenar)")
    if not slot:
        return
    val = display.get()
    if parent.selecao.get() == "Normal":
        val = val.replace(",", ".")
    if var.set_memory(slot, val):
        messagebox.showinfo("STO", f"Valor armazenado em {slot}", parent=parent)
    else:
        messagebox.showerror("STO", f"Não foi possível armazenar em {slot}", parent=parent)

def _rcl(display, parent):
    slot = _ask_slot(parent, "RCL (recuperar)")
    if not slot:
        return
    val = var.get_memory(slot)
    if val is None:
        messagebox.showerror("Erro", f"Nenhum valor em {slot}", parent=parent)
        return
    if parent.selecao.get() == "Normal":
        val = val.replace(".", ",")
    current = display.get()
    if current == "0" or current == "":
        display.delete(0, tk.END)
        display.insert(0, val)
    else:
        try:
            display.insert(tk.INSERT, val)
        except Exception:
            display.insert(tk.END, val)

'''
Aqui é a formatação dos graus
Faça com que o botão do grau adcione um símbolo de grau (°) ao final do número atual e a função vai reconhecer isso.
Coloque isso dentro da função de calcular, ele funciona como um eval normal, mas reconhece o símbolo de grau.
Usar assim:
 from functions.fnNew import formatDegree as fmtDeg
 fmtDeg.formatDegree(expression, app, display)
 expression = string que vai receber a formatação
 app = instância da classe App (main)
 display = campo de entrada (Entry) do tkinter
'''


from ItensLeandro import degrees as deg

def format_result(value, app):
    try:
        if hasattr(var, "get_round_settings"):
            mode, digits = var.get_round_settings()
        else:
            mode, digits = "norm", 2
        if mode == "fix":
            out = f"{value:.{digits}f}"
        elif mode == "sci":
            sig = max(1, int(digits))
            out = f"{value:.{sig}e}"
        else:
            out = f"{value:.12g}"
        if app.selecao.get() == "Normal":
            out = out.replace(".", ",")
        return out
    except Exception:
        return "Erro"

def formatDegree(expression, app, display):
    token_pattern = re.compile(r"([-+]?\d+(?:\.\d+)?)(°?)")
    tokens = list(token_pattern.finditer(expression))

    if tokens:
        all_have_deg = all(m.group(2) == "°" for m in tokens)

        def _strip_deg(match):
            return match.group(1)
        
        expr = token_pattern.sub(_strip_deg, expression)
        expr = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", expr)
        resultado = eval(expr)
        var.lastNumber = str(resultado)

        if all_have_deg:
            try:
                dms_str = deg.convertDecimal(str(resultado))
            except Exception:
                texto = format_result(resultado, app)
                display.delete(0, "end")
                display.insert(0, texto)
                
                return

            if app.selecao.get() == "Normal":
                dms_str = dms_str.replace(".", ",")

            display.delete(0, "end")
            display.insert(0, dms_str)
            
            return
        else:
            texto = format_result(resultado, app)
            display.delete(0, "end")
            display.insert(0, texto)
            
            return
    else:
        resultado = eval(expression)
        var.lastNumber = str(resultado)
        texto = format_result(resultado, app)
        display.delete(0, "end")
        display.insert(0, texto)
        
        return

def calcular(display, app):
    try:
        raw = display.get()

        expressao = (raw
            .replace("×", "*")
            .replace("÷", "/")
            .replace("√", "math.sqrt")
            .replace("sin(", "math.sin(math.radians(")
            .replace("cos(", "math.cos(math.radians(")
            .replace("tan(", "math.tan(math.radians(")
            .replace("asin(", "math.degrees(math.asin(")
            .replace("acos(", "math.degrees(math.acos(")
            .replace("atan(", "math.degrees(math.atan(")
            .replace("log(", "math.log10(")
            .replace("ln(", "math.log(")
            .replace("Ran#(", "random.uniform(0, ")
            .replace("^", "**")
        )

        if app.selecao.get() == "Normal":
            expressao = expressao.replace(",", ".")

        formatDegree(expressao, app, display)

    except (SyntaxError, ZeroDivisionError, NameError, ValueError, TypeError) as e:
        print(f"Erro: {e}")
        display.delete(0, "end")
        display.insert(0, "Erro")

def inserir(valor, display):
    atual = display.get()

    match = re.search(r"([0-9.,]+)$", atual)
    ultimo_numero = match.group(0) if match else ""

    if valor == "," and "," in ultimo_numero:
        return

    if valor == "." and "." in ultimo_numero:
        return

    if atual == "0" and valor not in "+-×÷%":
        display.delete(0, tk.END)

    display.insert(tk.END, valor)

def limpar_tudo(display):
    display.delete(0, tk.END)
    display.insert(0, "0")
    var.lastNumber = "0"

def limpar_ultimo(display):
    atual = display.get()
    if len(atual) > 1:
        display.delete(len(atual) - 1)
    else:
        limpar_tudo(display)

def calcular_raiz(display):
    try:
        valor = float(display.get().replace(",", "."))
        if valor < 0:
            raise ValueError
        resultado = math.sqrt(valor)
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except (ValueError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def ao_quadrado(display):
    try:
        valor = float(display.get().replace(",", "."))
        resultado = valor ** 2
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except (ValueError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def um_sobre_x(display):
    try:
        valor = float(display.get().replace(",", "."))

        if valor == 0:
            raise ZeroDivisionError
        
        resultado = 1 / valor
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except (ValueError, ZeroDivisionError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def ao_cubo(display):
    try:
        valor = float(display.get().replace(",", "."))
        resultado = valor ** 3
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except (ValueError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def calcular_raiz_cubica(display):
    try:
        valor = float(display.get().replace(",", "."))
        resultado = valor ** (1/3)
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except (ValueError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def nao_implementado():
    print("Função não implementada.")

"""
Aqui é invertido o sinal do número atual no display.
Display é o texto do campo Entry do tkinter.
Usar assim:
  from functions.fnNew import signals as sig
  sig.swapSignals(display)"""




def swapSignals(display):
    try:
        expr = display.get()
        m1 = re.search(r"([+-]?)(\d*+(?:[.,]\d+)?)$", expr)

        if m1:
            op = m1.group(1)
            num = m1.group(2)
            num_norm = num.replace(",", ".")

            try:
                if float(num_norm) == 0:
                    return
            except Exception:
                return
            
            num_sem_sinal = num.lstrip("+-")
            novo_op = "-" if op != "-" else "+"
            nova_expr = expr[:m1.start(1)] + novo_op + num_sem_sinal
            display.delete(0, tk.END)
            display.insert(0, nova_expr)

            if "," in num:
                var.lastNumber = num_sem_sinal
            else:
                var.lastNumber = num_sem_sinal
            
            return

        m2 = re.search(r"([+-]?\d*+([.,]\d+)?)$", expr)

        if m2:
            num = m2.group(1)
            num_norm = num.replace(",", ".")
            
            try:
                f = float(num_norm)
            except Exception:
                return

            if f == 0:
                return

            if num.startswith("-"):
                novo_num = num[1:]
            else:
                novo_num = "-" + num

            nova_expr = expr[:-len(num)] + novo_num
            display.delete(0, tk.END)
            display.insert(0, nova_expr)

            var.lastNumber = novo_num
            return

        return

    except Exception as e:
        print(f"Erro ao trocar sinal: {e}")
        return
################################### FIM GRUPO LEANDRO ########################
