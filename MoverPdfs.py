import os # Permite acceder a funcionalidades dependientes del sistema operativo, como manipulación de directorios, rutas de archivos.etc.
import shutil # Ofrece funciones para copiar, mover, eliminar y gestionar archivos y directorios de manera más conveniente que las funciones básicas de os.

# Se asigna la carpeta raiz donde se trabajara
CarpetaRaiz = "C:\\Users\\Usuario\\Desktop"
CarpetaPdf = os.path.join(CarpetaRaiz, "Pdfs")

# En caso de que no exista la carpeta "Pdfs" la crea en la ruta de la carpeta raiz
if not os.path.exists(CarpetaPdf):
    os.makedirs(CarpetaPdf)

# Función para mover los archivos PDF de una carpeta a la carpeta Pdfs
def moverArchivos(Carpeta):
    if os.path.isdir(Carpeta):
        for Archivo in os.listdir(Carpeta):
            if Archivo.lower().endswith(".pdf"):
                RutaArchivo = os.path.join(Carpeta, Archivo)
                shutil.move(RutaArchivo, CarpetaPdf)

# Función que recorrer los directorios ubicados en la carpeta principal
def recorrerCarpetas(Carpeta):
    for Archivo in os.listdir(Carpeta):
        Path = os.path.join(Carpeta, Archivo)
        if os.path.isfile(Path):
            moverArchivos(Carpeta)
        elif os.path.isdir(Path):
            recorrerCarpetas(Path)

# Se asigna la ruta de la carpeta principal a recorrer, donde se extraen los Pdfs
CarpetaPrincipal = os.path.abspath("C:\\Users\\Usuario\\Desktop\\11001310503620220045600")
recorrerCarpetas(CarpetaPrincipal)