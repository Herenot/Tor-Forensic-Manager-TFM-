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
    def is_installed_tor_and_where(self,function,type): #Le pueden pasar is or where
       system("chmod +x shellScripts/scripts.sh")
       system("./shellScripts/scripts.sh "+ function + " " + type)

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

    #Función que permite abrir un directorio, se puede usar para abrir los archivos sql
    def open_directory(self,path):
        try:
            os.startfile(path)
        except:
            subprocess.Popen(['xdg-open', path])
    