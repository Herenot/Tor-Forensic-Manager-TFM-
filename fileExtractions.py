from callsSystem import CallsSystem
from datetime import datetime
from PIL import Image
class FileExtractions:
    update_array =[]
    def obtain_hashes_sign(self,file):
        with open(file) as f:
            lines = [x.split() for x in f.read().split("-----BEGIN PGP SIGNATURE-----") if x]
        for i in range(3):
            del lines[1][len(lines[1])-1]
        return "".join(lines[1])
    def obtain_update_info(self):
        cs = CallsSystem()
        update_file = cs.get_update_info()
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