import ply.lex as lex
import ply.yacc as yacc

tokens = ('TRAEME', 'TODO', 'DE',  'LA', 'TABLA', 'DONDE', 'AGRUPANDO', 'POR', 'MEZCLANDO', 'EN', 'LOS', 'DISTINTOS', 
          'CONTANDO', 'METE', 'VALORES', 'ACTUALIZA', 'SETEA', 'BORRA', 'ORDENA', 'COMO', 'MUCHO', 'WHERE', 'DEL', 
          'GROUP', 'BY', 'EXISTE', 'ESTO', 'ENTRE', 'PARECIDO','A', 'ES', 'NULO', 'CAMBIA', 'AGREGA', 'COLUMNA', 'ELIMINA', 
          'CREA', 'TIRA', 'DEFECTO', 'UNICO', 'CLAVE', 'PRIMA', 'REFERENTE', 'NO', 'TRANSFORMA', 'MAYOR', 'MENOR', 'IGUAL', 
          'COMA', 'Y', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 'PUNTO', 'IDENTIFICADOR', 'NUMERO', 'CADENA', 'TYPE')

keywords = {
    'TRAEME': 'TRAEME',
    'TODO': 'TODO',
    'DE' : 'DE',
    'LA' : 'LA',
    'TABLA' : 'TABLA',
    'DONDE': 'DONDE', 
    'AGRUPANDO': 'AGRUPANDO',
    'POR': 'POR',
    'MEZCLANDO': 'MEZCLANDO',
    'EN': 'EN',
    'LOS': 'LOS',
    'DISTINTOS': 'DISTINTOS',
    'CONTANDO': 'CONTANDO',
    'METE': 'METE',
    'VALORES': 'VALORES',
    'ACTUALIZA': 'ACTUALIZA',
    'SETEA': 'SETEA',
    'BORRA': 'BORRA',
    'ORDENA': 'ORDENA',
    'COMO': 'COMO',
    'MUCHO': 'MUCHO',
    'WHERE': 'WHERE',
    'DEL': 'DEL',
    'GROUP': 'GROUP',
    'BY': 'BY',
    'EXISTE': 'EXISTE',
    'ESTO': 'ESTO',
    'ENTRE': 'ENTRE',
    'PARECIDO': 'PARECIDO',
    'A': 'A',
    'ES': 'ES',
    'NULO': 'NULO',
    'CAMBIA': 'CAMBIA',
    'AGREGA': 'AGREGA',
    'COLUMNA': 'COLUMNA',
    'ELIMINA': 'ELIMINA',
    'CREA': 'CREA',
    'TIRA': 'TIRA',
    'DEFECTO': 'DEFECTO',
    'UNICO': 'UNICO',
    'CLAVE': 'CLAVE',
    'PRIMA': 'PRIMA',
    'REFERENTE': 'REFERENTE',
    'NO': 'NO',
    'TRANSFORMA': 'TRANSFORMA',
    'MAYOR': 'MAYOR',
    'MENOR': 'MENOR',
    'IGUAL': 'IGUAL',
    'COMA': 'COMA',
    'Y': 'Y',
    'PARENTESIS_IZQ': 'PARENTESIS_IZQ',
    'PARENTESIS_DER': 'PARENTESIS_DER',
    'IDENTIFICADOR': 'IDENTIFICADOR',
    'NUMERO': 'NUMERO',
    'CADENA': 'CADENA',
    'TYPE': 'TYPE'
}

t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_COMA = r','
t_Y = r'Y'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PUNTO = r'\.'
t_TYPE = r'(INT|VARCHAR|DATE|CHAR)'

t_ignore = ' \t\n'

def t_IDENTIFICADOR(t):
    """Reconoce nombres de tablas, columnas y otros identificadores."""
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.type = keywords[t.value.upper()] 
    return t

def t_NUMERO(t):
    """Reconoce números enteros."""
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    """Reconoce cadenas de texto entre comillas simples."""
    r'\'[^\']*\''
    t.value = t.value.strip("'")
    return t

def t_error(t):
    """Muestra un error en caso de caracteres ilegales."""
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#parser
def p_statement(p):
    """Define el tipo de declaraciones que puede manejar el parser."""
    p[0] = p[1]


def p_statement_select(p):
    """Maneja las consultas tipo SELECT."""
    
    clauses = [
        generate_select(p[2]),
        generate_from(p[6]),
        generate_join(p[7]),
        generate_group_by(p[8]),
        generate_having(p[9]),
        generate_where(p[10])
    ]
    
    p[0] = " ".join(clause for clause in clauses if clause)

def generate_select(select_items):
    """Genera la cláusula SELECT de una consulta SQL."""
    return f"SELECT {select_items}"

def generate_from(table):
    """Genera la cláusula FROM de una consulta SQL."""
    return f"FROM {table}"

def generate_join(join_clause):
    """Genera la cláusula JOIN si está presente."""
    return join_clause if join_clause else ""

def generate_group_by(group_by_clause):
    """Genera la cláusula GROUP BY si está presente."""
    return group_by_clause if group_by_clause else ""

def generate_having(having_clause):
    """Genera la cláusula HAVING si está presente."""
    return having_clause if having_clause else ""

def generate_where(where_clause):
    """Genera la cláusula WHERE si está presente."""
    return where_clause if where_clause else ""  

