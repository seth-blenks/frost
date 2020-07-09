
from threading import Thread
from pathlib import Path
import time

class Article_Notification(Thread):
    


    def run(self):
        
        paths = [Path('templates/blogger/Animal'),Path('templates/blogger/Plant'),Path('templates/blogger/Cell')]
        
        while True:
            data = ""

            with open('./provider.txt','r') as new_file:
                data = new_file.read()

            for path in paths:
                directs = [x for x in path.iterdir()]
                for pox in directs:
                    full_file_path = str(pox.parent)+'/'+pox.name
                    if full_file_path not in data:

                        with open('./notification.txt','a') as update:
                            update.write(f"--> new file found in {full_file_path}\n")
                            update.write('*'*50)
                            update.write('\n')
                        with open('./provider.txt','a') as append:
                            append.write(full_file_path+'\n')

                
            time.sleep(2.5)