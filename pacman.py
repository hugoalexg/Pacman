
#Releitura do jogo do PAC-MAN feito por Hugo A. Gabardo
import pygame, random
from pygame.locals import *

#definição inicial da parede 30x21
#0 - caminho com frutas
#1 - parede
#2 - pacman
#4 - caminho sem frutas
#5 - coração (vidas)
#9 - utilizado na incialização, marcando regioes que nao podem ser parede
def init_matrix():
	wall_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
				   [1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 9, 1, 1, 9, 9, 1, 1, 9, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 9, 9, 9, 9, 1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 9, 9, 9, 9, 1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 9, 1, 1, 9, 9, 1, 1, 9, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
				   [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5, 5, 5, 5, 1],
				   [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
				   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	return wall_matrix
			   
class Pacman:
	def __init__(self, pacman_skin_path, pacman_skin_path2, pacman_position):
		self.skin = pygame.image.load(pacman_skin_path)
		self.skin2 = pygame.image.load(pacman_skin_path2)
		self.pos = pacman_position
		self.start_pos = pacman_position
		self.life_counter = 5
		self.pacman0 = pygame.transform.rotate(self.skin, 0)
		self.pacman90 = pygame.transform.rotate(self.skin, 90)
		self.pacman180 = pygame.transform.rotate(self.skin, 180)
		self.pacman270 = pygame.transform.rotate(self.skin, 270)
		self.timer1 = pygame.time.get_ticks()
		self.died = False
		self.black_block = pygame.image.load("images\\blackblock.png") 

	def return_start(self): #funçao que retorna a posição inicial
		self.pos = self.start_pos

	def lost_life(self): # diminui uma vida
		self.life_counter -= 1

	def return_lives(self): #volta ao numero inicial de vidas
		self.life_counter = 5

	def pacman_died(self):
		self.died = True

	def draw_pacman(self):
		if pygame.time.get_ticks() < (self.timer1 + 200):	
			screen.blit(self.skin, self.pos)
		else:
			screen.blit(self.skin2, self.pos)
		if pygame.time.get_ticks() > (self.timer1 + 250):
			self.timer1 = pygame.time.get_ticks()

	def died_effect(self):
		pygame.time.wait(1000)
		for i in range(0,4):
			screen.blit(self.skin, self.pos)
			pygame.display.update()
			pygame.time.wait(250)
			screen.blit(self.black_block, self.pos)
			pygame.display.update()
			pygame.time.wait(250)		
		self.died = False
	
	def pacman_move(self, matrix, direction):
		matrix[int(self.pos[1]/30)] [int(self.pos[0]/30)] = 4

		if direction == K_UP and matrix[int(pacman.pos[1]/30) - 1] [int(pacman.pos[0]/30)] != 1:
			self.pos = (self.pos[0], self.pos[1] - 30)
			self.skin = self.pacman90

		elif direction == K_DOWN and matrix[int(pacman.pos[1]/30) + 1] [int(pacman.pos[0]/30)] != 1:
			self.pos = (self.pos[0], self.pos[1] + 30)
			self.skin = self.pacman270

		elif direction == K_LEFT and matrix[int(pacman.pos[1]/30)] [int(pacman.pos[0]/30) - 1] != 1:
			self.pos = (self.pos[0] - 30, self.pos[1])
			self.skin = self.pacman180

		elif direction == K_RIGHT and matrix[int(pacman.pos[1]/30)] [int(pacman.pos[0]/30) + 1] != 1:
			self.pos = (self.pos[0] + 30, self.pos[1])
			self.skin = self.pacman0

		matrix[int(self.pos[1]/30)] [int(self.pos[0]/30)] = 2
		return matrix
			
#função que adiciona paredes aleatorias as ja existentes
def rand_wall(matrix):
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			if matrix[y][x] == 0:
				var = random.randint(0,50)
				if var < 15 and x%2 == 0:
					matrix[y][x] = 1
	return matrix

class Monster: #classe que define as caracteriticas dos monstros
	def __init__(self, skin_path, position):
		self.skin = pygame.image.load(skin_path)
		self.pos = position
		self.start_pos = position
		self.speed_monster = 4	#velocidade dos monstros 5-muito lento 4-lento 3-medio 2-rapido 1-insano
		self.counter = 0

	def return_start(self): #funçao que retorna a posição inicial
		self.pos = self.start_pos

	#função que auxilia da movimentação dos monstros
	def monster_move_rules(self, dir0, dirp90, dirm90, dir180, dirwall0, dirp90wall, dirm90wall, dir180wall):		
		var = random.randint(0,50)
		if dirwall0 != 1: #se nao tiver parede na frente
			self.pos = dir0
		elif dirp90wall != 1 and dirm90wall != 1: #se nao tiver parede em nenhum dos lados
			if var%2 == 0: #move aleatoriamente para um lado ou outro
				self.pos = dirp90
			else:
				self.pos = dirm90
		elif dirp90wall != 1: #se nao tem parede em um dos lados
			self.pos = dirp90
		elif dirm90wall != 1: #se nao tem parede no outro lado
			self.pos = dirm90
		else: #se tiver parede na frente e dos lados, move para tras
			self.pos = dir180 	

	#função que controla a posição dos monstros
	def monster_move(self, pacman_pos, matrix):

		if self.counter == self.speed_monster:		

			self.counter = 0

			UP = (self.pos[0], self.pos[1] - 30)
			DOWN = (self.pos[0], self.pos[1] + 30)
			LEFT = (self.pos[0] - 30, self.pos[1])
			RIGHT = (self.pos[0] + 30, self.pos[1])

			WALL_UP = matrix[int(self.pos[1]/30) - 1][int(self.pos[0]/30)]
			WALL_DOWN = matrix[int(self.pos[1]/30) + 1][int(self.pos[0]/30)]
			WALL_LEFT = matrix[int(self.pos[1]/30)][int(self.pos[0]/30) - 1]
			WALL_RIGHT = matrix[int(self.pos[1]/30)][int(self.pos[0]/30) + 1]

			var2 = random.randint(0,50)

			if var2%2 == 0: #mover coordenada X primeiro
				if pacman_pos[0] < self.pos[0]: #se posição x do monstro maior que do pacman, mover para esquerda
					self.monster_move_rules(LEFT,UP,DOWN,RIGHT,WALL_LEFT,WALL_UP,WALL_DOWN,WALL_RIGHT)
				elif pacman_pos[0] > self.pos[0]: #se posição x do monstro menor que do pacman
					self.monster_move_rules(RIGHT,UP,DOWN,LEFT,WALL_RIGHT,WALL_UP,WALL_DOWN,WALL_LEFT)
				else: #se coordenada X for igual, move Y
					if pacman_pos[1] < self.pos[1]: #se posição y do monstro maior que do pacman
						self.monster_move_rules(UP,LEFT,RIGHT,DOWN,WALL_UP,WALL_LEFT,WALL_RIGHT,WALL_DOWN)
					elif pacman_pos[1] > self.pos[1]: #se posição y do monstro menor que do pacman
						self.monster_move_rules(DOWN,LEFT,RIGHT,UP,WALL_DOWN,WALL_LEFT,WALL_RIGHT,WALL_UP)
			else: #mover coordenada Y primeiro
				if pacman_pos[1] < self.pos[1]: #se posição y do monstro maior que do pacman
					self.monster_move_rules(UP,LEFT,RIGHT,DOWN,WALL_UP,WALL_LEFT,WALL_RIGHT,WALL_DOWN)
				elif pacman_pos[1] > self.pos[1]: #se posição y do monstro menor que do pacman
					self.monster_move_rules(DOWN,LEFT,RIGHT,UP,WALL_DOWN,WALL_LEFT,WALL_RIGHT,WALL_UP)
				else: #se coordenada Y for igual, move X
					if pacman_pos[0] < self.pos[0]: #se posição x do monstro maior que do pacman, mover para esquerda
						self.monster_move_rules(LEFT,UP,DOWN,RIGHT,WALL_LEFT,WALL_UP,WALL_DOWN,WALL_RIGHT)		
					elif pacman_pos[0] > self.pos[0]: #se posição x do monstro menor que do pacman
						self.monster_move_rules(RIGHT,UP,DOWN,LEFT,WALL_RIGHT,WALL_UP,WALL_DOWN,WALL_LEFT)

		self.counter += 1			

def dot_count(matrix):
	dot_counter = 0
	for y in range(len(wall_matrix)):
		for x in range(len(wall_matrix[y])):
			if wall_matrix[y][x] == 0:
				dot_counter += 1
	return dot_counter


pygame.init()
#coordenada de (30, 30) até (870, 690)
#fazer parede externa de 30x21, deixar 3 ultimas linhas para painel
screen = pygame.display.set_mode((900, 720))
pygame.display.set_caption('PAC-MAN by Hugo')

#criação e inicialização do pacman
pacman = Pacman("images\\pacman.png","images\\pacman_c.png",( 30, 30))

#criação e inicialização de uma lista de monstros
monster_list = [Monster("images\\Pinky.png",( 390, 270)), 
				Monster("images\\Blinky.png",( 480, 270)),
				Monster("images\\Clyde.png",( 390, 330)),
				Monster("images\\Inky.png",( 480, 330))]

#inicialização de lista com as texturas da parede
wall_block = [pygame.image.load("images\\bluepir.png"),	
			 pygame.image.load("images\\greywall.png"),
			 pygame.image.load("images\\classicwall.png"),
			 pygame.image.load("images\\bluewall.png"),
			 pygame.image.load("images\\firewall.png")]

#pontos que o pacman ira comer
dot = pygame.image.load("images\\gold_dot.png")
life = pygame.image.load("images\\heart.png")

#gerar paredes aleatorias no labirinto
wall_matrix = init_matrix()
wall_matrix = rand_wall(wall_matrix)

#inicialização do timer
clock = pygame.time.Clock()

#inicialização das variaveis do jogo
dot_counter = 0 #contador dos pontos no cenario
game_over = False
win_game = False
stage = 1 #contador da fase do pacman
                      
pygame.font.init() #inicializando fontes  

#contagem de quantos pontos tem no cenario inicial
score_total = dot_count(wall_matrix)

#laço principal do jogo
while (not game_over) and (not win_game):

	clock.tick(16)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

	if pacman.died: #se morreu, volta a posição inicial e pisca na tela
		pacman.died_effect()

	screen.fill((0,0,0))
	 
	#movimentação do pac-man
	if event.type == KEYDOWN:
		pacman.pacman_move(wall_matrix, event.key)
		
	#imprime o pac-man na tela
	pacman.draw_pacman()
	
	dot_counter = 0
	#imprimi a parede e elementos do cenario
	for y in range(len(wall_matrix)):
		for x in range(len(wall_matrix[y])):
			if wall_matrix[y][x] == 1:
				screen.blit(wall_block[stage-1], (30*x,30*y))
			elif wall_matrix[y][x] == 0:
				screen.blit(dot, (30*x,30*y))
				dot_counter += 1
			elif wall_matrix[y][x] == 5:
				screen.blit(life, (30*x,30*y))

	#movimentação dos monstrons
	for i in range(len(monster_list)):
		monster_list[i].monster_move(pacman.pos, wall_matrix)	

	#imprime os monstros na tela
	for i in range(len(monster_list)):
		screen.blit(monster_list[i].skin, monster_list[i].pos)
	
	#imprimindo pontuação e fase na tela
	fontesys = pygame.font.SysFont("arialblack", 18)	
	text_score = fontesys.render("SCORE: " + str(score_total-dot_counter) + "/" + str(score_total), 1, (255,255,255)) 
	fontesys = pygame.font.SysFont("arialblack", 24)	
	text_stage = fontesys.render("STAGE - " + str(stage), 1, (255,255,255)) 
	screen.blit(text_score,(30,630))
	screen.blit(text_stage, text_stage.get_rect(center=(450,660)))  

	#verifica se monstros mataram o pac-man
	for i in range(len(monster_list)):
		if monster_list[i].pos == pacman.pos:#se algum monstro matou, voltam as posiçoes iniciais e perde uma vida			
			wall_matrix[int(pacman.pos[1]/30)] [int(pacman.pos[0]/30)] = 4
			pacman.return_start()
			wall_matrix[int(pacman.pos[1]/30)] [int(pacman.pos[0]/30)] = 2
			for j in range(len(monster_list)):
				monster_list[j].return_start()
			pacman.lost_life()
			pacman.pacman_died()
			wall_matrix[int(630/30)][int((840-(pacman.life_counter*30))/30)] = 9 #apaga um coração
			if pacman.life_counter < 0: #e as vidas acabam, gameover
				game_over = True
    
    #CHEAT - se apertar TAB passa de fase sem terminar de comer as frutas
	if event.type == KEYDOWN:
		if event.key == K_TAB:
			dot_counter=0

    #passa para a proxima fase
	if dot_counter == 0:
		stage += 1 
		background = pygame.image.load("images\\background.png")
		screen.blit(background, background.get_rect(center=(450,310)))
		game_over_font = pygame.font.SysFont("arialblack", 60)
		game_over_screen = game_over_font.render('NEXT STAGE...', True, (255, 255, 255))
		screen.blit(game_over_screen, game_over_screen.get_rect(center=(450,310)))
		pygame.display.update()
		pygame.time.wait(2000)		
		pacman.return_start()
		for j in range(len(monster_list)):
			monster_list[j].return_start()
		var = 0 
		pacman.return_lives()
		wall_matrix = init_matrix()
		wall_matrix = rand_wall(wall_matrix)
		score_total = dot_count(wall_matrix)

	#zerou o jogo	
	if stage > 5:
		win_game = True

	#pygame.display.update()
	pygame.display.flip()

#tela de game-over
while game_over:
	background = pygame.image.load("images\\background.png")
	screen.blit(background, background.get_rect(center=(450,310)))
	game_over_font = pygame.font.SysFont("arialblack", 60)
	game_over_screen = game_over_font.render('GAME OVER', True, (255, 255, 255))
	screen.blit(game_over_screen, game_over_screen.get_rect(center=(450,310)))
	pygame.display.update()
	pygame.time.wait(500)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

while win_game:
	screen.fill((0,0,0))
	background = pygame.image.load("images\\happy_pacman.png")
	screen.blit(background, background.get_rect(center=(450,340)))
	game_over_font = pygame.font.SysFont("arialblack", 60)
	game_over_screen = game_over_font.render('GREAT! YOU WIN!', True, (255, 255, 255))
	screen.blit(game_over_screen, game_over_screen.get_rect(center=(450,60)))
	pygame.display.update()
	pygame.time.wait(500)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()