# -*- coding: utf-8 -*-



import pygame,sys,random
from pygame.locals import *

color={ "died":(0,0,0), "alive":(200,200,100) }#生命体颜色与状态对应的字典
width=50#一行生命体的个数
height=50#一列生命体的个数
random_rate=0.25#初始化时生命体为活着的状态的几率
button_width=150#按钮宽度
button_height=63#按钮高度
left=610#按钮左侧x坐标
top=270#按钮上部y坐标


#画板类
class LifeGame(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))#设置窗口大小
        pygame.display.set_caption("LifeGame")#设置标题
        self.screen.fill((0, 0, 0))#设置背景色
        self.rule=GenerateRule()#初始化生命体状态
        self.component=Component(self.screen,self.rule.board)#绘制按钮和生命体
        pygame.display.update()#刷新界面
        self.clock = pygame.time.Clock()


    def run(self):
        stop=True
        clean=False
        while True:
            # max fps limit
            self.clock.tick(30)
            #鼠标事件捕获
            for event in pygame.event.get():
            	#退出
                if event.type == QUIT:
                    return
                #开始
                elif event.type == MOUSEBUTTONDOWN and left<=event.pos[0]<=left+button_width and top+70<=event.pos[1]<=top+button_height+70:
                    print("start") 
                    stop=False
                #结束
                elif event.type == MOUSEBUTTONDOWN and left<=event.pos[0]<=left+button_width and top+140<=event.pos[1]<=top+button_height+140:
                    stop=True
                #清空
                elif event.type == MOUSEBUTTONDOWN and left<=event.pos[0]<=left+button_width and top+210<=event.pos[1]<=top+button_height+210:
                    clean=True
                #创建新生命图
                elif event.type == MOUSEBUTTONDOWN and left<=event.pos[0]<=left+button_width and top<=event.pos[1]<=top+button_height:
                    self.rule=GenerateRule()
                    self.component.drawCells(self.rule.board)
            #更新生命图
            if not stop and not clean:
                self.component.drawCells(self.rule.board)
                self.rule.update()
            #清空生命图
            if clean:
                self.rule.clean()
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
        self.createBtn_Rect=pygame.Rect(left,top,button_width,button_height)
        self.beginBtn_Rect=pygame.Rect(left,top+70,button_width,button_height)
        self.finishBtn_Rect=pygame.Rect(left,top+140,button_width,button_height)
        self.clearBtn_Rect=pygame.Rect(left,top+210,button_width,button_height)
        #创建按钮
        self.screen.blit(self.createBtnImg,self.createBtn_Rect.topleft)
        self.screen.blit(self.beginBtnImg,self.beginBtn_Rect.topleft)
        self.screen.blit(self.finishBtnImg,self.finishBtn_Rect.topleft)  
        self.screen.blit(self.clearBtnImg,self.clearBtn_Rect.topleft)
    def drawCells(self,board):
        #画出生命体所在单元格
        pygame.draw.rect(self.screen,[228,56,73],[59,49,502,502],3)
        for i in range(0,height):
            for j in range(0,width):
                pygame.draw.rect(self.screen,color[board[(i,j)]],[60+10*i,50+10*j,10,10],1)
#生命体生存规则类        
class GenerateRule(object):
    def __init__(self):
        self.board=self.makeBoard(height,width)
    #随机生成活生命体分布位置
    def makeBoard(self,x,y):
        board=dict()
        for i in range(0,height):
            for j in range(0,width):
                if random.random()<random_rate:
                    board[(i,j)]="alive"
                else :
                    board[(i,j)]="died"
        return board
    #更新生命体存活状态
    def update(self):
    	#更具现存生命体的存活状态计算下一时刻的生命体状态，对于状态有改变的生命体的状态暂更新为一个待变化状态
        for cell in self.board:
            neighbors=self.countNeighbor(cell,self.board)
            if self.board[cell]=="died" and neighbors==3:
                self.board[cell]="toAlive"
            elif self.board[cell]=="alive" and not neighbors in [2,3]:
                self.board[cell]="toDied"
        #将待变化状态的生命体的状态更新
        for cell in self.board:
            if self.board[cell]=="toAlive":
                self.board[cell]="alive"
            if self.board[cell]=="toDied":
                self.board[cell]="died"
    #获取中心生命体存活的相邻生命体数
    def countNeighbor(self,cell,board):
        neighbors = [ (cell[0]-1,cell[1]), (cell[0]-1,cell[1]-1),
                  (cell[0],cell[1]-1), (cell[0]+1,cell[1]-1),
                  (cell[0]+1,cell[1]), (cell[0]+1,cell[1]+1),
                  (cell[0],cell[1]+1), (cell[0]-1,cell[1]+1) ]
        score = 0
        for neighbor in neighbors:
            if neighbor in board.keys():
                if board[neighbor] in ["alive","toDied"]: #待变化的生命体中，即将死亡的生命体证明其在进入下一时刻之前是活的，因而也需要计入
                    score += 1
        return score
    #清空面板
    def clean(self):
        for i in range(0,height):
            for j in range(0,width):
                self.board[(i,j)]="died"
if __name__ == '__main__':
    app = LifeGame()
    app.run()