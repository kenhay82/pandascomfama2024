import pandas as pd
from bs4 import BeautifulSoup

def crearTabla(dataFrame,nombreTabla):
    
    #crear un HTML desde un Datframe de python
    archivoHTML=dataFrame.to_html()
    
    #Establecemos la ruta donde vamos a guardar la tabla
    rutaArchivo=f"./assets/tables/{nombreTabla}.html"
    
    #Generamos una estructura HTML
    encabezadoHTML=''' 
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    '''
    
    #Adaptar los estilos de la tabla
    sopa=BeautifulSoup(archivoHTML,'html.parser')
    
    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)
    
    archivoHTML=str(sopa)
    
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    #Se escribe la tabla 
    with open(rutaArchivo,"w", encoding='utf-8') as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")