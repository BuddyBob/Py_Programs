import pygame
import random,string,time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,800))
class Board:
    def draw(self):
        white,blacks = (255,255,255),(0,0,0)
        x = [blacks,white]
        row = 0
        for i in range(8):
            x.reverse()
            count = 0
            column = 0
            for i in range(8):
                pygame.draw.rect(screen,x[count],(column,row,100,100))
                if count == 1:count = 0
                else:count += 1
                column += 100
            row += 100
    def returnBoard():
        return [[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[1]*8,[0]*8,]
        
class Pawn:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.pawn = pygame.image.load(f'peices/{self.color}/whitePawn.png')
    def display(self):
        self.pawn = pygame.transform.scale(self.pawn,(100,100))
        screen.blit(self.pawn,(self.x,self.y))
board = Board()
arrangeX = 0
pawns = []
for i in range(8):
    pawns.append(Pawn(arrangeX,600,"whites"))
    arrangeX += 100
dBoard = Board.returnBoard()
print(dBoard)
while True:
    board.draw()
    for pawn in pawns:
        pawn.display()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()