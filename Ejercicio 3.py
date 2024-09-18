# Enunciado:
# Escribe un programa que tome una cadena de texto del usuario y realice las siguientes operaciones:
# convierta la cadena a mayúsculas, cuente cuántos caracteres tiene, y verifique si la cadena contiene la palabra "Python".

# Andres Felipe Sanchez Romero

txt=input("Ingrese una pequeña frase: ")

txtM= txt.upper()

long=len(txt)

py = "Python"  in txt


print(f"Texto en Mayuscula: {txtM}")
print(f"Numero de caracteres: {long}")
print(f"Contiene la palabra 'Python': {py}")