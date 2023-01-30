def main():
    while 1:
        user_in_num_1 = int(input("Please input the first number"))
        x = False
        while x == False:
            user_in = input("Type in an operand (+,-,/,*)")
            if user_in in ['+','-','*', '/']:
                x = True
        user_in_num_2 = int(input("Please input number two."))
        if user_in == '+':
            print(user_in_num_1 + user_in_num_2)
        elif user_in == '-':
            print(user_in_num_1 - user_in_num_2)
        elif user_in == '*':
            print(user_in_num_1 * user_in_num_2)
        elif user_in == '/':
            print(user_in_num_1 / user_in_num_2)
    pass

if __name__ == '__main__':
    main()