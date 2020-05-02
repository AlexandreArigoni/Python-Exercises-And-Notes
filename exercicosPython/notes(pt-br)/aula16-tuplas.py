.Variáveis Compostas:
    #Tuplas        ()
    #Lists         []
    #Dictionaries  {}
print(snack[-1]) ---> -1 -> Prints the last snack
len(snack)
for c in snack:
    print(c)          ---> all snacks printed


print(sorted(snack)) -> print in order (transform in list just for a moment)

a = (1, 2)
b = (2, 4)
c = a + b
print(c)
print(c.count(2))
# count how many times 2 appears

print(c.index(2))
# gets the position of the first 2
print(c.index(2, 1))
# gets the position of the first 2 starting in the position 1


people = ('Alo', 40, 75.8) ------> IS POSSIBLE <-------
del(people) ----> Delete

                          """ TUPLAS ARE IMUTABLES """
