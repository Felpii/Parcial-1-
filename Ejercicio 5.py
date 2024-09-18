# Enunciado:
# Escribe un programa que tenga una función que verifique si un valor es None.
# Si el valor es None, debe imprimir un mensaje indicando que no tiene valor asignado. En caso contrario, debe mostrar el valor.

def vr_va(va):
    if va is None:
        print("El valor no esta asignado (es None).")
    else:
        print(f"El valor es: {va}")
vr_va(None)

vr_va(10)

