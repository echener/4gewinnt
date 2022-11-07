#!/usr/bin/env python3

import pygame
import pygame_gui

# local files
import vierGewinntController
import vierGewinntModel
import vierGewinntView


# Constants 
SCREEN_WIDTH = 900
TILE_LENGTH = 100
SCREEN_HEIGHT = SCREEN_WIDTH
GRID_HEIGHT = TILE_LENGTH * 6
GRID_WIDTH = TILE_LENGTH * 7
PAD_VERTICAL = 10
PAD_HORIZONTAL = 10
UIPANEL_HEIGHT = SCREEN_HEIGHT - GRID_HEIGHT - PAD_VERTICAL
UIMENU_WIDTH = SCREEN_WIDTH/3
UILOG_WIDTH = SCREEN_WIDTH - UIMENU_WIDTH - PAD_HORIZONTAL

FPS = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("4 Gewinnt")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

is_running = True
while is_running:
	time_delta = clock.tick(FPS) / 1000.0
	clock.tick(FPS) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			is_running = False
	
	ui_manager.update(time_delta)
	screen.fill(pygame.Color('#FFFFFF'))

	pygame.display.flip()
