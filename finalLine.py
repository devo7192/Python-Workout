from io import StringIO # to simulate a file
    
fakeFile = StringIO('''
nobody: *-2:-2::0:0:Unprivileged User:/var/empty/:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''') # doesn't touch the file system
        
def get_final_line(fileName):

    for current_line in fileName:
        pass
        
    return current_line

    
print(get_final_line(fakeFile), end='')
