def main():
    x = int(input("Enter the maximum number."))
    i = 1
    while i <= x: # while
        print(i)
        i+=1
    oranges = ["Clementine", "Satsuma", "Tangerine"]
    for orange in oranges:
        print(orange)
    print()
    print()

    for i in range(len(oranges)):
        print(oranges[i])

    # Enumerate combines both of the above attempts at for loops
    for k, v in enumerate(oranges):
        print(f'Value: {v} ------- Using list indexing: {oranges[k]}')
    
    print(raise_to_power(2,8))

def raise_to_power(base_num: int, pow_num: int):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

if __name__ == '__main__':
    main()