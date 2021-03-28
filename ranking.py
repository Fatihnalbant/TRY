largest = None
smallest = None
joke = []
while True: 
    number = input ("Enter a number : ")
    if number == "done" : break

    try:
        numberr=int(number)
    except:
        print("ERROR")
        break
    joke.append(numberr) 

largest = joke[0]
for i in joke:
    if i>largest:
        largest = i
print ("Invalid input")
print ("Maximum is ", largest )

smallest = joke [0]
for i in joke:
    if i<smallest:
        smallest = i
print ("Minimum is ", smallest)
# TRY 
