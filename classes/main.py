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

class initiate:
    __cs = CallsSystem()
    __fe = FileExtractions()
    __wr = WebRelatedActions()
    __c_string = Constant()
    __copy_done = False
    __security_copy = ''
    __dir_chosen = ''
    ubication = []
    __download_ubication = None
    __cache_dir = None
    __node_info_array = []

    #Constructor
    def __init__(self):
        self.ubication = self.__fe.get_tor_directory()
        self.__fe.set_ubication(self.ubication[0])
        self.__cs.set_ubication(self.ubication[0])
        self.__node_info_array = self.__fe.get_nodes_info()
        app = QtWidgets.QApplication([])
        self.main_window = uic.loadUi(self.__c_string.ppal_ui_dir)
        self.__show_dialog()
        self.main_window.date_label.setText(self.__c_string.executed_at+self.__cs.get_date())
        self.main_window.actionTor_info.triggered.connect(self.__tor_information)
        self.main_window.actionTorrc.triggered.connect(self.__torrc_info)
        self.main_window.actionCompatibility.triggered.connect(self.__compatibility_info)
        self.main_window.actionpreferences.triggered.connect(self.__preferences_info)
        self.main_window.actionExit.triggered.connect(self.__action_exit)
        self.main_window.actionManage_Files_Forensic.triggered.connect(self.__manage_file_forensic)
        self.main_window.actionShow_Nodes_Info.triggered.connect(self.__nodes_info_window)
        self.main_window.actionHelp.triggered.connect(self.__action_help)
        self.main_window.actionGitHub_Repository.triggered.connect(self.__action_GitHub)
        self.main_window.actionMake_security_copy.triggered.connect(self.__make_security_copy)
        self.main_window.actionOpen_security_copy.triggered.connect(self.__open_security_copy)
        self.main_window.action_ia.triggered.connect(self.__open_manageIA)
        self.main_window.show()
        app.exec()

    def __show_dialog(self):
        text1 = self.__c_string.dialog1
        text2 = self.__c_string.dialog2
        text3 = self.__c_string.dialog3
        self.dialog = uic.loadUi(self.__c_string.init_dialog_dir)
        self.dialog.info1_label.setText(text1)
        self.dialog.info2_label.setText(text2)
        self.dialog.info3_label.setText(text3)
        self.dialog.cancel_button.clicked.connect(lambda:self.dialog.close())
        self.dialog.okay_button.clicked.connect(self.__make_security_copy)
        self.dialog.show()
    
