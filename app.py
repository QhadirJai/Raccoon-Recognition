import sys
print(sys.executable)

import tkinter as tk 
from tkinter import filedialog, Text, Label 
from PIL import ImageTk, Image 
import tkinter.font as tkFont
import numpy as np 
import tensorflow as tf 
from tensorflow import keras
import os
import pygame
from tkinter import messagebox

pygame.mixer.init()
new_model = tf.keras.models.load_model('saved_model\saved_model\my_model.keras')
pygame.mixer.music.load("roar-13.wav")
pygame.mixer.music.play()

batch_size = 32
img_height = 300
img_width = 300

class_names = ['Cacomistles', 'Coati', 'NORMAL RACOON', 'Olingos', 'Ringtails']

root = tk.Tk()

image = Image.open(r"C:\Users\Acer\Dropbox\My PC (LAPTOP-9GCNLQM6)\Desktop\Project AI-CSC583\habitat-wallpaper.jpg")

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
image = image.resize((width,height), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.pack()

root.title('PROJECT RACOON RECOGNITION!')
root.iconbitmap()
root.geometry("700x650")

filename ="null"

apps = []
def addApp():
    for widget in frame3.winfo_children():
        widget.destroy()

    global filename
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
filetypes=(("all files","*.*"),("exe","*.exe")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame3,text=app,bg="red" )
        label.pack()
    

def runApps():
    global filename
    img = keras.preprocessing.image.load_img(
        filename, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array,0)
    predictions = new_model.predict(img_array)
    score= tf.nn.softmax(predictions[0])
    predicted_class = class_names[np.argmax(score)]
    confidence = 100 * np.max(score)
    output = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(predicted_class, confidence)
    
    window = tk.Toplevel()
    window.title("Prediction")
    img= ImageTk.PhotoImage(img)
    label_img = tk.Label(window, image=img)
    label_img.pack(pady=10)
    label_output = tk.Label(window, text=output, font=("Arial", 16))
    label_output.pack(pady=10)
    button_close = tk.Button(window,text="close", command=window.destroy)
    button_close.pack(pady=10)
    def openApps():
        for app in apps:
            os.startfile(app)
    window.protocol("WM_DELETE_WINDOW",openApps)
    window.mainloop()
    
canvas = tk.Canvas(root,height=700, width=700,bg="#263D42")
    
canvas.pack()
    
frame= tk.Frame(root, bg="peru")
frame2= tk.Frame(root, bg="lightgrey")
frame3= tk.Frame(root, bg="lightgrey")
frame.place(relwidth=0.7, relheight=0.7, relx =0.5,rely =0.5, anchor="center")
frame2.place(relwidth=0.7,relheight=0.1, relx =0.5,rely =0.8, anchor="center")
frame3.place(relwidth=0.5, relheight=0.2, relx =0.5,rely =0.55, anchor="center")

Racoon_image =ImageTk.PhotoImage(Image.open('images.jpg'))

fontstyle = tkFont.Font(family="Times New Roman", size=20,weight="bold")
labeltitle = Label(frame , text="RACCOON RECOGNITION" ,font= fontstyle,bg="peru")
labeltitle.pack()

labelproject = Label(frame , image=Racoon_image)
labelproject.pack()

line = tk.Frame(frame ,height=1, width=550, bg="peru", relief='groove')
line.pack()

openfile = tk.Button(frame2,text="Open File",padx=10,pady=5,fg="white",bg="#454545",command=addApp)
openfile.pack()

runApps = tk.Button(frame2,text="Run Apps",padx=10,pady=5,fg="white",bg="#454545",command=runApps)
runApps.pack()

root.mainloop()