#  PyGetEmails

Projeto em python para importar anexos de e-mail.

## Motivação
Precisamos constantemente consolidar os arquivos enviados pelo robô rodando na Secretária de Segurança de Guarulhos, preferi usar um repostório separado para ajudar na reutilização do código tendo em vista que podermos usar isso em projetos futuros.

## Algoritmo

O sitema antraves de uma data específica resgata e salva os anexos para uma pasta definida.

## Status
	[Em Teste] utilizado com sucesso pela primeira vez em 17/06/2016 onde buscou e extraiu 149 e-mails.

## Pré requisitos
	[Python 2.7](http://www.python.org.br/) ou mais recente(não testei em versões anteriores)
	[Python libs] urllib, urllib2,sys,os.path,datetime,smtplib,commands,zipfile,mimetypes,poplib,shutil,time,subprocess,imaplib


## Como Rodar
	buscarAnexos('YYYYMMDD','/path/para/download/')
	unzipFile('arquivo.zip','path/para/extracao/')
	unzipFileInFolder('path/contendo/lista/de/zips/','path/para/extracao/')



## Licença(CC)

	You are free to:
	    Share — copy and redistribute the material in any medium or format
	    Adapt — remix, transform, and build upon the material
	    for any purpose, even commercially.
	    The licensor cannot revoke these freedoms as long as you follow the license terms.

## Autor
	Cleber Silva
	cleber_pesilva@yahoo.com.br
	cleber@digitalmap.com.br

## Data
	06/2016
