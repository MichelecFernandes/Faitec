####Save the Dino###
##Autores: Dilton Thales Melho da Silva			Matrícula: 1202110055
##Autores: Lavínia Rodrigues Brandani Tenório		Matrícula: 1202210071
##Autores: Michele Cristina Fernandes			Matrícula: 1202210061

import os
import random
import pygame
from pygame import font
from pygame.locals import *

# importante, sempre tem que ter
pygame.init()
posdino = [650, 450, 145, 153]

fonte_jogar = pygame.font.SysFont("arial", 50)
fundo_inicial = pygame.image.load('img/tela_historia.png')
mensagem_inicial = fonte_jogar.render("", True, [0,0,0])

fonte_pontos = pygame.font.SysFont("arial", 35, bold=pygame.font.Font.bold)

fonte_informacoes = pygame.font.SysFont("arial", 50)
fundo_informacoes = pygame.image.load('img/sobre.png')
mensagem_informacoes = fonte_jogar.render("", True, [0, 0, 0])

fonte_tutorial = pygame.font.SysFont("arial", 50)
mensagem_tutorial = fonte_tutorial.render("", True, [0, 0, 0])
fundo_tutorial = pygame.image.load('img/turorial_inicio.png')

fonte_recorde = pygame.font.SysFont("arial", 35, bold=pygame.font.Font.bold)


fonte_inicio_gameover = pygame.font.SysFont("arial", 50)
mensagem_inicio_gameover = fonte_tutorial.render("", True, [0, 0, 0])
larguratexto_inicio_gameover = [350, 500, 200, 100]


fonte_inicio_sobre = pygame.font.SysFont("arial", 50)
mensagem_inicio_sobre = fonte_tutorial.render("", True, [0, 0, 0])
larguratexto_inicio_sobre = [350, 500, 200, 100]


fonte_historia = pygame.font.SysFont("arial", 50)
mensagem_historia = fonte_tutorial.render("", True, [0, 0, 0])
larguratexto_historia = [330, 510, 200, 100]


# definindo a tela
medidas_tela = [800, 600]
medidas_tela_2 = [0,0, 800, 600]
tela = pygame.display.set_mode(medidas_tela)
pygame.display.set_caption('Save the Dino')


larguraTexto_recomecar = [350, 280, 100, 50]

recorde = [0]


def sortearPosicaoMetoro(meteoro, tela):
    nova_posicao = random.randint(0, (tela[0]) - meteoro[2])
    meteoro[0] = nova_posicao

def atualizarObjeto(posmeteoro, tela, tempoClock, pontos, pontuacao):
    if posmeteoro[1] != tela[1]:
        posmeteoro[1] += 2
        return tempoClock, pontuacao, pontos

    pontos += 1
    pontuacao = fonte_pontos.render(str(pontos), True, [216, 65, 38])
    posmeteoro[1] = 0
    sortearPosicaoMetoro(posmeteoro, tela)
    return tempoClock + 800, pontuacao, pontos


def movimentoDino(direcao, posicaoDino):
    if(direcao == 1):
        posicaoDino[0] -= 2
    if (direcao == 2):
        posicaoDino[0] += 2

def colisaoTela(medidas_tela2, posdino, direcaoDino):
    if direcaoDino == 2 and ((posdino[0] + posdino[2]) > (medidas_tela2[0] + medidas_tela2[2])):
        return False

    # verifica esquerda
    if direcaoDino == 1 and posdino[0] == medidas_tela2[0]:
        return False

    return True

def colisao(posmeteoro, posicaodino):
    # verifica se p dino não está embaixado do meteoro
    if posmeteoro[0] >= (posicaodino[0] + posicaodino[2]) or posicaodino[0] >= (posmeteoro[0] + posmeteoro[2]):
        return False

    # verifica se o meteoro esta pra cima do dino
    if (posmeteoro[1] + posmeteoro[3]) < posdino[1]:
        return False
    # vai colidir
    return True

def verificarColisoesPossiveis(lista_metoros, posdino):
    colidiu = False
    qtd_meteoros = len(lista_metoros)
    i = 0
    while i < qtd_meteoros and not colidiu:
        colidiu = colisao(lista_metoros[i], posdino)
        i += 1

    return colidiu

