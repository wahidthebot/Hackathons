import tkinter as tk
from tkinter import PhotoImage, messagebox

class GPUTier:
    def __init__(self, cost, mining_rate):
        self.cost = cost
        self.mining_rate = mining_rate
        self.count = 0

class CryptoClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Crypto Clicker")
        self.master.geometry("400x400")

        self.crypto_coins = 0.0
        self.crypto_rate = 1.0
        self.base_gpu_costs = [10, 20, 30]
        self.gpus = [
            GPUTier(cost=self.base_gpu_costs[0], mining_rate=0.1),
            GPUTier(cost=self.base_gpu_costs[1], mining_rate=0.2),
            GPUTier(cost=self.base_gpu_costs[2], mining_rate=0.3),
        ]

        # Create labels to display crypto coins, mining rate, and GPU count
        self.label_crypto_coins = tk.Label(self.master, text="Crypto Coins: 0.0", font=("Helvetica", 16), fg="green")
        self.label_crypto_rate = tk.Label(self.master, text="Mining Rate: 1.0 per click", font=("Helvetica", 12), fg="blue")
        self.label_gpu_count = tk.Label(self.master, text="GPU Count: 0", font=("Helvetica", 12), fg="orange")

        # Create buttons for each GPU tier
        self.gpu_buttons = []
        for i, gpu_tier in enumerate(self.gpus):
            button = tk.Button(self.master, text=f"Buy GPU Tier {i + 1}\nCost: {gpu_tier.cost} coins\nMining Rate: {gpu_tier.mining_rate}\nCount: {gpu_tier.count}", command=lambda tier=gpu_tier: self.buy_gpu(tier), font=("Helvetica", 10), bg="purple", fg="white")
            self.gpu_buttons.append(button)

        # Create mine button
        eth_img = PhotoImage(file="Eth_hak_.png")
        self.click_button = tk.Button(self.master, image=eth_img, command=self.mine_crypto, font=("Helvetica", 14), bg="yellow", fg="black")
        self.click_button.image = eth_img  # Keeping a reference to the image to prevent it from being garbage collected

        # Place widgets on the window
        self.label_crypto_coins.pack(pady=10)
        self.label_crypto_rate.pack(pady=5)
        self.label_gpu_count.pack(pady=5)

        for button in self.gpu_buttons:
            button.pack(pady=5)

        self.click_button.pack(pady=20)

        # Start GPU auto mining loop
        self.start_gpu_mining()

    def mine_crypto(self):
        # Increment crypto coins based on mining rate
        self.crypto_coins += max(1.0, self.crypto_rate)  # Ensure that coins per click cannot go below 1.0
        self.crypto_coins = round(self.crypto_coins, 1)  # Round off to 1 decimal point

        # Update the labels
        self.label_crypto_coins.config(text=f"Crypto Coins: {self.crypto_coins}")
        self.label_crypto_rate.config(text=f"Mining Rate: {max(1.0, self.crypto_rate)} per click")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")

    def buy_gpu(self, tier):
        # Buy GPU if the player has enough coins
        if self.crypto_coins >= tier.cost:
            self.crypto_coins -= tier.cost
            tier.count += 1
            self.gpu_count += 1
            self.crypto_rate += tier.mining_rate
            self.crypto_rate = round(self.crypto_rate, 1)  # Round off to 1 decimal point
            messagebox.showinfo("GPU Purchased", f"You bought a GPU! Mining rate increased by {tier.mining_rate}")

            # Increase the cost of the purchased GPU tier by 5 coins
            tier.cost += 5

            # Update the labels for GPU buttons
            for i, button in enumerate(self.gpu_buttons):
                button.config(text=f"Buy GPU Tier {i + 1}\nCost: {self.gpus[i].cost} coins\nMining Rate: {self.gpus[i].mining_rate}\nCount: {self.gpus[i].count}")

        else:
            messagebox.showinfo("Not Enough Coins", f"You need at least {tier.cost} coins to buy this GPU.")

        # Update the labels
        self.label_crypto_coins.config(text=f"Crypto Coins: {self.crypto_coins}")
        self.label_crypto_rate.config(text=f"Mining Rate: {max(1.0, self.crypto_rate)} per click")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")

    def start_gpu_mining(self):
        # Start a loop to simulate automatic mining by GPUs
        self.master.after(5000, self.auto_mine)

    def auto_mine(self):
        # Automatically mine coins based on the GPU rate
        auto_mined_coins = self.gpu_count * self.gpus[0].mining_rate
        self.crypto_coins += auto_mined_coins
        self.crypto_coins = round(self.crypto_coins, 1)  # Round off to 1 decimal point

        # Update the labels
        self.label_crypto_coins.config(text=f"Crypto Coins: {self.crypto_coins}")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")

        # Schedule the next automatic mining after 5 seconds
        self.master.after(5000, self.auto_mine)


def main():
    root = tk.Tk()
    root.configure(bg='lightblue')  # Set background color
    game = CryptoClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
