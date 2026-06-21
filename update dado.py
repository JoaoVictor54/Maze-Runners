import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time
import cv2



import pygame
import cv2
import sys


def naobug():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




def intro():

    # ==========================
    # CONFIGURAÇÕES
    # ==========================
    LARGURA = 1331
    ALTURA = 610

    VIDEO_ARQUIVO = "Intro EEJE Games.mp4"
    AUDIO_ARQUIVO = "Intro-EEJE-Games.mp3"

    # ==========================
    # INICIALIZAÇÃO
    # ==========================
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Maze-Runners")

    clock = pygame.time.Clock()

    # ==========================
    # CARREGAR VÍDEO
    # ==========================
    video = cv2.VideoCapture(VIDEO_ARQUIVO)

    fps = video.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 60

    print("Carregando intro...")

    frames = []

    print("Carregando intro...")

    fonte = pygame.font.SysFont(None, 50)

    frames = []
    contador_animacao = 0

    animacoes = [
        "Carregando",
        "Carregando.",
        "Carregando..",
        "Carregando..."
    ]

    while True:

        # Mantém a janela responsiva
        naobug()

        sucesso, frame = video.read()

        if not sucesso:
            break

        # Atualiza o texto a cada 10 frames carregados
        if contador_animacao % 10 == 0:

            texto_str = animacoes[
                (contador_animacao // 10) % len(animacoes)
            ]

            tela.fill((0, 0, 0))

            texto = fonte.render(
                texto_str,
                True,
                (255, 255, 255)
            )

            tela.blit(
                texto,
                (
                    LARGURA // 2 - texto.get_width() // 2,
                    ALTURA // 2 - texto.get_height() // 2
                )
            )

            pygame.display.flip()

        contador_animacao += 1

        # Converte BGR -> RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Redimensiona apenas UMA VEZ durante o carregamento
        frame = cv2.resize(frame, (LARGURA, ALTURA))

        # Cria Surface
        surface = pygame.surfarray.make_surface(
            frame.swapaxes(0, 1)
        )

        frames.append(surface)

    video.release()

    print(f"{len(frames)} frames carregados.")
    while True:
        sucesso, frame = video.read()

        if not sucesso:
            break

        # Converte BGR -> RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Redimensiona apenas UMA VEZ durante o carregamento
        frame = cv2.resize(frame, (LARGURA, ALTURA))

        # Cria Surface
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        frames.append(surface)

    video.release()

    print(f"{len(frames)} frames carregados.")

    # ==========================
    # CARREGAR ÁUDIO
    # ==========================
    pygame.mixer.music.load(AUDIO_ARQUIVO)

    # ==========================
    # TOCAR INTRO
    # ==========================
    pygame.mixer.music.play()

    frame_atual = 0
    rodando_intro = True

    while rodando_intro:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Qualquer tecla pula a intro
            if event.type == pygame.KEYDOWN:
                rodando_intro = False

        if frame_atual >= len(frames):
            rodando_intro = False
            continue

        tela.blit(frames[frame_atual], (0, 0))
        pygame.display.flip()

        frame_atual += 1

        clock.tick(fps)

    # ==========================
    # LIMPEZA
    # ==========================
    pygame.mixer.music.stop()

    print("Intro concluída!")
    print("Iniciando jogo...")

    # =====================================
    # DAQUI PARA BAIXO VEM O JOGO
    # =====================================

#intro()














class JogoDados:

    def __init__(self):

        pygame.init()
        self.musica_menu = "menu.wav"
        self.musica_tabuleiro = "main.wav"
        pygame.mixer.music.load(self.musica_menu)
        pygame.mixer.music.play(-1)

        self.tela = pygame.display.set_mode((1331, 610))

        self.fonte = pygame.font.SysFont("arial", 60)
        self.fonte2 = pygame.font.SysFont("arial", 45)
        self.fonte3 = pygame.font.SysFont("arial", 30)
        self.fonte4 = pygame.font.SysFont("arial", 80)

        self.background = pygame.image.load("Background1.png").convert_alpha()

        # SPRITES DOS DADOS
        self.dado1 = pygame.image.load("dado1.png").convert_alpha()
        self.dado2 = pygame.image.load("dado2.png").convert_alpha()
        self.dado3 = pygame.image.load("dado3.png").convert_alpha()
        self.dado4 = pygame.image.load("dado4.png").convert_alpha()
        self.dado5 = pygame.image.load("dado5.png").convert_alpha()
        self.dado6 = pygame.image.load("dado6.png").convert_alpha()

        self.sprites_dados = [
            self.dado1,
            self.dado2,
            self.dado3,
            self.dado4,
            self.dado5,
            self.dado6,
            
        ]
        #SPRITES DE BARRAS DE VIDA
        self.vida1p1 = pygame.image.load("barradevida/vida1p1.png").convert_alpha()
        self.vida1p2 = pygame.image.load("barradevida/vida1p2.png").convert_alpha()
        self.vida2p1 = pygame.image.load("barradevida/vida2p1.png").convert_alpha()
        self.vida2p2 = pygame.image.load("barradevida/vida2p2.png").convert_alpha()
        self.vida3p1 = pygame.image.load("barradevida/vida3p1.png").convert_alpha()
        self.vida3p2 = pygame.image.load("barradevida/vida3p2.png").convert_alpha()
        self.vida4p1 = pygame.image.load("barradevida/vida4p1.png").convert_alpha()
        self.vida4p2 = pygame.image.load("barradevida/vida4p2.png").convert_alpha()
        self.vida5p1 = pygame.image.load("barradevida/vida5p1.png").convert_alpha()
        self.vida5p2 = pygame.image.load("barradevida/vida5p2.png").convert_alpha()
        self.vida6 = pygame.image.load("barradevida/vida6.png").convert_alpha()
        
        self.vidasp1 = [
            self.vida1p1,
            self.vida2p1,
            self.vida3p1,
            self.vida4p1,
            self.vida5p1,
            self.vida6,
            self.vida6,
            self.vida6
        ]
        self.vidasp2 = [
            self.vida1p2,
            self.vida2p2,
            self.vida3p2,
            self.vida4p2,
            self.vida5p2,
            self.vida6,
            self.vida6,
            self.vida6
        ]

        self.vidap1 = 0
        self.vidap2 = 0

        #SPRITES PÁGINAS
        self.seta = pygame.image.load("img/seta.png").convert_alpha()

        self.menu1 = pygame.image.load("img/menu1.png").convert_alpha()
        self.menu2 = pygame.image.load("img/menu2.png").convert_alpha()
        self.menu3 = pygame.image.load("img/menu3.png").convert_alpha()
        self.menu4 = pygame.image.load("img/menu4.png").convert_alpha()

        self.menu = self.menu1

        self.escolha = pygame.image.load("img/escolha.png").convert_alpha()
        self.pagempate = pygame.image.load("img/empate.png").convert_alpha()
        self.cmcw = pygame.image.load("img/cmcw.png").convert_alpha()
        self.cmco = pygame.image.load("img/cmco.png").convert_alpha()

        ## Telas de vitorias
            ## vitoria do player 1
        self.venc1= pygame.image.load("img/victory/perdp2 1.png").convert_alpha()
        self.perdp2_2= pygame.image.load("img/victory/perdp2 2.png").convert_alpha()
        self.perdp2_3= pygame.image.load("img/victory/perdp2 3.png").convert_alpha()
        self.perdp2_4= pygame.image.load("img/victory/perdp2 4.png").convert_alpha()
        self.perdp2_5= pygame.image.load("img/victory/perdp2 5.png").convert_alpha()
        self.perdp2_6= pygame.image.load("img/victory/perdp2 6.png").convert_alpha()
        self.anim1 = 0
            
            ## vitoria do player 2
        self.venc2 = pygame.image.load("img/victory/perdp1 1.png").convert_alpha()
        self.perdp1_2= pygame.image.load("img/victory/perdp1 2.png").convert_alpha()
        self.perdp1_3= pygame.image.load("img/victory/perdp1 3.png").convert_alpha()
        self.perdp1_4= pygame.image.load("img/victory/perdp1 4.png").convert_alpha()
        self.perdp1_5= pygame.image.load("img/victory/perdp1 5.png").convert_alpha()
        self.perdp1_6= pygame.image.load("img/victory/perdp1 6.png").convert_alpha()
        self.anim2 = 0


        self.contbut1 = pygame.image.load("continuebut.png").convert_alpha()
        self.contbut2 = pygame.image.load("continuebut2.png").convert_alpha()

        self.ogro = pygame.image.load("anim/ogro.png").convert_alpha()
        self.cavaleiro = pygame.image.load("anim/cavaleiro.png").convert_alpha()
        self.ogro = pygame.transform.scale(self.ogro, (100, 100))
        self.cavaleiro = pygame.transform.scale(self.cavaleiro, (100, 100))

        self.morte_cavaleiro = [
            pygame.image.load("anim/mortea.png").convert_alpha(),
            pygame.image.load("anim/morteb.png").convert_alpha(),
            pygame.image.load("anim/mortec.png").convert_alpha(),
            pygame.image.load("anim/morted.png").convert_alpha(),
        ]

        self.dano_cavaleiro = [
            pygame.image.load("anim/danocava1.png").convert_alpha(),
            pygame.image.load("anim/danocava2.png").convert_alpha(),
            pygame.image.load("anim/danocava3.png").convert_alpha(),
            pygame.image.load("anim/danocava1.png").convert_alpha(),
        ]

        self.morte_ogro = [
            pygame.image.load("anim/morteo1.png").convert_alpha(),
            pygame.image.load("anim/morteo2.png").convert_alpha(),
            pygame.image.load("anim/morteo3.png").convert_alpha(),
            pygame.image.load("anim/morteo4.png").convert_alpha(),
        ]

        self.dano_ogro = [
            pygame.image.load("anim/danogro1.png").convert_alpha(),
            pygame.image.load("anim/danogro2.png").convert_alpha(),
            pygame.image.load("anim/danogro3.png").convert_alpha(),
            pygame.image.load("anim/danogro4.png").convert_alpha(),
        ]
        
        self.idle_ogro = [
            pygame.image.load("anim/orc-idle1.png").convert_alpha(),
            pygame.image.load("anim/orc-idle2.png").convert_alpha(),
            pygame.image.load("anim/orc-idle3.png").convert_alpha(),
            pygame.image.load("anim/orc-idle4.png").convert_alpha(),
            pygame.image.load("anim/orc-idle5.png").convert_alpha(),
            pygame.image.load("anim/orc-idle6.png").convert_alpha(),
        ]
        
        self.idle_cava = [
            pygame.image.load("anim/idlecava1.png").convert_alpha(),
            pygame.image.load("anim/idlecava2.png").convert_alpha(),
            pygame.image.load("anim/idlecava3.png").convert_alpha(),
            pygame.image.load("anim/idlecava4.png").convert_alpha(),
            pygame.image.load("anim/idlecava5.png").convert_alpha(),
            pygame.image.load("anim/idlecava6.png").convert_alpha(),
        ]

        self.andar_cava = [
            pygame.image.load("anim/acava1.png").convert_alpha(),
            pygame.image.load("anim/acava2.png").convert_alpha(),
            pygame.image.load("anim/acava3.png").convert_alpha(),
            pygame.image.load("anim/acava4.png").convert_alpha(),
            pygame.image.load("anim/acava5.png").convert_alpha(),
            pygame.image.load("anim/acava6.png").convert_alpha(),
            pygame.image.load("anim/acava7.png").convert_alpha(),
        ]

        self.andar_ogro = [
            pygame.image.load("anim/aogro.png").convert_alpha(),
            pygame.image.load("anim/aogro2.png").convert_alpha(),
            pygame.image.load("anim/aogro3.png").convert_alpha(),
            pygame.image.load("anim/aogro4.png").convert_alpha(),
            pygame.image.load("anim/aogro5.png").convert_alpha(),
            pygame.image.load("anim/aogro6.png").convert_alpha(),
            pygame.image.load("anim/aogro7.png").convert_alpha(),
            pygame.image.load("anim/aogro8.png").convert_alpha(),
        ]









        


        # ESTADOS
        self.no_menu = True
        self.escolha_personagem = False
        self.empate = False
        self.personagem_comeca = False
        self.jogo = False
        self.vitoria = False
        self.efeitos = True
        self.rodando = True
        self.pode_jogar = True


        ##POSIÇÕES DOS JOGADORES
        self.vez = 1
        self.p1x =120; self.p1y = 4
        self.p2x = 120; self.p2y =35
        self.p1is = 0; self.p2is = 0
        self.movep1 = False; self.movep2 = False

        # easter eggs
        # CODIGO KONAMI
        self.entradas = []
        self.konami = [K_UP, K_UP, K_DOWN, K_DOWN, K_LEFT, K_RIGHT, K_LEFT, K_RIGHT]
        
        # ANIMAÇÃO
        self.frame_ogro_idx = 0
        self.ogro_animando = False
        self.frame_cava_idx = 0
        self.cava_animando = False
        
        self.frame_idle_cava = 0
        self.idle_timer = 0
        self.idle_timer_orc = 0
        self.frame_idle_orc = 0
        
        




        # RESULTADOS
        self.resultado_dado = ""
        self.resultado_dadop1 = ""
        self.resultado_dadop2 = ""

        self.playercmc = "JOGADOR 1"

        self.relogio = pygame.time.Clock()

        self.tranout = True

        self.t = 0

        self.vencedor = ""

        self.preso1 = False
        self.preso2 = False
        self.pp1 = 0
        self.pp2 = 0

        self.img_tranout = self.menu1

        self.click= True
        

        # TEXTOS
        self.msg_menu = self.fonte4.render("Maze Runners", False, (0, 0, 0))

        self.msg_instrucao = self.fonte3.render(
            "Aperte Enter para JOGAR",
            False,
            (0, 0, 0)
        )

        self.msg_gira = self.fonte3.render(
            "Gire o dado: (espaço)",
            False,
            (0, 0, 0)
        )

        self.msg_gira2 = self.fonte3.render(
            "Gire o dado:",
            False,
            (0, 0, 0)
        )

        self.msg_p1 = self.fonte.render(
            "Player 1",
            False,
            (0, 0, 0)
        )

        self.msg_p2 = self.fonte.render(
            "Player 2",
            False,
            (0, 0, 0)
        )

        self.msg_vs = self.fonte.render(
            "VS",
            False,
            (0, 0, 0)
        )

        self.msg_seta = self.fonte.render(
            "<-",
            False,
            (0, 0, 0)
        )

        self.msg_contseta = self.fonte2.render(
            "Continue <-",
            False,
            (0, 0, 0)
        )

        self.msg_playcmc = self.fonte.render(
            f"O {self.playercmc} é o primeiro!",
            False,
            (0, 0, 0)
        )

        self.msg_empate = self.fonte4.render(
            "EMPATE!",
            False,
            (0, 0, 0)
        )
        self.msg_playvencedor = self.fonte.render(
            f"O vencedor foi :{self.vencedor}",
            False,
            (0, 0, 0)
        )
    
    # movimento cavaleiro
    def mover_cavaleiro_para(self, alvo_x, alvo_y, step_x=10, step_y=4, frame_delay=20):
        self.cava_animando = True
        pixels_desde_ultimo_frame = 0
        while self.p1x != alvo_x or self.p1y != alvo_y:
            if self.p1x < alvo_x:
                self.p1x = min(self.p1x + step_x, alvo_x)
                pixels_desde_ultimo_frame += step_x
            elif self.p1x > alvo_x:
                self.p1x = max(self.p1x - step_x, alvo_x)
                pixels_desde_ultimo_frame += step_x

            if self.p1y < alvo_y:
                self.p1y = min(self.p1y + step_y, alvo_y)
                pixels_desde_ultimo_frame += step_y
            elif self.p1y > alvo_y:
                self.p1y = max(self.p1y - step_y, alvo_y)
                pixels_desde_ultimo_frame += step_y

            if pixels_desde_ultimo_frame >= frame_delay:
                pixels_desde_ultimo_frame = 0
                self.frame_cava_idx = (self.frame_cava_idx + 1) % len(self.andar_cava)

            self.desenhar()
            naobug()
            pygame.event.clear()
            frame_scaled = pygame.transform.scale(
                self.andar_cava[self.frame_cava_idx], (50, 300)
            )

            if self.p1y > 352:
                self.tela.blit(pygame.transform.flip(frame_scaled, True, False), (self.p1x, self.p1y))
            else:
                self.tela.blit(frame_scaled, (self.p1x, self.p1y))

            



            if self.p1y < self.p2y:
                if self.p2y > 352:
                    frame2 = pygame.transform.scale(self.idle_ogro[self.frame_idle_orc],(70,300))
                    #self.tela.blit(pygame.transform.flip(frame2, True, False), (self.p2x, self.p2y))
                else:
                    frame2 = pygame.transform.scale(self.idle_ogro[self.frame_idle_orc],(70,300))
                    self.tela.blit(frame2, (self.p2x, self.p2y))
            pygame.display.flip()
            self.relogio.tick(60)

        self.cava_animando = False
        

    #movimento do ogro
    def mover_ogro_para(self, alvo_x, alvo_y, step_x=10, step_y=4, frame_delay=5):
        self.ogro_animando = True
        pixels_desde_ultimo_frame = 0

        while self.p2x != alvo_x or self.p2y != alvo_y:
            if self.p2x < alvo_x:
                self.p2x = min(self.p2x + step_x, alvo_x)
                pixels_desde_ultimo_frame += step_x
            elif self.p2x > alvo_x:
                self.p2x = max(self.p2x - step_x, alvo_x)
                pixels_desde_ultimo_frame += step_x

            if self.p2y < alvo_y:
                self.p2y = min(self.p2y + step_y, alvo_y)
                pixels_desde_ultimo_frame += step_y
            elif self.p2y > alvo_y:
                self.p2y = max(self.p2y - step_y, alvo_y)
                pixels_desde_ultimo_frame += step_y

            if pixels_desde_ultimo_frame >= frame_delay:
                pixels_desde_ultimo_frame = 0
                self.frame_ogro_idx = (self.frame_ogro_idx + 1) % len(self.andar_ogro)

            self.desenhar()
            naobug()
            pygame.event.clear()
            
            frame_scaled = pygame.transform.scale(
                self.andar_ogro[self.frame_ogro_idx], (70, 300)
            )


            if self.p2y > 352:
                self.tela.blit(pygame.transform.flip(frame_scaled, True, False), (self.p2x, self.p2y))
            else:
                self.tela.blit(frame_scaled, (self.p2x, self.p2y))


            if self.p1y > self.p2y:
                if self.p1y > 352:
                    frame = pygame.transform.scale(self.idle_cava[self.frame_idle_cava],(50,300))
                    self.tela.blit(pygame.transform.flip(frame, True, False), (self.p1x, self.p1y))
                else:
                    frame = pygame.transform.scale(self.idle_cava[self.frame_idle_cava],(50,300))
                    self.tela.blit(frame, (self.p1x, self.p1y))
            pygame.display.flip()
            self.relogio.tick(60)

        self.ogro_animando = False
        


    def animacao_danocava(self):
        for frame in self.dano_cavaleiro:
            frame_scale = pygame.transform.scale(frame, (50, 300))
            pos_x = self.p1x
            pos_y = self.p1y
            self.p1x = -1000; self.p1y = -1000
            self.desenhar()
            self.tela.blit(frame_scale, (pos_x, pos_y))
            self.p1x = pos_x; self.p1y = pos_y
            pygame.display.flip()
            time.sleep(0.0000001)

    def animacao_morte_cavaleiro(self):
        for frame2 in self.morte_cavaleiro:
            frame2_scale = pygame.transform.scale(frame2, (120, 180))
            pos_x2 = self.p1x
            pos_y2 = self.p1y
            self.p1x = -500; self.p1y = -500
            self.desenhar()
            self.tela.blit(frame2_scale, (pos_x2, pos_y2))
            self.p1x = pos_x2; self.p1y = pos_y2
            pygame.display.flip()
            time.sleep(0.5)

    def animacao_danogro(self):
        for frame in self.dano_ogro:
            frame_scale = pygame.transform.scale(frame, (70, 200))
            pos_x = self.p2x
            pos_y = self.p2y
            self.p2x = -1000; self.p2y = -1000
            self.desenhar()
            self.tela.blit(frame_scale, (pos_x, pos_y))
            self.p2x = pos_x; self.p2y = pos_y
            pygame.display.flip()
            time.sleep(0.0000001)

    def animacao_morte_ogro(self):
        for frame in self.morte_ogro:
            frame_scale = pygame.transform.scale(frame, (200, 200))
            pos_x = self.p2x
            pos_y = self.p2y
            self.p2x = -500; self.p2y = -500
            self.desenhar()
            self.tela.blit(frame_scale, (pos_x, pos_y))
            self.p2x = pos_x; self.p2y = pos_y
            pygame.display.flip()
            time.sleep(0.5)

    def tratar_eventos(self):
        
        self.contbut = self.contbut1
        for evento in pygame.event.get():

            if evento.type == QUIT:
                self.rodando = False
            

            # MENU
            if self.no_menu:

                ## trocas de botoes para mouse
                self.img_tranout = self.menu1
                botao1 = pygame.Rect(510, 360, 300, 100)
                botao2 = pygame.Rect(510, 460, 300, 100)
                mouse_pos = pygame.mouse.get_pos()
                if botao1.collidepoint(mouse_pos):
                    self.menu = self.menu1
                    

                if botao2.collidepoint(mouse_pos):
                    self.menu = self.menu2

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    # Botão esquerdo
                    if evento.button == 1 and botao1.collidepoint(mouse_pos):
                        if self.menu == self.menu1:
                            
                            self.menu = self.menu3
                            self.desenhar()
                            time.sleep(0.01)
                            self.no_menu = False
                            self.img_tranout = self.escolha
                            self.escolha_personagem = True

                            self.transicao_in()

                            self.tranout = True

                            continue
                    if evento.button == 1 and botao2.collidepoint(mouse_pos):
                        if self.menu == self.menu2:
                            self.menu = self.menu4
                            self.desenhar()
                            time.sleep(0.01)
                            self.rodando = False


                ##trocas de botoes no teclado
                if evento.type == KEYDOWN:

                    if evento.key in [K_RETURN, K_KP_ENTER] and self.menu == self.menu1:

                        
                        self.menu = self.menu3
                        self.desenhar()
                        time.sleep(0.01)
                        self.no_menu = False
                        self.img_tranout = self.escolha
                        self.escolha_personagem = True

                        self.transicao_in()

                        self.tranout = True

                        continue

                    if evento.key in [K_DOWN,K_s,K_UP,K_w]:
                        
                        if self.menu == self.menu1:
                            self.menu = self.menu2
                        else:
                            self.menu = self.menu1
                        self.desenhar()
                    if evento.key in [K_RETURN, K_KP_ENTER] and self.menu == self.menu2:
                        self.menu = self.menu4
                        self.desenhar()
                        time.sleep(0.01)
                        self.rodando = False  
                        

                        

                        

                        
               
            # ESCOLHA DOS PERSONAGENS
            if self.escolha_personagem:
                ## teclado
                if evento.type == KEYDOWN :

                    if evento.key in [K_RETURN, K_KP_ENTER]:

                        if not self.resultado_dadop1:

                            self.girar_dado_player1()

                            continue

                        if not self.resultado_dadop2:

                            self.girar_dado_player2()

                        else:
                            self.contbut = self.contbut2 
                            self.desenhar()
                            time.sleep(0.01)  
                            self.transicao_in()

                            self.tranout = True

                            self.escolha_personagem = False

                            if self.n1 > self.n2:

                                self.playercmc = "JOGADOR 1"
                                self.personagem_comeca = True
                                self.img_tranout = self.cmcw

                            elif self.n1 < self.n2:

                                self.playercmc = "JOGADOR 2"
                                self.personagem_comeca = True
                                self.img_tranout = self.cmco

                            else:

                                self.transicao_in()

                                self.tranout = True
                                self.img_tranout = self.pagempate
                                self.empate = True

                            continue
                ## mouse
                botao = pygame.Rect(550, 475, 200, 60)
                mouse_pos = pygame.mouse.get_pos()
                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        if not self.resultado_dadop1:

                            self.girar_dado_player1()

                            continue

                        elif not self.resultado_dadop2:

                            self.girar_dado_player2()

                        elif self.resultado_dadop1 and self.resultado_dadop2 and botao.collidepoint(mouse_pos):
                            self.contbut = self.contbut2 
                            self.desenhar()
                            time.sleep(0.01)  
                            self.transicao_in()

                            self.tranout = True

                            self.escolha_personagem = False

                            if self.n1 > self.n2:

                                self.playercmc = "JOGADOR 1"
                                self.personagem_comeca = True
                                self.img_tranout = self.cmcw

                            elif self.n1 < self.n2:

                                self.playercmc = "JOGADOR 2"
                                self.personagem_comeca = True
                                self.img_tranout = self.cmco

                            else:

                                self.transicao_in()

                                self.tranout = True
                                self.img_tranout = self.pagempate
                                self.empate = True

                            continue
            # EMPATE
            if self.empate:
                ## teclado
                if evento.type == KEYDOWN:

                    if evento.key in [K_RETURN, K_KP_ENTER]:

                        self.resultado_dadop1 = ""
                        self.resultado_dadop2 = ""

                        self.empate = False
                        self.img_tranout = self.escolha
                        self.transicao_in()
                        
                        self.tranout = True

                        self.escolha_personagem = True
                ## mouse
                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        self.resultado_dadop1 = ""
                        self.resultado_dadop2 = ""

                        self.empate = False
                        self.img_tranout = self.escolha
                        self.transicao_in()
                        
                        self.tranout = True

                        self.escolha_personagem = True

            # QUEM COMEÇA
            if self.personagem_comeca:

                #teclado
                if evento.type == KEYDOWN:

                    self.tela.blit(self.menu, (0,0))
                    pygame.draw.rect(
                    self.tela,
                    (0, 0, 0),
                    (510,460,300,100)
                    )

                    if evento.key in [K_RETURN, K_KP_ENTER]:
                        self.img_tranout = self.background  
                        self.contbut = self.contbut2 
                        self.desenhar()
                        time.sleep(0.01)  
                        self.transicao_in()
                        self.tranout = True
                        pygame.mixer.music.load(self.musica_tabuleiro)
                        pygame.mixer.music.play(-1)
                        self.personagem_comeca = False
                        self.jogo = True
                       
                #mouse
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    botao = pygame.Rect(1050, 545, 200, 100)
                    mouse_pos = pygame.mouse.get_pos()
                    if evento.button == 1 and botao.collidepoint(mouse_pos):
                        self.img_tranout = self.background  
                        self.contbut = self.contbut2 
                        self.desenhar()
                        time.sleep(0.01)  
                        self.transicao_in()
                        self.tranout = True
                        pygame.mixer.music.load(self.musica_tabuleiro)
                        pygame.mixer.music.play(-1)
                        self.personagem_comeca = False
                        self.jogo = True
                        
            # JOGO
            if self.jogo:
                
                
                #teclado
                print("evento 1 ")
                if evento.type == KEYDOWN:
                    self.entradas.append(evento.key)
                    if self.entradas == self.konami:
                        self.entradas.pop() ##tira a última tecla, pq espaço ou enter não tá no konami
                        self.konami_code()
                        self.entradas.clear()
                        
                        print("konami utilizado")
                
                    if evento.key in [K_SPACE,K_RETURN, K_KP_ENTER] and self.t > 25 and self.pode_jogar:
                        self.pode_jogar = False ##nao pode jogar enquanto o dado estiver rolando
                        self.entradas.clear()##limpa a lista que checa pra easter egg
                        self.girar_dado()
                        
                            
                    if evento.key in [K_p] and self.t > 25:
                        pygame.mixer.music.stop()
                print("saiu 1")
                #mouse
                print("evento 2 ")
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1 and self.t > 25 and self.pode_jogar:
                        self.pode_jogar = False ##nao pode jogar enquanto o dado estiver rolando
                        self.entradas.clear()##limpa a lista que checa pra easter egg
                        pygame.event.clear()
                        self.girar_dado()
                        
                print("saiu 2")
                pygame.event.clear()   
                print("saiu 2.2")            

           

            
                


        if self.movep1:
            while self.n != 0:
                
                self.tv1 = 1 ##pode tirar vida
                self.cv1 = 1 ##pode curar
                self.pp1 = 1 ##pode prender
                self.pm1 = 1 ##pode mais 
                self.n -= 1
                self.p1is += 1

                destinos = {
                    1:  (240,  4),
                    2:  (350,  4),
                    3:  (460,  4),
                    4:  (570,  4),
                    5:  (700,  4),
                    6:  (800,  4),
                    7:  (910,  4),
                    8:  (1020, 4),
                    9:  (1140, 4),
                    10: (1140, 72),
                    11: (1140, 144),
                    12: (1140, 216),
                    13: (1140, 280),
                    14: (1140, 352),
                    15: (1140, 424),
                    16: (1020, 424),
                    17: (910,  424),
                    18: (800,  424),
                    19: (700,  424),
                    20: (570,  424),
                    21: (460,  424),
                    22: (350,  424),
                    23: (240,  424),
                    24: (120,  424),
                    25: (120,  352),
                    26: (120,  280),
                    27: (120,  216),
                }

                if self.p1is in destinos:
                    ax, ay = destinos[self.p1is]
                    time.sleep(0.35)
                    self.mover_cavaleiro_para(ax, ay)

            self.movep1 = False
            self.vez = 2
            pygame.event.clear()
            self.pode_jogar = True ##volta a poder rolar dado

        if self.movep2:
            
            while self.n != 0:
                self.tv2 = 1
                self.cv2 = 1
                self.pp2 = 1
                self.pm2 = 1
                self.n -= 1
                self.p2is += 1

                destinos = {
                    1:  (240,  35),
                    2:  (350,  35),
                    3:  (460,  35),
                    4:  (570,  35),
                    5:  (700,  35),
                    6:  (800,  35),
                    7:  (910,  35),
                    8:  (1020, 35),
                    9:  (1140, 35),
                    10: (1140, 103),
                    11: (1140, 175),
                    12: (1140, 247),
                    13: (1140, 311),
                    14: (1140, 383),
                    15: (1140, 455),
                    16: (1020, 455),
                    17: (910,  455),
                    18: (800,  455),
                    19: (700,  455),
                    20: (570,  455),
                    21: (460,  455),
                    22: (350,  455),
                    23: (240,  455),
                    24: (120,  455),
                    25: (120,  383),
                    26: (120,  311),
                    27: (120,  247),
                }

                if self.p2is in destinos:
                    ax, ay = destinos[self.p2is]
                    time.sleep(0.35)
                    self.mover_ogro_para(ax, ay)

            self.movep2 = False
            self.vez = 1
            pygame.event.clear()
            self.pode_jogar = True ##volta a poder rolar dado

        if self.efeitos:
            
            ## PERCA DE VIDA
            
            if (self.p1x == 350 and self.p1y == 4 or self.p1x == 1140 and self.p1y == 4 or self.p1x == 1140 and self.p1y == 424 or self.p1x == 570 and self.p1y == 424 or self.p1x == 120 and self.p1y == 424) and self.tv1 == 1:
                self.vidap1+=3
                self.tela.blit(self.vidasp1[self.vidap1], (400, 275))
                pygame.display.flip()
                self.animacao_danocava()
                
                time.sleep(1)

                
                self.tv1 = 0 ##pode tirar vida, 0 nao 1 sim
                
            if (self.p2x == 350 and self.p2y == 35 or self.p2x == 1140 and self.p2y == 35 or self.p2x == 1140 and self.p2y == 455 or self.p2x == 570 and self.p2y == 455 or self.p2x == 120 and self.p2y == 455) and self.tv2 == 1:
                self.vidap2+=3
                self.tela.blit(self.vidasp2[self.vidap2], (700, 275))
                pygame.display.flip()
                self.animacao_danogro()
                
                
                self.tv2 = 0
            
            ## MORRENDO
            if self.vidap1 == 5 or self.vidap1 == 6 or self.vidap1 == 7:
                self.tela.blit(self.vida6, (400, 275)) 

                self.img_vidap1 = (self.vidasp1[self.vidap1])
                self.img_vidap2 = (self.vidasp2[self.vidap2])
                self.animacao_morte_cavaleiro()
                self.p1is=0; self.p1x= 120; self.p1y = 4

                self.vidap1 = 0
            
            if self.vidap2 == 5 or self.vidap2 == 6 or self.vidap2 == 7:
                self.tela.blit(self.vida6, (700, 275)) 

                self.img_vidap1 = (self.vidasp1[self.vidap1])
                self.img_vidap2 = (self.vidasp2[self.vidap2])

                self.animacao_morte_ogro()
                self.p2is=0; self.p2x= 120; self.p2y = 35  
                
                self.vidap2 = 0

            


            ## ganho de vida

            if (self.p1x == 460 and self.p1y ==4 or self.p1x == 1140 and self.p1y==72 or self.p1x == 1020 and self.p1y==424 or self.p1x == 460 and self.p1y==424 or self.p1x == 120 and self.p1y== 280) and self.cv1 == 1:
                ## sprites de vida
                self.cv1 = 0
                if self.vidap1 !=0:
                    self.vidap1-=1
                    self.tela.blit(self.vidasp1[self.vidap1], (400, 275))
                    pygame.display.flip()
                    time.sleep(1)

            if (self.p2x == 460 and self.p2y ==35 or self.p2x == 1140 and self.p2y==103 or self.p2x == 1020 and self.p2y==455 or self.p2x == 460 and self.p2y==455 or self.p2x == 120 and self.p2y== 311) and self.cv2 == 1:
                ## sprites de vida
                self.cv2 = 0
                if self.vidap2 !=0:
                    self.vidap2-=1
                    self.tela.blit(self.vidasp2[self.vidap2], (700, 275))
                    pygame.display.flip()
                    time.sleep(1)
                    
            ## Buraco NEGRO
            if self.p1x == 1140 and self.p1y == 144:
                    self.p1is = 0; self.p1x = 120; self.p1y = 4
            if self.p2x == 1140 and self.p2y == 175:
                    self.p2is = 0; self.p2x = 120; self.p2y = 35

            ## RODADA SEM JOGAR
            if (self.p1x == 910 and self.p1y == 4 or self.p1x == 800 and self.p1y == 424 or self.p1x == 120 and self.p1y == 352) and self.pp1 == 1:
                self.preso1 = True
            if (self.p2x == 910 and self.p2y == 35 or self.p2x == 800 and self.p2y == 455 or self.p2x == 120 and self.p2y == 383) and self.pp2 == 1:
                self.preso2 = True

            ## MAIS UMA RODADA
            if (self.p1x == 700 and self.p1y == 4 or self.p1x == 1140 and self.p1y == 216 or self.p1x == 240 and self.p1y == 424) and self.pm1 == 1:
                self.pm1 = 0
                self.vez = 1
            if (self.p2x == 700 and self.p2y == 35 or self.p2x == 1140 and self.p2y == 247 or self.p2x == 240 and self.p2y == 455) and self.pm2 == 1:
                self.pm2 = 0
                self.vez = 2

            ## VENCER

            if self.p1x == 120 and self.p1y == 216 and self.anim1 == 0:
                self.img_victory = self.venc1
                self.vencedor = "PLAYER 1"
                self.jogo = False
                self.img_tranout = self.venc1
                self.transicao_in()
                self.tranout = True
                self.vitoria = True
                
            if self.p2x == 120 and self.p2y == 247 and self.anim2 == 0:
                self.img_victory = self.venc2
                self.vencedor = "PLAYER 2"
                self.jogo = False
                self.img_tranout = self.venc2
                self.transicao_in()
                self.tranout = True
                self.vitoria = True







            self.img_vidap1 = (self.vidasp1[self.vidap1])
            self.img_vidap2 = (self.vidasp2[self.vidap2])
            self.desenhar()


            







            
            
            
    #CÓDIGO KONAMI
    #quem usar ganha o jogo automaticamente
    def konami_code(self):
        if self.vez == 1:
            self.img_victory = self.venc1
            self.vencedor = "PLAYER 1"
            self.jogo = False
            self.img_tranout = self.venc1
            self.vitoria = True
        elif self.vez == 2:
            self.img_victory = self.venc2
            self.vencedor = "PLAYER 2"
            self.jogo = False
            self.img_tranout = self.venc2
            self.transicao_in()
            self.tranout = True
            self.vitoria = True     
    
    def girar_dado(self):
        print("rolar",self.vez)
        print("girou dado")
        for i in range(20):

            self.relogio.tick(120)

            face = self.sprites_dados[randint(0, 5)]
            tamanho = 80 + (i % 3) * 20
            face_animada = pygame.transform.scale(face, (tamanho, tamanho))
            self.desenhar()
            if self.vez == 2:
                self.tela.blit(face_animada, (720, 340))
            else:
                self.tela.blit(face_animada, (430, 340))
            pygame.display.flip()

        self.n = randint(1, 6)
        ##self.n = 2
        

        self.resultado_dado = self.sprites_dados[self.n - 1]
        
        print("saiu dado")
    
        

    def girar_dado_player1(self):

        for i in range(20):

            self.relogio.tick(8)

            face = self.sprites_dados[randint(0, 5)]
            tamanho = 80 + (i % 3) * 20
            face_animada = pygame.transform.scale(face, (tamanho, tamanho))

            self.desenhar()

            self.tela.blit(face_animada, (280, 400))
            pygame.display.flip()

        self.n1 = randint(1, 6)
        
        self.resultado_dadop1 = self.sprites_dados[self.n1 - 1]
        pygame.event.clear() ##limpa a fila de eventos, pra não guardar múltiplas tentativas de rolagem


    def girar_dado_player2(self):

        for i in range(20):

            self.relogio.tick(8)

            face = self.sprites_dados[randint(0, 5)]
            tamanho = 80 + (i % 3) * 20
            face_animada = pygame.transform.scale(face, (tamanho, tamanho))

            self.desenhar()
            self.tela.blit(face_animada, (920, 400))
            pygame.display.flip()

        self.n2 = randint(1, 6)
        
        self.resultado_dadop2 = self.sprites_dados[self.n2 - 1]
        pygame.event.clear() ##limpa a fila de eventos, pra não guardar múltiplas tentativas de rolagem


    def temporizador(self):
        self.relogio.tick(10)
        self.t +=1

    def transicao_in(self):
        
        for i in range(30):
            self.relogio.tick(220)
            pygame.draw.rect(
                self.tela,
                (0, 0, 0),
                (0, 820 - i * 30, 1331, 30)
            )

            pygame.display.flip()

    def transicao_out(self):
        
        
        for i in range(30):
            if self.img_tranout == self.cmcw or self.img_tranout == self.cmco:
                self.tela.blit(self.img_tranout, (0,-10))
            elif self.img_tranout == self.pagempate:
                self.tela.blit(self.img_tranout, (0,-75))
            else:
                self.tela.blit(self.img_tranout, (0,0))
            self.relogio.tick(220)
            
            pygame.draw.rect(
                self.tela,
                (0, 0, 0),
                (0, 0 + i * 25, 1331, 600)
            )
           
            pygame.display.flip()


    





    def desenhar(self): ## Apenas desenho
        
        if self.no_menu:

            self.tela.fill((0,0,0))
            
            self.tela.blit(self.menu, (0,0))
           

        elif self.escolha_personagem:

            self.tela.fill((255, 255, 255))

            

            
            self.tela.blit(self.escolha, (0,0))


            
        

            if not self.resultado_dadop1:
                
                self.tela.blit(self.seta, (450, 440))

            elif not self.resultado_dadop2:
                
                self.tela.blit(self.seta, (1060, 440))

            else:
                pygame.draw.rect(
                self.tela,
                (0, 0, 0),
                (550, 475, 200, 60)
                )
                self.tela.blit(self.contbut, (550, 475))
                self.tela.blit(self.seta,(770, 480))
                
            # DADO PLAYER 1
            if self.resultado_dadop1:

                self.tela.blit(self.resultado_dadop1, (280, 400))

            # DADO PLAYER 2
            if self.resultado_dadop2:

                self.tela.blit(self.resultado_dadop2, (920, 400))

        elif self.personagem_comeca:


            if self.playercmc == "JOGADOR 1":
                self.vez = 1
                self.tela.blit(self.cmcw,(0,-10))
        
            else:
                self.vez = 2
                self.tela.blit(self.cmco,(0,-10))
            
            self.tela.blit(self.contbut, (1050, 545))
            self.tela.blit(self.seta,(1270, 550))
          
        elif self.empate:
           self.tela.blit(self.pagempate,(0,-75)) 

        elif self.jogo:
            
            
            self.tela.blit(self.background, (0, 0))
        
           





            ## trocar a ordem de sobreposição dos personagens
            if self.p1y < self.p2y:
                if not self.cava_animando:
                   
                    self.idle_timer += 1
                    if self.idle_timer >= 1:
                    	self.idle_timer = 0
                    	self.frame_idle_cava = (self.frame_idle_cava +1)% len(self.idle_cava)
                    frame = pygame.transform.scale(self.idle_cava[self.frame_idle_cava], (50,300))
                    
                    if self.p1y > 352:
                        self.tela.blit(pygame.transform.flip(frame, True, False), (self.p1x, self.p1y))
                    else:
                        self.tela.blit(frame, (self.p1x, self.p1y))
                
                    
                if not self.ogro_animando:
                    self.idle_timer_orc += 1
                    if self.idle_timer_orc>=1:
                    	self.idle_timer_orc = 0
                    	self.frame_idle_orc = (self.frame_idle_orc+1)% len (self.idle_ogro)
                    frame2 = pygame.transform.scale(self.idle_ogro[self.frame_idle_orc],(70,300))
    
                    if self.p2y > 352:
                        self.tela.blit(pygame.transform.flip(frame2, True, False), (self.p2x, self.p2y))
                    else:
                        self.tela.blit(frame2, (self.p2x, self.p2y))

            else:

                if not self.ogro_animando:
                    self.idle_timer_orc += 1
                    if self.idle_timer_orc >=1:
                    	self.idle_timer_orc = 0
                    	self.frame_idle_orc = (self.frame_idle_orc+1)% len (self.idle_ogro)
                    frame2 = pygame.transform.scale(self.idle_ogro[self.frame_idle_orc],(70,300))
                    
                    if self.p2y > 352:
                        self.tela.blit(pygame.transform.flip(frame2, True, False), (self.p2x, self.p2y))
                    else:
                        self.tela.blit(frame2, (self.p2x, self.p2y))


                else:
                    frame = pygame.transform.scale(self.idle_cava[self.frame_idle_cava], (50,300))
                    frame2 = pygame.transform.scale(self.idle_ogro[self.frame_idle_orc],(70,300))
                    if self.p2y > 352:
                        self.tela.blit(pygame.transform.flip(frame2, True, False), (self.p2x, self.p2y))
                    else:
                        self.tela.blit(frame2, (self.p2x, self.p2y))

                if not self.cava_animando:
                    self.idle_timer += 1
                    if self.idle_timer >= 1:
                    	self.idle_timer = 0
                    	self.frame_idle_cava = (self.frame_idle_cava +1)% len(self.idle_cava)
                    frame = pygame.transform.scale(self.idle_cava[self.frame_idle_cava], (50,300))
                    
                    if self.p1y > 352:
                        self.tela.blit(pygame.transform.flip(frame, True, False), (self.p1x, self.p1y))
                    else:
                        self.tela.blit(frame, (self.p1x, self.p1y))
                    




            self.temporizador()
            if self.t > 25:
                self.tela.blit(self.img_vidap1, (400, 275))
                self.tela.blit(self.img_vidap2, (700, 275))
                if self.vez == 2 and self.cava_animando == False and self.ogro_animando == False:
                    self.tela.blit(self.seta, (890, 380))
                if self.vez == 1 and self.cava_animando == False and self.ogro_animando == False:
                    self.tela.blit(self.seta, (600, 380))
                if self.resultado_dado:
                    if self.vez == 2 and self.cava_animando == False and self.ogro_animando == False:
                        self.tela.blit(self.resultado_dado, (720, 340))
                        pygame.display.flip()
                        time.sleep(1)
                        
                        
                        
                    else:
                        self.tela.blit(self.resultado_dado, (430, 340))
                        pygame.display.flip()
                        time.sleep(1)
                        

                    if self.preso1 == True and self.vez == 1:
                        self.vez = 2
                        print("vez 2")
                        self.preso1 = False
                        self.pp1 = 0 ##pode prender o player1
                    if self.preso2 == True and self.vez == 2:
                        self.vez = 1
                        print("vez 1")
                        self.preso2 = False
                        self.pp2 = 0


                    if self.vez == 1:
                        self.resultado_dado = ""
                        self.movep1 = True
                        print("movep1")
                    if self.vez == 2:
                        self.movep2 = True
                        print("movep2")
                        self.resultado_dado = ""

        elif self.vitoria:
            pygame.mixer.music.stop()
            
            if self.vencedor == "PLAYER 1" and self.anim1 == 0:
                self.anim1 = 1
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(2)
                self.img_victory = self.perdp2_2.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.06)
                self.img_victory = self.perdp2_3.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp2_4.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp2_5.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp2_6.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
            if self.vencedor == "PLAYER 1":
                self.tela.blit(self.img_victory, (0,0))
                self.tela.blit(self.img_vidap1, (200, 520))
                self.tela.blit(self.img_vidap2, (970, 520))
            if self.vencedor != "PLAYER 1" and self.anim2 == 0:
                self.anim2 = 1
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(2)
                self.img_victory = self.perdp1_2.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.06)
                self.img_victory = self.perdp1_3.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp1_4.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp1_5.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
                self.img_victory = self.perdp1_6.copy()
                self.tela.blit(self.img_victory, (0,0))
                pygame.display.flip()
                time.sleep(0.04)
            if self.vencedor != "Player 1":
                self.tela.blit(self.img_victory, (0,0))
                self.tela.blit(self.img_vidap1, (200, 520))
                self.tela.blit(self.img_vidap2, (970, 520))
            for evento in pygame.event.get():    
                if evento.type == KEYDOWN:
                    #teclado
                    if evento.key in [K_SPACE,K_RETURN, K_KP_ENTER]:

                        self.vitoria = False
                        self.no_menu = True
                        self.transicao_in()
                        self.tranout = True
                        self.img_tranout = self.menu
                        meu_jogo = JogoDados()
                        meu_jogo.loop_principal()
                        
                    #mouse
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.vitoria = False
                        self.no_menu = True
                        self.transicao_in()
                        self.tranout = True
                        self.img_tranout = self.menu
                        meu_jogo = JogoDados()
                        meu_jogo.loop_principal()
        




        if self.tranout == True and self.vitoria == False:
            self.transicao_out()
            self.tranout = False
    

        pygame.display.flip()

    def loop_principal(self):

        while self.rodando:

            self.tratar_eventos() 
            
            self.desenhar()

        pygame.quit()

        exit()

if __name__ == "__main__":

    meu_jogo = JogoDados()

    meu_jogo.loop_principal()