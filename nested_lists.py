def main():
    lst = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    print(lst)
    print(lst[0][0]) # print first row / first column
    print(lst[0][1]) # print first row, second column
    print(lst[1][0]) # print second row, first column
    print("Iterating over the 2D list")
    for row in lst:
        for col in row:
            print(col)

if __name__ == '__main__':
    main()