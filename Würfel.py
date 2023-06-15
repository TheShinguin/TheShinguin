from random import randrange
#############################################################
#Globale Variablen
#############################################################
#Testfunktion
x=1

#Angriffswurf:
GeworfenerWert = int (0)
Getroffen = int (0)
KritischGetroffen = int (0)
Reroll = bool (True)    
KS = 0
SW = 0

#Rüstungswurf:
Geblockt= int (0)
Kritischgeblockt = int(0)

#Schadensberechnung:
Schaden = int (0)

#############################################################
#Testfunktion
#############################################################

def Testfunktion():
    global x
    x = x+x
    print (x)

#############################################################
#Angriffswurf
#############################################################

def Angriffswurf():
    global Getroffen
    global KritischGetroffen
    global SW
    global KS

    AT = int (input("Wie viele Würfel?   "))
    SF= int(input("Was für ein SF?     "))
    SW = int(input("Was für ein Schadenswert?   "))
    KS = int(input("Wie hoch ist der Kritschaden?   "))
    Relentless = str (input("Repentless? Ja/Nein?   "))
    print()

    for i in range(AT):
        Reroll=True
        GeworfenerWert=(randrange(1, 7))
    
        if Reroll == True:
            if (GeworfenerWert<SF):
                print("Sie haben", GeworfenerWert, "geworfen,")
                Abfrage = str (input("Möchten sie rerollen? Ja/Nein?   "))
                if Abfrage=="Ja":
                    print("REROLL, -1 CP!:")
                    #print("Alter wert: ", GeworfenerWert)
                    GeworfenerWert=(randrange(1, 6))                
                    Reroll = False
                #else:
                    #print("Kein Reroll, Keine CP abgezogen")
        if Reroll == True:
            if(Relentless=="Ja"):
                if(GeworfenerWert<SF):               
                    #print("Alter wert: ", GeworfenerWert)
                    GeworfenerWert=(randrange(1, 6))
                    print("Relentless Reroll!")
                    #else:
                    #print ("Kein Reroll benötigt: ", GeworfenerWert)
    
        print("Sie haben", GeworfenerWert, "geworfen!")

        if GeworfenerWert!=6 and GeworfenerWert>SF or GeworfenerWert==SF:
            Getroffen +=1
            print("Noch ein Treffer!")
        if GeworfenerWert==6:
            KritischGetroffen +=1
            print("Kritischer Treffer!")
        print()
        i += 1
    print("Getroffen:  ", Getroffen)
    print("Kritisch Getroffen: ", KritischGetroffen)
    print()

#Ausgegebene Variable: Getroffen/KritischGetroffen

#############################################################
#Rüstungswurf
#############################################################

def Ruestungswurf():
    global Geblockt
    global Kritischgeblockt

    DW = int (input("Wie viele Rüstungswürfel?  "))
    RW = int (input("Wie hoch ist der Rüstungswert? "))
    print()

    
    for i in range (DW):
        Ruestungswurf = randrange(1,7)
        print ("Rüstungswurf: ", Ruestungswurf)
        if Ruestungswurf<6 and Ruestungswurf>RW or Ruestungswurf==RW:
            Geblockt +=1
            #print("Wird geblockt!")
        if Ruestungswurf==6:
            Kritischgeblockt +=1
            #print("Wird kritisch geblockt!")

    #Ausgegebene Variable: Geblockt/KritischGeblockt
    print ("Es werden ", Geblockt+Kritischgeblockt, "Schadenswürfel geblockt, davon", Kritischgeblockt, "kritisch!")

#Ausgegebene Variable: Geblockt/KritischGeblockt

#############################################################
#Schadensberechnung
#############################################################

def Schadensberechnung():
    global Getroffen
    global KritischGetroffen
    global Schaden

    Getroffen=Getroffen-Geblockt
    KritischGetroffen=KritischGetroffen-Kritischgeblockt

    if Getroffen>0 and Getroffen!=0:
        Schaden=(Getroffen*SW)+(KritischGetroffen*KS)
        print("Schaden: ", Schaden)
    else:
        print("Kompletter Schaden geblockt!")

    #ausgegebene Variable: Schaden
    
#Ausgegebene Variable: Schaden

#Main Code/Loop:
print("1. Angreifen")
Menuewahl= int (input("Was möchten sie machen?  "))

match Menuewahl:
    case 1:
        Angriffswurf()
        Ruestungswurf()
        Schadensberechnung()
        
