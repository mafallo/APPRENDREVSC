import sys
import math

print(sys.version)
print("\n ------- \n")
#print(sys.executable)


def greet(who_to_greet):
    #test = 'TEST'
    greeting = 'Salut {}'.format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Mafal"))

#tester que le check de gihu fonctionne
