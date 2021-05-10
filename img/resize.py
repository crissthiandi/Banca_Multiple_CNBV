from PIL import Image
import os 

# Obtener los elementos de directorio img/
contenido = os.listdir("img/")
imagenes = []
for fichero in contenido:
        if fichero.endswith('.png'): # no es necesario checar si es file: os.path.isfile(os.path.join(ejemplo_dir, fichero)) and
                imagenes.append(fichero)

# leemos las imagenes imprimos tamaño original y final

for imagen in imagenes:
        file = Image.open("img/" + imagen)
        print(file.size)

        # ANTIALIAS filter (gives the highest quality)
        file = file.resize((30,30),Image.ANTIALIAS)
        file.save("img/test"+imagen,quality=95)
        # file.save("img/test"+imagen,optimize=True,quality=95)
