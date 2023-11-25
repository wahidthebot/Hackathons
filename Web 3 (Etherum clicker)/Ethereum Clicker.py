import tkinter as tk
from tkinter import messagebox

class AutoClickTier:
    def __init__(self, cost, mining_rate):
        self.cost = cost
        self.mining_rate = mining_rate
        self.count = 0

class GPUTier:
    def __init__(self, cost, mining_rate):
        self.cost = cost
        self.mining_rate = mining_rate
        self.count = 0

class Upgrade:
    def __init__(self, cost, description, effect):
        self.cost = cost
        self.description = description
        self.effect = effect
        self.is_purchased = False

class CryptoClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Crypto Clicker")
        self.master.geometry("500x400")

        self.crypto_coins = 0.0
        self.crypto_rate = 1.0
        self.gpu_count = 0
        self.base_gpu_costs = [10, 20, 30]
        self.gpus = [
            GPUTier(cost=self.base_gpu_costs[0], mining_rate=0.2),
            GPUTier(cost=self.base_gpu_costs[1], mining_rate=0.6),
            GPUTier(cost=self.base_gpu_costs[2], mining_rate=1),
        ]
        
        self.base_autoclick_costs = [1000, 2000, 3000]
        self.autoclicks = [
            AutoClickTier(cost=self.base_autoclick_costs[0], mining_rate=10),
            AutoClickTier(cost=self.base_autoclick_costs[1], mining_rate=20),
            AutoClickTier(cost=self.base_autoclick_costs[2], mining_rate=50),
        ]

        self.ethereum_value = 2084.26  # Value of 1 Ethereum in USD

        self.label_crypto_coins = tk.Label(self.master, text="Crypto Coins: 0.0", font=("Helvetica", 16), fg="green")
        self.label_crypto_rate = tk.Label(self.master, text="Mining Rate: 1.0 per click", font=("Helvetica", 12), fg="blue")
        self.label_gpu_count = tk.Label(self.master, text="GPU Count: 0", font=("Helvetica", 12), fg="orange")
        self.label_usd_value = tk.Label(self.master, text="USD Value: 0.0", font=("Helvetica", 12), fg="black")

        self.gpu_buttons = []
        for i, gpu_tier in enumerate(self.gpus):
            button = tk.Button(self.master, text=f"Buy GPU Tier {i + 1}\nCost: {gpu_tier.cost} coins\nMining Rate: {gpu_tier.mining_rate}\nCount: {gpu_tier.count}", command=lambda tier=gpu_tier, index=i: self.buy_gpu(tier, index), font=("Helvetica", 10), bg="purple", fg="white", padx=10, pady=5)
            self.gpu_buttons.append(button)

        self.autoclick_buttons = []
        for i, autoclick_tier in enumerate(self.autoclicks):
            button = tk.Button(self.master, text=f"Tier {i + 1} Auto-Clicking\nCost: {autoclick_tier.cost} coins\nMining Rate: {autoclick_tier.mining_rate}\nCount: {autoclick_tier.count}", command=lambda tier=autoclick_tier, index=i: self.buy_autoclick(tier, index), font=("Helvetica", 10), bg="orange", fg="black")
            self.autoclick_buttons.append(button)

        self.upgrades = [
            Upgrade(cost=500, description="Double Click Value", effect=self.double_click_value),
            Upgrade(cost=1500, description="Triple Click Value", effect=self.triple_click_value),
            # Add more upgrades here
        ]

        self.upgrade_buttons = []
        for i, upgrade in enumerate(self.upgrades):
            button = tk.Button(
                self.master,
                text=f"Upgrade: {upgrade.description}\nCost: {upgrade.cost} coins",
                command=lambda u=upgrade, index=i: self.buy_upgrade(u, index),
                font=("Helvetica", 10),
                bg="yellow",
                fg="black",
            )
            self.upgrade_buttons.append(button)

        eth_img = tk.PhotoImage(file=r"C:\Users\hussa\OneDrive\Desktop\hackathon\Web 3 (Etherum clicker)\Eth_hak_logo.png")
        self.click_button = tk.Button(
            self.master, 
            image=eth_img, 
            command=self.mine_crypto, 
            font=("Helvetica", 14), 
            bg='lightblue', 
            fg="black", 
            bd=0, 
            highlightthickness=0, 
            activebackground='lightblue',
            relief=tk.RAISED
        )
        self.click_button.image = eth_img

        self.label_crypto_coins.pack(pady=10)
        self.label_crypto_rate.pack(pady=5)
        self.label_gpu_count.pack(pady=5)

        for button in self.gpu_buttons:
            button.pack(pady=5)

        for button in self.autoclick_buttons:
            button.pack(pady=5)

        for button in self.upgrade_buttons:
            button.pack(pady=5)

        self.label_usd_value.pack(pady=5)

        self.click_button.pack(pady=20)

        self.start_gpu_mining()

    def update_usd_value(self):
        usd_value = self.crypto_coins * self.ethereum_value
        self.label_usd_value.config(text=f"USD Value: ${usd_value:.2f}")

    def mine_crypto(self):
        self.click_button.config(relief=tk.SUNKEN)
        self.crypto_coins += max(1.0, self.crypto_rate)
        self.crypto_coins = round(self.crypto_coins, 1)
        self.label_crypto_coins.config(text=f"Ethereum Coins: {self.crypto_coins}")
        self.label_crypto_rate.config(text=f"Mining Rate: {max(1.0, self.crypto_rate)} per click")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")
        self.update_usd_value()
        self.master.after(100, self.reset_button_relief)

    def reset_button_relief(self):
        self.click_button.config(relief=tk.RAISED)

    def buy_gpu(self, tier, index):
        if self.crypto_coins >= tier.cost:
            self.crypto_coins -= tier.cost
            tier.count += 1
            self.gpu_count += 1
            self.crypto_rate += self.gpus[index].mining_rate
            self.crypto_rate = round(self.crypto_rate, 1)
            messagebox.showinfo("GPU Purchased", f"You bought a GPU! Mining rate increased by {self.gpus[index].mining_rate}")
            self.label_crypto_rate.config(text=f"Mining Rate: {self.crypto_rate}")
            for gpu in self.gpus:
                gpu.cost *= 2
            for i, button in enumerate(self.gpu_buttons):
                button.config(text=f"Buy GPU Tier {i + 1}\nCost: {self.gpus[i].cost} coins\nMining Rate: {self.gpus[i].mining_rate}\nCount: {self.gpus[i].count}")
        else:
            messagebox.showinfo("Not Enough Coins", f"You need at least {tier.cost} coins to buy this GPU.")
        self.label_crypto_coins.config(text=f"Ethereum Coins: {self.crypto_coins}")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")
        self.update_usd_value()

    def buy_autoclick(self, tier, index):
        if self.crypto_coins >= tier.cost:
            self.crypto_coins -= tier.cost
            tier.count += 1
            self.crypto_rate += tier.mining_rate
            self.crypto_rate = round(self.crypto_rate, 1)
            messagebox.showinfo("Auto-Clicking GPU Purchased", f"You bought an auto-clicking GPU! Mining rate increased by {tier.mining_rate} per second")
            tier.cost *= 2
            for i, button in enumerate(self.autoclick_buttons):
                button.config(text=f"Tier {i + 1} Auto-Clicking\nCost: {self.autoclicks[i].cost} coins\nMining Rate: {self.autoclicks[i].mining_rate}\nCount: {self.autoclicks[i].count}")
        else:
            messagebox.showinfo("Not Enough Coins", f"You need at least {tier.cost} coins to buy this auto-clicking GPU.")
        self.label_crypto_coins.config(text=f"Ethereum Coins: {self.crypto_coins}")
        self.update_usd_value()

    def double_click_value(self):
        self.crypto_rate *= 2

    def triple_click_value(self):
        self.crypto_rate *= 3

    def buy_upgrade(self, upgrade, index):
        if self.crypto_coins >= upgrade.cost and not upgrade.is_purchased:
            self.crypto_coins -= upgrade.cost
            upgrade.is_purchased = True
            upgrade.effect()
            messagebox.showinfo("Upgrade Purchased", f"You purchased: {upgrade.description}")
            for i, button in enumerate(self.upgrade_buttons):
                button.config(text=f"Upgrade: {self.upgrades[i].description}\nCost: {self.upgrades[i].cost} coins")
        else:
            messagebox.showinfo("Not Enough Coins or Already Purchased", f"Cost: {upgrade.cost} coins")
        self.label_crypto_coins.config(text=f"Ethereum Coins: {self.crypto_coins}")
        self.label_crypto_rate.config(text=f"Mining Rate: {self.crypto_rate} per click")
        self.update_usd_value()

    def start_gpu_mining(self):
        self.master.after(1000, self.auto_mine)

    def auto_mine(self):
        auto_mined_coins = 0
        for autoclicker in self.autoclicks:
            auto_mined_coins += autoclicker.count * autoclicker.mining_rate
        self.crypto_coins += auto_mined_coins
        self.crypto_coins = round(self.crypto_coins, 1)
        self.label_crypto_coins.config(text=f"Ethereum Coins: {self.crypto_coins}")
        self.label_gpu_count.config(text=f"GPU Count: {self.gpu_count}")
        self.update_usd_value()
        self.master.after(1000, self.auto_mine)

def main():
    root = tk.Tk()
    root.configure(bg='lightblue')
    game = CryptoClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()