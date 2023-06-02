import subprocess
from time import sleep
import pygetwindow as gw
from datetime import datetime as dt


def printLog(text):
        with open('C:/Users/Pichau/Desktop/log_service.txt','a') as f:
            f.write(f'\n{text} | {dt.now().strftime("%d/%m/%Y %H:%M:%S")}')
            print(f'{text} | {dt.now().strftime("%d/%m/%Y %H:%M:%S")}')
            f.close()

def processExists(window_title = str()):
        try:
            windows = gw.getAllTitles()
            if window_title in windows:
                return True
            else:
                return False
        except Exception as E:
            printLog(f'\nErro na função processExists: {E.__str__()}')
             
def startService():
        running = True
        while running:
            try:
                if not processExists('Nova guia - Pessoal — Microsoft\u200b Edge'):
                    cmd = 'start "Microsoft Edge" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge"'
                    subprocess.call(cmd, shell=True)
                    printLog(f'\nEdge aberto')
            except Exception as E:
                printLog(f'\nErro na função startService: {E.__str__()}')
            sleep(1)

