
print ("Enter your name :") 
name= input ()

print ("Enter your notes :")

notes = input()

with open('file' , 'w') as w : 
    w.write(name)

with open('file','a') as a:
    a.write(notes) 

with open('file','r') as r:
    print(r.read())
