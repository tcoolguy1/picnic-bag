from tkinter import*
import random

root = Tk()
root.title("Picnic Bag")
root.geometry("400x400")

label_word = Label(root)
label_no = Label(root)

list1["Bottle","Chips","Chocolate","Napkin","Tiffin","Tickets","ID Card"]

label_word["text"] = "Items" +str(list1)

def bag_items():
    random_item = random.sample(range(0,7),1)
    label_no["text"] = "Put Item Number " +str(random_item) + " in your bag" 
label_word.place(relx = 0.5, rely=0.4, anchor = CENTER)
btn = Button(root, text = "Which item to put in the bag?", command = bag_items)
btn.place(relx = 0.5, rely=0.5, anchor = CENTER)
label_no.place(relx = 0.5, rely=0.6, anchor = CENTER)

root.mainloop()