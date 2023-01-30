def main():
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: dictionary_print, # You can put functions here!
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    x = int(input("Enter 1-12: "))
    month = months[x]
    if isinstance(month, str):
        print(month)
    else:
        month()


def dictionary_print():
    print("Mayday, mayday!")


if __name__ == '__main__':
    main()