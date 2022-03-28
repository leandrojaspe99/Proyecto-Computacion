#Leandro Jaspe
#Programa ver donde hacer publicidad

arch1=open("redes.txt","r") #r=readline lectura
arch2=open("usaredsocial.txt", "w") #w=write
arch3=open("Nolasencuentas.txt","w")#w=write escritura

linea=1
cont=0 #Para contar cuantos prefieren Facebook
cont1=0 #Para contar cuanto prefieren myspace
cont2=0 #Para contar cuanto prefieren hi5
band=0  # Decir quien es el primero qe elige hi5
 
contenido=arch1.readlines()

w=int(contenido[0]) #Es para que en nuestro archivo creado redes.txt el primer valor sera las veces que se repita el ciclo

for i in range(w):
    lista = contenido[linea].split(',')
    
    linea+=1 #para que lea linea a linea

    nombre = str(lista[0]) #str porque es en letras
    genero =str(lista[1])
    edad = int(lista[2]) #int porque es numero entero
    red = int(lista[3])

    
        
    if red==1: #Esto es para saber cuantas personas la prefieren facebook
        cont+=1
        fb= "facebook"
        
    elif red ==2:#Esto es para saber cuantas personas la prefieren myspace
            cont1+=1
            mp="myspace"

    elif red==3:#Esto es para saber cuantas personas la prefieren hi5
        cont2+=1
        h5="hi5"

        if band==0: #esta e una bandera que usaremos pra indicar quien ser el primero en elegir hi5
            nombre_primerhi5 = nombre
            edad_primer = edad
            band = 1
        else:
            porcentaje= (cont+cont1+cont2)/w*100

   
    elif red==4:#Esto imprime en los archivos las personas no encuestadas
        arch3.write(str(nombre) + '\n' )
    else :#Esto imprime en los archivos las personas si encuestadas
        arch2.write(str(nombre) + '\n')

# %s cadena usada para unir valores

print("De el publico que prefiere usar Facebook son %s " %cont)
print("De el publico que prefiere usar Myspace son  %s" %cont1)
print("De el publico que prefiere usar Hi5 son %s" %cont2)

print("el %.2f" % porcentaje,  "% d de personas usan una de las tres principales redes sociales" )

print("la primera persona encuestada que usa Hi5 es %s con %d años de edad" %(nombre_primerhi5,edad_primer))

#Pra saber quien es ms usada y por ende mas factible en invertir para publicidad
if cont > cont1 and cont > cont2:
    print("la red social mas usada es ", fb)

elif cont1 > cont and cont1 > cont2:
    print("la red social mas usada es ", mp)

else:
    print("la red social mas usada es ", h5)

#Siempre que usamos archivo debemos de cerrarlo
arch1.close()
arch2.close()
arch3.close()
