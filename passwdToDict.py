from io import StringIO # to simulate a file - doesn't touch the file system
    
fakeFile = StringIO('''
nobody:*-2:-2::0:0:Unprivileged User:/var/empty/:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''') # each line represents one user record

def password_to_dict(fileName):
    # returns a dict based on /etc/passwd in which the keys are usernames and the values are users' IDs
    users = {}
    for line in fileName:
        if not line.startswith(('\n', '#')): 
            userInfo = line.split(':')
            users[userInfo[0]] = int(userInfo[2])
    
    return users


print(password_to_dict(fakeFile))