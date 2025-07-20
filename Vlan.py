# vlan.py
# Entrada de datos
vlan = int(input("Ingrese el número de VLAN: "))

# Lógica básica
if 1 <= vlan <= 1005:
    print("VLAN de rango NORMAL")
elif 1006 <= vlan <= 4094:
    print("VLAN de rango EXTENDIDO")
else:
    print("Número de VLAN no válida")
