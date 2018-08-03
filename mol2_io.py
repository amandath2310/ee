


def leer_mol2(nombre):

	# Leer archivo mol2
	contenido = ''

	with open (nombre, 'r') as f:
		contenido = f.readlines() 

	# Hallar atomos y enlaces
	at = False
	atomos = []
	en = False
	enlaces = []

	for l in contenido:
		if 'ATOM' in l:
			at = True
			en = False
		if 'BOND' in l:
			at = False
			en = True
		if at:
			atomos.append(l)
		elif en:
			enlaces.append(l)

	# Quitar @<TRIPOS>ATOM y @<TRIPOS>BOND, y la linea nueva \n
	atomos = [ i[:-1] for i in atomos[1:] ]
	enlaces = [ i[:-1] for i in  enlaces[1:] ]

	# Separar cada linea por espacios en blanco
	atomos = [ j.split(' ') for j in atomos ]
	enlaces = [j.split(' ') for j in enlaces ] 

	# Eliminar espacios en blanco
	atomos = map( lambda x: [k for k in x if k != ''], atomos)
	enlaces = map( lambda x: [k for k in x if k != ''], enlaces)

	# Extraer la informacion de cada atomo y enlaces
	atomos = map( lambda e: [int(e[0]), e[1], float(e[2]), float(e[3]), float(e[4]),
							float(e[-1])], atomos)
	enlaces = map( lambda x: [int(e) for e in x[:-1]] + [x[-1]], enlaces)

	return atomos, enlaces

# Crear clase atomo
class Atomo:
	
	def __init__(self, numero = 1, simbolo = 'H', carga = 0, peso = 1.0079, coordenadas = [0, 0, 0]):
		self.numero = numero
		self.simbolo = simbolo
		self.carga = carga
		self.peso = peso
		self.coordenadas = coordenadas

	def __repr__(self):
		arg = '< ' + self.simbolo + ' >  ' + '\nX: ' + str(self.coordenadas[0]) + '\nY: ' + str(self.coordenadas[1]) + '\nZ: ' + str(self.coordenadas[2]) + '\nCarga: ' + str(self.carga)
		return arg

# Crear clase molecula
class Molecula:

	def __init__(self, atomos = [Atomo(), Atomo(coordenadas=[1,0,0])], enlaces = [[0, 1, 1]]):
		self.atomos = atomos
		self.enlaces = enlaces