#Desenvolvido por Cleber Silva[DigitalMap] parceria com Soflex
#Criado em 01/03/2016
#Contatos cleber@digitalmap.com.br/cleber_pesilva@yahoo.com.br

import urllib, urllib2,sys,os.path,datetime,smtplib,commands,zipfile,mimetypes,poplib,shutil,time,subprocess,imaplib


from email.MIMEText import MIMEText
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import parser
import email
import email.header

reload(sys)
sys.setdefaultencoding('iso8859-1')



def buscarAnexos(dataInicial, pastaDestino):
	os.system('cls' if os.name == 'nt' else 'clear')
	print '******************************************************'
	print '************* Verificando e-mails.... ****************'
	print '******************************************************'
	time.sleep(3)
	mail = imaplib.IMAP4_SSL('imap4.terra.com.br')
	(retcode, capabilities) = mail.login('xxxx', 'xxxxx')
	mail.list()
	mail.select('inbox')

	n=0
	(retcode, messages) = mail.search(None, '(ALL)') #(UNSEEN) (ALL)
	if retcode == 'OK':
	   for emailid in messages[0].split() :
	      n=n+1
	      typ, data = mail.fetch(emailid,'(RFC822)')
	      msg = email.message_from_string(data[0][1])
	      decode = email.header.decode_header(msg['Subject'])[0]
	      subject = unicode(decode[0])
	      date_tuple = email.utils.parsedate_tz(msg['Date'])
	      if date_tuple:
		      local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
		      data=local_date.strftime("%Y%m%d")
		      if(data > dataInicial):
		      	print "Baixando do dia ",data
		      	downloaAttachmentsInEmail(mail, emailid, pastaDestino)


	print 'Finalizando....'
	time.sleep(10)

# Download all attachment files for a given email
def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_string(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

#descompactar todos os zips em uma pasta
def unzipFileInFolder(pathZip ,pathUnzip):
	 #filename = "C:tempextract"
	 for pathzip in os.listdir(pathZip):
		 extzip = os.path.splitext(pathzip)[1]
		 if extzip in (".zip") and not os.path.isdir(pathZip+pathzip):
			 # Call unzip method (Extract Files)
			 print "Extraindo arquivo " + pathZip+pathzip
			 unzipFile(pathZip+pathzip,pathUnzip)



#descompactar arquivo
def unzipFile(pathZip ,pathUnzip):
		 if not os.path.exists(pathUnzip):
			 # Create that directory
			 os.mkdir(pathUnzip)
		 file = zipfile.ZipFile(pathZip, "r")
		 # list file information
		 for info in file.infolist():
			 fullPath = ('/'+info.filename).split('/')
			 fileName = fullPath[len(fullPath) -1]
			 # list filenames
			 for name in file.namelist():
					 ext = os.path.splitext(name)[1]
					 # check extension file
					 if ext in (".csv"):
						 # Write files to disk
						 temp = open(pathUnzip+fileName, "wb") # create the file
						 data = file.read(name) #read the binary data
						 temp.write(data)
						 temp.close()
		 file.close()

#colocar a data inicial no formato YYYYMMDD e o caminho onde devera salvar os anexos
#buscarAnexos('20160609','/media/noct/Tudo/01Digital/01SecretariaSeg/Baixados')
#unzipFile('arquivo.zip','path/para/extracao/')
#unzipFile('/media/noct/Tudo/01Digital/01SecretariaSeg/Baixados/20160111.zip','/media/noct/Tudo/01Digital/01SecretariaSeg/Baixados/unZip/')
#unzipFileInFolder('path/contendo/lista/de/zips/','path/para/extracao/')
#unzipFileInFolder('/media/noct/Tudo/01Digital/01SecretariaSeg/Baixados/','/media/noct/Tudo/01Digital/01SecretariaSeg/Baixados/unZip/')
