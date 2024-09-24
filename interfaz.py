import tkinter as tk

from app import main


root = tk.Tk()

root.title('EXTRACTOR DE INFORMACION (FACTURAS)')
root.geometry('500x300')
label = tk.Label(root, text="Nombre del archivo", font=("Arial", 17))
label.pack(pady=5)

entry = tk.Entry(root, width=25,font=("Arial", 16))
entry.insert(0, "Extraccion")
entry.pack(pady=5)


label = tk.Label(root, text="Folder", font=("Arial", 17))
label.pack(pady=5)

entry2 = tk.Entry(root,width=25,font=("Arial", 16))
entry2.pack(pady=5)


def EXE():
    Endfile = entry.get()
    Path = entry2.get()
    main(Path,Endfile)


button = tk.Button(root, text="Extraer informacion", command=EXE)
button.pack(pady=10)



Version = tk.Label(root, text='V1.0.0', font=('Arial',9))
Version.pack(pady=5)
root.mainloop()