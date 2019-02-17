#Program to display a friend's birthday or adding it to birthday list.

def displayBirthday(birthDaysList):
    searchAgain = 'Yes'
    while True:
        name = input('Pls enter your friend\'s name to display birthday.\nOr nothing to quit!. ')
        if name == '':
            break
        
        if name in birthDaysList:
         print(name + ' birthday is ' + birthDaysList[name])
        else:
            print(name + ' does not exist in the birthday list.')
            birthDaysList[name] = input('Pls enter birthday: ')
            print('Birthday\'s list updated.')
            print(name + ' birthday is ' + birthDaysList[name])
            
        searchAgain = input('Do you want to search again? ')
        if searchAgain == 'Yes':
            continue
        else:
            break
           

birthdays = {'Alice' : 'April 14', 'Ngozi' : 'June 2', 'Joseph': 'May 20', 'Amaka' : 'Nov 10'}
displayBirthday(birthdays)
print('Updated birthday\'s list is: \n')
print(birthdays )


