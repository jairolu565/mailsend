import hashlib
from time import sleep 
from difflib import SequenceMatcher
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from datetime import datetime

while True:
    def hash_file(filename1,filename2):
        h1 = hashlib.sha1()
        h2 = hashlib.sha1()

        with open(filename1, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read (1024)
                h1.update (chunk)
        with open(filename2, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read (1024)
                h2.update (chunk)
        return h1.hexdigest(),h2.hexdigest()

    origin = 'C:\\Users\\admin\\Desktop\\RELATORIO.pdf'
    copy = 'C:\\Users\\admin\\Documents\\new\\RELATORIO.pdf'

    msg1,msg2 = hash_file(origin,copy)
    print(msg1+"\t"+msg2)
    razao = (SequenceMatcher(None,msg1,msg2).ratio())*100
    if razao == 100:
        print('A RAZAO ENTRE OS ARQUIVOS É DE ', razao, '%')
        print('TESTANDO ALTERAÇÕES NO ARQUIVO NOVAMENTE EM 10 SEGUNDOS')
        print('\n')
    else:
        print('OS ARQUIVOS SÃO DIVERGENTES E O E-MAIL SERÁ ENVIADO')
        servidor=smtplib.SMTP('smtp-mail.outlook.com', 587)
        servidor.ehlo()

        servidor.starttls()

        fromaddr = "pyenviar@outlook.com"
        toaddr = "jairolu565@gmail.com"

        msg = MIMEMultipart() 
        msg['From'] = fromaddr
        msg['To'] = toaddr 
        msg['Subject'] = "RELATÓRIO DE ONUS"
        body = "Boa tarde. Segue relatório de ONUS para reparo do dia."

        msg.attach(MIMEText(body, 'plain')) 
        filename = "RELATORIO.pdf"
        attachment = open(origin, "rb") 
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)
     
        servidor.login("pyenviar@outlook.com","ravenclaw13")
        text = msg.as_string()
        servidor.sendmail(fromaddr,toaddr,text)
        servidor.quit()
        print('TESTANDO ALTERAÇÕES NO ARQUIVO NOVAMENTE EM 1 SEGUNDO')
        print('\n')
        src_path = r'C:\\Users\\admin\\Desktop\\RELATORIO.pdf'
        dst_path = r'C:\\Users\\admin\\Documents\\new\\RELATORIO.pdf'
        shutil.copy(src_path, dst_path)
        print('Arquivo atualizado. Aguardando uma nova alteração.')
        print('\n')
    sleep(1)
    





