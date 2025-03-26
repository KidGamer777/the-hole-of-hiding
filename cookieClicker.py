# This is the importing of the main libraries needed.
import tkinter as tk
import threading
from pathlib import Path 
import time 
# These are all of my global variables. They store values I need across my entire code. 
increment = 1
upgradeCost = 20
upgradeCost2 = 100
cakeincrement = 1
cakeupgradecost = 50
cpsupgradecost = 200
cpsinterval = 1
upgradecost3 = 300
upgradecost4 = 1000
root = tk.Tk()

# This code is the main increasing function. It adds the increment of cookies per click to the main number. 
def increase():
    global increment 
    bigger = numbah["text"] + increment
    numbah["text"] = bigger

# This is the upgrading function. It checks if the cookies you have are more than the upgrade cost, and if it is, increases the upgrade cost, the CPC, then updates the icons for those. 
def upgrade():
    global upgradeCost
    global increment
    if numbah["text"] >= upgradeCost:
        increment += 2
        smaller = numbah["text"] - upgradeCost
        numbah["text"] = smaller
        upgradeCost += 200
        upgrade1["text"] = f"Purchase for {upgradeCost} cookies!"
        cpc["text"] = f"Cookies Per Click: {increment}"
    else:
        return

# This is the second upgrading function. It does the same as the first one, but multiplies the CPC by 2.
def upgrade2():
    global upgradeCost2
    global increment
    if numbah["text"] >= upgradeCost2:
        increment += increment
        smaller2 = numbah["text"] - upgradeCost2
        numbah["text"] = smaller2
        upgradeCost2 = upgradeCost2 * 5
        upgradeAgain["text"] = f"Purchase for {upgradeCost2} cookies!"
        cpc["text"] = f"Cookies Per Click: {increment}"
    else:
        return
    
# This is the cake increasing function. It does the same thing as the increasing function, but for the cakes. 
def cakeIncrease():
    global cakeincrement
    numbah2["text"] += cakeincrement
    numbah2["text"]
    cakepc["text"] = f"Cakes Per Click: {cakeincrement}"

# This does the same thing as the upgrading functions, but multiplies CPC by 5 and adds 5 more cakes to the cake upgrade button. 
def cakeUpgrade():
    global cakeupgradecost
    global increment
    if numbah2["text"] >= cakeupgradecost:
        increment = increment*5
        smaller3 = numbah2["text"] - cakeupgradecost
        numbah2["text"] = smaller3
        cakeupgradecost += 5
        cakeupgrade["text"] = f"Upgrade Cookies with Cakes! Costs {cakeupgradecost} cakes!"
        cpc["text"] = f"Cookies Per Click: {increment}"
    else:
        return

# This is the button that places the cake button. It 
def cakePlacement():
    if numbah["text"] >= 10000:
        evisceration = numbah["text"] - 10000
        numbah["text"] = evisceration 
        cake.grid(row=3, column= 1)
        cakebutton.forget
        cakeupgrade.grid(row=2, column=1)
    else:
        return




def cookies_brrrt():
    global cpsupgradecost
    global cpsinterval
    while True:
        time.sleep(3)
        zoomies =numbah["text"] + cpsinterval
        numbah["text"] = zoomies

def zoom_go_UPPIES():
    global cpsinterval 
    global cpsupgradecost
    if numbah["text"] >= cpsupgradecost:
        numbah["text"] -= cpsupgradecost 
        cpsinterval += 1
        cpsupgradecost = cpsupgradecost + 250
        cpsupgrade["text"] = f"Purchase Motor Power For {cpsupgradecost} cookies!"
        cpslabel["text"] = f"Cookies Per Second: {cpsinterval}"
    else:
        return 

def cpsupgrade_1():
    global upgradecost3
    global cpsinterval
    if numbah["text"] >= upgradecost3:
        numbah["text"] -= cpsupgradecost 
        cpsinterval = cpsinterval + 5
        upgradeCost3 = upgradeCost3 + 1000
        upgradeAgain["text"] = f"Purchase for {upgradeCost2} cookies!"
        cpslabel["text"] = f"Cookies Per Second: {cpsinterval}"
    else:
        return




# These seven files are my seven image files. 
img = tk.PhotoImage(file="./assets/cookie.png").subsample(2)

img2 = tk.PhotoImage(file="./assets/upgrade1.png").subsample(10)

img3 = tk.PhotoImage(file="./assets/upgrade2.png").subsample(55)

img4 = tk.PhotoImage(file="./assets/upgrade3.png").subsample(3)

img5 = tk.PhotoImage(file="./assets/upgrade4.png").subsample(5)

# This code forms the cake clicker and the cake placement button. 
cake = tk.Button(root, image=img4, command = cakeIncrease)
cakebutton = tk.Button(root, text="Purchase Cakes For 10,000 Cookies!", command=cakePlacement)
cakebutton.grid(row=2, column=1)
cakeupgrade = tk.Button(root, text=f"Upgrade Cookies with Cakes! Costs {cakeupgradecost} cakes!", command=cakeUpgrade)

# This code places my main cookie that continues to increase. 
lbl =tk.Button(root, image=img, command = increase)
lbl.grid(row = 1, column = 1)

# This is the main label for the cookies. It shows how many cookies you have. 
numbah = tk.Label(root, text=0, font = 300)
numbah.grid(row = 0, column = 1)

# This is the label that signifies where the upgrades are. 
upgradenotif = tk.Label(root, text="Upgrades", font = 50)
upgradenotif.grid(row= 4, column = 2)

# This button is what you click to upgrade the cookies. 
upgrade1 = tk.Button(root, text = f"Purchase for {upgradeCost} cookies!", command = upgrade, image=img2, compound="left")
upgrade1.grid (row = 1, column = 2)

# This is the button for the second upgrade. 
upgradeAgain = tk.Button(root, text = f"Purchase for {upgradeCost2} cookies!", command = upgrade2, image=img3, compound="left")
upgradeAgain.grid (row = 2, column = 2)

# This is the label that shows how many cookies per click you have. 
cpc = tk.Label(root, text=f"Cookies Per Click: {increment}")
cpc.grid (row=1, column=0)

# This is the labels that shows how many cakes per click you have. 
cakepc = tk.Label(root, text=f"Cakes Per Click: {cakeincrement}")
cakepc.grid(row=2, column=0)

# This is the label that shows how many cakes you have. 
numbah2 = tk.Label(root, text=0, font = 300)
numbah2.grid(row=4, column=0)

# This is the button that allows you to unlock and upgrade your CPS. 
cpsupgrade = tk.Button(root, text= f"Purchase Motor Power For {cpsupgradecost} cookies!", command = zoom_go_UPPIES, image = img5, compound="left")
cpsupgrade.grid(row=3, column=2)

# This is the label that tracks your cookies per second.
cpslabel = tk.Label(root, text=f"Cookies Per Second: {cpsinterval}")
cpslabel.grid(row = 4, column = 0)

# This is the button for the second upgrade. 
upgrade3 = tk.Button(root, text = f"Purchase for {upgradecost3} cookies!", command = cpsupgrade_1, image=img5, compound="left")
upgrade3.grid (row = 0, column = 3)

# This thread allows the autoclicker to run in the background of the main code. 
licoriche = threading.Thread(target=cookies_brrrt)
licoriche.start()

root.mainloop()
