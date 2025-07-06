from random import choice
from sys import exit

def menu(state):
    while True:
        opt = input("\n**menu**: luckygame, store, status, quit: ")
        if opt == "luckygame" or opt.strip() == "":
            luckygame(state)
        elif opt == "store":
            store(state) 
        elif opt == "status":
            status(state)
        elif opt == "quit":
            print(f"\nYour final score: {state["score"]}")
            print("Thanks for playing!")
            return exit()

def luckygame(state):
    while True:
        opt = input("\n**luckygame**: box => -1 chance, back => menu: ")
        if (opt == "box" or opt.strip() == "") \
            and state["chance"]:
            box, (s, m) = choice(list(state["boxdict"].items()))
            state["score"] += s
            state["money"] += m
            state["chance"] -= 1
            print(f"You got a {box} box!")
            print(f"chances: {state["chance"]} (-1)", \
                f"score: {state["score"]} (+{s})", \
                f"money: {state["money"]} (+{m})")
        elif opt == "back":
            break
        else:
            print("**out of chance**")

def store(state):
    while True:
        opt = input("\n**store**: buy => chance (+1) money (-30), back => menu: ")
        if (opt == "buy" or opt.strip() == "") \
            and state["money"] >= 30:
            state["money"] -= 30
            state["chance"] += 1
            print(f"chances: {state["chance"]} (+1)", \
                f"money: {state["money"]} (-30)")
        elif opt == "back":
            break
        else:
            print("**out of money**")

def status(state):
        print(f"chances: {state["chance"]}", \
            f"score: {state["score"]}", \
            f"money: {state["money"]}")

def main():
    state = {
        "chance": 3,
        "money": 0, 
        "score": 0, 
        "boxdict": {
            "normal": (5, 15),
            "rare": (10, 30),
            "epic": (15, 60),
            "legendary": (20, 120)
        } 
    }
    
    state = menu(state)


if __name__ == "__main__":
    main()
