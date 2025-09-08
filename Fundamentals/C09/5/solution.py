def is_valid(username, password):
    # Write code here
    if username=="user" and password=="qweasd" or username=="admin" :
        return True
    else:
        return False
    
usr=input()
pswd=input()
test=is_valid(usr,pswd)
print(test)