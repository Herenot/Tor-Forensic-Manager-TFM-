#Clase de prueba en la que se realizarán llamadas a otras clases
from callsSystem import CallsSystem
from fileExtractions import FileExtractions
from webRelatedActions import WebRelatedActions
from PyQt5 import QtWidgets,uic
import sys
#print("Se está ejecutando el MAIN")
#print('--------------------------');
#cs = CallsSystem()
#fe = FileExtractions()
#wr = WebRelatedActions()
#whereIsInstalled = "/home/francisco_javier/.local/share/torbrowser"
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
#array = fe.get_nodes_info()
#for i in range(len(array)):
#    print(wr.curl_nodes(array[i].id))

#print(wr.curl_nodes('3D5D6178C44537E3692853B344385F6572A55767'))
#print('--------------------------------')
#print(wr.curl_nodes('37EB4C9361D2F80F279B949CB3CB41DA2F46A2FA'))
#print('--------------------------------')
#print(wr.curl_nodes('AE95BDA37A5BB4685FEBB7F06649D6CE949B5316'))
#print('--------------------------------')
#print(wr.curl_nodes('CE9003208A047960246052C604A213C3BF096F61'))
#print('--------------------------------')
#print(wr.curl_nodes('CD39C258265B25EAA4ABA4FDCB2DF98104CAA362'))
#print('--------------------------------')
#print(wr.curl_nodes('69C9BFA0C228AFA0548A9FF9B7C8C229B6AA9FAC'))
#print('--------------------------------')
#print(wr.curl_nodes('050A1245EEC76B7438337BAAF19F4AB0666B375F'))

class initiate:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("./frontend/principal.ui")
        self.ventana.show()
        app.exec()
initiate()