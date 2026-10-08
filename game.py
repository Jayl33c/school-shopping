# FIXED: Standardized dictionary types to 'worker' to match the state machine logic
ROUTE = [
    {"type": "worker", "name": "Manager", "where": "In Foot Locker by the cashier",
     "says": "Back in '89 this Bay Plaza had a payphone that WORKED. Respect the payphone."},
    {"type": "robber", "name": "Five Finger Discount Freddy", "where": "lurking by the entrance",
     "toll": 40},
    {"type": "worker", "name": "Mr. Garces", "where": "watching the whole interaction from the store across",
     "says": "Yo kid, fix your collar. And tell those kids to do their homework."},
    {"type": "robber", "name": "Richard the Rich", "where": "posted up by the ATM that's always broken",
     "toll": 60},  # inflation hit Richard too
]


def ask(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"  Pick one of: {', '.join(options)}")


state = "walking"   # walking | worker | robber | Bay Plaza Mall | broke
money = 200         # FIXED: Set to $200 for school shopping
respect = 0         # how many workers you showed love to
stop = 0            # how far along the route you are
who = None          # who you're dealing with right now

print("Jaylee leaves the house with $200. Destination: Bay Plaza Mall.")

while state not in ("Bay Plaza Mall", "broke"):
    print(f"\n[STATE: {state.upper()} | ${money} | respect: {respect}]")

    if state == "walking":
        if stop == len(ROUTE):
            state = "Bay Plaza Mall"
            continue
        who = ROUTE[stop]
        stop += 1
        print(f"You spot {who['name']} {who['where']}.")
        state = who["type"]  # Switches to 'worker' or 'robber'

    elif state == "worker":  # FIXED: Now matches the 'worker' type from ROUTE
        if ask(f"(t)alk to {who['name']} or (n)od and keep it moving? ", ["t", "n"]) == "t":
            print(f"{who['name']}: \"{who['says']}\"")
            respect += 1
            print("  +1 respect. Word gets around.")
        else:
            print(f"{who['name']} squints at you. Noted.")
        state = "walking"

    elif state == "robber":
        if respect > 0:  # SAME bandit, different outcome -- because of state
            print(f"{who['name']} sees the managers nod at you. \"Oh my bad, Jaylee. Have a blessed day.\"")
        else:
            print(f"{who['name']}: \"Yo, lend me ${who['toll']}.\"")
            if ask("(r)un or (p)ay the toll? ", ["r", "p"]) == "r":
                if random.random() < 0.5:
                    print("You walk away. Escaped!")
                else:
                    print(f"You trip over a wet spot on the floor. He gets ${who['toll']} anyway.")
                    money -= who["toll"]
            else:
                print(f"You hand over ${who['toll']}. At least he said thank you.")
                money -= who["toll"]
        state = "broke" if money <= 0 else "walking"

# Final ending screens
print(f"\n[STATE: {state.upper()} | ${money}]")
if state == "broke":
    print("Jaylee is broke before she reaches the door. The Mall security stares in disappointment.")
elif money == 200:
    print("Full $200 intact. Shoes and a Shirt. Legendary run.")
elif money >= 100:
    print(f"Made it with ${money}. Got your shoes with minor losses.")
else:
    print(f"Made it with ${money} and your dignity. Barely.")
