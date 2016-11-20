# -*- coding: utf-8 -*-

import pygame,sys,random
from pygame.locals import *

color={ 0:(0,0,0), 1:(200,200,100) }
#画笔类
class Brush(object):
    def __init__(self,screen):
        self.screen=screen
        self.color=(0,0,0)

#画板类
class LifeGame(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("LifeGame")
        self.screen.fill((0, 0, 0))
        self.rule=GenerateRule()
        self.component=Component(self.screen,self.rule.board)
        pygame.display.update()
        self.clock = pygame.time.Clock()


    def run(self):
        stop=True
        clean=False
        while True:
            # max fps limit
            self.clock.tick(30)
            #鼠标事件捕获
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == MOUSEBUTTONDOWN and 610<=event.pos[0]<=710 and 340<=event.pos[1]<=390: 
                    print("start") 
                    stop=False
                    pass
                elif event.type == MOUSEBUTTONDOWN and 610<=event.pos[0]<=710 and 410<=event.pos[1]<=460:
                    stop=True
                    pass
                elif event.type == MOUSEBUTTONDOWN and 610<=event.pos[0]<=710 and 480<=event.pos[1]<=530:
                    clean=True
                    pass
                elif event.type == MOUSEBUTTONDOWN and 610<=event.pos[0]<=710 and 270<=event.pos[1]<=320:
                    self.rule=GenerateRule()
                    self.component.drawCells(self.rule.board)
                    pass
            if not stop and not clean:
                self.component.drawCells(self.rule.board)
                self.rule.update()
            if clean:
                self.rule.clean()
                #self.rule=GenerateRule()
                self.component.drawCells(self.rule.board)
                clean=False
                stop=True
            self.component.drawButton()
            pygame.display.update()

#组件类
class Component(object):
    def __init__(self,screen,board):
        self.screen=screen      
        self.drawButton()
        self.drawCells(board)
        
    def drawButton(self):
        #加载图片
        self.createBtnImg=pygame.image.load(".\\create.png").convert_alpha()#C:\\Users\\Administrator\\Desktop\\3.0\\create.png
        self.beginBtnImg=pygame.image.load(".\\beginBtn.png").convert_alpha()
        self.finishBtnImg=pygame.image.load(".\\finishBtn.png").convert_alpha()
        self.clearBtnImg=pygame.image.load(".\\clearBtn.png").convert_alpha()
        #创建rectangle
        self.createBtn_Rect=pygame.Rect(610,270,100,50)
        self.beginBtn_Rect=pygame.Rect(610,340,100,50)
        self.finishBtn_Rect=pygame.Rect(610,410,100,50)
        self.clearBtn_Rect=pygame.Rect(610,480,100,50)
        #创建按钮
        self.screen.blit(self.createBtnImg,self.createBtn_Rect.topleft)
        self.screen.blit(self.beginBtnImg,self.beginBtn_Rect.topleft)
        self.screen.blit(self.finishBtnImg,self.finishBtn_Rect.topleft)  
        self.screen.blit(self.clearBtnImg,self.clearBtn_Rect.topleft)
    def drawCells(self,board):
        #画出生命体所在单元格
        pygame.draw.rect(self.screen,[228,56,73],[59,49,502,502],3)
        for i in range(0,50):
            for j in range(0,50):
                pygame.draw.rect(self.screen,color[board[(i,j)]],[60+10*i,50+10*j,10,10],1)
#生命体生存规则类        
class GenerateRule(object):
    def __init__(self):
        self.board=self.makeBoard(50,50)
    #随机生成活生命体分布位置
    def makeBoard(self,x,y):
        board=dict()
        for i in range(0,50):
            for j in range(0,50):
                if random.random()<0.25:
                    board[(i,j)]=1
                else :
                    board[(i,j)]=0
        return board
    #更新生命体存活状态
    def update(self):
        for cell in self.board:
            neighbors=self.countNeighbor(cell,self.board)
            if self.board[cell]==0 and neighbors==3:
                self.board[cell]=2
            elif self.board[cell]==1 and not neighbors in [2,3]:
                self.board[cell]=-1
        for cell in self.board:
            if self.board[cell]==2:
                self.board[cell]=1
            if self.board[cell]==-1:
                self.board[cell]=0
    #获取中心生命体存活的相邻生命体数
    def countNeighbor(self,cell,board):
        neighbors = [ (cell[0]-1,cell[1]), (cell[0]-1,cell[1]-1),
                  (cell[0],cell[1]-1), (cell[0]+1,cell[1]-1),
                  (cell[0]+1,cell[1]), (cell[0]+1,cell[1]+1),
                  (cell[0],cell[1]+1), (cell[0]-1,cell[1]+1) ]
        score = 0
        for neighbor in neighbors:
            if neighbor in board.keys():
                if board[neighbor] in [1,-1]: 
                    score += 1
        return score
    #清空面板
    def clean(self):
        for i in range(0,50):
            for j in range(0,50):
                self.board[(i,j)]=0
if __name__ == '__main__':
    app = Painter()
    app.run()