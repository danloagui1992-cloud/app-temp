import secretos

print("🚦 APLICACIÓN BANCARIA ")

contrasenia = input("Ingresa la contraseña: ")

if contrasenia == secretos.password:
    print("####################")
    print("## ACCESO CORRECTO ##")
    print("####################")
else:
    print("⚠====================⚠")
    print("⚠     ACCESO DENEGADO     ⚠")
    print("⚠====================⚠")