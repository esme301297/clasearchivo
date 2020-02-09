from sys import exit

class Archivo:
    def __init__(self,nombre): #self indica que es un metodo, si no lleva es una funcion
        try:
            self.f=open(nombre,'r')
            self.nombre=nombre
        except:
            print("No se puede abrir el archivo", nombre)
            exit()

    def muestra(self):
        i=1
        for linea in self.f:
            print("Linea{:3}, La palabra: {}".format(i,linea))
            i+=1 ##AQUI VA ACONTAR LAS LINEAS DE PALABRAS DEL ARCHIVO, SIN NECESIDAD DE CREAR UNA FUNCION 
        self.f.seek(0)
    #cuenta vocales
    def cuentavocales(self):
        def vocales(s):
            contador=0;
            for i in range(len(s)):
                if s[i] in set ("aeiouáéíóú"):
                    contador+=1
            return contador
        contador=0;
        for linea in self.f:
            contador += vocales(linea)
        self.f.seek(0)
        return contador
    def cuentaconsonantes(self):
        def consonates(s):
            contador=0;
            for i in range(len(s)):
                if s[i] in set ("bcdfghjklmnqrpstvwxyzBCDFGHJKLMNPQRSTVWXYZ"):
                    contador+=1
            return contador
        contador=0;
        for linea in self.f:
            contador += consonates(linea)
        self.f.seek(0)
        return contador
    def cuentasignos(self):
        def signos(s):
            contador=0;
            for i in range(len(s)):
                if s[i] in set (",.;:-[]()/¡!¿?"):
                    contador+=1
            return contador
        contador=0;
        for linea in self.f:
            contador += signos(linea)
        self.f.seek(0)
        return contador
    def cuentaespacio(self):
        def espacio(s):
            contador=0;
            for i in range(len(s)):
                if s[i] in set (" "):
                    contador+=1
            return contador
        contador=0;
        for linea in self.f:
            contador += espacio(linea)
        self.f.seek(0)
        return contador
        
    #main
nombre=input("Nombre del archivo: ")
archivo=Archivo(nombre)
archivo.muestra()
archivo.cuentavocales()
archivo.cuentaconsonantes()
archivo.cuentasignos()
archivo.cuentaespacio()
print("La cantidad de vocales es:") 
print(archivo.cuentavocales())
print("La cantidad de consonantes es:") 
print(archivo.cuentaconsonantes())
print("La cantidad de signos es:") 
print(archivo.cuentasignos())
print("La cantidad de espacio es:") 
print(archivo.cuentaespacio())
print("Convertir a mayusculas")
print(archivo.muestra().lower())