######## PRINCIPAL MENU ################
    def __tor_information(self):
        work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
        self.info = uic.loadUi(self.__c_string.info_window_dir)
        self.info.table.setColumnWidth(0,700)
        self.__load_tor_info_data(self.info,work_directory)
        self.info.open_directory_button.clicked.connect(self.__open_tor_directory)
        self.__download_ubication = self.__cs.download_ubication(work_directory)
        self.__cache_dir = self.__cs.cache_ubication(work_directory)
        self.info.open_download.clicked.connect(self.__show_download_directory)
        self.info.open_cachedir_button.clicked.connect(self.__show_cachedir_directory)
        self.info.show()

    def __load_tor_info_data(self,window,work_directory):
        size = self.__cs.get_size(work_directory)
        information_array = self.__fe.get_update_info()
        hash_value = information_array[11].split("=")[1]
        update_pending = self.__c_string.update_yes + self.__cs.update_pending() if self.__cs.update_pending() != None else self.__c_string.update_no
        node ={'Browser name':information_array[7].split("=")[1]+" "+information_array[8]+" "+information_array[9],'Browser version':information_array[4].split("=")[1],"Version's hash Part I":hash_value[slice(0,len(hash_value)//2)],"Version's hash Part II":hash_value[slice(len(hash_value)//2, len(hash_value))],'Update pending':update_pending,'Previous version':information_array[10].split("=")[1],'Install date':information_array[5].split("=")[1],'Last executed':'"'+self.__fe.last_modified_state_file+'"',"Tor's directory":'"'+self.ubication[0]+'"',"Tor's directory size":'"'+size.split('\t')[0]+'"'}
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
    
    def __torrc_info(self):
        work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
        self.torrc_info = uic.loadUi("./frontend/torrcWindow.ui")
        torrc = self.__cs.get_file(work_directory,'torrc')
        array_torrc = self.__fe.get_torrc_info(torrc)
        text = self.__c_string.torrc_user.format(self.__cs.get_user())
        for i in range(1,len(array_torrc)):
           text += "  "+str(i)+". "+array_torrc[i]+"\n\n"
        self.torrc_info.torrc_label.setText(text)
        self.torrc_info.show()

    def __compatibility_info(self):
        work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
        self.comp_info = uic.loadUi("./frontend/compatibilityWindow.ui")
        info = self.__cs.get_file(work_directory,'compatibility.ini')
        array_info = self.__fe.get_torrc_info(info)
        text = self.__c_string.compatibility_string
        for i in range(1,len(array_info)):
           text += "  "+str(i)+". "+array_info[i]+"\n\n"
        self.comp_info.content_label.setText(text)
        self.comp_info.show()
    
    def __preferences_info(self):
        work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
        self.pref_info = uic.loadUi("./frontend/prefsWindow.ui")
        info = self.__cs.get_file(work_directory,'prefs.js')
        array_info = self.__fe.get_preferences_info(info)
        text = self.__c_string.compatibility_string
        for i in range(2,len(array_info)):
            text += "  "+str(i-1)+". "+array_info[i]+"\n\n"
        self.pref_info.content_label.setText(text)
        self.pref_info.show()

    def __action_exit(self):
        sys.exit()

######## FILE FORENSIC MENU ################
    def __manage_file_forensic(self):
        self.management = uic.loadUi(self.__c_string.info_manage_dir)
        self.management.intro_label.setText(self.__c_string.intro_manage)
        self.management.open_sql_viewer.clicked.connect(self.open_sql_viewer)
        self.management.artifacts_dir.clicked.connect(self.open_artifacts_dir)
        self.__fill_artifacts_label()
        self.management.bookmarks_dir.clicked.connect(self.open_bookmarks_dir)
        self.management.bookmarks_viewer.clicked.connect(self.open_bookmarks_viewer)
        
        self.management.show()

    def open_sql_viewer(self):
        self.__wr.open_sql_viewer()

    def open_bookmarks_dir(self):
        if(self.__copy_done):
            work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
            self.__cs.open_directory(self.__cs.bookmarks_backup_ubication(work_directory))
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)

    def open_artifacts_dir(self):
        if(self.__copy_done):
            work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
            self.__cs.open_directory(self.__fe.get_artifacts_directory(work_directory))
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)
        
    def open_bookmarks_viewer(self):
        self.__wr.open_bookmarks_viewer()

######## NODE INFO MENU ################
    def __nodes_info_window(self):
        self.management = uic.loadUi(self.__c_string.info_nodes_info_dir)
        self.__column_config(self.management)
        self.management.browser_button.clicked.connect(self.__show_detailed_nodes)
        self.__load_data(self.management)
        self.management.show()

######## MORE MENU ################       
    def __action_help(self):
       self.help = uic.loadUi(self.__c_string.info_help_window_dir)
       self.help.help_label.setText(self.__cs.get_readme_file(self.__c_string.info_readme_dir))
       self.help.show()

    def __action_GitHub(self):
        self.__wr.open_repository()

    def __open_security_copy(self):
        dir_path = str(QtWidgets.QFileDialog.getExistingDirectory(None,self.__c_string.copy_title))
        if(dir_path!=''):
            self.__security_copy = dir_path+'/tbb'
            self.__dir_chosen = dir_path
            self.__copy_done = True
    
    def __make_security_copy(self):
        dir_path = str(QtWidgets.QFileDialog.getExistingDirectory(None,self.__c_string.copy_title))
        if(dir_path!=''):
            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.__cs.copy_directory(self.ubication[0],dir_path)
            self.__cs.calculate_hash256(self.ubication[0],dir_path,1)
            self.__cs.calculate_hashmd5(self.ubication[0],dir_path,1)
            self.dialog.close()
            self.__security_copy = dir_path+'/tbb'
            self.__copy_done = True
            QApplication.restoreOverrideCursor() 
######## MANAGE IA DIALOG ################ 
    def __open_manageIA(self):   
        self.IA = uic.loadUi(self.__c_string.ia_manage_dir)
        if(self.__dir_chosen !=''):
            find1 = self.__cs.get_file(self.__dir_chosen, 'hashes256.txt.asc')
            find2 = self.__cs.get_file(self.__dir_chosen, 'hashesmd5.txt.asc')   
            if(find1 == '' or find2 == ''):
                self.__show_error_dialog(self.__c_string.not_find_hashes_files)
            else:
                self.IA.manage_IA_info_label.setText(self.__c_string.intro_ia)
                self.IA.SHA256_sign_label.setText(self.__get_sign_text('SHA256'))
                self.IA.MD5_sign_label.setText(self.__get_sign_text('MD5'))
                self.IA.verify_sha256.clicked.connect(lambda: self.__search_hashes('SHA256'))
                self.IA.verify_MD5.clicked.connect(lambda: self.__search_hashes('MD5'))
                self.IA.compare_sha256.clicked.connect(lambda: self.__compare_hashes('SHA256'))
                self.IA.compare_md5.clicked.connect(lambda: self.__compare_hashes('MD5'))
                self.IA.show()
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)
        
