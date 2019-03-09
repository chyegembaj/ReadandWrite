import os
print(os.getcwd())

with open('todo.txt', 'w') as f:
    f.write('''
            1) I'm going to school late.\n
            2) My mother visited last year.\n
            3) I travelled out of state last year.\n
            4)I'm good thank you
            ''')

with open('todo.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
