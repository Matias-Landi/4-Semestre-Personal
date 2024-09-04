
# Bool contiene los valores de True y False
# Los tipos numéricos, es false para el 0 (cero), true para los demás valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo string -> False '', True demás valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo colecciones -> False para colecciones vacías
# Tipo colecciones -> True para todas las demás
# Lista
valor = []
resultado = bool(valor)
print(f'valor lista vacía: {valor}, Resultado: {resultado}')

valor = [2, 'l', 4]
resultado = bool(valor)
print(f'valor lista con elementos: {valor}, Resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor tupla vacía: {valor}, Resultado: {resultado}')

valor = (5,1)
resultado = bool(valor)
print(f'valor tupla con elementos: {valor}, Resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'valor diccionario vacío: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Pérez'}
resultado = bool(valor)
print(f'valor diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 3
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')