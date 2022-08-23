#Clase de prueba en la que se realizarán llamadas a otras clases
from this import s
from callsSystem import CallsSystem
from fileExtractions import FileExtractions
from webRelatedActions import WebRelatedActions
from constantStrings import Constant
from PyQt5 import QtWidgets,uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
#sign256 = fe.obtain_hashes_sign(destination+"/hashes256.txt.asc")
#signmd5 = fe.obtain_hashes_sign(destination+"/hashesmd5.txt.asc")

class initiate:
    cs = CallsSystem()
    fe = FileExtractions()
    wr = WebRelatedActions()
    c_string = Constant()
    copy_done = False
    security_copy = ''
    dir_chosen = ''
    ubication = []
    download_ubication = None
    cache_dir = None
    node_info_array = []

    #Constructor
    def __init__(self):
        self.ubication = self.fe.get_tor_directory()
        self.fe.set_ubication(self.ubication[0])
        self.cs.set_ubication(self.ubication[0])
        self.node_info_array = self.fe.get_nodes_info()
        app = QtWidgets.QApplication([])
        self.main_window = uic.loadUi(self.c_string.ppal_ui_dir)
        self.show_dialog()
        self.main_window.date_label.setText(self.c_string.executed_at+self.cs.get_date())
        self.main_window.actionTor_info.triggered.connect(self.tor_information)
        self.main_window.actionTorrc.triggered.connect(self.torrc_info)
        self.main_window.actionCompatibility.triggered.connect(self.compatibility_info)
        self.main_window.actionpreferences.triggered.connect(self.preferences_info)
        self.main_window.actionExit.triggered.connect(self.action_exit)
        self.main_window.actionManage_Files_Forensic.triggered.connect(self.manage_file_forensic)
        self.main_window.actionShow_Nodes_Info.triggered.connect(self.nodes_info_window)
        self.main_window.actionHelp.triggered.connect(self.action_help)
        self.main_window.actionGitHub_Repository.triggered.connect(self.action_GitHub)
        self.main_window.actionMake_security_copy.triggered.connect(self.make_security_copy)
        self.main_window.actionOpen_security_copy.triggered.connect(self.open_security_copy)
        self.main_window.action_ia.triggered.connect(self.open_manageIA)
        self.main_window.show()
        app.exec()

    def show_dialog(self):
        text1 = self.c_string.dialog1
        text2 = self.c_string.dialog2
        text3 = self.c_string.dialog3
        self.dialog = uic.loadUi(self.c_string.init_dialog_dir)
        self.dialog.info1_label.setText(text1)
        self.dialog.info2_label.setText(text2)
        self.dialog.info3_label.setText(text3)
        self.dialog.cancel_button.clicked.connect(lambda:self.dialog.close())
        self.dialog.okay_button.clicked.connect(self.make_security_copy)
        self.dialog.show()
    
