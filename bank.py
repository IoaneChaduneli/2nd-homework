bank_greeting = input("You enter in the bank: ").lower()

if "hello" in bank_greeting:
    print("$ 0")
elif "h" in bank_greeting[0:]:
    print("$ 20")
else:
    print("$ 100")