def gameover(pontos):
    game_over = True
    fundo = pygame.image.load('img/reviver_historia.png')
    fonte_recomecar = pygame.font.SysFont("arial", 35, bold=pygame.font.Font.bold)
    mensagem = fonte_recomecar.render("", True, [255, 255, 255])


    jogar_denovo = False
    reviver = False

    record_atual = recorde[0]
    if pontos > recorde[0]:
        recorde[0] = pontos
        record_atual = recorde[0]

    while game_over:
        texto_recorde = fonte_recorde.render(str(record_atual), True, [216, 65, 38])
        tela.blit(fundo, [0, 0])
        tela.blit(mensagem, [325, 450])
        tela.blit(texto_recorde, [450, 358])
        tela.blit(mensagem_inicio_gameover, larguratexto_inicio_gameover)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = False

            if event.type == MOUSEBUTTONDOWN:
                pos_mouse_2 = pygame.mouse.get_pos()
                x1 = pos_mouse_2[0]
                y1 = pos_mouse_2[1]

                if ((x1 > larguraTexto_recomecar[0] and x1 < (
                        larguraTexto_recomecar[0] + larguraTexto_recomecar[2])) and (
                        y1 > larguraTexto_recomecar[1] and y1 < (
                        larguraTexto_recomecar[1] + larguraTexto_recomecar[3]))):
                    reviver = True
                    jogar_denovo = True
                    game_over = False

                if ((x1 > larguratexto_inicio_gameover[0] and x1 < (
                        larguratexto_inicio_gameover[0] + larguratexto_inicio_gameover[2])) and (
                        y1 > larguratexto_inicio_gameover[1] and y1 < (
                        larguratexto_inicio_gameover[1] + larguratexto_inicio_gameover[3]))):
                    game_over = False
                    jogar_denovo = True


        pygame.display.update()

    return jogar_denovo, reviver

def jogar(tela):
    fundo = pygame.image.load('img/tela_jogo.png')
    pygame.display.update()

    # definições do objeto
    posmeteoro1 = [100, -200, 94, 173]
    posmeteoro2 = [300, -300, 94, 173]
    posmeteoro3 = [450, -500, 94, 173]
    lista_meteoros = [posmeteoro1, posmeteoro2, posmeteoro3]

    # imagens objetos
    meteoro1 = pygame.image.load('img/asteroide_oficial.png')
    meteoro2 = pygame.image.load('img/asteroide_oficial.png')
    meteoro3 = pygame.image.load('img/asteroide_oficial.png')
    dinomorto = pygame.image.load('img/tela_jogo.png')

    # caminho da imagem do dino
    caminho_img = 'img/dino5.png'
    posdino = [650, 450, 145, 153]
    direcaoDino = 0

    # tempo que desce outro meteoro
    clock = pygame.time.Clock()
    tempoClock = 200

    # pontuação
    pontos = 0
    pontuacao = fonte_pontos.render(str(pontos), True, [216, 65, 38])
    parar_tudo = False

    continuar = True
    while continuar:

        clock.tick(tempoClock)

        tela.blit(fundo, [0, 0])
        tela.blit(meteoro1, [posmeteoro1[0], posmeteoro1[1]])
        tela.blit(meteoro2, [posmeteoro2[0], posmeteoro2[1]])
        tela.blit(meteoro3, [posmeteoro3[0], posmeteoro3[1]])

        tela.blit(pygame.image.load(caminho_img), [posdino[0], posdino[1]])
        tela.blit(pontuacao, [750, 23])
        for event in pygame.event.get():
            if event.type == QUIT:
                continuar = False
                parar_tudo = True

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    caminho_img = 'img/dino5_esquerda.png'
                    direcaoDino = 1
                elif event.key == K_RIGHT:
                    caminho_img = 'img/dino5.png'
                    direcaoDino = 2

            if event.type == KEYUP:
                direcaoDino = 0

        tempoClock, pontuacao, pontos = atualizarObjeto(posmeteoro1, medidas_tela, tempoClock, pontos, pontuacao)
        tempoClock, pontuacao, pontos = atualizarObjeto(posmeteoro2, medidas_tela, tempoClock, pontos, pontuacao)
        tempoClock, pontuacao, pontos = atualizarObjeto(posmeteoro3, medidas_tela, tempoClock, pontos, pontuacao)

        if not verificarColisoesPossiveis(lista_meteoros, posdino):
            if direcaoDino != 0 and colisaoTela(medidas_tela_2, posdino, direcaoDino):
                movimentoDino(direcaoDino, posdino)
        else:
            continuar = False


        pygame.display.update()

    return parar_tudo, pontos


def tutorial(tela):
    fundo = pygame.image.load('img/turorial_inicio.png')
    pygame.display.update()

    continuar = True
    while continuar:
        tela.blit(fundo, [0, 0])

        for event in pygame.event.get():
            if event.type == QUIT:
                continuar = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuar = False

            if event.type == MOUSEBUTTONDOWN:
                pos_mouse_2 = pygame.mouse.get_pos()
                x3 = pos_mouse_2[0]
                y3 = pos_mouse_2[1]

                if ((x3 > larguratexto_inicio_sobre[0] and x3 < (larguratexto_inicio_sobre[0] + larguratexto_inicio_sobre[2])) and (y3 > larguratexto_inicio_sobre[1] and y3 < (larguratexto_inicio_sobre[1] + larguratexto_inicio_sobre[3]))):

                    continuar =  False
                    tutorial = False
                    jogar_denovo = True




        pygame.display.update()

    return jogar_denovo, tutorial



