#Inicio de pygame
import pygame, sys, random, time
pygame.init()

#Tamaño de Ventana
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H
controlPreguntas = 0
#Crear ventana
screen = pygame.display.set_mode((W, H))
c = 0
#Fuente de letra
fuente = pygame.font.SysFont("Impact", 30)
fuenteVel =pygame.font.SysFont("Impact", 60)

#Tipo de fondo
fondoType = 2

#Definir FPS
clock = pygame.time.Clock()

#Definir colores
WHITE = (255,255,255)
CROMA = (16,15,33)

#Imagenes
Auto = pygame.image.load("Sprites/Camioneta.png")
piedra = pygame.image.load("Sprites/Piedra.png")
bkgd = pygame.image.load("Sprites/Paisaje-1.png").convert()
borrar = "Sprites/borrar.png"
play1 = pygame.image.load("Sprites/Play-1.png")
play2 = pygame.image.load("Sprites/Play-2.png")
option1 = pygame.image.load("Sprites/Options-1.png")
option2 = pygame.image.load("Sprites/Options-2.png")
shop1 = pygame.image.load("Sprites/Shop-1.png")
shop2 = pygame.image.load("Sprites/Shop-2.png")
menu = pygame.image.load("Sprites/Menu.png")
obstaculoP = "Sprites/Piedra.png"
obstaculoS = "Sprites/Barrera.png"

#Variables
escudo = 0
opcion = 0
contadorFrames = 0
autoX = 0
speedAutoX = 0
multiplicadorVelocidad = 2
y = 0

velocidad = 0
obstaculoX = 605
obstaculoY = -200

obstaculo2X = 585
obstaculo2Y = -500

speedX = 0
speedY = 0

colisionX = 620
velocidadLimit= 50
ir = 2

carril = 0
carril2 = 0


listaPreguntas1 = ["El que conduce un vehículo ¿qué documentación personal debe llevar consigo?: ",
					"Con carácter general, cuando nos encontramos con una señal de “PROHIBIDO ESTACIONAR"+ "\n" +"¿está permitido parar para subir o bajar pasajeros de un automóvil?",
					"Segun lo que surge del Art. 30 de la ley 24.449 de los que se enumeran, cual dispositivo"+ "\n" +" de seguridad debe contener como minimo un automotor",
					"En la caja de una camioneta pueden trasladarse: ",
					"La edad minima para obtener la licencia clase B es de:"]


listaRespuestas = [["A) La licencia de conductor es suficiente." ,"B) La licencia de conductor y su documento de identidad.", "C) La licencia de conductor, su documento de identidad y la cédula verde"]
					,["A. Si.", "B. No.", "C.  Según la hora."], ["A)2 personas." ,"B)Ninguna persona." ,"C)5 personas"],["A)2 personas."," B)Ninguna persona."," C)5 personas"],
					["A)21", "B)17", "C)16"]]

respuestasCorrectasList = ["3","1","2","2","2"]



#clases
class Puntaje():
	def __init__(self):
		self.puntajeInicial = 100
		self.imagenTextoPresent = fuente.render("puntaje: "+str(self.puntajeInicial),True, (200,200,200), (0,0,0) )
	def draw(self):
		self.imagenTextoPresent = fuente.render("puntaje: "+str(int(self.puntajeInicial)),True, (200,200,200), (0,0,0) )
		screen.blit(self.imagenTextoPresent, (600,50))

def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(fuente.render(l, True, (200,200,200),(0,0,0)), (x, y + fsize*i))
def preguntas():
	global imagenTextoPresent, opcion, controlPreguntas, respuestasRender, controlRespuestas, contadorFrames


	controly = 0
	controlRespuestas = 0
	#if len(listaPreguntas1[controlPreguntas]) >=80:
		#fuente = pygame.font.SysFont("Impact", 15)
	#else:
		#fuente = pygame.font.SysFont("Impact", 30)

	if contadorFrames >= 100:
		if controlPreguntas < len(listaPreguntas1):
			#imagenTextoPresent = fuente.render(str(listaPreguntas1[controlPreguntas]),True, (200,200,200), (0,0,0) )
			render_multi_line(str(listaPreguntas1[controlPreguntas]),50,100,30)

			for controlRespuestas in range(3):
				respuestasRender = fuente.render(str(listaRespuestas[controlPreguntas][controlRespuestas]),True, (200,200,200), (0,0,0) )
				screen.blit(respuestasRender, (50, 200+controly))
				controly += 50


		try:
			if respuestasCorrectasList[controlPreguntas] == "1":
				print("1")
				if opcion != 0 and opcion == 1:
					puntaje.puntajeInicial += 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0
				elif opcion != 0:
					puntaje.puntajeInicial -= 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0

			if respuestasCorrectasList[controlPreguntas] == "2":
				print("2")
				if opcion != 0 and opcion == 2:
					puntaje.puntajeInicial += 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0
				elif opcion != 0:
					puntaje.puntajeInicial -= 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0

			if respuestasCorrectasList[controlPreguntas] == "3":
				print("3")
				if opcion != 0 and opcion == 3:
					puntaje.puntajeInicial += 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0
				elif opcion != 0:
					puntaje.puntajeInicial -= 10
					opcion = 0
					controlPreguntas = controlPreguntas+1
					contadorFrames = 0
		except:
			pass
		#screen.blit(imagenTextoPresent, (50, 100))
	else:
		contadorFrames += 1



