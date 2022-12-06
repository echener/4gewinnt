#!/usr/bin/env python3

import pygame
import pygame_gui

# local files
from vierGewinntModel import *
from vierGewinntComputer import *

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
X_TILES = 7
Y_TILES = 6
baseGridY = GRID_HEIGHT - TILE_LENGTH
baseGridX = (SCREEN_WIDTH-X_TILES*TILE_LENGTH)/2 

PARTICIPANTS = ["Human", "KI"]
FPS = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("4 Gewinnt")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# ui_manager
player1_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL), (UIMENU_WIDTH, 30)), text="Player 1 Red:", manager=ui_manager)
player1_desc = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+30), (UIMENU_WIDTH, 30)), text="Human (You)", manager=ui_manager)
#player1_drop = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+30), (UIMENU_WIDTH, 30)), options_list=["Human"], starting_option="Human", manager=ui_manager)
player2_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+3*30), (UIMENU_WIDTH, 30)), text="Player 2 Blue:", manager=ui_manager)
player2_drop = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+4*30), (UIMENU_WIDTH, 30)), options_list=PARTICIPANTS, starting_option="KI", manager=ui_manager)
restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+7*30), (UIMENU_WIDTH, 30)), text="Restart", manager=ui_manager)
log_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((UIMENU_WIDTH+PAD_HORIZONTAL, PAD_VERTICAL+GRID_HEIGHT), (SCREEN_WIDTH-UIMENU_WIDTH-PAD_HORIZONTAL, SCREEN_HEIGHT-PAD_VERTICAL-GRID_HEIGHT)), html_text="", manager=ui_manager)

tileEmpty = pygame.image.load("graphics/tileEmpty.png").convert()
tileRed = pygame.image.load("graphics/tileRed.png").convert()
tileBlue = pygame.image.load("graphics/tileBlue.png").convert()


def draw_grid(grid, screen):
	tile = tileEmpty
	for x in range(X_TILES):
		for y in range(Y_TILES):
			if grid[x][y] == 1:
				tile = tileRed
			elif grid[x][y] == 2:
				tile = tileBlue
			else:
				tile = tileEmpty
			screen.blit(tile, (baseGridX+TILE_LENGTH*x, baseGridY-	y*TILE_LENGTH))

def validateClick(x, y):
	xPos = None
	if x >= baseGridX and x <= baseGridX+TILE_LENGTH*X_TILES and y <= GRID_HEIGHT:
		xPos = int((x-baseGridX)//TILE_LENGTH)
	return xPos

model = vierGewinntModel()
aiPlayer = vierGewinntStupidComputer(2)
aiPlaying = True
gameOver = False
	
log_box.append_html_text("Welcome to 4 Gewinnt <br>")
is_running = True
while is_running:
	time_delta = clock.tick(FPS) / 1000.0
	clock.tick(FPS) 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			is_running = False
		if event.type == pygame_gui.UI_BUTTON_PRESSED:
			if event.ui_element == restart_button:
				gameOver = False
				model = vierGewinntModel()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if not gameOver:
				model.play(validateClick(event.pos[0], event.pos[1]), model.getCurrPlayer())
		if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
			if event.text == "Human":
				aiPlaying = False
			else:
				aiPlaying = True
		ui_manager.process_events(event)
	
	winner = model.checkWinner()
	if winner != None and not gameOver:
		gameOver = True
		log_box.append_html_text("Congratulations Player " + str(winner) + " you won <br>")

	if model.getMoves() >= X_TILES * Y_TILES and not gameOver:
		gameOver = True
		log_box.append_html_text("Tie, no one won <br>")

	# if I understand pygame correctly this shouldn't allow a double play with double click
	# because the events are not executed separatly
	if model.getCurrPlayer() == 2 and aiPlaying == True and not gameOver:
		model.play(aiPlayer.makeAMove(model.getGrid()), 2)

	ui_manager.update(time_delta)
	screen.fill(pygame.Color('#000000'))
	
	draw_grid(model.getGrid(), screen)
	ui_manager.draw_ui(screen)
	pygame.display.flip()
