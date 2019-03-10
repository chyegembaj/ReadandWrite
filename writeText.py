#Write to a file

#texts ='1. New healine to write.\n 2. Second headline for testing.\n 3. Third headline for checking inline text '
with open('test.txt', 'r') as fr:
    with open('test2.txt', 'w') as fw:
        for line in fr:
            fw.write(line)
            
        
    
