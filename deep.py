
deep_thought = input("What is the Answer to the great question of life, the Universe and everything? ")

match deep_thought:
    case "42" | "forty two" | "forty-two":
        print("YES")
    case _:
        print("NO")