from callsSystem import CallsSystem
from datetime import datetime
from PIL import Image
import re
class FileExtractions:
    update_array =[]
    cs = CallsSystem()

    def get_hashes_sign(self,file):
        with open(file) as f:
            lines = [x.split() for x in f.read().split("-----BEGIN PGP SIGNATURE-----") if x]
        for i in range(3):
            del lines[1][len(lines[1])-1]
        return "".join(lines[1])

    # Se obtiene tambi'en el hash de la actualización para verificar la veracidad de la misma
    def get_update_info(self):
        update_file = self.cs.get_update_info()
        with open(update_file) as f:
            lines = [x.split() for x in f.read().split('xmlns="http://www.mozilla.org/2005/app-update"') if x]
        for i in range(11):
            if(i==5):
                x =lines[2][i].split("=")[1].split('"')[1]
                ts = int(x)
                lines[2][i] = ''.join('installDate="'+datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')+'"')
            self.update_array.append(lines[2][i]);
        self.update_array.append(lines[2][24]);
        self.update_array.append(lines[2][25]);
        return self.update_array

    def open_images(self, image_path):
        im = Image.open(image_path)
        im.show()
    
    #Función que permite la visualización de información del usuario en el fichero torrc
    def get_torrc_info(self,file):
        torrc = open(file,'r')
        file_evidence = open('./data.txt','w')
        for line in torrc.readlines():
            started_with = re.findall("^#",line)
            if not started_with:
                file_evidence.write(line)
        torrc.close()
        file_evidence.close()
        with open('./data.txt') as f:
            lines = [line.rstrip() for line in f]
        self.cs.delete_file('./data.txt')
        return lines
    
    def num_lines_in_file(self,file):
        with open(file, 'r') as fp:
            lines = len(fp.readlines())
        print(lines)

