print ("Welcome to the pizza making machine")

v_pizzaorder = input("How big do you want your pizza to be?, What type of pizza sauce do you want,What type of cheese do you want?, What toppings do you want?")


def order():
    openfile = open("pizza.txt", 'a')
    openfile.write (str(v_pizzaorder) + '\n')
    openfile.close()
order()

print ("This is your order")
openfile = open('pizza.txt', 'r')
file = openfile.read()
print (file)
openfile.close()
print("thanks for your service")
openfile = open('pizza.txt', 'w')



openfile.truncate()
openfile.close()
exit()





