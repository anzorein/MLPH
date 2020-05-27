# MLPH - Mercadolibre Price History

## Requerimientos

- Python 3.8.x (https://www.python.org/downloads)
- Archivo de texto "links.txt"

## Funcionamiento

En primer lugar se guardan el nombre y el link del producto que queremos seguir en el archivo de texto "links.txt" de la siguiente forma:

![](https://i.imgur.com/3apLMjC.png)

name = AMD Threadripper 3960x  
https://articulo.mercadolibre.com.ar/MLA-844499248-micro-procesador-amd-threadripper-3960x-strx4-2-_JM?quantity=1

Es importante que "name = NombreProducto" tenga el espacio luego del "=". Además el URL debe ser https.  
Si se quieren agregar más productos simplemente se escribe una nueva línea con su nombre y la dirección.

Luego podemos ejecutar el script de python "MLPH.py" desde la ventana de comandos. Para esto podemos seguir los siguientes pasos:

En el directorio donde nos encontramos, hacemos click en la ruta de la carpeta.

![](https://i.imgur.com/LzIPvRj.png)

Luego borramos esa ruta y escribimos "cmd" para ejecutar la ventana de comandos desde el directorio donde nos encontramos actualmente.

![](https://i.imgur.com/Xcf3sbk.png)

A continuación escribimos "python scraper.py" y luego de unos segundos debería aparecer un archivo llamado "price-history.csv".

![](https://i.imgur.com/ifujtNx.png)

Finalmente podemos abrir este archivo con Excel para verificar que el script se ha ejecutado correctamente.

## Ejecución automática

Si no queremos actualizar manualmente el valor de los productos, podemos utilizar el archivo MLPH.bat para realizarlo automáticamente.

Para esto apretamos el inicio de windows y escribimos "Programador de Tareas" (o task scheduler en inglés) y luego en "Crear tarea básica". Colocamos un nombre (por ejemplo: ActualizarPrecios), seleccionamos cada cuánto queremos que se repita la tarea, cuándo debería ejecutarse y finalmente la opción "Iniciar un programa". Aquí buscamos el archivo "MLPH.bat", pulsamos siguiente y finalizar.

Por último, si no queremos que cuando se ejecute aparezca una ventana de comando, hacemos doble click sobre la tarea y seleccionamos las opciones "Ejecutar tanto si el usuario inició sesión como si no" y "No almacenar contraseña.".

![](https://i.imgur.com/1VjgKa3.png)

## TODO

- Añadir el nombre de un producto a la primera fila de un archivo CSV existente luego de añadirse al archivo links.txt
