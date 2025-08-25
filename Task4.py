fruits ={
    "Apple":10
    ,"orrange":15
    ,"Pineapple": 20
    ,"Peach" :50
    ,"Cantala":40
}
name = input("Enter the fruit name ")
if name in fruits:
    print(fruits[name])
else: print("Sorry, this fruit is not availabl")
