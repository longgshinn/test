gameplay=["player","enemy1"]
print(*gameplay,sep=", ")
x=input("New enemy's name?")
gameplay.append(x)
for _ in range(2):
    y=input("Shoot/Spawn?").lower()
    if y=="shoot":
        gameplay.append("Bullet")
        print(*gameplay, sep=", ")
    elif y=="spawn":
        gameplay.append("Enemy")
        print(*gameplay, sep=", ")