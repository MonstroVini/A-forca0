# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:35:44 2015

@author: viniciusra
"""


import turtle
import random
import tkinter
import sys
import os

def recomecar():
    turtle = sys.executable
    os.execl(turtle,turtle,* sys.argv)
    
    


f = open("entrada.txt", encoding="UTF-8").readlines()
palavra = random.choice(f)
b = palavra.strip()
print (b)


window = turtle.Screen()
window.bgcolor('black')
window.title('A Forca')

tartaruga = turtle.Turtle()
tartaruga.color('white')
tartaruga.speed(5)
tartaruga.penup()
tartaruga.setpos(-200, 150)
tartaruga.pendown()
tartaruga.left(90)
tartaruga.forward(50)
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.forward(400)
tartaruga.right(90)
tartaruga.forward(30)
tartaruga.right(180)
tartaruga.forward(60)




    
def tracos ():
    tartaruga.penup()
    tartaruga.forward(30)
    tartaruga.pendown()
    tartaruga.forward(20)
    tartaruga.penup()
    tartaruga.hideturtle()
    return tracos
    
def gap ():    
    
    tartaruga.penup()
    tartaruga.forward(25)
    tartaruga.pendown()
    return gap
    
    

    
i = 0
j = 0


while i != len(b) and j!=len(b) :
    if b[i] != " ":
        tracos()
        i += 1
    else:
        gap()
        i +=1
        
    
   

def head ():
    head = turtle.Turtle()
    head.pendown()
    head.setpos(-200,100)
    head.color('white')
    head.pendown()
    head.circle(25)
    head.forward(-10)
    

def body():
    body = turtle.Turtle()
    body.penup()
    body.color('white')
    body.setpos(-200,100)
    body.pendown()    
    body.right(90)
    body.forward(120)
    

def arm1 ():
    arm1 = turtle.Turtle()
    arm1.penup()
    arm1.color('white')
    arm1.setpos(-200,70)
    arm1.pendown()
    arm1.right(45)
    arm1.forward(50)
    

def arm2 ():
    arm2 = turtle.Turtle()
    arm2.penup()
    arm2.color('white')
    arm2.setpos(-200,70)
    arm2.pendown()
    arm2.right(135)
    arm2.forward(50)


def leg1 ():
    leg1 = turtle.Turtle()
    leg1.penup()
    leg1.color('white')
    leg1.setpos(-200,-15)
    leg1.pendown()
    leg1.right(45)
    leg1.forward(50)
    

def leg2 ():
    leg2 = turtle.Turtle()
    leg2.penup()
    leg2.color('white')
    leg2.setpos(-200,-15)
    leg2.pendown()
    leg2.right(135)
    leg2.forward(50)



x = 'acerto'
y = 'erro'
acerto = 0
erro = 0





#def posicao_letra():
#    posicao_letra =turtle.Turtle()
#    turtle.penup()
#    turtle.setpos (-260 + 50*(i) , -200)
#    turtle.pendown()
#    turtle.color('yellow')
#    turtle.write (letra, font = ('Arial', 22))
#    return posicao_letra
#    
#    

    

while erro != 6 and acerto != i :
    letra= window.textinput('A Forca', 'Faça seu chute')
            
    if letra in palavra:
#        j = b.index(letra)
#        print (j)
#        posicao_letra()
        lista1 = []
        for a in range(len(palavra)):
            if palavra[a] == letra:
                lista1.append(a)
                print (lista1)
                
        for letra in lista1:
            turtle.penup()
            turtle.hideturtle()
            turtle.speed(10)
            turtle.setpos(-260 + 50*letra ,-200)
            turtle.color('yellow')
            turtle.pendown()            
            turtle.write(palavra[letra], font = ('Arial', 22))
            l = lista1
            
            
        acerto+=1
        
        if acerto == len(b) :
            turtle.penup()
            turtle.setpos(-50,130)
            turtle.pendown()
            turtle.color('green')
            turtle.write( 'MONSTRO!', font = ('Arial',40))
            resposta =tkinter.messagebox.askyesno('MONSTRO!', 'Deseja jogar de novo?')
            if resposta == False:
                sys.exit()
            if resposta == True:
                
                continue
            
       
                
        
    else:
        
     
        erro += 1
     
        
    if erro ==1:
        head()
        turtle.penup()
        turtle.setpos(60,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
       
                    
    if erro == 2:
        body()
        turtle.penup()
        turtle.setpos(95,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
  
        
    if erro == 3:
        arm1()
        turtle.penup()
        turtle.setpos(130,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
       
    
    if erro == 4:
        arm2()
        turtle.penup()
        turtle.setpos(165,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
    
        
    if erro == 5:
        leg1()
        turtle.penup()
        turtle.setpos(200,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
      
        
    if erro == 6:
        leg2()
        turtle.penup()
        turtle.setpos(235,50)
        turtle.pendown()
        turtle.color('yellow')
        turtle.write(letra, font = ('Arial',22))
        turtle.penup()
        turtle.setpos(-50,130)
        turtle.pendown()
        turtle.color('red')
        turtle.write( 'ENFORCADO!', font = ('Arial',40))
        resposta =tkinter.messagebox.askyesno('ENFORCADO!', 'Deseja jogar de novo?')
        if resposta == False:
            sys.exit()
        if resposta == True:
            recomecar()
          
            
            

    
    


    
    
    

        
        
        
    
window.exitonclick()














    
    









    
    
    












