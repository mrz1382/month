#
password="MORTEZA"
attempts=3
for i in range(attempts):
    user=input('please enter the password==>')
    
if user == password:
    print('password is ok')
    break

else:
    print('passord is not ok')