from callsSystem import CallsSystem
from constantStrings import Constant
from datetime import datetime
from node import Node
from PIL import Image
import subprocess
import re

class FileExtractions:
    update_array =[]
    cs = CallsSystem()
    c_string = Constant()
    offset = 4
    last_modified_state_file = ''
    def set_ubication(self,ubication):
        self.cs.set_ubication(ubication)

    def get_hashes_sign(self,file):
        with open(file) as f:
            lines = [x.split() for x in f.read().split(self.c_string.signature) if x]
        for i in range(3):
            del lines[1][len(lines[1])-1]
        return "".join(lines[1])

    # Se obtiene tambi'en el hash de la actualización para verificar la veracidad de la misma
    def get_update_info(self):
        update_file = self.cs.get_update_info_location()
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
        data_file = self.c_string.aux_data_file
        torrc = open(file,'r')
        file_evidence = open(data_file,'w')
        for line in torrc.readlines():
            started_with = re.findall("^#",line)
            if not started_with:
                file_evidence.write(line)
        torrc.close()
        file_evidence.close()
        with open(data_file) as f:
            lines = [line.rstrip() for line in f]
        self.cs.delete_file(data_file)
        return lines

    
    def get_tor_directory(self):
        data_file = self.c_string.aux_data_file
        self.cs.where_is_tor()
        find_output = open(self.c_string.aux_elements_find_file,'r') 
        file_evidence = open(data_file,'w')
        for line in find_output.readlines():
            started_with = re.findall("^find:",line)
            if not started_with:
                file_evidence.write(line)
        find_output.close()
        file_evidence.close()
        with open(data_file) as f:
            lines = [line.rstrip() for line in f]
        self.cs.delete_file(data_file)
        self.cs.delete_file(self.c_string.aux_elements_find_file)

        return lines


    def get_nodes_info(self):
        file_node = subprocess.getoutput([self.cs.find_element(self.cs.get_directory(),"state")])
        state = open(file_node,'r')
        file_evidence = open(self.c_string.aux_nodes_file,'w')
        for line in state.readlines():
            started_with = re.findall("^#|^CircuitBuildTimeBin|^CircuitBuildAbandonedCount|^Dormant",line)
            if not started_with:
                file_evidence.write(line)
        state.close()
        file_evidence.close()
        with open(self.c_string.aux_nodes_file) as f:
            lines = [line.rstrip() for line in f]
        size = self.cs.mum_of_ocurrences("Guard in",self.c_string.aux_nodes_file).split(" ")[0]
        array_of_nodes = []
        for i in range(1,int(size)-self.offset):
           unlisted_value = lines[i].split(' ')[7].split('=')[1] if lines[i].split(' ')[7].split('=')[1]!='1' else None
           listed = 1 if lines[i].split(' ')[7].split('=')[1]=='1' else 0
           node = Node(lines[i].split(' ')[2].split('=')[1],
           lines[i].split(' ')[3].split('=')[1],
           lines[i].split(' ')[4].split('=')[1],
           listed,unlisted_value)
           array_of_nodes.append(node)
        self.last_modified_state_file = lines[len(lines)-3].split(' ')[1] + ' ' + lines[len(lines)-3].split(' ')[2]
        self.cs.delete_file(self.c_string.aux_nodes_file)
        return array_of_nodes

