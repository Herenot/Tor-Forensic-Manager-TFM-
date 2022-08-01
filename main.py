#Clase de prueba en la que se realizarán llamadas a otras clases
from callsSystem import CallsSystem
from fileExtractions import FileExtractions
from webRelatedActions import WebRelatedActions
print("Se está ejecutando el MAIN")
print('--------------------------');
cs = CallsSystem()
fe = FileExtractions()
wr = WebRelatedActions()
whereIsInstalled = "/home/francisco_javier/.local/share/torbrowser"
#destination="/home/francisco_javier/Desktop/pruebas"
#cs.calculate_hash256(whereIsInstalled,destination)
#cs.calculate_hashmd5(whereIsInstalled,destination)
#cs.copy_directory(whereIsInstalled,destination)
#sign256 = fe.obtain_hashes_sign(destination+"/hashes256.txt.asc")
#signmd5 = fe.obtain_hashes_sign(destination+"/hashesmd5.txt.asc")
#print(sign256)
#print('--------------------------');
#print(signmd5)
#print(cs.files_downloaded())
#fe.open_images([ruta imagen])
#fe.get_torrc_info([ruta])
#fe.num_lines_in_file([ruta])
#cs.update_pending()
#print(cs.get_date())
#print(cs.get_user())
#wr.open_sqlViewer()
#cs.open_directory()
#fe.get_nodes_info()
print(wr.curl_nodes('050A1245EEC76B7438337BAAF19F4AB0666B375F'))
print(wr.curl_nodes('37EB4C9361D2F80F279B949CB3CB41DA2F46A2FA'))