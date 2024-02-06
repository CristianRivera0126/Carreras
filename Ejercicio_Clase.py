#CREAR UN DICT CON LA SIGUIENTE TABLA
'''
SISTEMAS    CIVIL   MATEMATICAS
PROGRA2     SUELOS  MM110
ALGO        DIBUJO  MM111
POO         CARGAS  CALCULO

CRUD = CREAR, LEER, ACTUALIZAR, BORRAR
'''

carreras = []
materias = []
seguir = True

while seguir: 
    print(carreras)
    print('+++++++++++++++++ MENU +++++++++++++++++')
    print('1. Crear Carrera')
    print('2. Leer Carrera')
    print('3. Actualizar Carrera')
    print('4. Borrar Carrera')
    print('5. Seleccionar Carrera ')
    print('6. Salir')

    try:
        opcion = int(input('ingrese su opcion: '))
        if opcion < 1 or opcion > 6:
            raise ValueError
        print('-------------------------------------')
        if opcion==1:
            print('ingresar carrera')
            nombre = input('Nombre: ')
            dicCarrera = {}
            dicCarrera['carrera'] = nombre
            carreras.append(dicCarrera)

        elif opcion==2:
            print('Leer (Mostrar) Carreras')
            for carrera in carreras:
                indice = carreras.index(carrera)
                print(f'{indice}: {carrera["carrera"]}')

        elif opcion==3:
            Actualizar_Carrera = input('Ingresa la carrera que quieres modificar: ')
            Nueva_Carrera = input('Ingresa la nueva Carrera: ')
            encontrada = False

            for carrera in carreras:
                if carrera['carrera'] == Actualizar_Carrera:
                    carrera['carrera'] = Nueva_Carrera
                    encontrada = True

            if not encontrada:
                print(f'La carrera {Actualizar_Carrera} no esta en la lista')
            else:
                print('Carrera Actualizada')

        elif opcion==4:
            borrar_carrera = input('Ingresa la carrera que deseas borrar: ')

            for carrera in carreras:
                if carrera['carrera'] == borrar_carrera:
                    carreras.remove(carrera)
                    print(f'La carrera {borrar_carrera} fue eliminada')
                    break
                else:
                    print(f'La carrera {borrar_carrera} no esta en la lista')
                    
        elif opcion==5:
            seguirMateria = True      

            while seguirMateria:
                selCarrera = input('Seleccione el nombre de su Carrera: ')
                carreraEn = False

                for carrera in carreras:
                    if carrera['carrera'] == selCarrera:
                        print(f'Su carrera es {selCarrera} ')
                        carreraEn = True
                        break

                if not carreraEn:
                    print(f'La carrera {selCarrera} no esta dentro de la lista')
                else:
                    print(materias)
                    print('+++++++++Menu Clases+++++++++')
                    print(f'7. Crear clases de {carrera["carrera"] }')
                    print(f'8. Mostrar clases de {carrera["carrera"] }')
                    print(f'9. Actualizar clases de {carrera["carrera"] }')
                    print(f'10. Borrrar clases de {carrera["carrera"] }')            
                    print(f'11. Salir a Menú Carreras')
                    
                    try:
                        opMateria = int(input('Ingrese la opcion a realizar : '))
                        print('-------------------------------')
                        if opMateria < 7 or opMateria > 11:
                            raise ValueError
                        if opMateria == 7:
                            print('Crear Clase')
                            nomMateria = input('Nombre de la Clase: ')
                            dicMateria = {}
                            dicMateria['materia'] = nomMateria
                            dicMateria['carrera'] = selCarrera
                            materias.append(dicMateria)
   
                        elif opMateria == 8:
                            print('Mostrar clases y obtener indice')
                            print('-----------Clases-----------')
                            
                            for materia in materias:
                                indice = materias.index(materia)
                                if materia['carrera'] == selCarrera:
                                    print(f'carrera: {carrera["carrera"]}-- clases: {materia["materia"]}')

                        elif opMateria == 9:
                            actualMateria = input('Ingrese la clase que desea actualizar: ')
                            nuevaMateria = input('Ingrese la clase nueva: ')
                            materiaEn = False

                            for materia in materias:
                                if materia['materia'] == actualMateria:
                                    materia['materia'] = nuevaMateria
                                    materiaEn = True
                                    
                            if not materiaEn:
                                print(f'La clase {actualMateria} no esta en la lista')
                            else:
                                print('Clase actualizada')

                        elif opMateria == 10:
                            borrarMateria = input('Ingresa la clase que deseas borrar: ')

                            for materia in materias:
                                if materia['materia'] == borrarMateria:
                                    materias.remove(materia)
                                    print(f'La clase {borrarMateria} fue eliminada')
                                    break
                                else: print(f'La clases {borrarMateria} no esta en la lista')
                    
                        elif opMateria == 11:
                            seguirMateria=False

                        print('-------------------------------')
                    except ValueError:
                        print('Ingrese un numero entero del 7-11 porfavor')
                 
        elif opcion==6:
                print('Hasta Pronto')
                seguir = False
                print('-------------------------------------')
    except ValueError:
        print('Ingrese un numero el 1-6 porfavor')