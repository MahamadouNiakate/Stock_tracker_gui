import tkinter as Tk
import db_interface

class MainWindow():
    def __init__(self, master):
        self.master = master
        self.master.geometry("220x290")
        
        #Title
        self.lbl_title = Tk.Label(master, text="Todo with Excel" )
        self.lbl_title.place(x=10, y=10)

        #Item name
        self.lbl_item_name = Tk.Label(master, text="Item name" )
        self.lbl_item_name.place(x=10, y=50)

        self.txt_item_name = Tk.Entry(master)
        self.txt_item_name.place(x=10, y=70)

        #Item price
        self.lbl_buy_price = Tk.Label(master, text="Buy price" )
        self.lbl_buy_price.place(x=10, y=100)

        self.txt_buy_price = Tk.Entry(master)
        self.txt_buy_price.place(x=10, y=120)

        #Sell price
        self.lbl_sell_price = Tk.Label(master, text="Sell price" )
        self.lbl_sell_price.place(x=10, y=150)

        self.txt_sell_price = Tk.Entry(master)
        self.txt_sell_price.place(x=10, y=170)

        #Quantity
        self.lbl_quantity = Tk.Label(master, text="Quantity" )
        self.lbl_quantity.place(x=10, y=200)

        self.txt_quantity = Tk.Entry(master)
        self.txt_quantity.place(x=10, y=220)

        #Button
        self.btn_submit = Tk.Button(master, text="Submit", command=self.submit_to_db)
        self.btn_submit.place(x=10, y=260)

    def submit_to_db(self):
        item_name = self.txt_item_name.get()
        buy_price = int(self.txt_buy_price.get())
        sell_price = int(self.txt_sell_price.get())
        quantity = int(self.txt_quantity.get())

        db_interface.write_to_database(item_name, buy_price, sell_price, quantity)



root = Tk.Tk()
my_gui = MainWindow(root)
root.mainloop()