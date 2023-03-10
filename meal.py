
def main():
    current_time = convert(input("What time is it?"))
    if 7 <= current_time <= 8:
        print("breakfeast time")
    elif 12 <= current_time <= 13:
        print("dinner time")
    elif 18 <= current_time <= 19:
        print("supper time")
    else:
        print("finish meal time")


def convert(time):
    hours, minutes = time.split(":")
    convert_time = float(minutes) / 60
    return float(hours) + convert_time


if __name__ == "__main__":
    main()


