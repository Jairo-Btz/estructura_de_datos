import sys
import time
import csv
import os
from datetime import datetime
#funcion que imprime el menú

def imprimirMenu():
    print("Elige una opción\n1-Registrar Venta\n2-Consultar Venta\n3-Reporte\n4-Salir")
#separador
SEPARACION = 15*"-"
#nombre archivo
f = 'ventas.csv'
_fecha = ""
#iniciamos ciclo 
while True:
    #lista para almacenar los articulos(no venta,detalle,cantidad y precio total)
    venta = []
    #imprimimos menu
    imprimirMenu()
    opcion = input()    #entrada de la opcion elegida
    if opcion=="1":
        #condicional para ver si existe el csv
        if not os.path.exists(f):
            
            #si no existe este bloque de codigo crea el csv
            encabezados = [['No. Venta','Fecha','Descripcion','Cantidad','PU']]
            myFile = open(f, 'w',newline='')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(encabezados)
            #definimos el numero de venta
            _n_venta=1
            print("Writing complete")
        else:
            
            #bloque de codigo para leer el csv
            with open(f) as File:
                reader = csv.reader(File, delimiter=',')
                ventas=(list(reader))
                ultima_venta = ventas[-1][0]
                #obtenemos el numero de venta
                if ultima_venta=="No. Venta":
                    _n_venta = 1
                else:
                    _n_venta = int(ultima_venta)+1
            
            
        #se abre menú de ventas
        print(f"{SEPARACION}Menú de Ventas{SEPARACION}")
        while True: #bucle menú de ventas
            print("1 para añadir artículo - 2 para cerrar venta")
            eleccion = input()
            if eleccion=="1":
                while True:
                	if _fecha !="":
                	    break
                		
                	try:
                		print('Fecha de la venta')
                		print('1- Fecha actual')
                		print('2-Fecha personalizada')
                		opcion = int(input())
                	except:
                		print('Opcion no valida')
                	else: 
                		if opcion == 1:
                			
                			_fecha = datetime.now()
                			_fecha= _fecha.date()
                			break
                		else:
                			while True:
                				
                				try:

                					dia = int(input())
                				except:
                					print('Valor introducido no valido')
                				else:
                					if dia in range(1,32):
                						dia=str(dia)
                						if len(dia)==1:
                							
                							dia =f'0{dia}'
                							print(dia)
                						break
                			while True:
                				
                				try:

                					mes = int(input())
                				except:
                					print('Valor introducido no valido')
                				else:
                					if mes in range(1,13):
                						mes=str(mes)
                						if len(mes)==1:
                							mes=f'0{mes}'
                						break
                			while True:
                				
                				try:
                					anio = int(input())
                				except:
                					print('Valor introducido no valido')
                				else:
                					_fecha = datetime.now()
                					anio_actual = _fecha.year
                					
                					if anio in range(1901,anio_actual+1):
                						_fecha=f'{anio}-{mes}-{dia}'
                						
                						print(_fecha)
                						break
                			break
                

                				
                print("Descripcion del artículo")
                _descripcion = input()#entrada articulo
                while True:

                    print("Cantidad de articulos")
                    try:
                        _cantidad_piezas = int(input())#entrada cantidad
                    except:
                        print("Valor introducido no es correcto, Intente de nuevo.")
                    else:
                        break
                while True:

                    print("Precio unitario")
                    try:
                        _precio_unitario = int(input())#entrada precio unitario
                    except:
                        print("Valor introducido no es correcto, Intente de nuevo.")
                    else:
                        break
                _precio_total = _cantidad_piezas*_precio_unitario #calculamos el importe subtotal
                venta.append((_n_venta,_fecha,_descripcion,_cantidad_piezas,_precio_total))#añadimos la venta a memoria con ayuda del diccionario -venta-
                print("Articulo añadido.")
            elif eleccion=="2":
                #cerramos la venta 
                importe_total = 0  #inicializamos variable para almacenar el importe total
                if len(venta)>0: #si la lista ventas es mayor a 0, quiere decir que hay ventas por lo tanto se puede procesar la venta
                    for i in venta: #recorremos cada venta 
                        importe_total = importe_total + i[4]#extraemos su precio subtotal 
                    print(f"Total a pagar: ${importe_total}")
                    print("1 Finalizar - 2 Cancelar venta")
                    finalizar= input() #entrada para ver si se finalizará o cancelará la venta
                    if finalizar == "1": #finalizamos la venta cobrandola                        
                        myFile = open(f, 'a',newline='')
                        with myFile:
                            writer = csv.writer(myFile)
                            writer.writerows(venta)
     
                        for i in venta:
                            print(i)

                        del venta #eliminamos de memoria principal la lista venta
                        _fecha = ""
                        print("Venta Finalizada.")
                        break #terminamos con el ciclo del menú de ventas

                    elif finalizar == "2": #cancelamos venta
                        print("Venta cancelada")
                        break #terminamos con el ciclo del menú de ventas
                    else:
                        print("Opcion no existe.")
                else:
                    print("Ningun artículo añadido.") 
                    break
            else:
                print("Opcion no existe.")
    elif opcion=="2":
        if os.path.exists(f):
            with open(f) as File:
                reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
                ventas=(list(reader))
        else:
        	ventas = []
        #menu para consulatr ventas
        if len(ventas)>1: #si hay ventas entonces entramos al menú
            print(f"{SEPARACION}Menú de Consulta{SEPARACION}")
            
            while True:
                print("Introduce el numero de venta para ver los detalles 0 Volver")
                try:
                    _venta = int(input())
                except:
                    print("Valor introducido no es correcto.")
                else:
       
                    if _venta > len(ventas) or _venta <= 0:
                        if _venta>len(ventas):
                        	print("Venta no existente")
                        elif _venta ==0:
                        	break
                    else:
                    	_total_venta=0
                    	print("No. Venta\tFecha\t\t\tDescripcion\tCantidad\tImporte")
                    	for i in ventas:
                    		if i[0]==str(_venta):
                    			print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
                
                				
              
                    					  		    
                    			_total_venta += int(i[4])
                    	print(f"Importe Total: {_total_venta}")
                
        else:
            print("No hay ventas registradas")
    #opcion para obtener un reporte
    elif opcion=="3":
        if os.path.exists(f):
            with open(f) as File:
                reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
                ventas=(list(reader))
        else:
        
            ventas = []
        while True:
            if len(ventas)==0:
                print("No hay ventas realizadas")
                break
            else:
                while True:

                    try:
                        print("1 Introducir Fecha 2 Salir")
                        opcion=int(input())
                    except:
                        pass
                    else:
                        break
                if opcion==1:
                        while True:
                            try:
                                print('Dia')
                                dia = int(input())
                            except:
                                print('Valor introducido no valido')
                            else:
                                if dia in range(1,32):
                                    dia=str(dia)
                                    if len(dia)==1:
                                        dia =f'0{dia}'
                                        #print(dia)
                                    break
                        while True:
                            try:
                                print('Mes')
                                mes = int(input())
                            except:
                                print('Valor introducido no valido')
                            else:
                                if mes in range(1,13):
                                    mes=str(mes)
                                    if len(mes)==1:
                                        mes=f'0{mes}'
                                    break
                        while True:
                            try:
                                print('Año')
                                anio = int(input())
                            except:
                                print('Valor introducido no valido')
                            else:
                                _fecha = datetime.now()
                                anio_actual = _fecha.year
                                if anio in range(1901,anio_actual+1):
                                    _fecha=f'{anio}-{mes}-{dia}'
                                    #print(_fecha)
                                    break
                        print(f"Reporte de Ventas del {_fecha}")
                        print("Venta\t\tFecha\t\t\tDescripcion\tPiezas\t\tTotal")
                        contador = 0
                        acumulado = 0
                        for i in ventas:
                            #si la fecha coincide, extramos su detalle
                            if i[1]==_fecha:
                                print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
                                acumulado = acumulado + int(i[4])
                                contador += 1
                        if contador == 0:
                            print("NINGUNA VENTA")
                        else:
                            print(f"Total vendido: {acumulado}")
                        _fecha = ""
                elif opcion==2:
                    break
                else:
                    print("Opcion no valida")

               

                
                    
#opcion para salir del programa
    elif opcion=="4":
        print("Saliendo del programa...")
        time.sleep(2)
        sys.exit()
    #si no se ingreso una opcion correcta entonces será tomada como opción no válida
    else:
        print("Opcion no válida")
