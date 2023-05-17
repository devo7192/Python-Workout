from io import StringIO # to simulate a file
import csv

fakeFile = StringIO('''
nobody: *-2:-2::0:0:Unprivileged User:/var/empty/:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
# I am a comment line
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''') # doesn't touch the file system

def passwd_to_csv(file1, file2):
    # file1 is a passwd file to read from
    # file2 is the name of the output file
    
    with open(file2, 'w') as f:
        
        o = csv.writer(f, delimiter='\t')

        for current_line in file1:

            if not current_line.startswith(('#', '\n')):
                userInfo = current_line.split(':')
                o.writerow((userInfo[0],userInfo[2]))


passwd_to_csv(fakeFile, 'stuff.csv')

