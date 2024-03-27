# operaciones de lectura y escritura en archivos de texto en Python.
with open('my_note.txt', 'a') as file:
    # Escribir mis apuntes
    file.write("Nota 1: LEVANTARME 5:30 AM.\n")
    file.write("Nota 2: DUCHARME Y LAVARME LA BOCA.\n")
    file.write("Nota 3: VESTIRME PARA IR A TRABAJAR EN LA EMPRESA.\n")

# Abrir el archivo  en modo lectura 
with open('my_note.txt', 'r') as file:
    # Leer y muestra cada línea del archivo utilizando un bucle
    for line in file:
        print(line, end='')
