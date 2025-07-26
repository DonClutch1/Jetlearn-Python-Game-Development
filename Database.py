#create an empty dictionary
countryDB = {}
while True:
    #print menu
    print("1. Insert")
    print("2. Display all the countries")
    print("3. Display all the capitals")
    print("4. Get capital")
    print("5. Delete")
    #user input
    choice = int(input("Enter your choice (1-5)"))
    if choice == 1:
        country = input("Enter the country: ").upper()
        capital = input("Enter the capital: ").upper()
        countryDB[country] = capital
    #display the data of countries
    elif choice == 2:
        print(list(countryDB.keys()))
        #display the data of capitals
    elif choice == 3:
        print(list(countryDB.values()))
    # to display specific capital
    elif choice == 4:
        country = input("Enter the country: ").upper()
        print(countryDB.get(countryDB))
    #delete the entry from the dictionary countryDB
    elif choice == 5:
        country = input("Enter the country: ").upper()
        del(countryDB[country])
    #if user chooses the wrong option
    else:
        print("Enter the valid choice")
        break