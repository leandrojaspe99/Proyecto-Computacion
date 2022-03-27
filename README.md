# Proyecto-Computacion

Con la intención de hacer la web más social se han creado múltiples aplicaciones o sitios en Internet que
permiten compartir información y establecer comunicación entre grupos de personas, estos sitios
son denominados REDES SOCIALES. Una empresa de publicidad cuyo lema es “las empresas que invierten
en publicidad, son las empresas que permanecen en la mente de las personas”, quiere evaluar la posibilidad de
colocar publicidad en alguna de las tres redes sociales que considera de mayor uso o más
comunes. Para ello se realiza una encuesta a un conjunto W de personas a quienes se les solicita
suministren la siguiente información: 
NOMBRE, GÉNERO, EDAD Y RED SOCIAL MÁS UTILIZADA
Desarrolle un programa que procese la información, almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre USAREDSOCIAL.TXT y NOLASENCUESTADAS.TXT, con los nombres de los
usuarios que usan alguna de las tres redes sociales consideradas en el estudio o los que no usan
ninguna de las redes sociales consideradas en el
estudio respectivamente, además...
determine e imprima por pantalla:
✓ Cantidad de personas que utilizan cada uno de las tres principales redes sociales
considerados en la encuesta
✓ Porcentaje de personas que utilizan alguna de las tres principales redes sociales
considerados en la encuesta
✓ Nombre y edad del primer usuario procesado que usa hi5
✓ En cuál de las tres redes sociales sería más rentable invertir en publicidad.
Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para tipo de red social más utilizada son 1 =Facebook, 2 =Myspace, 3=Hi5 y
4=Ninguno u otro
o Mientras más usuarios usen una red social, esta se considera más rentable para hacer
publicidad

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
