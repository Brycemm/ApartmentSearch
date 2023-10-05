# dunder
if __name__ == "__main__":
    # Defining function to search for apartments
    def apt_search1(city, max_rent, min_beds, pets_allowed):

        # Defining the city variable using user input
        # city = str(input("Which city are you looking for an apartment in? "))
        # # User input for max rent
        # max_rent = int(input("What is the maximum budget? "))
        # # user input for number of bedrooms
        # min_beds = int(input("How many bedrooms do you need? "))
        # # user input for pets allowed
        # pets_allowed = str(input("Are you looking for a place that allows pets? y/n "))
        # # final output
        # print(
        #     f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all "
        #     f"within a budget of ${max_rent} per month.")
        # # bool statement
        # if pets_allowed.lower() == "y":
        #     print("Pets are allowed.")
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, '
              f'all within a budget of ${max_rent} per month. Pets are allowed!')
    apt_search1("Detroit", 1000, 2, pets_allowed=True)

    # function 2
    def apt_search2(city, max_rent, min_beds=0, pets_allowed=False):
        # function with both allowed
        if min_beds and pets_allowed:
            print(
                f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, '
                f'all within a budget of ${max_rent} per month. Pets are allowed!')
        # function with just min beds
        elif min_beds:
            print(
                f'Welcome to GC property Management! Looking up listings in {city} for {min_beds} bedroom apartments,'
                f' all within a budget of ${max_rent} per month.')
        # function with just pets allowed
        elif pets_allowed:
            print(f'Welcome to GC property Management! Looking up listings in {city} all within a budget of ${max_rent}'
                  f' per month. Pets are allowed!')
        # function with both pets and beds omitted
        else:
            print(f'Welcome to GC property Management! Looking up listings in {city} all within a budget'
                  f' of ${max_rent}.')


    apt_search2("Detroit", 1000, 2)
    apt_search2("Detroit", 1000, pets_allowed=True)
    apt_search2("Detroit", 1000)

    # lamda 1
    def plus_one_hundred(y):
        return y + 100

    result1 = plus_one_hundred(14)
    print(result1)

    # lamda 2
    def square_num(z):
        return z ** 2

    result2 = square_num(14)
    print(result2)

    # lamda 3

    def concatenate(c):
        return "-" + c

    result3 = concatenate("World!")
    print(result3)

    # lamda 4
    def divide_by_three(d):
        return d / 3

    result4 = divide_by_three(14)
    print("{0:.3f}".format(result4))
