import os

bandera = 1
print("Bienvenido a nuestro interprete de comandos")
print("")
input("Precione enter para continuar...")
os.system("clear")

while(bandera == 1):
        os.system("pwd")
        a = input()

        if a == "pwd":
                os.system("cd")
        elif a == "date":
                os.system("date")
        elif a == "time":
                os.system("time")
        elif a == "exit":
                bandera = 2
        elif a == "clear":
                os.system("cls")
        elif a == "Man":
                print("pwd Muestra el directorio activo")
                print("time muestra/establece la hora.")
                print("date muestra/establece la fecha.")
                print("exit sale del intérprete ó programa.-")
                print("clear borra pantalla.")
                print("Man Proporciona ayuda de los comandos.")
                print("úname -a versión del OS. ")
                print("cd [directorio] Cambia el directorio activo.")
                print("ls [opciones][dir] Muestra el contenido del directorio especificado o, en caso de no especificar ninguno, el directorio activo.")
                print("rm files borra archivos.")
                print("mkdir [directorio] crea un directorio")
                print("rmdir [directorio] crea un directorio")
                print("")
        elif a == "uname -a":
                os.system("ver")

        #El CD NO FUNCIONA
        elif a == "cd":
                os.system("cd ..")

        elif a[0:2] == "ls":
                b = "ls "+ str(a[3:])
                os.system(b)

        elif a[0:5] == "mkdir":
                b = "mkdir "+ str(a[6:])
                os.system(b) 
        elif a[0:5] == "rmdir":
                b = "rmdir "+ str(a[6:])
                os.system(b) 
        elif a[0:2] == "rm":
                b = "rm "+ str(a[3:])
                os.system(b)                     
        else:
                print("Comando equivocado")

        print("")
     
        
