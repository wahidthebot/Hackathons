import tkinter as tk
import random

user_bitcoin = 0.00
user_ethereum = 0.00
user_usd = 500.00

def update_labels():
    bit.config(text="User Bitcoin: " + format(user_bitcoin, '.4f'))
    eth.config(text="User Ethereum: " + format(user_ethereum, '.3f'))
    usd.config(text="User USD: " + format(user_usd, '.2f'))

    if user_usd == 0 and user_bitcoin == 0 and user_ethereum == 0:
        disable_buttons()
        show_popup()

def ethereum_button():
    global user_ethereum
    if user_ethereum != 0:
        pos_neg_ethereum = random.choice([0, 1])

        if pos_neg_ethereum == 0:
            percentage_to_subtract = random.uniform(0.1, 50.0) / 100.0
            user_ethereum -= user_ethereum * percentage_to_subtract
            text_box.insert(tk.END, "The Ethereum stock market went down by " +
                            format(percentage_to_subtract * 100, '.2f') + "%\n")
        else:
            percentage_to_subtract = random.uniform(0.1, 50.0) / 100.0
            user_ethereum += user_ethereum * percentage_to_subtract
            text_box.insert(tk.END, "The Ethereum stock market went up by " +
                            format(percentage_to_subtract * 100, '.2f') + "%\n")
    else:
        text_box.insert(tk.END, "You have no Ethereum\n")

    update_labels()

def bitcoin_button():
    global user_bitcoin
    if user_bitcoin != 0:
        pos_neg = random.choice([0, 1])

        if pos_neg == 0:
            percentage_to_subtract = random.uniform(0.1, 50.0) / 100.0
            user_bitcoin -= user_bitcoin * percentage_to_subtract
            text_box.insert(tk.END, "The Bitcoin stock market went down by " +
                            format(percentage_to_subtract * 100, '.2f') + "%\n")
        else:
            percentage_to_add = random.uniform(0.1, 50.0) / 100.0
            user_bitcoin += user_bitcoin * percentage_to_add
            text_box.insert(tk.END, "The Bitcoin stock market went up by " +
                            format(percentage_to_add * 100, '.2f') + "%\n")
    else:
        text_box.insert(tk.END, "You have no Bitcoin\n")
    update_labels()

def sell_bit():
    global user_usd, user_bitcoin
    if user_bitcoin == 0:
        text_box.insert(tk.END, "Insufficient funds\n")
    else:
        try:
            amount = float(transfer_entry_bitcoin.get())
            if amount <= user_bitcoin:
                user_usd += amount * 34101
                user_bitcoin -= amount
            else:
                text_box.insert(tk.END, "Insufficient Bitcoin\n")
            update_labels()
        except ValueError:
            pass

def sell_eth():
    global user_usd, user_ethereum
    if user_ethereum == 0:
        text_box.insert(tk.END, "Insufficient funds\n")
    else:
        try:
            amount = float(transfer_entry.get())
            if amount <= user_ethereum:
                user_usd += amount * 1784.95
                user_ethereum -= amount
            else:
                text_box.insert(tk.END, "Insufficient Ethereum\n")
            update_labels()
        except ValueError:
            pass

def transfer_bit():
    global user_usd, user_bitcoin
    try:
        amount = float(transfer_entry.get())
        if amount <= user_usd:
            user_usd -= amount
            user_bitcoin += amount / 34101
        else:
            text_box.insert(tk.END, "Insufficient funds\n")
        update_labels()
    except ValueError:
        pass

def transfer_eth():
    global user_usd, user_ethereum
    try:
        amount = float(transfer_entry.get())
        if amount <= user_usd:
            user_usd -= amount 
            user_ethereum += amount / 1784.95
        else:
            text_box.insert(tk.END, "Insufficient funds\n")
        update_labels()
    except ValueError:
        pass

def disable_buttons():
    button.config(state=tk.DISABLED)
    transfer_bit.config(state=tk.DISABLED)
    transfer_ethereum.config(state=tk.DISABLED)
    sell_bit.config(state=tk.DISABLED)
    sell_ethereum.config(state=tk.DISABLED)
    invest_bitcoin.config(state=tk.DISABLED)

def show_popup():
    popup = tk.Toplevel(root)
    popup.geometry("200x100")
    popup.title("Game Over")
    label = tk.Label(popup, text="You lost all your money :(")
    label.pack()

root = tk.Tk()
root.geometry("600x600")
root.title("Crypto Trading")
root.configure(bg="#84828F")

bit = tk.Label(root, text="User Bitcoin: " + str(user_bitcoin), bg="#6A687A")
bit.pack()
bit.place(relx=0.85, rely=0.0)

eth = tk.Label(root, text="User Ethereum: " + str(user_ethereum), bg="#6A687A")
eth.pack()
eth.place(relx=0.0, rely=0.0)

usd = tk.Label(root, text="User USD: " + str(user_usd), font=("Arial", 16), bg="#536271")
usd.pack()
usd.place(relx=0.4, rely=0.0)

button = tk.Button(root, text="Invest Bitcoin", command=bitcoin_button, bg="#3E4C5E", fg="white")
button.pack()
button.place(relx=0.85, rely=0.13)
invest_bitcoin = button

button = tk.Button(root, text="Invest Ethereum", command=ethereum_button, bg="#3E4C5E", fg="white")
button.pack()
button.place(relx=0.0, rely=0.13)

transfer_entry = tk.Entry(root)
transfer_entry.pack()
transfer_entry.place(relx=0.42, rely=0.3)

transfer_bit = tk.Button(root, text="Buy Bitcoin", command=transfer_bit, bg="#2C3D55", fg="white")
transfer_bit.pack()
transfer_bit.place(relx=0.85, rely=0.3)

transfer_ethereum = tk.Button(root, text="Buy Ethereum", command=transfer_eth, bg="#2C3D55", fg="white")
transfer_ethereum.pack()
transfer_ethereum.place(relx=0.0, rely=0.3)

transfer_entry_bitcoin = tk.Entry(root)
transfer_entry_bitcoin.pack()
transfer_entry_bitcoin.place(relx=0.85, rely=0.55)

transfer_entry_etheruem = tk.Entry(root)
transfer_entry_etheruem.pack()
transfer_entry_etheruem.place(relx=0, rely=0.55)

text_box = tk.Text(root, width=50, height=10)
text_box.pack()
text_box.place(relx=0.18, rely=0.5)

sell_bit = tk.Button(root, text="Sell Bitcoin", command=sell_bit, bg="#3E4C5E", fg="white")
sell_bit.pack()
sell_bit.place(relx=0.87, rely=0.5)

sell_ethereum = tk.Button(root, text="Sell Ethereum", command=sell_eth, bg="#3E4C5E", fg="white")
sell_ethereum.pack()
sell_ethereum.place(relx=0.0, rely=0.5)

root.mainloop()
