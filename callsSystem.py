from os import system
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
    def get_update_info(self):
        command = 'find {} -name updates.xml'.format(self.where_installed)
        file = subprocess.getoutput([command])
        return file
    def files_downloaded(self):
        directory = subprocess.getoutput(['find {} -name Downloads'.format(self.where_installed)])
        downloaded_list = subprocess.getoutput('ls -lRah {}'.format(directory)); 
        return downloaded_list