def p_select_items(p):
    """Define los elementos seleccionados en una consulta SELECT."""
    if len(p) == 2:
        if p[1] == 'TODO':
            p[0] = '*' 
        else:
            p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"DISTINCT {p[3]}"
    else:
        p[0] = "COUNT(*)"

def p_column(p):
    """Define una columna con o sin un prefijo de tabla."""
    if len(p) == 4:
        p[0] = f"{p[1]}.{p[3]}"
    else:
        p[0] = p[1]

def p_column_list(p):
    """Define una lista de columnas."""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_join_clause(p):
    """Define las cláusulas JOIN en las consultas."""
    if len(p) == 7:
        p[0] = f"JOIN {p[2]} ON {p[4]} = {p[6]}"
    else:
        p[0] = ""

def p_where_clause(p):
    """Define la cláusula WHERE en las consultas."""
    if len(p) == 3:
        p[0] = f"WHERE {p[2]}"
    else:
        p[0] = ""

def p_having_clause(p):
    """Define la cláusula HAVING en las consultas."""
    if len(p) == 6:
        p[0] = f"HAVING {p[5]}"
    else:
        p[0] = ""

def p_value(p):
    """Define un valor numérico o de cadena."""
    if isinstance(p[1], str):
        p[0] = p[1]  
    else:
        p[0] = p[1] 

def p_value_list(p):
    """Define una lista de valores."""
    if len(p) == 2:
        if isinstance(p[1], str): 
            p[0] = f"'{p[1]}'"
        else:
            p[0] = p[1]
    else:
        if isinstance(p[3], str): 
            p[0] = f"{p[1]}, '{p[3]}'"
        else:
            p[0] = f"{p[1]}, {p[3]}"

def p_statement_update(p):
    """Maneja las consultas tipo UPDATE."""
    if isinstance(p[6], str):  
        p[0] = f"UPDATE {p[2]} SET {p[4]} = '{p[6]}' {p[7]}"
    else:
        p[0] = f"UPDATE {p[2]} SET {p[4]} = {p[6]} {p[7]}"

def p_condition(p):
    """Define las condiciones de la cláusula WHERE y HAVING."""
    if len(p) == 4:
        if isinstance(p[3], str):  
            p[0] = f"{p[1]} {p[2]} '{p[3]}'"
        else:
            p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 6:
        p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"
    elif len(p) == 7:
        p[0] = f"COUNT(*) > {p[6]}"

def p_statement_delete(p):
    """Define una declaración DELETE."""
    p[0] = f"DELETE FROM {p[3]} {p[4]}"

def p_statement_alter(p):
    """Define una declaración ALTER TABLE para modificar tablas."""
    p[0] = f"ALTER TABLE {p[4]} {p[5]}"

def p_alter_action(p):
    """Define las acciones ALTER, como agregar o eliminar columnas."""
    if len(p) == 8:
        p[0] = f"ADD COLUMN {p[4]} {p[5]} NOT NULL"
    else:
        p[0] = f"DROP COLUMN {p[4]}"

def p_data_type(p):
    """Define un tipo de dato con o sin especificación de tamaño."""
    if len(p) == 5:
        p[0] = f"{p[1]}({p[3]})"
    else:
        p[0] = p[1]

def p_group_by_clause(p):
    """Define la cláusula GROUP BY."""
    if len(p) == 4:
        p[0] = f"GROUP BY {p[3]}"
    else:
        p[0] = ""

def p_table(p):
    """Define el nombre de la tabla."""
    p[0] = p[1]

def p_statement_insert(p):
    """Define una declaración INSERT. """
    p[0] = f"INSERT INTO {p[3]} ({p[5]}) VALUES ({p[9]})"

def p_empty(p):
    """Define una producción vacía."""
    pass

def p_error(p):
    """Maneja errores de sintaxis."""
    if p:  # Si existe el token donde falló
        raise SyntaxError(f"Syntax error at token '{p.value}' in line {p.lineno}")
    else:
        raise SyntaxError("Syntax error: unexpected end of input")


parser = yacc.yacc()

# Definición de tokens y reglas de parsing aquí (como ya los tienes definidos)

# Clase TraductorUSQL
class TraductorUSQL:
    def __init__(self):
        # Inicializar lexer y parser
        self.lexer = lex.lex()
        self.parser = yacc.yacc()
    
    def parse(self, consulta):
        try:
            # Usar el parser para traducir USQL a SQL
            sql = self.parser.parse(consulta, lexer=self.lexer)
            return sql
        except SyntaxError as e:
            print(f"Error de sintaxis: {e}")
            return None


# Prueba
#consulta = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18" #FUNCIONA
#consulta = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid'" #FUNCIONA
#consulta = "METE EN usuarios (nombre, edad) VALORES ('Juan', 25)" #FUNCIONA
#consulta = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'" #FUNCIONA
#consulta = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona'" #FUNCIONA
#consulta = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(TODO) > 5" #FUNCIONA
#consulta = "BORRA DE clientes DONDE edad ENTRE 18 Y 25" #FUNCIONA
#consulta = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO" #FUNCIONA
#consulta =  "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion" #FUNCIONA

# Enviar la consulta al lexer
# lexer.input(consulta)

# # Procesar los tokens (opcional para debug)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# # Enviar la consulta al parser
# sql = parser.parse(consulta)

# # Mostrar la salida
# print("Consulta SQL generada:", sql)