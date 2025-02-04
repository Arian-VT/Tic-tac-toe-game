#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:20:34 2024

@author: arian
"""

import pygame
import numpy as np
import random
import sys

pygame.init() #Inicializamos pygame

# Definición de colores de la interfaz
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 128, 255)
NEON_GREEN = (57, 255, 20)
NEON_PINK = (255, 20, 147)
GRAY = (170, 170, 170)
DARK_GRAY = (100, 100, 100)

# Tamaño ventana
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 10
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

#Inicializamos la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego del Gato")

# Fuentes de texto
font = pygame.font.Font(None, 50) #Titulo
button_font = pygame.font.Font(None, 25)  #Botones


tablero = np.zeros(9) #Definimos el número de casillas de nuestro tablero

# Secuencias ganadoras previamente calculadas
secuencias = [[5, 9, 3, 7, 1, 6, 8, 4, 2],
              [5, 7, 1, 9, 3, 4, 8, 2, 6],
              [5, 3, 1, 9, 7, 2, 6, 4, 8],
              [5, 1, 3, 7, 9, 2, 4, 6, 8]]

# Definimos los turnos
turno = random.randint(1, 2)  # 1: jugador, 2: computadora
sec = random.choice(secuencias)
game_over = False
playing = False

elex = 0

# Dibujar líneas del tablero
def draw_lines():
    screen.fill(BLACK)  
    # Líneas verticales
    pygame.draw.line(screen, WHITE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # Líneas horizontales
    pygame.draw.line(screen, WHITE, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

# Dibujar X y O
def draw_figures():
    for row in range(3):
        for col in range(3):
            if tablero[row * 3 + col] == 1:  # Jugador X
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif tablero[row * 3 + col] == 2:  # Jugador O
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Ganador
def ganar():
    for i in range(1, 3):
        if (tablero[0] == i and tablero[1] == i and tablero[2] == i) or \
           (tablero[3] == i and tablero[4] == i and tablero[5] == i) or \
           (tablero[6] == i and tablero[7] == i and tablero[8] == i) or \
           (tablero[0] == i and tablero[3] == i and tablero[6] == i) or \
           (tablero[1] == i and tablero[4] == i and tablero[7] == i) or \
           (tablero[2] == i and tablero[5] == i and tablero[8] == i) or \
           (tablero[0] == i and tablero[4] == i and tablero[8] == i) or \
           (tablero[2] == i and tablero[4] == i and tablero[6] == i):
            return i
    return 0

# Verificar si existe empate
def empate():
    return 0 not in tablero

# Turno computadora
def compu():
    global sec
    for num in sec:
        if tablero[num - 1] == 0:
            tablero[num - 1] = 2
            sec.remove(num)
            return
        
def compu2():
   global tablero
   s = []
   ciclo = False
   ciclo0 = False
   i =0
   a = 2
   fin = False
   tiro = False
   while not ciclo0:   
       i = 0
       while i < 8:
           if i == 0:
               s = [0, 1, 2]
           elif i == 1:
               s = [3,4,5]
           elif i == 2:
               s = [6,7,8]
           elif i == 3:
               s = [0,3,6]
           elif i == 4:
               s = [1,4,7]
           elif i == 5:
               s = [2,5,8]
           elif i == 6:
               s = [0,4,8]
           elif i == 7:
               s = [2,4,6]
           if tablero[s[0]] == a and tablero[s[1]] == a and tablero[s[2]]== 0:
               tablero[s[2]] = 2
               tiro = True
               ciclo0 = True
               fin = False
               break
           elif tablero[s[0]] == a and tablero[s[1]]== 0 and tablero[s[2]]== a:
               tablero[s[1]] = 2
               tiro = True
               ciclo0 = True
               fin = False
               break
           elif tablero[s[0]]== 0 and tablero[s[1]] == a and tablero[s[2]] == a:
               tablero[s[0]] = 2
               tiro = True
               ciclo0 = True
               fin = False
               break
           i+=1
       if a == 1:
           fin = True
           ciclo0 = True
       else:
           a -= 1
           
   if fin == True and tiro == False:
       evento = True
       while evento:
           pos = np.random.randint(9)
           if tablero[pos] == 0:
               tablero[pos] = 2
               return tablero
               evento = False

    

# Actualizamos la pantalla despues del tiro
def update_screen():
    draw_lines()
    draw_figures()
    pygame.display.update()

# Reinciar el juego
def reset_game():
    global tablero, sec, turno, game_over
    tablero = np.zeros(9)
    sec = random.choice(secuencias)
    turno = random.randint(1, 2)
    game_over = False
    update_screen()

# Pantalla de inicio 
def draw_start_screen():
    screen.fill(BLACK)

    
    title_text = font.render("Juego del Gato", True, RED)
    text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_text, text_rect)

    #Botones
    play_button = pygame.Rect(100, 175, 200, 50)
    pygame.draw.rect(screen, NEON_PINK, play_button)
    play_text = button_font.render("Probabilistico (1)", True, BLACK)
    play_text_rect = play_text.get_rect(center=play_button.center)
    screen.blit(play_text, play_text_rect)
    
    play2_button = pygame.Rect(100, 250, 200, 50)
    pygame.draw.rect(screen, NEON_PINK, play2_button)
    play_text2 = button_font.render("Estocastico (2)", True, BLACK)
    play_text_rect2 = play_text2.get_rect(center=play2_button.center)
    screen.blit(play_text2, play_text_rect2)
    
    quit_button = pygame.Rect(100, 325, 200, 50)
    pygame.draw.rect(screen, NEON_PINK, quit_button)
    quit_text = button_font.render("Salir", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_text_rect)

    pygame.display.update()

    return play_button, quit_button

# Ciclo principal del juego
running = True
while running:
    if not playing:
        play_button, quit_button = draw_start_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pantalla de inicio
        if not playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.draw.rect(screen, DARK_GRAY, play_button)
                    pygame.display.update()
                    pygame.time.wait(100)
                    playing = True
                    reset_game()
                
                if event.key == pygame.K_1:
                    pygame.draw.rect(screen, DARK_GRAY, play_button)
                    pygame.display.update()
                    pygame.time.wait(100)
                    playing = True
                    reset_game()
                    elex = 1
                    
                if event.key == pygame.K_2:
                    pygame.draw.rect(screen, DARK_GRAY, play_button)
                    pygame.display.update()
                    pygame.time.wait(100)
                    playing = True
                    reset_game()
                    elex = 2
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                
                if quit_button.collidepoint((mouseX, mouseY)):
                    pygame.draw.rect(screen, DARK_GRAY, quit_button)
                    pygame.display.update()
                    pygame.time.wait(100)
                    running = False

        # Juego
        if playing:
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                clicked_pos = clicked_row * 3 + clicked_col

                if tablero[clicked_pos] == 0 and turno == 1:
                    tablero[clicked_pos] = 1
                    turno = 2
                    winner = ganar()
                    update_screen()

                    if winner != 0:
                        print(f"Ganó el humano")
                        game_over = True
                    elif empate():
                        print("¡Empate!")
                        game_over = True

            if turno == 2 and not game_over:
                pygame.time.wait(500)
                if elex == 1:
                    compu()
                elif elex == 2:
                    compu2()
                turno = 1
                winner = ganar()
                update_screen()

                if winner != 0:
                    print(f"Ganó la computadora")
                    game_over = True
                elif empate():
                    print("¡Empate!")
                    game_over = True

            if event.type == pygame.KEYDOWN:#Reiniciamos el juego con la tecla R
                if event.key == pygame.K_r:
                    reset_game()

    if playing:
        update_screen()

pygame.quit()
