from tkinter import *

import training
import cv2
from os.path import exists


def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    reply = e.get().lower()
    if(reply =='hi'):
        text.insert(END, "\n" + "Bot: Hello, want to see something interesting? (1: Yes, 2: No)")
    elif(reply=='hello'):
        text.insert(END, "\n" + "Bot: Hi, want to see something interesting? (1: Yes, 2: No)")
    elif (reply == 'how are you?'):
        text.insert(END, "\n" + "Bot: I'm fine and you?")
    elif (reply == "i'm fine too"):
        text.insert(END, "\n" + "Bot: Nice to hear that")
    elif reply.__contains__("1"):
        text.insert(END,"\n" + "Bot: Please enter an image file ")
    elif reply.__contains__("2"):
        text.insert(END,"\n" + "Bot: Too bad, you're missing out")
    elif reply.contains("3"):
        text.insert(END,"\n" + "Bot: Enter another image file or q to quit")
        png = cv2.imread("edge.png")
        cv2.imshow("edge", png)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif reply.__contains__("4"):
        text.insert(END,"\n" + "Bot: Are you sure?")
    elif reply.__contains__("yes"):
        text.insert(END,"\n" + "Bot: Ok")
    elif reply.__contains__("no"):
        text.insert(END,"\n" + "Bot: Same deal: 3 for yes, 4 for no")

    elif reply.__contains__("4"):
        text.insert(END,"\n" + "Bot:")
    elif reply.__contains__("q"):
        text.insert(END,"\n" + "Bot: Thank you for watching, want to see the sketch of the image? (3:yes, 4:no)")


    elif reply.__contains__(".jpg"):
        tmp_canvas = training.Cartoonizer()
        send = "You:"+ e.get()
        text.insert(END, "\n" + "Bot: Enter another image file or q to stop")  # File_name will come here
        file_name = e.get()
        file_exists = exists(file_name)
        if file_exists :
            res = tmp_canvas.render(file_name)
            cv2.imwrite("Cartoon version.jpg", res)
            cv2.imshow("Cartoon version", res)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            while cv2.getWindowProperty('Cartoon version', cv2.WND_PROP_VISIBLE) >= 1:
                print(cv2.getWindowProperty("Cartoon version", res))
                cv2.destroyAllWindows()
        else:
            text.insert(END, "\n" + "File does not exists, Enter another filename")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
    e.delete(0,"end")


root = Tk()
text = Text(root, bg='sky blue', fg='purple')
text.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=80)
send = Button(root, text='Send', bg='blue', width=20, command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title(' CHATBOT')
root.mainloop()