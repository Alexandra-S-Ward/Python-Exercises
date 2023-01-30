from functools import reduce

def main():
    lst = [1,2,3,4,5]
    print(multiply_by(lst,5))
    print(list(map(multiply_by_two_map, [3,4,5,6])))
    print(lst) # lst unmodified
    print(list(filter(is_even, lst))) # only even
    print(list(zip(lst, [44,33,22]))) # Combine x iterables into a tuple
    print(reduce(accumulator, lst,0))

    # lambda param: action(param)
    print(list(map(lambda item: item*2,lst))) # multiply_by_two

    tuple_sort = [(0,2),(4,3),(9,9), (10,-1)]
    print(list(map(lambda x: x[0]**2, tuple_sort))) # get the square number of all item 0 in tuple
    tuple_sort.sort(key=lambda x: x[1])
    print(tuple_sort)

    # List Comprehension
    lst_1 = [char for char in 'hello world'] 
    lst_2 = [num for num in range(0,10)]
    lst_3 = [num**2 for num in range(0,10)]
    lst_4 = [num**2 for num in range(0,10) if num % 2 == 0]
    print(lst_1)
    print(lst_2)
    print(lst_3)
    print(lst_4)
    simple_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

    # Dictionary comprehension
    my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0 }
    print(my_dict)

    # Another lambda test, multiple parameters
    multiply = lambda x,y : x*y if x % 2 == 0 else x**y
    print(multiply(4,3))


def multiply_by(lst: list, operand : int): # Only impacts the new list
    new_list = []
    for i in lst:
        new_list.append(i*operand)
    return new_list

def multiply_by_two_map(item):
    return item * 2

def is_even(item):
    return item % 2 == 0

def accumulator(acc, item):
    print(f'{acc} - {item}')
    return acc + item

if __name__ == '__main__':
    main()