class Obstaculo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(obstaculoP)
		self.rect = self.image.get_rect()
		self.image.set_colorkey(CROMA)

	def update(self):
		global obstaculoX, obstaculoY
		obstaculoPosicion()
		obstaculoX += speedX
		obstaculoY += speedY
		obstaculo.rect.x = obstaculoX
		obstaculo.rect.y = obstaculoY

class Obstaculo2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(obstaculoS)
		self.rect = self.image.get_rect()
		self.image.set_colorkey(CROMA)

	def update(self):
		global obstaculo2X, obstaculo2Y
		obstaculoPosicion()
		obstaculo2X += speedX
		obstaculo2Y += speedY
		obstaculo2.rect.x = obstaculo2X
		obstaculo2.rect.y = obstaculo2Y

class Colision(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Sprites/colision.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

	def update(self):
		global colisionX
		colisionX += speedAutoX
		colision.rect.x = colisionX
		colision.rect.y = 500

#Funciones
class Señales(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Sprites/pngegg.png")
		self.image = pygame.transform.scale(self.image,(100,100))
		self.rect = self.image.get_rect()
	def update(self):
		señales.rect.x = 1150
		señales.rect.y = 50



def events():
	global ir, fondoType, opcion, velocidad, y
	#Cerrar ventana
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] == 1:
		velocidad += 0.05
	if keys[pygame.K_DOWN] == 1:
		velocidad -= 0.2
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#Eventos teclado
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if fondoType == 1:
					if ir == 1:
						ir = 2
					elif ir == 2:
						ir = 3

			if event.key == pygame.K_RIGHT:
				if fondoType == 1:
					if ir == 3:
						ir = 2
					elif ir == 2:
						ir = 1

			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			if event.key == pygame.K_1:
				opcion = 1
			if event.key == pygame.K_2:
				opcion = 2
			if event.key == pygame.K_3:
				opcion = 3
			if event.key == pygame.K_4:
				opcion = 4






		if event.type == pygame.KEYUP:
			if event.key == pygame.K_1:
				opcion = 0
			if event.key == pygame.K_2:
				opcion = 0
			if event.key == pygame.K_3:
				opcion = 0
			if event.key == pygame.K_4:
				opcion = 0
			pass


		#Eventos Mouse
		if event.type == pygame.MOUSEBUTTONDOWN:
			#Play
			if (mouseX > 900 and mouseX < 1258) and (mouseY > 130 and mouseY < 295) and fondoType == 2:
				objetosSpaw()
				fondoType = 1


		if event.type == pygame.MOUSEBUTTONUP:
			pass

def velocimetro():
	global velocidad
	velfont= str(int(velocidad*8))+" km/h"
	velocimetroRender = fuenteVel.render(velfont,False, (200,200,200))
	screen.blit(velocimetroRender, (1000, 600))

def auto():
	global autoX, speedAutoX
	if fondoType == 1:
		autoX += speedAutoX
		screen.blit(Auto,[autoX,0])

def scrolling():
	global y, speedY, velocidad
	if fondoType == 1:
		speedY = velocidad

		rel_y = y % bkgd.get_rect().height
		screen.blit(bkgd, (0, rel_y - bkgd.get_rect().height))
		if rel_y < W:
			screen.blit(bkgd, (0, rel_y))
		y += velocidad

def posicion():
	global autoX, speedAutoX, ir, velocidad
	if ir == 1:
		if autoX < 125:
			speedAutoX = 10
		else: speedAutoX = 0

	if ir == 2:
		if autoX != 0:
			if autoX < -125:
				speedAutoX = 10
			if autoX > 125:
				speedAutoX = -10
		else: speedAutoX = 0

	if ir == 3:
		if autoX > -125:
			speedAutoX = -10
		else: speedAutoX = 0
	if velocidad >= 10:
		velocidad = 10
	if velocidad <= -5:
		velocidad = -5
def obstaculoPosicion():
	global obstaculoX, obstaculoY, obstaculo2X, obstaculo2Y, carril, carril2

	if obstaculoY > 725:
		carril = random.randrange(9)
		obstaculoY = -200

		if carril == 1 or carril == 5 or carril == 9:
			obstaculoX = 730
		if carril == 8 or carril == 2 or carril == 6:
			obstaculoX = 605
		if carril == 4 or carril == 7 or carril == 3:
			obstaculoX = 480

	if obstaculo2Y > 725:
		obstaculo2Y = -400

		if carril2 == 1 or carril2 == 5 or carril2 == 9:
			obstaculo2X = 710
		if carril2 == 8 or carril2 == 2 or carril2 == 6:
			obstaculo2X = 585
		if carril2 == 4 or carril2 == 7 or carril2 == 3:
			obstaculo2X = 450

	if obstaculo2X == 710 and obstaculoX == 730 and obstaculoY < 725:
		obstaculo2X = 450
	elif obstaculo2X == 585 and obstaculoX == 605 and obstaculoY < 725:
		obstaculo2X = 710
	elif obstaculo2X == 450 and obstaculoX == 480 and obstaculoY < 725:
		obstaculo2X = 585

def objetosSpaw():
	#Agregar al Grupo
	allSpriteList.add(colision)

	obstaculo2List.add(obstaculo2)
	allObjectList.add(obstaculo2)

	obstaculoList.add(obstaculo)
	allObjectList.add(obstaculo)

cronometro = 1
def excesoVel():
	global cronometro, velocidadLimit, puntajeInicial
	cronometro += 1
	if velocidad > (velocidadLimit / 8):
		puntaje.puntajeInicial -= 0.1
	if cronometro > 600:
		velocidadLimit = 60
	if cronometro > 1200:
		velocidadLimit = 75

	velimitrender = fuenteVel.render(str(velocidadLimit),False, (251,44,0))
	pygame.draw.circle(screen, (251,44,0), [1030, 340], 60)
	pygame.draw.circle(screen, (255,255,255), [1030, 340], 50)

	screen.blit(velimitrender, (1000, 300))


def Menu():
	if fondoType == 2:
		screen.blit(menu, [0,0])
		screen.blit(option1, [0,15])


		#Play
		if (mouseX > 900 and mouseX < 1258) and (mouseY > 130 and mouseY < 295):
			screen.blit(play2, [0,-15])
		else: screen.blit(play1, [0,-15])

		#Shop
		if (mouseX > 946 and mouseX < 1216) and (mouseY > 375 and mouseY < 505):
			screen.blit(shop2, [0,5])
		else: screen.blit(shop1, [0,5])

		#Options
		if (mouseX > 965 and mouseX < 1203) and (mouseY > 575 and mouseY < 695):
			screen.blit(option2, [0,15])
		else: screen.blit(option1, [0,15])
def mouseLoc():
	global mouseY, mouseX, mousePos
	mousePos = pygame.mouse.get_pos()
	mouseX = mousePos[0]
	mouseY = mousePos[1]
	#return mouseY, mouseX


#Variables de Clases
obstaculo = Obstaculo()
colision = Colision()
obstaculo2 = Obstaculo2()
señales = Señales()
puntaje = Puntaje()

#Grupos
allSpriteList = pygame.sprite.Group()
obstaculoList = pygame.sprite.Group()
obstaculo2List = pygame.sprite.Group()
allObjectList = pygame.sprite.Group()


while True:
	events()


	mouseLoc()

	#print(f"X:{mouseX}, Y:{mouseY}")
	Menu()
	if fondoType == 1:
		scrolling()

		#Avanzar
		posicion()
		#Llamar a los updates dentro de las clases
		allSpriteList.update()
		allObjectList.update()
		rectcolision = [pygame.sprite.collide_rect(colision,obstaculo), pygame.sprite.collide_rect(colision,obstaculo2)]
		#Objetos que tocana al jugador
		obstaculoHitList = pygame.sprite.spritecollide(colision, obstaculoList, False)
		for obstaculo in obstaculoHitList:
			puntaje.puntajeInicial -= 20

		obstaculo2HitList = pygame.sprite.spritecollide(colision, obstaculo2List, False)
		for obstaculo2 in obstaculo2HitList:
			puntaje.puntajeInicial -= 20

		if rectcolision[0]:
			velocidad = 0
			obstaculoY -= 10
		if rectcolision[1]:
			velocidad = 0
			obstaculo2Y -= 10


		#if obstaculoY+5 in obstaculoHitList:
			#velocidad = 0



		puntaje.draw()
		preguntas()
		excesoVel()

	#Mostrar todos los sprites en pantalla
	allSpriteList.draw(screen)
	allObjectList.draw(screen)
	velocimetro()
	auto()

	#Actualizar Pantalla
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
