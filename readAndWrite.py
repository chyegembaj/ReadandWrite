import os
print(os.getcwd())
print(os.listdir())

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


for foldername, subfolders, filenames in os.walk('/Users/cegemba/Desktop/practicePython'):
	print('foldername: ' + foldername)
	for subfolder in subfolders:
		print('subfolder: ' +subfolder)
	for file in filenames:
		print('file is' +file)
	print('')
