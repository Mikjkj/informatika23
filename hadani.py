import random
print ("uhodni číslo od 1 do 1000 máš na to 30 pokusů")
while True:
    print("Tak jdeme na to")
    x = random.randint(0,1000)
    inp = 0
    i=0
    
    while inp != x and i < 20:
        i = i + 1
        inp =int(input())
        if x < inp:
            print( random.choice(["Haha jsi L","rly?...","vy nevidíte že máte v kuchyni pneumatiku?"]))
        if x > inp:
            print (random.choice(["bruh","gay","da hell bro?"]))
        if x == inp:
            print ("Spravne bro")
        print ("bacha more už jen " + str(30-i) + " pokusů")
    print ("Konec kamo")