def historia(tela):
    fundo = pygame.image.load('img/extincao.png')
    pygame.display.update()

    continuar = True
    while continuar:
        tela.blit(fundo, [0, 0])

        for event in pygame.event.get():
            if event.type == QUIT:
                continuar = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuar = False

            if event.type == MOUSEBUTTONDOWN:
                pos_mouse_2 = pygame.mouse.get_pos()
                x4 = pos_mouse_2[0]
                y4 = pos_mouse_2[1]

                if ((x4 > larguratexto_inicio_sobre[0] and x4 < (larguratexto_inicio_sobre[0] + larguratexto_inicio_sobre[2])) and (y4 > larguratexto_inicio_sobre[1] and y4 < (larguratexto_inicio_sobre[1] + larguratexto_inicio_sobre[3]))):

                    continuar =  False
                    historia = False
                    jogar_denovo = True



        pygame.display.update()

    return jogar_denovo, historia

def sobre(tela):
    fundo = pygame.image.load('img/sobre.png')

    pygame.display.update()

    continuar = True
    while continuar:
        tela.blit(fundo, [0, 0])
        tela.blit(mensagem_inicio_sobre, larguratexto_inicio_sobre)
        for event in pygame.event.get():
            if event.type == QUIT:
                continuar = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuar = False

            if event.type == MOUSEBUTTONDOWN:
                pos_mouse_2 = pygame.mouse.get_pos()
                x2 = pos_mouse_2[0]
                y2 = pos_mouse_2[1]

                if ((x2 > larguratexto_inicio_sobre[0] and x2 < (larguratexto_inicio_sobre[0] + larguratexto_inicio_sobre[2])) and (y2 > larguratexto_inicio_sobre[1] and y2 < (larguratexto_inicio_sobre[1] + larguratexto_inicio_sobre[3]))):

                    continuar =  False
                    sobre = False
                    jogar_denovo = True


        pygame.display.update()

    return jogar_denovo, sobre

larguraTexto_jogar = [350, 235, 200, 50]
larguraTexto_informacoes = [300, 420, 200, 100]
larguratexto_tutorial = [340, 330, 200, 100]
reviver = False
clicouJogar = False
parar_jogo = False

inicial = True
while inicial:
    tela.blit(fundo_inicial, [0,0])
    tela.blit(mensagem_inicial, larguraTexto_jogar)
    tela.blit(mensagem_informacoes,larguraTexto_informacoes)
    tela.blit(mensagem_tutorial,larguratexto_tutorial)
    tela.blit(mensagem_historia, larguratexto_historia)

    if (reviver or clicouJogar):
        reviver = False
        clicouJogar = False

        parar_jogo, pontos = jogar(tela)
        if (parar_jogo):
            inicial = False
            parar_jogo = False
        else:
            inicial, reviver = gameover(pontos)

    for event in pygame.event.get():
        if event.type == QUIT:
            inicial = False

        if event.type == MOUSEBUTTONDOWN:
            pos_mouse_1 = pygame.mouse.get_pos()
            x = pos_mouse_1[0]
            y = pos_mouse_1[1]

            if((x > larguraTexto_jogar[0] and x < (larguraTexto_jogar[0] + larguraTexto_jogar[2])) and (y > larguraTexto_jogar[1] and y < (larguraTexto_jogar[1] + larguraTexto_jogar[3]))):
                clicouJogar = True

            if ((x > larguraTexto_informacoes[0] and x < (larguraTexto_informacoes[0] + larguraTexto_informacoes[2])) and (y > larguraTexto_informacoes[1] and y < (larguraTexto_informacoes[1] + larguraTexto_informacoes[3]))):
                sobre(tela)

            if ((x > larguratexto_tutorial[0] and x < (larguratexto_tutorial[0] + larguratexto_tutorial[2])) and (y > larguratexto_tutorial[1] and y < (larguratexto_tutorial[1] + larguratexto_tutorial[3]))):
                tutorial(tela)

            if ((x > larguratexto_historia[0] and x < (larguratexto_historia[0] + larguratexto_historia[2])) and (y > larguratexto_historia[1] and y < (larguratexto_historia[1] + larguratexto_historia[3]))):
                historia(tela)


    pygame.display.update()
