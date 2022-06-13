import wikipedia as wiki
import tkinter as tk

####---------------------------------------------------
"""
Fecha: 13/03/2021
Nombre: BusquedaWiki.py
Autor: @linkfydev
Descripcion: Realiar una busqueda en Wikipedia y regresar en una UI
Librerias:
    -> wikipedia = Realizar la consulta a la pagina.
    -> tkinter = generador para la UI.
"""
#####--------------------------------------------------

def search(event):
    content = search_box.get()
    result = wiki.summary(content,sentences=1)
    T.delete("1.0",tk.END)
    T.insert(tk.END, result)

window = tk.Tk()
window.geometry("450x450")
search_box = tk.Entry(window)
search_box.place(x=0, y=0)
search_box.bind('<Return>',search)
T = tk.Text(window)
search_box.pack()
T.pack()
T.insert(tk.END, "test")

window.mainloop()