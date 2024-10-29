import pygame
from pong import run_game

# Inicializa o Pygame
pygame.init()

# Define o tamanho da janela
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong 2: O Inimigo Agora É Outro")

# Estado do jogo
game_state = "menu"

# Função para desenhar o menu
def draw_menu():
    # Desenha o título
    font = pygame.font.Font(None, 72)
    title = font.render("PONG 2: O INIMIGO AGORA É OUTRO", True, (255, 255, 255))
    screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 2 - 100))

    # Desenha o botão de "Start Game"
    button_width = 200
    button_height = 50
    button_x = WINDOW_WIDTH // 2 - button_width // 2
    button_y = WINDOW_HEIGHT // 2 + 50
    pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    button_text = font.render("Start Game", True, (0, 0, 0))
    screen.blit(button_text, (button_x + 40, button_y + 10))

    # Verifica se o mouse está sobre o botão
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if (
        button_x <= mouse_pos[0] <= button_x + button_width
        and button_y <= mouse_pos[1] <= button_y + button_height
        and mouse_pressed[0]
    ):
        global game_state
        game_state = "game"
        run_game()

# Loop principal do menu
running = True
while running:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha o menu
    draw_menu()

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()