import numpy as np

def riqueza_paisaje(poblacion, t=-1, abundancia_min = 5.):
    """ Entrada: un arreglo poblacion = [tiempo] [x][y] [especies]
        Salida: la abundancia y la riqueza de especies en UN tiempo, en todo el paisaje;
        si no se especifica el tiempo se toma la última iteración.
    """
    riqueza = []
    for idx in range(poblacion.shape[3]):
        if np.sum(poblacion[t,:,:,idx]) > abundancia_min: #suma de cada especie en la iteración t
            riqueza.append(1) 

    abundancia = np.sum(poblacion[t,:,:,:]) #suma total de individuos
    return abundancia, np.sum(riqueza)  #riqueza de especies


def medidas_por_celda(poblacion, t=-1, abundancia_min = 5.):
    """
    Entrada: un arreglo 4D con la forma poblacion = [tiempo] [x][y] [especies]
    Salida: arreglo 2D que indican la abundancia y la riqueza 
    de cada celda de poblacion en UN tiempo; 
    si no se indica el tiempo, se toma la última iteración
    """
    poblacion = poblacion[t]
    abundancia = np.zeros((poblacion.shape[0], poblacion.shape[1]))
    riqueza = np.zeros((poblacion.shape[0], poblacion.shape[1]))

    for x in range(poblacion.shape[0]):
        for y in range(poblacion.shape[1]):
            abundancia[x] [y] = np.sum(poblacion[x, y, :])
            riqueza[x] [y] = np.sum(poblacion[x, y, :] > abundancia_min)
              
    return abundancia, riqueza


def riqueza_agricola(poblacion, paisaje, t=-1, abundancia_min = 5.):
    """ Entrada: un arreglo poblacion = [tiempo] [x][y] [especies],
        el paisaje y el tiempo (si no se indica el tiempo se toma la última iteración).
        Salida: la abundancia y la riqueza de especies en UN tiempo, en las celdas que no son bosque;
        si no se especifica el tiempo se toma la última iteración.
    """
    x_celdas = len(paisaje)
    y_celdas = len(paisaje[1])
    
    riqueza = np.zeros(poblacion.shape[3])
    for idx in range(poblacion.shape[3]):
        
        for i in range(x_celdas): #para todo x y
            for j in range(y_celdas):
                if paisaje[i][j] != "b":
                    riqueza[idx] += poblacion[t,i,j,idx]  
    
    abundancia = np.sum(riqueza) # abundancia
    return abundancia, len(riqueza[riqueza > abundancia_min])  #riqueza de especies
