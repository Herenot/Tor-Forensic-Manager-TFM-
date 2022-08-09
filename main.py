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
    cs = CallsSystem()
    fe = FileExtractions()
    wr = WebRelatedActions()
    ubication = []
    node_info_array = []
    def __init__(self):
        self.ubication = self.fe.get_tor_directory()
        self.node_info_array = self.fe.get_nodes_info()
        self.cs.calculate_hash256(self.ubication[0],'.')
        self.cs.calculate_hashmd5(self.ubication[0],'.')
        app = QtWidgets.QApplication([])
        self.main_window = uic.loadUi("./frontend/principal.ui")
        self.main_window.actionExit.triggered.connect(self.action_exit)
        self.main_window.actionTor_info.triggered.connect(self.tor_information)
        self.main_window.actionTorrc.triggered.connect(self.torrc_info)
        self.main_window.actionHelp.triggered.connect(self.action_help)
        self.main_window.actionGitHub_Repository.triggered.connect(self.action_GitHub)
        self.main_window.show()
        app.exec()


        #Al iniciar mostrar una ventana con el arbol de directorio donde copiar la carpeta
        #Iniciar el árbol de directorio

    def action_exit(self):
        sys.exit()

    def action_help(self):
       self.help = uic.loadUi("./frontend/helpWindow.ui")
       #self.help.readme_label.setText(self.cs.get_readme_file('./extraFiles/readme.txt'))
       #self.help.scrollArea.setWidget(self.help.readme_label)
       self.help.show()

    def action_GitHub(self):
        self.wr.open_repository()
        

    def tor_information(self):
        self.info = uic.loadUi("./frontend/infoWindow.ui")
        information_array = self.fe.get_update_info()
        
        size = self.cs.get_size(self.ubication[0])
        self.info.where_installed_label.setText('"'+self.ubication[0]+'"')
        self.info.name_label.setText(information_array[7].split("=")[1]+" "+information_array[8]+" "+information_array[9])
        self.info.actual_version_label.setText(information_array[4].split("=")[1])
        self.info.install_date_label.setText(information_array[5].split("=")[1])
        update_pending = 'Yes, ' + self.cs.update_pending() if self.cs.update_pending() != None else 'No pending updates'
        self.info.update_pending_label.setText(update_pending)
        self.info.previous_version_label.setText(information_array[10].split("=")[1])
        hash_value = information_array[11].split("=")[1]
        self.info.hash_label1.setText(hash_value[slice(0,len(hash_value)//2)])
        self.info.hash_label2.setText(hash_value[slice(len(hash_value)//2, len(hash_value))])
        self.info.size_label.setText('"'+size.split('\t')[0]+'"')
        self.info.last_execution_label.setText('"'+self.fe.last_modified_state_file+'"')
        self.info.show()

    def torrc_info(self):
        self.info = uic.loadUi("./frontend/torrcWindow.ui")
        torrc = self.cs.get_torrc_file(self.ubication[0],'torrc')
        print(self.fe.get_torrc_info(torrc))
        self.info.show()
        
initiate()