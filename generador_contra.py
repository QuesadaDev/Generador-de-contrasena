import string
import random
import tkinter as tk


def generador(longitud: int, mayus: bool, numeros: bool, simbolos: bool):

    caracteres = string.ascii_uppercase if mayus else string.ascii_lowercase
    caracteres += string.digits if numeros else ''
    caracteres += string.punctuation if simbolos else ''

    if not (mayus or numeros or simbolos):
        print("Debes seleccionar al menos un tipo de carácter.")
        return None

    if longitud < 8 or longitud > 16:
        return print("La longitud debe estar entre 8 y 16")

    contra = "".join(random.choice(caracteres) for i in range(longitud))

    return print(contra)


def generar_contra_interfaz(entry_longitud, var_mayusculas, var_numeros, var_simbolos):

    longitu = 0
    try:
        longitu = int(entry_longitud.get())
    except ValueError:
        print("La longitud introducida debe ser un número")

    mayuscu = var_mayusculas.get() == 1
    numer = var_numeros.get() == 1
    simbolo = var_simbolos.get() == 1

    generador(longitu, mayuscu, numer, simbolo)


def generar_interfaz():

    ventana = tk.Tk()
    ventana.title("Generador de Contraseña")

    label_longitud = tk.Label(ventana, text="Longitud:")
    label_longitud.pack()

    entry_longitud = tk.Entry(ventana)
    entry_longitud.pack()

    var_mayusculas = tk.IntVar()
    check_mayusculas = tk.Checkbutton(ventana, text="Incluir letras mayúsculas", variable=var_mayusculas)
    check_mayusculas.pack()

    var_numeros = tk.IntVar()
    check_numeros = tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros)
    check_numeros.pack()

    var_simbolos = tk.IntVar()
    check_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos)
    check_simbolos.pack()

    boton_generar = tk.Button(ventana, text="Generar contraseña", command=lambda: generar_contra_interfaz(entry_longitud,
                                                                                                          var_mayusculas,
                                                                                                          var_numeros,
                                                                                                          var_simbolos))
    boton_generar.pack()
    ventana.mainloop()


generar_interfaz()



