from os import system
import os
import subprocess
# Clase en la que se llevarán a cabo las llamadas al sistema operativo
# source es la ruta absoluta donde se encuentra el navegador
# destination es la ruta absoluta donde se quieren almacenar las salidas
class CallsSystem:
    where_installed = "/home/francisco_javier/Desktop/pruebas/torbrowser"
    hash256_file = "/hashes256.txt"
    hashmd5_file = "/hashesmd5.txt"

    def where_is_tor(self): #Le pueden pasar is or where
       return subprocess.getoutput([self.find_element_and_store_output('/',"tbb")])

    def find_element_and_store_output(self,directory,file):
        return 'find {} -name {} > ./find_elements.txt'.format(directory,file)

    def calculate_hash256(self,source,destination):
        self.delete_file(destination+self.hash256_file+".asc")
        system("find "+ source +"/ -type f -print0  | xargs -0 sha256sum > "+destination+self.hash256_file)
        system("gpg --clearsign "+destination+self.hash256_file)

    def calculate_hashmd5(self,source,destination):
        self.delete_file(destination+self.hashmd5_file+".asc")
        system("find "+ source +"/ -type f -print0  | xargs -0 md5sum > "+destination+self.hashmd5_file)
        system("gpg --clearsign "+destination+self.hashmd5_file)

    def copy_directory(self,source,destination):
        system("cp -rf "+source+" "+destination)

    def delete_file(self,file):
        system("rm -f "+file)

    def get_directory(self):
        return self.where_installed;

    def find_element(self,directory,file):
        return 'find {} -name {}'.format(directory,file)

    def get_update_info_location(self):
        return subprocess.getoutput([self.find_element(self.where_installed,"updates.xml")])
    
    def get_torrc_file(self,directory,file):
        return subprocess.getoutput([self.find_element(directory,"torrc")])

    def files_downloaded(self):
        directory = subprocess.getoutput([self.find_element(self.where_installed,"Downloads")])
        return subprocess.getoutput('ls -lRah {}'.format(directory))

    #Si no devuelve nada, entonces no hay actualización, si devuelve, si la hay
    def update_pending(self):
        next_version = None;
        pending = subprocess.getoutput([self.find_element(self.where_installed,"active-updates.xml")])
        if(pending != ""):
            version_file = subprocess.getoutput([self.find_element(self.where_installed,"update.version")])
            next_version = subprocess.getoutput('cat {}'.format(version_file))
        return next_version

    def get_user(self):
        return subprocess.getoutput('who')

    def get_date(self):
        return subprocess.getoutput('date')

    def get_readme_file(self,file):
        return subprocess.getoutput('cat '+file)

    #Función que permite abrir un directorio, se puede usar para abrir los archivos sql
    def open_directory(self,path):
        try:
            os.startfile(path)
        except:
            subprocess.Popen(['xdg-open', path])
            
    def mum_of_ocurrences(self,word,file):
        return subprocess.getoutput('echo "'+word+'" | wc -l '+file);

    def get_size(self,file):
         return subprocess.getoutput('du -sh '+file);
        