######## ERROR DIALOG ################ 
    def __show_error_dialog(self,text):
        self.dialog = uic.loadUi(self.__c_string.error_dialog_dir)
        self.dialog.error_label.setText('"'+text+'"')
        self.dialog.okay_button.clicked.connect(lambda:self.dialog.close())
        self.dialog.show()

######## HASHES DIALOGS ################ 
    def __show_not_found_dialog(self,text):
        self.dialog = uic.loadUi(self.__c_string.hashes_not_found_dialog_dir)
        self.dialog.message_label.setText('"'+text+'"')
        self.dialog.show()

    def __show_found_dialog(self,text,dir):
        self.dialog = uic.loadUi(self.__c_string.hashes_found_dialog_dir)
        self.dialog.message_label.setText('"'+text+'"')
        self.dialog.open_dir.clicked.connect(lambda: self.__cs.open_directory(dir))
        self.dialog.show()

######## AUXILIAR FUNTIONS ################     
    def __open_tor_directory(self):
        if(self.__copy_done):
            self.__cs.open_directory(self.__security_copy)
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)
    
    def __show_download_directory(self):
        if(self.__copy_done):
             self.__cs.open_directory(self.__download_ubication)
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)

    def __show_cachedir_directory(self):
        if(self.__copy_done):
            self.__cs.open_directory(self.__cache_dir)
        else:
            self.__show_error_dialog(self.__c_string.error_dialog)
    
    def __load_data(self,window):
        nodes = []
        for i in range(len(self.__node_info_array)):
            node ={'Nickname':self.__node_info_array[i].nickname,'FingerPrint':self.__node_info_array[i].id,'Sampled on':str(self.__node_info_array[i].sampled_on),'Listed':str(self.__node_info_array[i].listed),'Unlisted since':str(self.__node_info_array[i].unlisted_since)}
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

    def __show_detailed_nodes(self):
        info = self.__wr.curl_nodes(self.management.browser.text())
        if(info==None):
            self.__style_label(True)
            self.management.more_info_label.setText(self.__c_string.no_available_error)
        else:
            self.__style_label(False)
            header_list = ['Nickname','URL','e-mail','Exit Address','Observed Bandwidth','Consensus Weight','Last Restarted',
            'Country','First Seen','Fingerprint']
            text=''
            for i in range(0,len(info)-1):
                information = self.__c_string.null_data
                if(info[i] != None):
                    information = info[i]
                text+=header_list[i]+'\n>> '+information+'\n\n'
            self.management.more_info_label.setText(text)

    def __column_config(self,object):
        object.table.setColumnWidth(0,160)
        object.table.setColumnWidth(1,290)
        object.table.setColumnWidth(2,150)
        object.table.setColumnWidth(3,50)
        object.table.setColumnWidth(4,140)

    def __style_label(self,is_none):
        if(is_none):
            self.management.more_info_label.setStyleSheet("color: red")
            self.management.more_info_label.setAlignment(Qt.AlignCenter)
        else:
            self.management.more_info_label.setStyleSheet("color: black")
            self.management.more_info_label.setAlignment(Qt.AlignLeft)

    def __fill_artifacts_label(self):
        work_directory = self.__security_copy if(self.__copy_done == True) else self.ubication[0]
        array = self.__fe.get_artifacts_information(work_directory)
        text = ''
        for i in range(len(array)):
            text += str(i+1)+'. '+array[i]+'\n'
        self.management.artifacts_label.setText(text)

    def __get_sign_text(self,type):
        file = self.__c_string.file_hash256_asc if(type == 'SHA256') else self.__c_string.file_hashmd5_asc
        sign_value = self.__fe.get_hashes_sign(self.__dir_chosen+file)
        text = sign_value[slice(0,len(sign_value)//6)]+'\n'+sign_value[slice(len(sign_value)//6, 2*len(sign_value)//6)] + '\n' + sign_value[slice(2*len(sign_value)//6,3*len(sign_value)//6)] + '\n' + sign_value[slice(3*len(sign_value)//6,4*len(sign_value)//6)] + '\n' + sign_value[slice(4*len(sign_value)//6,5*len(sign_value)//6)]+ '\n' + sign_value[slice(5*len(sign_value)//6,len(sign_value))]
        return text

    #9a13bcc810c3eac12a8c45362e93edd54443566df171bac1
    def __search_hashes(self,type):
        file = self.__c_string.file_hash256 if(type == 'SHA256') else self.__c_string.file_hashmd5  
        result = self.__cs.search_hashes_in_file(self.__dir_chosen,self.IA.hash_field.text(),file)
        if(result == ''):
            self.__show_not_found_dialog(self.__c_string.no_matches_text.format(file))
        else:
            split_array = result.split('/')
            result = split_array[len(split_array)-1]
            split_array.pop(0)
            split_array.pop(len(split_array)-1)
            path = '/'
            for i in range(len(split_array)):
                path += split_array[i]+'/' if(i != (len(split_array)-1)) else split_array[i]
            self.__show_found_dialog(self.__c_string.matches_found_text.format(result),path)


    def __compare_hashes(self,type):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        file = self.__c_string.file_hash256 if(type == 'SHA256') else self.__c_string.file_hashmd5
        aux_file = self.__c_string.aux_hash256 if(type == 'SHA256') else self.__c_string.aux_hashmd5
        if(type == 'SHA256'):
            self.__cs.calculate_hash256(self.ubication[0],'.',2)
        else:
            self.__cs.calculate_hashmd5(self.ubication[0],'.',2)
        #Comparamos los datos llamando a diff
        text = self.__cs.diff_in_file('.'+aux_file,self.__dir_chosen+file) #'/prueba.txt'
        if(text!=""):
            self.__cs.write_diff_results(self.__c_string.explanation_text+text+'"',self.__dir_chosen,type)
        else:
            self.__cs.write_diff_results(self.__c_string.same_hashes_text,self.__dir_chosen,type)
        #eliminamos el archivo auxiliar
        self.__cs.delete_file('.'+aux_file)
        QApplication.restoreOverrideCursor()
        self.__cs.open_directory(self.__dir_chosen+self.__c_string.diff_dir)



#LAUNCH PROGRAM     
initiate()