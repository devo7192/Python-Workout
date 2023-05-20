import csv

def passwd_to_csv(file1, file2):
    # file1 is a passwd file to read from
    # file2 is the name of the output file
    
    with open(file1, 'r') as f1:
        with open(file2, 'w') as f2:
            
            o = csv.writer(f2, delimiter='\t')

            for current_line in f1:

                if not current_line.startswith(('#', '\n')):
                    userInfo = current_line.split(':')
                    o.writerow((userInfo[0],userInfo[2]))


passwd_to_csv('passwd.txt', 'stuff.csv')

