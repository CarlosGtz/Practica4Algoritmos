#!/usr/bin/python
from time import time

TAM = 980000
	
def fibonacci(n):
	a,b = 1,1
	for i in range(n-1):
 		a,b = b,a+b
	return a	

def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()


init_time = time()
x = fibonacci(TAM)
final_time = time()
e_time = final_time - init_time
str_time = str("%.20f" % e_time)
writeFile(str_time)
print "Time: %.20f" % e_time

    
    
  