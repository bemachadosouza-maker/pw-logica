import pygame
pygame.int()
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela inicial")
fonte = pygame.font.SysFont("arial", 40, bold=True)
mensagem = fonte.render("tela em python",
                        True, (255, 100, 180))
posicao_x = (LARGURA - mensagem.get_width()) // 2
posicao_y = (LARGURA - mensagem.get_height()) // 2
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        tela.fill((20, 20, 30))
        tela.blit(mensagem, (posicao_x, posicao_y))
        pygame.display.update()
pygame.quit()
