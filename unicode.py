import random
#pour utiliser random.randrange()

#ACS_NESW (X on, O off)
ACS_XOXO = "\u2502"
ACS_OXOX = "\u2500"
ACS_XXOO = "\u2514"
ACS_OXXO = "\u250C"
ACS_OOXX = "\u2510"
ACS_XOOX = "\u2518"
ACS_XXXO = "\u251C"
ACS_XXOX = "\u2534"
ACS_XOXX = "\u2524"
ACS_OXXX = "\u252C"
ACS_XXXX = "\u253C"
ACS_XOOO = ACS_XOXO
ACS_OXOO = ACS_OXOX
ACS_OOXO = ACS_XOXO
ACS_OOOX = ACS_OXOX
ACS_OOOO = ACS_XXXX
#define LINE_XOXO 4194424 // '|' Vertical line. ncurses: ACS_VLINE; Unicode: U+2502
#define LINE_OXOX 4194417 // '-' Horizontal line. ncurses: ACS_HLINE; Unicode: U+2500
#define LINE_XXOO 4194413 // '|_' Lower left corner. ncurses: ACS_LLCORNER; Unicode: U+2514
#define LINE_OXXO 4194412 // '|^' Upper left corner. ncurses: ACS_ULCORNER; Unicode: U+250C
#define LINE_OOXX 4194411 // '^|' Upper right corner. ncurses: ACS_URCORNER; Unicode: U+2510
#define LINE_XOOX 4194410 // '_|' Lower right corner. ncurses: ACS_LRCORNER; Unicode: U+2518
#define LINE_XXXO 4194420 // '|-' Tee pointing right. ncurses: ACS_LTEE; Unicode: U+251C
#define LINE_XXOX 4194422 // '_|_' Tee pointing up. ncurses: ACS_BTEE; Unicode: U+2534
#define LINE_XOXX 4194421 // '-|' Tee pointing left. ncurses: ACS_RTEE; Unicode: U+2524
#define LINE_OXXX 4194423 // '^|^' Tee pointing down. ncurses: ACS_TTEE; Unicode: U+252C
#define LINE_XXXX 4194414 // '-|-' Large Plus or cross over. ncurses: ACS_PLUS; Unicode: U+253C

def bordure_h(col):
 return [1]*col

def ligne(col):
 return [1] + [0]*(col-2) + [1]

def r_ligne(col):
 t = [1]
 for i in range(col-2):
  t = t + [random.randrange(2)]
 t = t + [1]
 return t

def laby(col,li):
 t = [bordure_h(col)]
 for i in range(li-2):
  t = t + [r_ligne(col)]
 t = t + [bordure_h(col)]
 return t

def carre(col,li):
 return [bordure_h(col)] + [ligne(col)]*(li-2) + [bordure_h(col)]

def imprime_forme(tab):
 for y in range(len(tab)):
  for x in range(len(tab[0])):
   if tab[y][x] == 1:
    if (y == 0):
     if (x == 0):
      print(ACS_OXXO,end="")
     else: #else if?
      if (x == len(tab[0])-1):
       print(ACS_OOXX,end="")
      else:
       if (tab[1][x] > 0):
        print(ACS_OXXX,end="")
       else:
        print(ACS_OXOX,end="")
    else:
     if (y == len(tab)-1):
      if (x == 0):
       print(ACS_XXOO,end="")
      else:
       if (x == len(tab[0])-1):
        print(ACS_XOOX,end="")
       else:
        if (tab[y-1][x] > 0):
         print(ACS_XXOX,end="")
        else:
         print(ACS_OXOX,end="")
     else:
      if (x == 0):
       if (tab[y][1] > 0):
        print(ACS_XXXO,end="")
       else:
        print(ACS_XOXO,end="")
      else:
       if (x == len(tab[0])-1):
        if (tab[y][x-1] > 0):
         print(ACS_XOXX,end="")
        else:
         print(ACS_XOXO,end="")
       else:
        #ici on est a l'interieur du rectangle, il faut tester chaque direction
        # nord
         # est
          # sud
           # ouest
        if (tab[y-1][x] > 0):
         if (tab[y][x-1] > 0):
          if (tab[y+1][x] > 0):
           if (tab[y][x+1] > 0):
            print(ACS_XXXX,end="")
           else:
            print(ACS_XXXO,end="")
          else:
           if (tab[y][x+1] > 0):
            print(ACS_XXOX,end="")
           else:
            print(ACS_XXOO,end="")
         else:
          if (tab[y+1][x] > 0):
           if (tab[y][x+1] > 0):
            print(ACS_XOXX,end="")
           else:
            print(ACS_XOXO,end="")
          else:
           if (tab[y][x+1] > 0):
            print(ACS_XOOX,end="")
           else:
            print(ACS_XOOO,end="")
        else:
         if (tab[y][x-1] > 0):
          if (tab[y+1][x] > 0):
           if (tab[y][x+1] > 0):
            print(ACS_OXXX,end="")
           else:
            print(ACS_OXXO,end="")
          else:
           if (tab[y][x+1] > 0):
            print(ACS_OXOX,end="")
           else:
            print(ACS_OXOO,end="")
         else:
          if (tab[y+1][x] > 0):
           if (tab[y][x+1] > 0):
            print(ACS_OOXX,end="")
           else:
            print(ACS_OOXO,end="")
          else:
           if (tab[y][x+1] > 0):
            print(ACS_OOOX,end="")
           else:
            print(ACS_OOOO,end="")
   else:
    print(" ",end="")
  print("")

imprime_forme(carre(80,10))

print("\n")
imprime_forme(laby(80,10))