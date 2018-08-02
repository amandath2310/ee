
# Leer archivo mol2
contenido = ''

with open ('etano.mol2', 'r') as f:
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
enlaces = map( lambda x: [int(k) for k in x if k != ''], enlaces) # Convertir en enteros

atomos = map( lambda e: [int(e[0]), e[1], float(e[2]), float(e[3]), float(e[4]),
						float(e[-1])], atomos) # Extraer la informacion de cada atomo

print atomos,enlaces