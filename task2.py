username = input("Enter your user name :")
password = input ("Enter your password : ")


username = username.replace(" " ,"_")
username =username.lower()
length = len(password) 

print(f" The first three question\n{username}   {length}" )

print(length >= 8)                 # print(username == "admin") 
usercheck = username == "admin" 

print(usercheck)                   # print(password == "1234") 
passcheck = password == "1234"

print(usercheck and passcheck)                                    # print(username == "admin" and password == "1234")

print(f"Welcome in this small program {username} your password lenght is {length}")

