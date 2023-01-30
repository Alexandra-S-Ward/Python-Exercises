def main():
    print("    /|")
    print("   / |")
    print("  /  |")
    print(" /   |")
    print("/____|")
    name = "Alexandra"
    working_with_strings(name)
    working_with_numbers([1,2,3,4,5])
    user_input()
    print()
    calculator()
    print()
    mad_libs()
    print()
    list_brushups()
    print()
    co_ords = return_coords([(33,2.1), (39.3,23.9)], 1)
    if_test(co_ords)

def variables_brushup(name):
    # Casting is done via TYPE(variable) ie int(x)
    x = 52 # int
    age_in_years = 30.3 # float
    print(f'{x} {name} {age_in_years}')
    # Casting to different types
    y = float(52) # float
    age_in_years_int = int(30.3) # int
    print(f'{y} {name} {age_in_years_int}')

def working_with_strings(name):
    # length
    print(len(name))
    print(name[::-1]) # reverse string
    print(name[0:4]) # First four chars
    print(name.upper()) # cases
    print(name.lower()) # cases
    print(name.index('x')) # find index
    print(name.replace('dra','der')) # replace
    print(name.split("x")) # split

def working_with_numbers(nums):
    print(nums)
    results = []
    results.append(nums[4]+nums[0])
    results.append(nums[4]-nums[0])
    results.append(nums[4]*nums[1]) # times
    results.append(nums[4]/nums[0]) # divide
    results.append(nums[4]%nums[0]) # remainder
    total_add = 0
    for args in nums:
        total_add += args
    print(total_add) # total of all numbers added
    print(abs(nums[0] - -300)) # 301 = -301
    print(max(nums)) # maximum
    print(min(nums)) # minimum
    print(results) # result of adding, subtracting, dividing etc
    print(pow(3,2)) # power -> 9
    print(pow(2,8)) # 256

def user_input():
    user_in = input("Input a number: ")
    print()
    user_in_second = input("And a second: ")
    print()
    print(int(user_in)*int(user_in_second))

def calculator():
    x = input("Enter an equation")
    print(eval(x)) # DANGEROUS, but we are building a better calculator later

def mad_libs():
    colour = input("Enter a colour: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Who is your favourite celebrity? ")
    print(f'Roses are {colour}')
    print(f'{plural_noun} are blue')
    print(f'I love {celebrity}')

def list_brushups():
    friends = ["Alexandra", "Rupali", "Prosper", "Ewo"]
    print(friends)
    print(" ".join(friends)) # make a string
    print(friends[1::]) # Alexandra is not alexandra's friend
    print(friends[-1]) # only Ewo
    print(friends[-1::-2]) # Ewo and Rupali. It skips due to the final parameter
    print(friends[::-1]) # Reverse list
    friends[0] = "Devi" 
    print(friends[0])
    friends.append("Oscar") # Back of the list
    friends.pop(0) # Remove element 0
    other_friends = ["Connor", "Jacob"]
    friends.append(other_friends)
    print(friends) # append makes the list 3d
    friends.pop(-1) # remove the last element, in this case the list
    friends.extend(other_friends)
    print(friends) # the friends list now has all friends instead of a list with an embedded list.
    friends.insert(0, "James")
    print(friends)
    print(friends.index("Ewo")) # Ewo is index 3
    friends.remove("Ewo")
    friends.clear() # Clear the list
    friends.insert(0,"Ewo")
    friends.insert(0,"Ewo") # insert Ewo twice
    friends.extend(other_friends)
    print(friends.count("Ewo"))
    x = [1,44,32,66,2,3,4,5]
    x.sort() # x.sort returns nothing, it modifies object x
    print(x) 
    x.insert(3,500)
    print(sorted(x)) # sorted returns, so it can be printed
    reversed_list = x[::-1]
    x.reverse()
    print(f'{x} --- {reversed_list}')
    tuples_brushup()

def tuples_brushup():
    # Tuples are similar to lists but are immutable.
    co_ordinates = (43.2, 45.3)
    print(co_ordinates)
    print(co_ordinates[0])
    print(co_ordinates[::-1])

# FUNCTION practice. Typecasted, with a return
def return_coords(co_ords_list: list, i: int):
    return co_ords_list[i]

def if_test(co_ords: tuple):
    expected = (39.3, 23.9)
    if co_ords == expected:
        print(True)
    else:
        print(False)
    number = co_ords[0]
    if number < 0:
        print("Co-ordinate 1 is below zero.")
    elif 0 < number < 30:
        print("Co ordinate 1 is less than 30")
    else:
        print(number)

if __name__ == "__main__":
    main()