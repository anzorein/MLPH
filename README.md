# MLPH - Mercadolibre Price History

## Requerimientos

- Python 3.8.x (https://www.python.org/downloads)
- Archivo de texto "links.txt"

## Funcionamiento

En primer lugar se guardan el nombre y el link del producto que queremos seguir en el archivo de texto "links.txt" de la siguiente forma:

name = AMD Threadripper 3960x  
https://articulo.mercadolibre.com.ar/MLA-844499248-micro-procesador-amd-threadripper-3960x-strx4-2-_JM?quantity=1

Es importante que "name = NombreProducto" tenga el espacio luego del "=". Además el URL debe ser https.

Luego podemos ejecutar el script de python "MLPH.py" desde la ventana de comandos. Para esto podemos seguir los siguientes pasos:

En el directorio donde nos encontramos, hacemos click en la ruta de la carpeta.

![](https://i.imgur.com/LzIPvRj.png)[]

Luego borramos esa ruta y escribimos "cmd" para ejecutar la ventana de comandos desde el directorio donde nos encontramos actualmente.

![](https://i.imgur.com/Xcf3sbk.png)[]

A continuación escribimos "python scraper.py" y luego de unos segundos debería aparecer un archivo llamado "MLPH.csv".

Finalmente podemos abrir este archivo con Excel para verificar que el script se ha ejecutado correctamente.
