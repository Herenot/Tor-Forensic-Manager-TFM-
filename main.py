#Clase de prueba en la que se realizarán llamadas a otras clases
from callsSystem import CallsSystem
from fileExtractions import FileExtractions
print("Se está ejecutando el MAIN")
print('--------------------------');
cs = CallsSystem()
fe = FileExtractions()
whereIsInstalled = "/home/francisco_javier/.local/share/torbrowser"
destination="/home/francisco_javier/Desktop/pruebas"
cs.calculate_hash256(whereIsInstalled,destination)
cs.calculate_hashmd5(whereIsInstalled,destination)
cs.copy_directory(whereIsInstalled,destination)
sign256 = fe.obtain_hashes_sign(destination+"/hashes256.txt.asc")
signmd5 = fe.obtain_hashes_sign(destination+"/hashesmd5.txt.asc")
print(sign256)
print('--------------------------');
print(signmd5)
