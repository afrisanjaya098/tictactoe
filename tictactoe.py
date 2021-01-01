row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']



def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Wrong input")
        
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("out of range")
                within_range = False
         
    return int(choice)




def display(x,y,z):
    print(row1)
    print(row2)
    print(row3)

    user_choice()




display(row1,row2,row3)