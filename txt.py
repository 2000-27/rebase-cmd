from gtts import gTTS
from playsound import playsound
from tkinter import *
#initialized window
root = Tk()
root.geometry('600x600')
root.title('BUG NINZA')
root.config(bg='white')

#Labels

Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

# text variable

Msg = StringVar()

#Entry

input_field = Entry(root, textvariable=Msg, width = '60')
input_field.place(x=20, y=100)

#tts function
def tts():
    Message = input_field.get()
    speech = gTTS(text = Message)
    speech.save('Ninza.mp3')
    playsound('Ninza.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
#Buttons


Button(root, text = "PLAY" , font = 'arial 15 bold', command = tts, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'Red').place(x=150,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=225 , y =140)
#infinite loop to run program
root.mainloop()