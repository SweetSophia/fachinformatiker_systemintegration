#GUi Test, Versuch 1
from tkinter import *

#root widget aufrufen
root=Tk()

#fenstername festlegen
root.title("GUI Test 27-09-2024")

#jetzt groesse festlegen WxH
root.geometry("300x300")

#label fuer basic text im root fenster
guitest = Label(root, text="<<-  So jetzt testen wir mal ob das geht  ->>")
guitest.grid(column=1, row=1)
#label kann bild, text, icon etc sein

#laben von button definieren wenn geklickt
def clicked():
    guitest.configure(text = "<<-  Text ist jetz ein anderer  ->>")
    
# button mit Text. in root schreib neuen text in FG Blau wenn clicked
klickmich = Button(root, text = "Digga klick da drauf" ,
                fg = "blue", command=clicked)

#button grid
klickmich.grid(column=1, row=2)

# guitest.pack()
#fenstergroesse an text anpassen

root.mainloop()
#all widgets werden, gesammelt, dargestellt und interkativ gemacht. und dann wirds geloopt damit es solange displayed wird bis geschlossen wird