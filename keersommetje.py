
import random
import time


def keersommen(totaan):
    """Programma welke 5 keer-sommen voorschotelt en als output geeft hoeveel
    procent je goed had en hoe lang je er over deed"""

    alleantw = 0
    goedeantw = 0
    start_time = time.time()

    while goedeantw < 5:
        a = (random.randint(1, totaan))
        b = (random.randint(1, totaan))
        antwoord = (a * b)
        reactie = int(input('Hoeveel is ' + str(a) + ' maal ' + str(b) + '? '))
        if reactie == antwoord:
            goedeantw = goedeantw + 1
            alleantw = alleantw + 1
            print("Heel goed!")
        else:
            alleantw = alleantw + 1
            print("Ai, dat is helaas fout...")
    print("Je scoorde " + str(goedeantw / alleantw * 100) + "% goed!")
    print("En je deed daar " + str(time.time() - start_time) + " seconden over.")


totaan = int(input('Hoe hoog mogen de getallen in de sommen zijn? Voor een cijfer in: '))
keersommen(totaan)
