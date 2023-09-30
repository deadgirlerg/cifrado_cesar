def cifrado_cesar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            # Verifica si el caracter es una letra
            mayuscula = caracter.isupper() # Verifica si es mayúscula
            caracter = caracter.lower() # Convierte a minúscula para facilitar el cifrado
            codigo = ord(caracter) - ord('a') # Convierte a número del 0 al 25
            codigo = (codigo + clave) % 26 # Aplica el desplazamiento (módulo 26 para volver al alfabeto)
            caracter_cifrado = chr (codigo + ord('a')) # Convierte de nuevo a letra mayúscula
            if mayuscula:
                caracter_cifrado = caracter_cifrado.upper() # Convierte de vuelta a mayúscula si era mayúscula
            resultado += caracter_cifrado
        else:
            resultado += caracter # Si no es una letra, mantener sin cambios
    return resultado

def descifrado_cesar(texto_cifrado, clave):
    # El descifrado es simplemente el cifrado con una clave negativa
    return cifrado_cesar(texto_cifrado, -clave)

# Ejemplo de uso
texto_original = "Esto es una prueba de cifrado cesar."
clave = 3
texto_cifrado = cifrado_cesar(texto_original, clave)
texto_descifrado = descifrado_cesar(texto_cifrado, clave)

print("Texto Original:  ", texto_original)
print("Texto Cifrado:   ", texto_cifrado)
print("Texto descifrado:", texto_descifrado)