import pygame

def run_game():
    # Inicializa o Pygame
    pygame.init()

    # Define o tamanho da janela
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong")
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    class Pong:
        def __init__(self):
            self.novas_bolinhas = []
            self.projéteis = []

        def criar_nova_bolinha(self):
            self.novas_bolinhas.append(Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 20, (255, 255, 255)))

        def atirar_projétil(self):
            self.projéteis.append(Projétil(paddle1.x + paddle1.width, paddle1.y + paddle1.height // 2.5, 10, 50, (255, 255, 0)))

        def atualizar_novas_bolinhas(self):
            for bola in self.novas_bolinhas:
                bola.move()
                if bola.y - bola.radius < 0 or bola.y + bola.radius > WINDOW_HEIGHT:
                    bola.speed_y *= -1
                if bola.x - bola.radius < 0 or bola.x + bola.radius > WINDOW_WIDTH:
                    bola.speed_x *= -1
                if (
                    bola.x - bola.radius <= paddle1.x + paddle1.width
                    and bola.y >= paddle1.y
                    and bola.y <= paddle1.y + paddle1.height
                ):
                    bola.speed_x *= -1
                if (
                    bola.x + bola.radius >= paddle2.x
                    and bola.y >= paddle2.y
                    and bola.y <= paddle2.y + paddle2.height
                ):
                    bola.speed_x *= -1

        def atualizar_projéteis(self):
            for projétil in self.projéteis:
                projétil.move()
                if projétil.x <= 0:
                    self.projéteis.remove(projétil)
                if (
                        projétil.x + projétil.width >= paddle2.x + paddle2.width
                        and projétil.y >= paddle2.y
                        and projétil.y <= paddle2.y + paddle2.height
                ):
                    jogo_pong.projéteis.remove(projétil)
                    paddle2.height = 0
                elif projétil.x - projétil.width < 0 or projétil.x + projétil.width > WINDOW_WIDTH:
                    self.projéteis.remove(projétil)

        def desenhar_novas_bolinhas(self, screen):
            for bola in self.novas_bolinhas:
                bola.draw(screen)

        def desenhar_projéteis(self, screen):
            for projétil in self.projéteis:
                projétil.draw(screen)

    class Ball:
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.speed_x = 0.8
            self.speed_y = 0.8

        def move(self):
            self.x += self.speed_x
            self.y += self.speed_y

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        def reiniciar(self):
            self.x = WINDOW_WIDTH // 2
            self.y = WINDOW_HEIGHT // 2
            self.speed_x *= -1
            self.speed_y *= -1

    class Projétil:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = height  # Largura e altura trocadas para ficar deitado
            self.height = width
            self.color = color
            self.speed_x = 2  # Velocidade para a direita

        def move(self):
            self.x += self.speed_x

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    class Paddle:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.speed = 1

        def move_up(self):
            self.y -= self.speed

        def move_down(self):
            self.y += self.speed

        def move_right(self):
            self.x += self.speed

        def move_left(self):
            self.x -= self.speed

        def increase_size(self):
            self.height += 10

        def decrease_size(self):
            if self.height > 10:
                self.height -= 10

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    # Cria a bola e as raquetes
    ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 20, (255, 255, 255))
    paddle1 = Paddle(50, WINDOW_HEIGHT // 2 - 50, 20, 100, (255, 255, 255))
    paddle2 = Paddle(WINDOW_WIDTH - 70, WINDOW_HEIGHT // 2 - 50, 20, 100, (255, 255, 255))

    # Cria uma instância do jogo Pong
    jogo_pong = Pong()

    # Loop principal do jogo
    running = True
    while running:
        # Tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS:
                    paddle1.increase_size()
                elif event.key == pygame.K_MINUS:
                    paddle1.decrease_size()
                elif event.key == pygame.K_c:
                    # Cria uma nova bolinha
                    jogo_pong.criar_nova_bolinha()
                elif event.key == pygame.K_r:
                    paddle2.height = 100
                    paddle2.speed = 1
                if event.key == pygame.K_q:  # Botão esquerdo do mouse
                    jogo_pong.atirar_projétil()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    jogo_pong.atirar_projétil()

        # Movimentação das raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] and keys[pygame.K_p]:
            paddle2.speed = 0
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_d]:
            paddle1.move_right()
        if keys[pygame.K_a]:
            paddle1.move_left()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()
        if paddle1.y < 0:
            paddle1.y = 0
        if paddle1.y + paddle1.height > WINDOW_HEIGHT:
            paddle1.y = WINDOW_HEIGHT - paddle1.height
        if paddle2.y < 0:
            paddle2.y = 0
        if paddle2.y + paddle2.height > WINDOW_HEIGHT:
            paddle2.y = WINDOW_HEIGHT - paddle2.height

        # Atualiza a posição da bola
        ball.move()

        # Atualiza a posição das bolinhas
        jogo_pong.atualizar_novas_bolinhas()

        # Atualiza a posição dos projéteis
        jogo_pong.atualizar_projéteis()

        # Detecta colisões com a barra da direita
        for projétil in jogo_pong.projéteis:
            if (
                    projétil.x == paddle2.x
                    and projétil.y == paddle2.y
            ):
                jogo_pong.projéteis.remove(projétil)

        # Detecta colisões com as bordas
        if ball.y - ball.radius < 0 or ball.y + ball.radius > WINDOW_HEIGHT:
            ball.speed_y *= -1
        if ball.x - ball.radius < 0 or ball.x + ball.radius > WINDOW_WIDTH:
            ball.speed_x *= -1

        # Verifica se houve colisão com a raquete esquerda
        if (
                ball.x - ball.radius <= paddle1.x + paddle1.width
                and ball.y >= paddle1.y
                and ball.y <= paddle1.y + paddle1.height
        ):
            ball.speed_x *= -1
            ball.x = paddle1.x + paddle1.width + ball.radius

        # Verifica se houve colisão com a raquete direita
        if (
                ball.x + ball.radius >= paddle2.x
                and ball.y >= paddle2.y
                and ball.y <= paddle2.y + paddle2.height
        ):
            ball.speed_x *= -1
            ball.x = paddle2.x - ball.radius

        # Limpa a tela
        screen.fill((0, 0, 0))

        # Desenha a bola e as raquetes
        ball.draw(screen)
        paddle1.draw(screen)
        paddle2.draw(screen)

        # Verifica se houve gol
        if ball.x - ball.radius <= 0:
            pontos_jogador2 += 1
            ball.reiniciar()

        elif ball.x + ball.radius >= WINDOW_WIDTH:
            pontos_jogador1 += 1
            ball.reiniciar()


        for bola in jogo_pong.novas_bolinhas:
            if bola.x - bola.radius <= 0:
                pontos_jogador2 += 1
                bola.reiniciar()
            elif bola.x + bola.radius >= WINDOW_WIDTH:
                pontos_jogador1 += 1
                bola.reiniciar()

        # Desenha a pontuação
        font = pygame.font.Font(None, 36)
        texto_pontos = font.render(f"{pontos_jogador1}:{pontos_jogador2}", True, (255, 255, 255))
        screen.blit(texto_pontos, (WINDOW_WIDTH // 2 - texto_pontos.get_width() // 2, 10))

        # Desenha as bolinhas e as raquetes
        jogo_pong.desenhar_novas_bolinhas(screen)
        jogo_pong.desenhar_projéteis(screen)

        # Atualiza a tela
        pygame.display.flip()

    # Encerra o Pygame
    pygame.quit()
