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

PARTICIPANTS = ["Human", "KI"]
FPS = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("4 Gewinnt")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# ui_manager
player1_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL), (UIMENU_WIDTH, 30)), text="Player 1:", manager=ui_manager)
player1_drop = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+30), (UIMENU_WIDTH, 30)), options_list=PARTICIPANTS, starting_option="Human", manager=ui_manager)
player2_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+3*30), (UIMENU_WIDTH, 30)), text="Player 2:", manager=ui_manager)
player2_drop = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+4*30), (UIMENU_WIDTH, 30)), options_list=PARTICIPANTS, starting_option="KI", manager=ui_manager)
restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, GRID_HEIGHT+PAD_VERTICAL+7*30), (UIMENU_WIDTH, 30)), text="Restart", manager=ui_manager)
log_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((UIMENU_WIDTH+PAD_HORIZONTAL, PAD_VERTICAL+GRID_HEIGHT), (SCREEN_WIDTH-UIMENU_WIDTH-PAD_HORIZONTAL, SCREEN_HEIGHT-PAD_VERTICAL-GRID_HEIGHT)), html_text="", manager=ui_manager)

log_box.append_html_text("Welcome to 4 Gewinnt <br>")
is_running = True
while is_running:
	time_delta = clock.tick(FPS) / 1000.0
	clock.tick(FPS) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			is_running = False
	
	ui_manager.update(time_delta)
	screen.fill(pygame.Color('#000000'))


	ui_manager.draw_ui(screen)
	pygame.display.flip()
