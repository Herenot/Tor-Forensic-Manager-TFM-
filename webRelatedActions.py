import webbrowser
import subprocess
class WebRelatedActions:
    def open_sqlViewer(self):
        webbrowser.open('https://inloop.github.io/sqlite-viewer/')

    def curl_nodes(self,fingerPrint):
        # 37EB4C9361D2F80F279B949CB3CB41DA2F46A2FA
        # Elementos de la petición a obtener:
        # <dt>Nickname</dt>
        # <dt>url</dt>
        # <dt>email</dt>
        # <dt>OR Address</dt>
        # <dt>Exit Address</dt>
        # <dt>First Seen</dt>
        # <dt>Observed Bandwidth</dt>
        # <dt>Consensus Weight</dt>
        # <dt>Last Restarted</dt>
        # <dt>Country</dt>
        # <dt>Fingerprint</dt>
        #print(subprocess.getoutput('curl https://nusenu.github.io/OrNetStats/w/relay/'+fingerPrint+'.html'))
        if(self.get_status_code(fingerPrint) == '200'):
            return "ok"
        else:
            return None
            
    def get_status_code(self,fingerPrint):
        output = subprocess.getoutput('curl -I https://nusenu.github.io/OrNetStats/w/relay/'+fingerPrint+'.html')
        output = output.split('HTTP/2')[1].split(' ')[1];
        return output