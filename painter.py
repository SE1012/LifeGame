# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

#画笔类
class Brush(object):
	def __init__(self,screen):
		self.screen=screen
		self.color=(0,0,0)

#画板类
class Painter(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("LifeGame")
		self.screen.fill((0, 0, 0))
		self.component=Component(self.screen)
		pygame.display.update()
		self.clock = pygame.time.Clock()

	def run(self):
		while True:
			# max fps limit
			self.clock.tick(30)
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN:
					pass
				elif event.type == MOUSEBUTTONDOWN:
					pass
				elif event.type == MOUSEMOTION:
					pass
				elif event.type == MOUSEBUTTONUP:
					pass

			self.component.drawButton()
			pygame.display.update()

#组件类
class Component(object):
	def __init__(self,screen):
		self.screen=screen      
		self.drawButton()
		self.drawCells()
        
	def drawButton(self):
        #加载图片
		self.beginBtnImg=pygame.image.load("E:\\work\\LifeGame\\3.0\\beginBtn.png").convert_alpha()
		self.finishBtnImg=pygame.image.load("E:\\work\\LifeGame\\3.0\\finishBtn.png").convert_alpha()
		self.clearBtnImg=pygame.image.load("E:\\work\\LifeGame\\3.0\\clearBtn.png").convert_alpha()
		self.createBtnImg=pygame.image.load("E:\\work\\LifeGame\\3.0\\createBtn.png").convert_alpha()
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

	def drawCells(self):
		pygame.draw.rect(self.screen,[228,56,73],[59,49,502,502],3)
		for i in range(0,50):
			for j in range(0,50):
				pygame.draw.rect(self.screen,[0,0,0],[60+10*i,50+10*j,10,10],0)
       
if __name__ == '__main__':
	app = Painter()
	app.run()