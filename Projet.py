def heros (x1,x2,x3,x4):
    print(x1,x2,x3*27,x4)


def heros2(y1,y2,y3,y4,y5):
    print(y1,y2,y3,y4*25,y5)


def heros3(a1,a2,a3,a4,a5):
    print(a1,a2*3,a3,a4*23,a5)


    
def baton(b1,b2,b3):
    print(b1,b2*29,b3)



def tiret (yo,yo1):
    print(yo, yo1*29,yo)
    
    
TabLab = [ ('+') , ('-') ]
TabLab2 = [('|'),(' '),('|')]
TabLab3 = [TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2,TabLab2]
TabLab4 = [TabLab*29]
TabLabx = [('X')]
i=0
z=1

for i in range (len(TabLab4)):
    tiret (TabLab[0],TabLab[1])
   


for i in range (len(TabLab3)):
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    

    
        
        
        

for i in range (len(TabLab4)):
    tiret (TabLab[0],TabLab[1])


deplacement = int ( input("1 pour lancé le jeu, 0 pour quitter  "))

while deplacement != 0 :
    for i in range (len(TabLab4)):
        tiret (TabLab[0],TabLab[1])
        
    

    heros(TabLab2[0],TabLabx[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    baton(TabLab2[0],TabLab2[1],TabLab2[2])
    
    
    
        

    for i in range (len(TabLab4)):
        tiret (TabLab[0],TabLab[1])

    
        
    deplacement2 = int ( input("Bas, Droite, Haut, Gauche ? Respectivement 1, 2, 3, 4  "))

    if deplacement2 == 1 :
        for i in range (len(TabLab4)):
            tiret (TabLab[0],TabLab[1])

        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        heros(TabLab2[0],TabLabx[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        
        for i in range (len(TabLab4)):
            tiret (TabLab[0],TabLab[1])

        deplacement3 = int ( input("Bas, Droite, Haut, Gauche ? Respectivement 1, 2, 3, 4  "))

        if deplacement3 == 1:
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            heros(TabLab2[0],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])

            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

        if deplacement3 == 2 :
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])
                
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            heros2(TabLab2[0],TabLab2[1],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

        if deplacement3 == 3 :
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

            heros(TabLab2[0],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])

            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])
            

        
    if deplacement2 ==2 :
        for i in range (len(TabLab4)):
            tiret (TabLab[0],TabLab[1])

            
        heros2(TabLab2[0],TabLab2[1],TabLabx[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])
        baton(TabLab2[0],TabLab2[1],TabLab2[2])






        for i in range (len(TabLab4)):
            tiret (TabLab[0],TabLab[1])

        deplacement3 = int ( input("Bas, Droite, Haut, Gauche ? Respectivement 1, 2, 3, 4  "))

        if deplacement3 == 1:
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])
                
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            heros2(TabLab2[0],TabLab2[1],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            

            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

        if deplacement3 == 2 :
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])
            
            heros3(TabLab2[0],TabLab2[1],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])


            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

        if deplacement3 == 4 :
            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

            heros(TabLab2[0],TabLabx[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])
            baton(TabLab2[0],TabLab2[1],TabLab2[2])


            for i in range (len(TabLab4)):
                tiret (TabLab[0],TabLab[1])

            
            
    
        

    deplacement = deplacement-1
        

