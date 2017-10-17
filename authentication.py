#   This module provides functions for authenticating users.

def login(username, password):
    try:
        '''
        file = open('users.txt','w+')
        user_buf = file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        print('users: ')
        print(user_buf)
        '''
        user_buf = "netease|password"
        users = [line.split("|") for line in user_buf.split("\n")]
        if[username, password] in users:
            return True

        return False
    #except Exception as exc:
    except Exception, exc:
        print('I can\'t authenticate you.')
        return False

def logout():
    print('This line won\'t be covered.')
    print('This line won\'t be covered too.')
