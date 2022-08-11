#Clase de prueba en la que se realizarán llamadas a otras clases
from this import s
from callsSystem import CallsSystem
from fileExtractions import FileExtractions
from webRelatedActions import WebRelatedActions
from PyQt5 import QtWidgets,uic
import sys
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
    copy_done = False
    security_copy = ''
    ubication = []
    node_info_array = []

    #Constructor
    def __init__(self):
        self.ubication = self.fe.get_tor_directory()
        self.node_info_array = self.fe.get_nodes_info()
        app = QtWidgets.QApplication([])
        self.main_window = uic.loadUi("./frontend/principal.ui")
        self.showDialog()
        self.main_window.date_label.setText('Executed at: '+self.cs.get_date())
        self.main_window.actionTor_info.triggered.connect(self.tor_information)
        self.main_window.actionTorrc.triggered.connect(self.torrc_info)
        self.main_window.actionExit.triggered.connect(self.action_exit)
        self.main_window.actionManage_Files_Forensic.triggered.connect(self.manage_file_forensic)
        self.main_window.actionOpen_Web_Viewer.triggered.connect(self.open_sql_viewer)
        self.main_window.actionShow_Nodes_Info.triggered.connect(self.nodes_info_window)
        self.main_window.actionHelp.triggered.connect(self.action_help)
        self.main_window.actionGitHub_Repository.triggered.connect(self.action_GitHub)
        self.main_window.show()
        app.exec()


        #TODO:Al iniciar mostrar una ventana con el arbol de directorio donde copiar la carpeta
        #Iniciar el árbol de directorio
    def showDialog(self):
        text1 = ' To preserve the evidence of the equipment under\n investigation, it is important to make a copy.'
        text2 = ' Canceling this operation could damage evidence\n and invalidate any judicial investigation.'
        text3 = '----WARNING!----'
        self.dialog = uic.loadUi("./frontend/initialDialogBox.ui")
        self.dialog.info1_label.setText(text1)
        self.dialog.info2_label.setText(text2)
        self.dialog.info3_label.setText(text3)
        self.dialog.cancel_button.clicked.connect(lambda:self.dialog.close())
        self.dialog.okay_button.clicked.connect(self.make_security_copy)
        self.dialog.show()
           

        #TODO: REVISAR QUE SI SE CIERRA LA PESTAÑA, SE CIERRE LA APP COMPLETA.
    
    def make_security_copy(self):
        dir_path = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select destination directory"))
        if(dir_path!=''):
            self.cs.copy_directory(self.ubication[0],dir_path)
            self.cs.calculate_hash256(self.ubication[0],dir_path)
            self.cs.calculate_hashmd5(self.ubication[0],dir_path)
            self.dialog.close()
            self.security_copy = dir_path+'/tbb'
            self.copy_done = True


######## PRINCIPAL MENU ################
    def tor_information(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.info = uic.loadUi("./frontend/infoWindow.ui")
        information_array = self.fe.get_update_info()
        size = self.cs.get_size(work_directory)
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
        self.info.open_directory_button.clicked.connect(self.open_tor_directory)
        self.info.show()
    
    def torrc_info(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.torrc_info = uic.loadUi("./frontend/torrcWindow.ui")
        torrc = self.cs.get_torrc_file(work_directory,'torrc')
        array_torrc = self.fe.get_torrc_info(torrc)
        text = 'The content of the torrc file for user {} is shown in the following list: \n\n'.format(self.cs.get_user())
        for i in range(1,len(array_torrc)):
           text += "  "+str(i)+". "+array_torrc[i]+"\n\n"
        self.torrc_info.torrc_label.setText(text)
        self.torrc_info.show()

    def action_exit(self):
        sys.exit()


######## FILE FORENSIC MENU ################
    def manage_file_forensic(self):
        self.management = uic.loadUi("./frontend/manageFiles.ui")
        #TODO: OPERACIONES CON MANAGE
        self.management.show()
    def open_sql_viewer(self):
        self.wr.open_sql_viewer()

######## NODE INFO MENU ################
    def nodes_info_window(self):
        self.management = uic.loadUi("./frontend/nodesInfo.ui")
        #TODO: OPERACIONES CON NODOS
        self.management.show()


######## MORE MENU ################       
    def action_help(self):
       self.help = uic.loadUi("./frontend/helpWindow.ui")
       self.help.help_label.setText(self.cs.get_readme_file('./extraFiles/readme.txt'))
       self.help.show()

    def action_GitHub(self):
        self.wr.open_repository()
    

######## AUXILIAR FUNTIONS ################     
    def open_tor_directory(self):
        self.cs.open_directory(self.ubication[0])

#LAUNCH PROGRAM       
initiate()