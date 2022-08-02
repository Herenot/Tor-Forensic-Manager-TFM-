import webbrowser
import subprocess
from bs4 import BeautifulSoup
class WebRelatedActions:
    def open_sqlViewer(self):
        webbrowser.open('https://inloop.github.io/sqlite-viewer/')

    def curl_nodes(self,fingerPrint):
        elements =['Nickname','url','email','Exit Address','Observed Bandwidth','Consensus Weight','Last Restarted',
        'Country','First Seen','Fingerprint']
        # 37EB4C9361D2F80F279B949CB3CB41DA2F46A2FA --> Enlace caído
        # '050A1245EEC76B7438337BAAF19F4AB0666B375F' --> Funciona
        # Elementos de la petición a obtener:
        # <dt>Nickname</dt>
        # <dt>url</dt>
        # <dt>email</dt>
        # <dt>Exit Address</dt>
        # <dt>Observed Bandwidth</dt>
        # <dt>Consensus Weight</dt>
        # <dt>Last Restarted</dt>
        # <dt>Country</dt>
        # <dt>First Seen</dt>
        # <dt>Fingerprint</dt> ---> Es el parámetro
        if(self.get_status_code(fingerPrint) == '200'):
            petition =subprocess.getoutput('curl https://nusenu.github.io/OrNetStats/w/relay/'+fingerPrint+'.html')
            soup = BeautifulSoup(petition,'lxml')
            data = []
            for i in range(len(elements)-3):
                if(str(soup.find('dt', string=elements[i]))!= 'None'):
                    if(len(soup.find('dt', string=elements[i]).find_next_siblings('dd'))>0):
                        line = str(soup.find('dt', string=elements[i]).find_next_siblings('dd')[0])
                        data.append(line.split('<dd>')[1].split('</dd>')[0])
                    else:
                        data.append(None)
                else:
                    data.append(None)
            
            line = str(soup.find('dt', string=elements[7]).find_next_siblings('dd')[0]) 
            data.append(line.split('/></a>')[1].split('title="')[0].split('\n')[0])
            line = str(soup.find('dt', string=elements[8]).find_next_siblings('dd')[0])
            data.append(line.split('<a href=')[1].split('">')[1].split("</a></dd>")[0])
            data.append(fingerPrint)
            return data
        else:
            return None
       

    def get_status_code(self,fingerPrint):
        output = subprocess.getoutput('curl -I https://nusenu.github.io/OrNetStats/w/relay/'+fingerPrint+'.html')
        output = output.split('HTTP/2')[1].split(' ')[1];
        return output