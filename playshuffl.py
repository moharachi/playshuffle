playlist = {}


libreria = {"California_Uber_Alles.mp3": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }
import random



def seleccionaCancionRandom(libreria):
	import random
	assert isinstance(libreria, dict),"la libreria no es diccionario"
	longitud = len(libreria)
	dict_keys = libreria.keys()
	tituloCancion = random.choice(list(dict_keys))
	assert len(libreria)==longitud,"longitud ha cambiado"
	assert tituloCancion in libreria,"la cancion no esta en la libreria"
	return tituloCancion
##CASOS TEST
##for i in range(1, 21):
##	print (seleccionaCancionRandom(libreria))



def iniciarPlayList(tituloCancion):
#pasar playlist
#agregar la cancionrandom

	print(seleccionaCancionRandom)

#assert while len(playlist) != libreria


 
##CASO TEST

#chequear numeroCancion == diccionario

#chequear que la cancion no esta dentro del diccionario