######## PRINCIPAL MENU ################
    def tor_information(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.info = uic.loadUi(self.c_string.info_window_dir)
        self.info.table.setColumnWidth(0,700)
        self.load_tor_info_data(self.info,work_directory)
        self.info.open_directory_button.clicked.connect(self.open_tor_directory)
        self.download_ubication = self.cs.download_ubication(work_directory)
        self.cache_dir = self.cs.cache_ubication(work_directory)
        self.info.open_download.clicked.connect(self.show_download_directory)
        self.info.open_cachedir_button.clicked.connect(self.show_cachedir_directory)
        self.info.show()

    def load_tor_info_data(self,window,work_directory):
        size = self.cs.get_size(work_directory)
        information_array = self.fe.get_update_info()
        hash_value = information_array[11].split("=")[1]
        update_pending = self.c_string.update_yes + self.cs.update_pending() if self.cs.update_pending() != None else self.c_string.update_no
        node ={'Browser name':information_array[7].split("=")[1]+" "+information_array[8]+" "+information_array[9],'Browser version':information_array[4].split("=")[1],"Version's hash Part I":hash_value[slice(0,len(hash_value)//2)],"Version's hash Part II":hash_value[slice(len(hash_value)//2, len(hash_value))],'Update pending':update_pending,'Previous version':information_array[10].split("=")[1],'Install date':information_array[5].split("=")[1],'Last executed':'"'+self.fe.last_modified_state_file+'"',"Tor's directory":'"'+self.ubication[0]+'"',"Tor's directory size":'"'+size.split('\t')[0]+'"'}
        window.table.setItem(0,0,QtWidgets.QTableWidgetItem(node['Browser name']))
        window.table.setItem(0,1,QtWidgets.QTableWidgetItem(node['Browser version']))
        window.table.setItem(0,2,QtWidgets.QTableWidgetItem(node["Version's hash Part I"]))
        window.table.setItem(0,3,QtWidgets.QTableWidgetItem(node["Version's hash Part II"]))
        window.table.setItem(0,4,QtWidgets.QTableWidgetItem(node['Update pending']))
        window.table.setItem(0,5,QtWidgets.QTableWidgetItem(node['Previous version']))
        window.table.setItem(0,6,QtWidgets.QTableWidgetItem(node['Install date']))
        window.table.setItem(0,7,QtWidgets.QTableWidgetItem(node['Last executed']))
        window.table.setItem(0,8,QtWidgets.QTableWidgetItem(node["Tor's directory"]))
        window.table.setItem(0,9,QtWidgets.QTableWidgetItem(node["Tor's directory size"]))
    
    def torrc_info(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.torrc_info = uic.loadUi("./frontend/torrcWindow.ui")
        torrc = self.cs.get_file(work_directory,'torrc')
        array_torrc = self.fe.get_torrc_info(torrc)
        text = self.c_string.torrc_user.format(self.cs.get_user())
        for i in range(1,len(array_torrc)):
           text += "  "+str(i)+". "+array_torrc[i]+"\n\n"
        self.torrc_info.torrc_label.setText(text)
        self.torrc_info.show()

    def compatibility_info(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.comp_info = uic.loadUi("./frontend/compatibilityWindow.ui")
        info = self.cs.get_file(work_directory,'compatibility.ini')
        array_info = self.fe.get_torrc_info(info)
        text = self.c_string.compatibility_string
        for i in range(1,len(array_info)):
           text += "  "+str(i)+". "+array_info[i]+"\n\n"
        self.comp_info.content_label.setText(text)
        self.comp_info.show()
    
    def preferences_info(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        self.pref_info = uic.loadUi("./frontend/prefsWindow.ui")
        info = self.cs.get_file(work_directory,'prefs.js')
        array_info = self.fe.get_preferences_info(info)
        text = self.c_string.compatibility_string
        for i in range(2,len(array_info)):
            text += "  "+str(i-1)+". "+array_info[i]+"\n\n"
        self.pref_info.content_label.setText(text)
        self.pref_info.show()

    def action_exit(self):
        sys.exit()

######## FILE FORENSIC MENU ################
    def manage_file_forensic(self):
        self.management = uic.loadUi(self.c_string.info_manage_dir)
        self.management.intro_label.setText(self.c_string.intro_manage)
        self.management.open_sql_viewer.clicked.connect(self.open_sql_viewer)
        self.management.artifacts_dir.clicked.connect(self.open_artifacts_dir)
        self.fill_artifacts_label()
        self.management.bookmarks_dir.clicked.connect(self.open_bookmarks_dir)
        self.management.bookmarks_viewer.clicked.connect(self.open_bookmarks_viewer)
        
        self.management.show()

    def open_sql_viewer(self):
        self.wr.open_sql_viewer()

    def open_bookmarks_dir(self):
        if(self.copy_done):
            work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
            self.cs.open_directory(self.cs.bookmarks_backup_ubication(work_directory))
        else:
            self.show_error_dialog(self.c_string.error_dialog)

    def open_artifacts_dir(self):
        if(self.copy_done):
            work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
            self.cs.open_directory(self.fe.get_artifacts_directory(work_directory))
        else:
            self.show_error_dialog(self.c_string.error_dialog)
        
    def open_bookmarks_viewer(self):
        self.wr.open_bookmarks_viewer()

######## NODE INFO MENU ################
    def nodes_info_window(self):
        self.management = uic.loadUi(self.c_string.info_nodes_info_dir)
        self.column_config(self.management)
        self.management.browser_button.clicked.connect(self.show_detailed_nodes)
        self.load_data(self.management)
        self.management.show()

######## MORE MENU ################       
    def action_help(self):
       self.help = uic.loadUi(self.c_string.info_help_window_dir)
       self.help.help_label.setText(self.cs.get_readme_file(self.c_string.info_readme_dir))
       self.help.show()

    def action_GitHub(self):
        self.wr.open_repository()

    def open_security_copy(self):
        dir_path = str(QtWidgets.QFileDialog.getExistingDirectory(None,self.c_string.copy_title))
        if(dir_path!=''):
            self.security_copy = dir_path+'/tbb'
            self.dir_chosen = dir_path
            self.copy_done = True
    
    def make_security_copy(self):
        dir_path = str(QtWidgets.QFileDialog.getExistingDirectory(None,self.c_string.copy_title))
        if(dir_path!=''):
            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.cs.copy_directory(self.ubication[0],dir_path)
            self.cs.calculate_hash256(self.ubication[0],dir_path,1)
            self.cs.calculate_hashmd5(self.ubication[0],dir_path,1)
            self.dialog.close()
            self.security_copy = dir_path+'/tbb'
            self.copy_done = True
            QApplication.restoreOverrideCursor() 
######## MANAGE IA DIALOG ################ 
    def open_manageIA(self):
       # self.show_not_found_dialog('PRUEBA NO OKAY')
       # self.show_found_dialog('PRUEBA OKAY')        
        self.IA = uic.loadUi(self.c_string.ia_manage_dir)
        if(self.dir_chosen !=''):
            find1 = self.cs.get_file(self.dir_chosen, 'hashes256.txt.asc')
            find2 = self.cs.get_file(self.dir_chosen, 'hashesmd5.txt.asc')   
            if(find1 == '' or find2 == ''):
                self.show_error_dialog(self.c_string.not_find_hashes_files)
            else:
                self.IA.manage_IA_info_label.setText(self.c_string.intro_ia)
                self.IA.SHA256_sign_label.setText(self.get_sign_text('SHA256'))
                self.IA.MD5_sign_label.setText(self.get_sign_text('MD5'))
                self.IA.verify_sha256.clicked.connect(lambda: self.search_hashes('SHA256'))
                self.IA.verify_MD5.clicked.connect(lambda: self.search_hashes('MD5'))
                self.IA.compare_sha256.clicked.connect(lambda: self.compare_hashes('SHA256'))
                self.IA.compare_md5.clicked.connect(lambda: self.compare_hashes('MD5'))
                self.IA.show()
        else:
            self.show_error_dialog(self.c_string.error_dialog)
        
######## ERROR DIALOG ################ 
    def show_error_dialog(self,text):
        self.dialog = uic.loadUi(self.c_string.error_dialog_dir)
        self.dialog.error_label.setText('"'+text+'"')
        self.dialog.okay_button.clicked.connect(lambda:self.dialog.close())
        self.dialog.show()

######## HASHES DIALOGS ################ 
    def show_not_found_dialog(self,text):
        self.dialog = uic.loadUi(self.c_string.hashes_not_found_dialog_dir)
        self.dialog.message_label.setText('"'+text+'"')
        self.dialog.show()

    def show_found_dialog(self,text,dir):
        self.dialog = uic.loadUi(self.c_string.hashes_found_dialog_dir)
        self.dialog.message_label.setText('"'+text+'"')
        self.dialog.open_dir.clicked.connect(lambda: self.cs.open_directory(dir))
        self.dialog.show()

######## AUXILIAR FUNTIONS ################     
    def open_tor_directory(self):
        if(self.copy_done):
            self.cs.open_directory(self.security_copy)
        else:
            self.show_error_dialog(self.c_string.error_dialog)
    
    def show_download_directory(self):
        if(self.copy_done):
             self.cs.open_directory(self.download_ubication)
        else:
            self.show_error_dialog(self.c_string.error_dialog)

    def show_cachedir_directory(self):
        if(self.copy_done):
            self.cs.open_directory(self.cache_dir)
        else:
            self.show_error_dialog(self.c_string.error_dialog)
    
    def load_data(self,window):
        nodes = []
        for i in range(len(self.node_info_array)):
            node ={'Nickname':self.node_info_array[i].nickname,'FingerPrint':self.node_info_array[i].id,'Sampled on':str(self.node_info_array[i].sampled_on),'Listed':str(self.node_info_array[i].listed),'Unlisted since':str(self.node_info_array[i].unlisted_since)}
            nodes.append(node)
        row = 0
        window.table.setRowCount(len(nodes))
        for n in nodes:
            window.table.setItem(row,0,QtWidgets.QTableWidgetItem(n['Nickname']))
            window.table.setItem(row,1,QtWidgets.QTableWidgetItem(n['FingerPrint']))
            window.table.setItem(row,2,QtWidgets.QTableWidgetItem(n['Sampled on']))
            window.table.setItem(row,3,QtWidgets.QTableWidgetItem(n['Listed']))
            window.table.setItem(row,4,QtWidgets.QTableWidgetItem(n['Unlisted since']))
            row+=1

    def show_detailed_nodes(self):
        info = self.wr.curl_nodes(self.management.browser.text())
        if(info==None):
            self.style_label(True)
            self.management.more_info_label.setText(self.c_string.no_available_error)
        else:
            self.style_label(False)
            header_list = ['Nickname','URL','e-mail','Exit Address','Observed Bandwidth','Consensus Weight','Last Restarted',
            'Country','First Seen','Fingerprint']
            text=''
            for i in range(0,len(info)-1):
                information = self.c_string.null_data
                if(info[i] != None):
                    information = info[i]
                text+=header_list[i]+'\n>> '+information+'\n\n'
            self.management.more_info_label.setText(text)

    def column_config(self,object):
        object.table.setColumnWidth(0,160)
        object.table.setColumnWidth(1,290)
        object.table.setColumnWidth(2,150)
        object.table.setColumnWidth(3,50)
        object.table.setColumnWidth(4,140)

    def style_label(self,is_none):
        if(is_none):
            self.management.more_info_label.setStyleSheet("color: red")
            self.management.more_info_label.setAlignment(Qt.AlignCenter)
        else:
            self.management.more_info_label.setStyleSheet("color: black")
            self.management.more_info_label.setAlignment(Qt.AlignLeft)

    def fill_artifacts_label(self):
        work_directory = self.security_copy if(self.copy_done == True) else self.ubication[0]
        array = self.fe.get_artifacts_information(work_directory)
        text = ''
        for i in range(len(array)):
            text += str(i+1)+'. '+array[i]+'\n'
        self.management.artifacts_label.setText(text)

    def get_sign_text(self,type):
        file = self.c_string.file_hash256_asc if(type == 'SHA256') else self.c_string.file_hashmd5_asc
        sign_value = self.fe.get_hashes_sign(self.dir_chosen+file)
        text = sign_value[slice(0,len(sign_value)//6)]+'\n'+sign_value[slice(len(sign_value)//6, 2*len(sign_value)//6)] + '\n' + sign_value[slice(2*len(sign_value)//6,3*len(sign_value)//6)] + '\n' + sign_value[slice(3*len(sign_value)//6,4*len(sign_value)//6)] + '\n' + sign_value[slice(4*len(sign_value)//6,5*len(sign_value)//6)]+ '\n' + sign_value[slice(5*len(sign_value)//6,len(sign_value))]
        return text

    #9a13bcc810c3eac12a8c45362e93edd54443566df171bac1
    def search_hashes(self,type):
        file = self.c_string.file_hash256 if(type == 'SHA256') else self.c_string.file_hashmd5  
        result = self.cs.search_hashes_in_file(self.dir_chosen,self.IA.hash_field.text(),file)
        if(result == ''):
            self.show_not_found_dialog(self.c_string.no_matches_text.format(file))
        else:
            split_array = result.split('/')
            result = split_array[len(split_array)-1]
            split_array.pop(0)
            split_array.pop(len(split_array)-1)
            path = '/'
            for i in range(len(split_array)):
                path += split_array[i]+'/' if(i != (len(split_array)-1)) else split_array[i]
            self.show_found_dialog(self.c_string.matches_found_text.format(result),path)


    def compare_hashes(self,type):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        file = self.c_string.file_hash256 if(type == 'SHA256') else self.c_string.file_hashmd5
        aux_file = self.c_string.aux_hash256 if(type == 'SHA256') else self.c_string.aux_hashmd5
        if(type == 'SHA256'):
            self.cs.calculate_hash256(self.ubication[0],'.',2)
        else:
            self.cs.calculate_hashmd5(self.ubication[0],'.',2)
        #Comparamos los datos llamando a diff
        text = self.cs.diff_in_file('.'+aux_file,self.dir_chosen+file) #'/prueba.txt'
        if(text!=""):
            self.cs.write_diff_results(self.c_string.explanation_text+text+'"',self.dir_chosen,type)
        else:
            self.cs.write_diff_results(self.c_string.same_hashes_text,self.dir_chosen,type)
        #eliminamos el archivo auxiliar
        self.cs.delete_file('.'+aux_file)
        QApplication.restoreOverrideCursor()
        self.cs.open_directory(self.dir_chosen+self.c_string.diff_dir)



#LAUNCH PROGRAM     
initiate()