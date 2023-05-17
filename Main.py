import machine
import ssd1306
import time
import random

#configuração dos botões RESET e START
START_PIN = 16
RESET_PIN = 17
Start_Button = machine.Pin(START_PIN, machine.Pin.IN, machine.Pin.PULL_UP) #Configuração do botão start
Reset_Button = machine.Pin(RESET_PIN, machine.Pin.IN, machine.Pin.PULL_UP) #Configuração do botão reset

# Configuração do display OLED
WIDTH = 128
HEIGHT = 32
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1)) 
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Configuração dos pinos ADC para os potenciômetros
pot1_pin = machine.ADC(26)
pot2_pin = machine.ADC(27)
#Variaveis de jogo
paddle_height = 8
paddle_width = 2
paddle_gap = 100
paddle_left_pos = 100
paddle_right_pos = 50
ball_pos = [WIDTH//2, HEIGHT//2]
ball_dir = [1, 1]
ball_speed = 0.01
score = [0, 0]

#Funções do jogo
def draw_paddle(pos):
    # Define as posições das barras esquerda e direita
    left_paddle_pos = 0
    right_paddle_pos = WIDTH - paddle_width
    
    # Calcula as novas posições das paddles com base nos valores dos potenciômetros
    new_left_paddle_pos = int((pot1_pin.read_u16() / 65535) * (HEIGHT - paddle_height))
    new_right_paddle_pos = int((pot2_pin.read_u16() / 65535) * (HEIGHT - paddle_height))

    # Desenha as paddles nas novas posições calculadas
    oled.fill_rect(left_paddle_pos, new_left_paddle_pos, paddle_width, paddle_height, 1)
    oled.fill_rect(right_paddle_pos, new_right_paddle_pos, paddle_width, paddle_height, 1)

#Desenha a bola
def draw_ball(pos):
    oled.fill_rect(pos[0], pos[1], 2, 2, 1)

#Desenha os placares
def draw_scores():
    oled.text(str(score[0]), 50, 0, 1)
    oled.text(str(score[1]), 70, 0 , 1)
    
    # Desenha a linha vertical na metade da tela
    oled.vline(WIDTH//2, 0, HEIGHT, 1)

    
#Move a bola
def move_ball():
    global ball_pos, ball_dir, score
    ball_pos[0] += ball_dir[0]
    ball_pos[1] += ball_dir[1]
    
    #Toque de cima ou Toque de baixo
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - 2:
        ball_dir[1] *= -1
        
    #Contato com a barra esquerda
    if ball_pos[0] == paddle_width and paddle_left_pos <= ball_pos[1] <= paddle_left_pos + paddle_height:
        ball_dir[0] *= -1
        
    #Contato com a barra direita
    if ball_pos[0] == WIDTH - paddle_width - 2 and paddle_right_pos <= ball_pos[1] <= paddle_right_pos + paddle_height:
        ball_dir[0] *= -1
        
    #Ponto *NO* lado esquerdo
    if ball_pos[0] < 0:
        score[1] += 1
        ball_pos = [WIDTH//2, HEIGHT//2]
        ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]
        
    #Ponto *NO* lado direito
    if ball_pos[0] > WIDTH - 2:
        score[0] += 1
        ball_pos = [WIDTH//2, HEIGHT//2]
        ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]

#Variavel controladora de Telas
Counter_Menu = 0  

#Logica dos menus
while True:

    #Menu inicial
    if Counter_Menu == 0: 
        oled.fill(0)
        oled.show()
        oled.text("Press Start",20,15)
        oled.show()
        
        #Logica botão start para o Menu inicial
        if not Start_Button.value():
            Counter_Menu = 1
        
    #Menu de iniciação do jogo
    if Counter_Menu == 1: 
        oled.fill(0)
        oled.text("Pong!",45,15)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        Counter_Menu = 2
        


    # Tela do jogo
    if Counter_Menu == 2:
        oled.fill(0) # Limpa a tela
        draw_scores()
        draw_paddle(paddle_left_pos)
        draw_ball(ball_pos)
        move_ball()

        #movimento barra esquerda
        left_pot = machine.ADC(26)
        left_pot_value = left_pot.read_u16()
        paddle_left_pos = int((left_pot_value / 65535) * (HEIGHT - paddle_height))
        print(left_pot)
        print(left_pot_value)

        #movimento barra direita
        right_pot = machine.ADC(27)
        right_pot_value = right_pot.read_u16()
        paddle_right_pos = int((right_pot_value / 65535) * (HEIGHT - paddle_height))

        oled.show()
        time.sleep(ball_speed)

        # Verifica se um dos jogadores atingiu a pontuação de 3
        if score[0] == 3 or score[1] == 3:
            # Muda para a tela de vitória
            Counter_Menu = 3


    # Tela de vitória
    if Counter_Menu == 3:
        oled.fill(0)
        if score[0] == 3:
            oled.text("Player 1 Wins!", 10, 15)
        elif score[1] == 3:
            oled.text("Player 2 Wins!", 10, 15)
        oled.show()
    
    #Logica botão de reset       
    if not Reset_Button.value():
            score = [0, 0]
            Counter_Menu = 0
  

    
