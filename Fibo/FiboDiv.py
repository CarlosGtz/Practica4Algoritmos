#!/usr/bin/python
from time import time

TAM = 6000000
	
def fibonacci(n):
	h = 1 
	i = 1
	j = 0
	k = 0
	while n > 0:
		if n % 2 != 0:
			aux = h*j
			j = h*i + j*k + aux
			i = i*k + aux
		aux = h*h
		h = 2*h*k + aux
		k = k*k + aux
		n = n/2
	return j

def writeFile(fTime):
	archivo = open("datosD.txt", "r+")
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

    
    
  