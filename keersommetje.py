### Bugs:
### 1. If you enter an incorrect or invalid answer the count of goedeantw < 5 is set to < 10s

from multiprocessing.sharedctypes import Value
import random
import time
import numpy

def keersommen(totaan):
    """Programma welke maximaal 10 keer-sommen voorschotelt en als output geeft hoeveel
    procent je goed had en hoe lang je er over deed"""

    alleantw = 0
    goedeantw = 0
    start_time = time.time()
    antwgoed = ['Heel goed!', 'Super!', 'Ga zo door!', 'Yesss']
    antwfout = ['Jammer!', 'Probeer de volgende eens', 'Helaas!', 'Oei...']

    while goedeantw < 5 and alleantw < 10:
        a = (random.randint(1, totaan))
        b = (random.randint(1, totaan))
        antwoord = (a * b)
        reactie = int(input('Hoeveel is ' + str(a) + ' maal ' + str(b) + '? '))
        if reactie == antwoord:
            goedeantw = goedeantw + 1
            alleantw = alleantw + 1
            print(random.choice(antwgoed))
        else:
            alleantw = alleantw + 1
            print(random.choice(antwfout))
    print("Je had " + str(goedeantw / alleantw * 100) + "% goed!")
    print(time.time() - start_time)
    print("En je deed daar " + str(round(time.time() - start_time)) + " seconden over.")

while True:
    try:
        totaan = int(
            input('Hoe hoog mogen de getallen in de sommen zijn? Voor een cijfer in: '))
        keersommen(totaan)
        break
    except ValueError:
        print("Oeps! Dat is geen getal. Probeer het nog eens?")
