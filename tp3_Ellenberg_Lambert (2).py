#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Sun Nov 12 20:48:39 2023

@author: anapaulacherep
"""
#Importamos la libreria matplotlib para crear graficos. Asignamos el alias plt, 
# para utilizar funciones de este módulo.
import matplotlib.pyplot as plt

#Creamos la variable que contendra el archivo con el que operaremos.  
archivo1 = "transacciones_simple.txt"

#Crearemos una función con una única entrada , una cadena con la ruta hacia un
# archivo de texto
def archivo_a_dic_v2(nombre_archivo):
    '''

    Parameters
    ----------
    nombre_archivo (string): es el nombre del archivo a leer, el cual debe encontrarse
    en la misma carpeta que este programa        

    Returns
    -------
    deudas_nombres : (dic): la funcion retorna un diccionario cuyas claves son los nombres de todas las
    personas que aparecen en el archivo, y cuyos valores corresponden con los valores de sus deudas acumuladas desde 
    la primer fecha que figura en el archivo, hasta la ultuima. 
        DESCRIPTION.
        La funcion  toma dicho archivo con la información registrada sobre los gastos y la procesa para analizar
        la evolución de la deuda de cada persona respecto a la vivienda. Es decir, se lee el archivo, se
        reestructura la información, y luego se grafica la evolución de las deudas a lo largo de los años.

    '''
    #creamos las variables que necesitaremos para m,anipular los datos del archivo. 
    dic = {}
    deudas_nombres = {}
    fechas = []
    personas = []
    deuda = {}
    eliminado=[]
    #Abriremos el archivo con permisos de lectura.
    with open(archivo1, "r") as archivo:
    #  Creamos la estructura del for para iterar sobre las líneas de un archivo, asignando un número de línea (i) y 
    # la propia línea (linea) en cada iteración mediante el enumerate. Es decir, utilizamos el enumerate para enumerar las líneas del archivo, 
    # y asi poder iterar sobre los pares indice y linea.
    # comienza desde 1 en vez de su valor por default "0", para que itere directo en la primer linea, que contiene a los nombres.   
        for i, linea in enumerate(archivo, 1):
    #establecemos si el indice es 1, que entre al condicional y que primero le quite los caracteres especiales, como el 
    #/n del salto de linea. luego le pedimos que nmos separe a cada elemento.        
            if i == 1:
                linea = linea.strip().split()
    #Una vez separado, iteramos sobre cada nombre y lo agregamos a las variables que creamos al inicio de la funcion,
    # siendo estas.
                for nombre in linea:
    #Al ser un dicciionario,  agregamos el nombre que se este iterando como clave, y como valor le asignamos un 0. este numero
    #ira cambiando, dado que contendra un unico valor, el cual sera la suma final de sus deudas hasta ese momento. 
                    deudas_nombres[nombre] = 0
    #Agregamos al nombre en la lista de nombres                
                    personas.append(nombre)
    #Al ser un dicciionario,  agregamos el nombre que se este iterando como clave, y como valor le asignamos un 0, el cual 
    # ira sumando nuevos valores con el transcurso de la evolucion de las deudas.               
                    deuda[nombre] = []
  
     #Ahora si, mientras no se itere sobre la primer lineia, se comenzara a iterar sobre las lineas que efectivamente
    # contienen a las transacciones de cada dia. (notar que por mas de que se separen a las lineas por fecha,
    #una linea NO contiene TODAS LAS tramnsaccion de ese dia, sino que es liniea POR TRANSACCION. )               
            else:
    #le quitamos los caracteres especiales a la linea.           
                linea = linea.strip()  
    #separamso los elementos de la linea, y los agregamos a la variable "valores".               
                valores = linea.split()
    # establecemos que las clave del diccionario que se hace en la linea de abajo seran las fechas de cada linea.         
                claves = valores[0]
    # este diccionario va a tener las fechas como claves, y el suceso como valor. 
    #Notar que utilizamos una secuencia, slicing, para asignar que vaya desade el elemento 1, para que justamente no 
    #considere a la fecha.             
                dic[claves] = valores[1:]
    #mediante el metodo "get",  obtenemos el valor, que es efetivamente los datos de la transaccion asociado a la clave "claves" en el diccionario "dic".           
                suceso = dic.get(claves, []) 
                
    #PUNTO EXTRA: Creamos un condicional en caso de que, con el acracter "-", se elimine a una persona.            
                if suceso [0]== "-":
    # Establecemos que para acdaa persona de suceso se analice si esta escrita luego del caracter "-". si asi lo es
   # con el metodo pop (el cual necesita un indice, por eso tambien usamos la funcion index) lo eliminamos de la lista de personas.                 
                    for persona in personas:
                        if persona == suceso[1]:                           
                           eliminados = personas.pop(personas.index(persona))
     # agregamos a esa persona a la lista de eliminados.                       
      #                     eliminado.append(eliminado)
      # a este "suceso" lo debemos registrar, con lo cual agregamos la clave a la lista que contiene las fechas.
                           fechas.append(claves)
                       
      # en caso de que se agregue una persona nueva, luego de la linea le seguira el caracter "*". Por eso, el
      # el programa entrara al siguiente elifcuando no se este registrandoi el ingreso de una nueva pewrsona, sino que 
      # se este registrando la transaccion.         
                elif suceso[0] != "*":
       # Creamos la variable "valor", que contendra al monto pagado por quien haya pagado la deuda, y el cual sera 
       # dividido por los deudores.               
                    valor = int(suceso[1])
        # creamos una condicion para cuando NO se trata de una deuda a dividir "entre tantas personas EXCEPTO POR", sino 
      # una deuda a dividir por las personas que le sigan al caracter especial de "~".           
                    if suceso[2] != "~":
       # la cantidad de deudorres sera el largo de la lista que contiene a la transaccion, menos  1 elemento, el cual corresponde al monto.                   
                        cant_deudores = len(suceso)-1
       #Definimos que los deudores de esa transaccion seran los elementos de la lista "suceso", pero a partir del elemento 2
        # en adelante, es decir, luego del monto, dado que asi esta estructurado el archivo.                  
                        nombres_deudores = suceso[2:]
        #Con el for, iteramos en cada e;lemento del suceso, y establecemos que siel elemento i coincide 
       # con el elemento 0 de sucesio, eso significa que esa persona del elemento 0 fue quien pago la deuda, y 
     # por eso su respectivo calculo, en la linea   117.              
                        for i in suceso:
                            if i == suceso[0]:
      # para quien pago la deuda, el valor de su deuda sera negativo, dado que tiene plata a favor. por eso 
     # al valor que ya tenia antes (el cual en la primera iteracion sera cero), se le suma lo que le corresponde pagar a cada uno
   # menos todo lo que esa persona ya pago.                             
                                deudas_nombres[suceso[0]] += (valor/cant_deudores) - valor 
    # En cambion para quienes deben parte de ese monto de la deuda, y no es la persona quien lo pago, el valor de su deuda 
    # sI sera positivo, dado que lo que deben claramente es mayor a lo que pagaron o, mejor dicho,es mayor a lo que tienen a favor.                         
                            elif i in nombres_deudores: 
                                deudas_nombres[i] += valor/cant_deudores 
                                
  # Creamos uan condicion para el caso de que la deuda sea pagada por "todos menos x/tal persona". Esto es asi, porque 
  # en el archivo se indica que si la deuda es pagada por todos menos alguien, se pone "~", y seguido el/los nombre/s de quien/es no debe/n dinero en esa transaccion.          
                    elif len(suceso) > 3:
                       # cant_no_deudores = len(suceso)-2
    # establecemos que para los elementos que van desde el caracter "~", hasta el final de la lista se los agregue
   # a la lista de nombres_no_deudores.                    
                        nombres_no_deudores = suceso[3:]
     #por otro lado, creamos una lista vacia para quienes si deben dinero, que seran todos, menos quienes esten en la lista de "nombres_no_deudores".                   
                        los_deudores = []
    # lo mencionado anteriormente se efectua con el siguiente bloque de codigo:       
             # establecemos que para cada persona en la lista de personas, se evalue si no esta en nombres_no_deudores, es decir
             # que es deudor, se lo agregue a la lista de los_deudores.                 
                        for persona in personas:
                            if persona not in nombres_no_deudores:
                                los_deudores.append (persona)
             # para cada elemento de personas, se calculan sus respectivas deudas:                          
                        for i in personas:
             # si es parte de los deudores, pero fue quien pago la deuda, se le agrega lo que debe cada una menos lo que esa persona ya pago.                   
                            if i not in nombres_no_deudores:
                                if i == suceso[0]:
                                    deudas_nombres[suceso[0]] += valor/(len(deudas_nombres) - len(nombres_no_deudores)) - valor
            # si por lo contrario forma parte de la deuda y no fue quien la pago, su al valor de sus deuda hasta el diade la fecha
            # se le suma, el valor dividido entre todos los nombres de TOODOS, menos quienes no la deben            
                                elif i in los_deudores:
                                    deudas_nombres[i] += valor/(len(deudas_nombres) - len(nombres_no_deudores)) 
        
          # Creamos una condicion en caso de que la deuda se pague entre TODOS.  
                    else:
          # para cada elemento del suceso, se calcula que si el elemento es la persona quien pago la dedua, se calcule lo que debe cada uno, menos lo que efectivamente pago.
                        for i in suceso:
                            if i == suceso[0]:
                                deudas_nombres[suceso[0]] += valor/len(deudas_nombres) - valor 
          # cuando el elemento de la lista suceso, es decir la persona, no sea quien pago el monto, pero aun asi debe 
          # su respectiva parte, se clacula el valor total de la deuda dividido todas las personas, es decir, dividido el largo de deudas_nombres.
          # (al aplicarle la funcion len() a un diccionario, se cuenta la cantidad de claves del diccionario. )
                            else: 
                                for persona in personas:
                                    if persona != suceso [0]:
                                       deudas_nombres[persona] += valor/len(deudas_nombres)
                                       
          # este condcicional no fucniona para el calculo, sino que para el grafico, para cuando quien use el programa quiere acceder a la dedua 
          # que tiene en la fecha ingresada. 
          # la siguiente linea es una condicion para cuando estemos en el ultimo dia registrado en el archivo.
                    if len (fechas) > 1 and claves == fechas [-1]:
                        for persona in personas:
          # para cada clave del; diccionario de deuda, le elimiinamos el ultimo elemento, para que no quede registrada dos veces.            
                           deuda[persona].remove (deuda[persona][-1])
          # a cada  clave del diccionario "deuda" le agregamos la lista de la evolucion de la deuda de cada persona.             
                           deuda[persona].append(deudas_nombres[persona])  
         
            # si no es el ultimo dia, a cada clave del diccionario "deuda" le agregamos la lista de la evolucion de la deuda de cada persona.  
            # y tambien a la lista de las fechas le agregamos  "claves', que es la fecha de la correspondiente transaccion.                    
                    else:
                        for persona in personas:
                             
                          deuda[persona].append(deudas_nombres[persona])
                          
                        fechas.append(claves)
            # En caso de que una persona haya sido eliminada, tambien aghregamos su evolucion de tooda su deuda, en el valor de la clave de su nombre, del diccionario de deuda, que es el que se usara para graficar.         
                        for eliminados in eliminado:
                            deuda[eliminados].append(deudas_nombres[eliminados])
           # por ultimo, creamos un bloque de coigo en caso de que el segundo elemento de la lista de suceso sea "*", 
           # que basicamente es cuando se incorpora un nuevo inquilino.                  
                else:
            #el nombre de ese nueo inquilino sera elelemento qcon indice 1.  
                    nuevo_inquilino = suceso[1]
            # creamos la lista de nuevos inquilinos.       
                    inquilinos_nuevos = []
            # agregamos a dicho inquilino a la lista de los nuevos inquilinos.         
                    inquilinos_nuevos. append (nuevo_inquilino)
            # lo agregamos al diccionario que contiene la evolucion de las deudas, y a El con el valor cero.         
                    deudas_nombres[nuevo_inquilino] = 0     
            # agregamos al nuyevo inquilino a la lista de personas, para que el programa lo considere una vez incorporado.         
                    personas.append(nuevo_inquilino)
                    # Ajustar las listas de deuda y fechas para el nuevo inquilino.
           # al diccionario de "deuda" tambien lo agregamos, para que en su clave aparezca la evolucion de su deuda. 
           # Nuevamente su dedua arranca en cero. Notar que esta entre corchetes porque debe ser una loista, dado que 
           # que en dicha lista se iran guardando las sumas de los montos acumulados de sus deudas. 
                    deuda[nuevo_inquilino]= []
                    deuda[nuevo_inquilino] = [0]
           # a la lista de fechas le agregamos l aclave, para que quede registrada la fecha su incoporacion.          
                    fechas. append(claves)
           # creamos una lista para las fechas en las que opere el nuevo inquilino.         
                    fechas_nuevo_inquilino = []
           # a esa lista le agregamos la clave de la operacion en la que se este operando.         
                    fechas_nuevo_inquilino.append (claves)
           # Ahora bien , para cada persona, si la persona sobre la cual se esta iterando NO ES UN NUEVO INQUILINO,
           # que a la clave  del dic "deuda", es decir, a cada perosna, se le agregue el monto acumulado de su deuda hasta el dia de la fecha. 
                    for persona in personas:
                        if persona not in inquilinos_nuevos:
            # de este modo, deudas_nombres es un dic que contiene como clave el nombre d etodos los inquilinos, y como valor
           # el monto acumulado de sus deudas, siendo este un valor positivo si DEBE DINERO, o negativo si LE DEBEN DINERO.                
                           deuda[persona].append(deudas_nombres[persona])
                           
# Ahora si cxreamos una nueva figura para el gráfico , con los datos obtenidos en el bloque de codgo de arriba.   
        plt.figure()
        for persona in personas:
        # Si la persona es un inquilino nuevo, le vamos a pedir que grafique las deudas a partir de la fecha del inquilino nuevo.   
            if persona in inquilinos_nuevos:
                i = 0
                fecha_nueva = fechas.index(fechas_nuevo_inquilino[i])
                # el eje x tendra las fechas, mientras que el eje y los correspondientes valores de la sdeudas al final del dia de la fecha.
                plt.plot (fechas[fecha_nueva:], deuda[persona], label=persona)
                i += 1
        # En cambio, si la persona no es un inquilino nuevo, le pedimos que grafique todas las fechas.        
            else:
                plt.plot(fechas, deuda[persona], label=persona)
    
    # Ahora "personalizamos" el gráfico
        #En el eje x le ponemos como etiqueta "Fechas"
        plt.xlabel('Fechas')
        #En el eje y le ponemos como etiqueta "la deuda en pesos"
        plt.ylabel('Deuda en Pesos')
        plt.legend()
        # como titulo le ponemos "Grafico de Deudas"
        plt.title('Gráfico de Deudas') 
        # Ahora mostramos solo la primera y última fecha en el eje X
        plt.xticks([fechas[0], fechas[-1]])  
        # # Establecemos el r
        plt.ylim(-300000, 200000)  
        plt.show()

    # Como mencionamos al rpincipio de la funcion en el docstring, si bien la funcion grafica la evolucion de las deudas, 
    # como return, esta funcion nos retorna el diccionario de las deudas hasta el ultimo dia. 
    return deudas_nombres

print(archivo_a_dic_v2(archivo1))



##Segunda parte

#Lo primero que realizamos antes de comenzar la segunda funcion, es pedirle al usuario un input con la fecha de la cual desea ver el grafico de pie de deudas.
fecha_final = input("Ingrese la fecha deseada:")

#A continuacion creamos una funcion llamada archivo_y_fechas donde estaremos resolciendo la segunda consigna:
def archivo_y_fechas (nombre_archivo, fecha_final):
    '''

    Parameters
    ----------
    nombre_archivo (string): es el nombre del archivo a leer, el cual debe encontrarse
    en la misma carpeta que este programa  
    fecha_final (string): es la fecha indicada por el usuario en el mismo formato que se muestra en el archivo.  

    Returns
    -------
    None: Dado que lo unico que queremos son ambos graficos esta funcion devuelve los graficos, pero nada escrito por la terminal

    '''
    #Esta funcion es igual a la de arriba solamente cambia el final, comenzaremos a comentar cuando algo sea diferente. Sino aplica lo de arriba. 
    dic = {}
    deudas_nombres = {}
    fechas = []
    personas = []
    deuda = {}
    
    with open(archivo1, "r") as archivo:
        for i, linea in enumerate(archivo, 1):
            if i == 1:
                linea = linea.strip().split()  
                for nombre in linea:
                    deudas_nombres[nombre] = 0
                    personas.append(nombre)
                    deuda[nombre] = []
                    
            else:
                linea = linea.strip()  
                valores = linea.split()
                claves = valores[0]
                dic[claves] = valores[1:]
                
                suceso = dic.get(claves, []) 
    
                if suceso[0] != "*":
                    valor = int(suceso[1])
                    if suceso[2] != "~":
                        cant_deudores = len(suceso)-1
                        nombres_deudores = suceso[2:]
                        for i in suceso:
                            if i == suceso[0]:
                                deudas_nombres[suceso[0]] += (valor/cant_deudores) - valor 
                            elif i in nombres_deudores: 
                                deudas_nombres[i] += valor/cant_deudores                                
                
                    elif len(suceso) > 3:
                        nombres_no_deudores = suceso[3:]
                        los_deudores = []
                        for persona in personas:
                            if persona not in nombres_no_deudores:
                                los_deudores. append (persona)
                        for i in suceso:
                            if i not in nombres_no_deudores:
                                if i == suceso[0]:
                                    deudas_nombres[suceso[0]] += valor/(len(deudas_nombres) - len(nombres_no_deudores)) - valor 
                                elif i in los_deudores:
                                    deudas_nombres[i] += valor/(len(deudas_nombres) - len(nombres_no_deudores)) 
        
    
    
                    else:
                        for i in suceso:
                            if i == suceso[0]:
                                deudas_nombres[suceso[0]] += valor/len(deudas_nombres) - valor 
    
                            else: 
                                for persona in personas:
                                   deudas_nombres[persona] += valor/len(deudas_nombres)
                   
                    if len (fechas) > 1 and claves == fechas [-1]:
                        for persona in personas:
                           deuda[persona].remove (deuda[persona][-1])
                           deuda[persona].append(deudas_nombres[persona])  
                        
                    else:
                        for persona in personas:
                          deuda[persona].append(deudas_nombres[persona])
                        
                        fechas.append(claves)
    
                
                else:
                    nuevo_inquilino = suceso[1]
                    inquilinos_nuevos = []
                    inquilinos_nuevos. append (nuevo_inquilino)
                    deudas_nombres[nuevo_inquilino] = 0     
                    personas.append(nuevo_inquilino)
                    deuda[nuevo_inquilino]= []
                    deuda[nuevo_inquilino] = [0]
                    fechas. append(claves)
                    fechas_nuevo_inquilino = []
                    fechas_nuevo_inquilino.append (claves)
                    for persona in personas:
                        if persona not in inquilinos_nuevos:
                           deuda[persona].append(deudas_nombres[persona])
                           
    
    #A continuacion dividimos ambas fechas por año, mes y dia (en este formato 2022-02-21, quedaria anio:2022, mes:02 y dia:21 usando el split en cada "-")
    anio, mes, dia = fechas[0].split("-")
    anio1, mes1, dia1 = fecha_final.split("-")
    
    #Aqui comparamos si la fecha del input es correcta, es decir si no es luego de la ultima fecha del archivo.
    #Esto lo hacemos comparando primero que nada, si el año es menor. Si los años son iguales, si el mes es menor. Y si el año y el mes son iguales, si el dia es menor.
    if (int(anio1) > int(anio)) or (int(anio) == int(anio1) and int(mes1)>int(mes)) or (int(anio)== int(anio1) and int(mes1)==int(mes) and int(dia1)>=int(dia)):
        #Si todo esto se cumple el siguente codigo se ejecutara. En este primero que nada creamos las variables que etsaremos utilizando para poner los deudores y los no deudores, y los montos de ambos. Siendo listas vacias
        deudores=[]
        no_deudores=[]
        total_deudores=[]
        total_no_deudores=[]
        #Luego buscamos donde se encuentra la fecha indicada por el usuario, buscando su index, es decir en que momento aparece en fechas.
        fecha_indice = fechas.index(fecha_final) 
        for persona in personas:
            #Primero nos fijamos en los inquilinos nuevos, ya que estos no tendran una deuda al incio.
           if persona in inquilinos_nuevos :
               i=0
               indice_inicio = fechas.index(fechas_nuevo_inquilino[i])
               sus_fechas = fechas[indice_inicio:]
               fecha_indice2=sus_fechas.index(fecha_final)
               i+=1
               #Una vez obtenida la deuda de la persona, debemos ver si debe o si le deben, para luego posiscionari en el grafico de pie, esto lo hacemos viendo si su deuda es mayor o menor a 0.
               if deuda[persona][fecha_indice2]<0:
                    deudores.append(persona)
                    #Agregamos la persona a los deudores
                    #Cambiamos su deuda a positivo ya que los indices del grafico pie deben ser positivos.
                    positivo= float(deuda[persona][fecha_indice]) * -1
                    total_deudores.append (positivo)
                    #Agregamos la deuda al total debido
               else:
                   #De ser menos a sro, es decir que le deben lo agregamos a no_deudores y su monto a el total de ellos.
                    no_deudores.append(persona)
                    total_no_deudores.append(deuda[persona][fecha_indice2])
               
           else:
               #Ahora nos fijamos en los inquilinos originales, es decir, que estuviron siempre.
               #Ahora ebemos ver si debe o si le deben, para luego posiscionari en el grafico de pie, esto lo hacemos viendo si su deuda es mayor o menor a 0.
               if deuda[persona][fecha_indice]<0:
                    deudores.append(persona)
                    positivo= float(deuda[persona][fecha_indice]) * -1
                    #Agregamos la persona a los deudores
                    #Cambiamos su deuda a positivo ya que los indices del grafico pie deben ser positivos.
                    total_deudores.append (positivo)
                    #Agregamos la deuda al total debido

               else:
                   #De ser menos a sro, es decir que le deben lo agregamos a no_deudores y su monto a el total de ellos.
                    no_deudores.append(persona)
                    total_no_deudores.append(deuda[persona][fecha_indice])
                    
        # Para el grafico de pie:
        #Ambas estructuras de los graficos los sacamos de https://stackoverflow.com/questions/53782591/how-to-display-actual-values-instead-of-percentages-on-my-pie-chart-using-matplo
        #Lo que hacen es crear el valor de total_duedores/total_no_dedudores y los muestra en nuesto grafico en vez del porcentaje que ocupan, la cantidad que deben o les deben.
        #Primero realizamos el de los deudores, creando la figura y luego utlizando lo que dijimos arriba.
        plt.figure(figsize=(6, 6))
        def autopct_format(values):
            def my_format(pct):
                total = sum(total_deudores)
                val = int(round(pct*total/100.0))
                return '{v:d}'.format(v=val)
            return my_format
        plt.pie(total_deudores, labels = deudores, autopct = autopct_format(total_deudores))
        #Luego le damos los parametros al grafico de pie, y los labels de las personas
        plt.title('Personas Deudoras')
        #Le pusimos un titulo al grafico para luego poder identificarlo
        plt.show()
        #De esta forma hacemos que nuestro grafico se muestre.
               
        

        # A continuacion, pasamos a realizar el de los no deudores
        #Primero que nada creamos la base del grafico
        plt.figure(figsize=(6, 6))
        #Aqui utilizamos lo mismo que mencionamos arriba de la misma pagina web, pero lo modificamos para los no deudores 
        def autopct_format(values):
            def my_format(pct):
                total = sum(total_no_deudores)
                val = int(round(pct*total/100.0))
                return '{v:d}'.format(v=val)
            return my_format
        #Luego le damos los parametros al grafico de pie, y los labels de las personas
        plt.pie(total_no_deudores, labels = no_deudores, autopct = autopct_format(total_no_deudores))
        #Le pusimos un titulo al grafico para luego poder identificarlo
        plt.title('Personas No Deudoras')
        plt.show()
        #De esta forma hacemos que nuestro grafico se muestre.
       
    else:
        print ("La fecha ingresada es incorrecta")
        #Por ultimo si el if que ingresamos al incio (de ver si la fecha era menor a la ultima) no se cumple, imprimira esto por pantalla indicamndo que no es correcta.
        
#Ahora si, para que nuestra fucnion sirva, debemos llamarla y lo hacemos con el archivo de transacciones y con el input ingresado por el usuario.
print (archivo_y_fechas(archivo1, fecha_final))
