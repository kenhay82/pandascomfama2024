import matplotlib.pyplot as plt

def generarGrafica(dataFrame):
    #Agrupar datos del DataFrame según el analisís que quiera graficar
    ##Estadisticas de un alimento (PAN) y su promedio al año.
    ## EJE X= (), EJE Y=values[]
    preciosPromedioPais = dataFrame.groupby('Origen')['PrecioporUnidad'].mean()
    ##print(preciosPromedioPais)

    #0. Generando lista de colores.
    colores=['#CEC627','#7BE649','#C8E675','#B88836','#3BE649']
    #1. Generar una FIGURA 
    plt.figure(figsize=(10,10))

    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(preciosPromedioPais.index,preciosPromedioPais.values)

    #3. Muestrar la grafica
    #plt.show()

    #4. Agregar un titulo a la tabla
    plt.title('Ventas Promedio de Panes por Paises')

    #5. Agregar un nombre al EJE X
    plt.xlabel('Paises')

    #6. Agregar un nombre al EJE Y
    plt.ylabel('Precio Promedio')

    #7. Activar el grid
    plt.grid(True)

    #8. Inclinar los X labels
    plt.xticks(rotation=45)

    #9.

    #. Guardando nuestra Gráfica
    plt.savefig("./assets/graphs/promedioPanes.png")

    

