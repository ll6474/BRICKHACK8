from tkinter import *

def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    reply = e.get().lower()
    if(reply =='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(reply=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (reply == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (reply == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")

root = Tk()
text = Text(root, bg='pink')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title(' CHATBOT')
root.mainloop()
