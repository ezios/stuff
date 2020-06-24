import pypff
import sys
from threading import Thread
import calendar
import time
import datetime
import os
import random
import string
import re

debug=0
verbose = 1
fields = ['m_unique', 'm_fullheader','m_from','m_replyto','m_to','m_cc','m_subject',\
'm_contenttype','m_importance','m_xmailer', 'm_returnpath', 'm_client','m_id','m_date', 'm_body', 'm_attachment_count']

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def usage():
	print("usage : ")
	sys.exit()
try:
	filepath = sys.argv[1]
except:
	usage()
	sys.exit()

def save(mail):
	global destdir
	text = "Date :" + mail["m_date"] +"\n\n"
	text += mail["m_from"] + "\n"
	text +="Nombre de piece jointes " +str(mail["m_attachment_count"])+"\n\n"
	text += mail["m_to"] +"\n"
	text += mail["m_body"]
	
	with open(destdir+"/"+str(time.time())+".txt","w") as f:
		f.write(text)


def openMailBox(filepath):
	OstPstFile = open(filepath,"rb")
	pff_file = pypff.file()
	pff_file.open_file_object(OstPstFile)
	print('[+] File '+filepath+' opened')
	return pff_file


def getmessages(folder):
	messages = 0
	emailproccessor = {}
	attachments = []
	nummess = folder.number_of_sub_messages
	if verbose:
		print("------[+] Number of sub messages "+str(nummess))
	if folder.number_of_sub_messages == 0:
		return
	else:
		for message in folder.sub_messages:
			messages += 1
			#print(messages,end="\r")
			m_unique = id_generator()
			emailproccessor[m_unique] = {}
			try:
				emailproccessor[m_unique]['m_fullheader'] = message.get_transport_headers()
				headers = message.get_transport_headers().splitlines()
				for header in headers:
					if header.strip().lower().startswith("from:"):
						emailproccessor[m_unique]['m_from'] = header.strip().lower().strip('from:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_from'])
					elif header.strip().lower().startswith("reply-to:"):
						emailproccessor[m_unique]['m_replyto'] = header.strip().lower().strip('reply-to:').lstrip(' ')
						if debug:
							emailproccessor[m_unique]['m_replyto'] = header.strip().lower().strip('reply-to:').lstrip(' ')

					elif header.strip().lower().startswith("to:"):
						emailproccessor[m_unique]['m_to'] = header.strip().lower().strip('to:').lstrip(' ')

						if debug:
							print(emailproccessor[m_unique]['m_to'])
					elif header.strip().lower().startswith("cc:"):
						emailproccessor[m_unique]['m_cc'] = header.strip().lower().strip('cc:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_cc'])

					elif header.strip().lower().startswith("subject:"):
						emailproccessor[m_unique]['m_subject'] = header.strip().lower().strip('subject:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_subject'])

					elif header.strip().lower().startswith("content-type:"):
						emailproccessor[m_unique]['m_contenttype'] = header.strip().lower().strip('content-type:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_contenttype'])
					elif header.strip().lower().startswith("importance:"):
						emailproccessor[m_unique]['m_importance'] = header.strip().lower().strip('content-type:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_importance'])

					elif header.strip().lower().startswith("x-mailer:"):
						emailproccessor[m_unique]['m_xmailer'] = header.strip().lower().strip('x-mailer:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_xmailer'])

					elif header.strip().lower().startswith("x-originating-client"):
						emailproccessor[m_unique]['m_client'] = header.strip().lower().strip('x-originating-client:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_client'])

					elif header.strip().lower().startswith("message-id:"):
						emailproccessor[m_unique]['m_id'] = header.strip().lower().strip('message-id:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_id'])

					elif header.strip().lower().startswith("date:"):
						datetest = header.strip().lower().strip('date:').lstrip(' ')
						emailproccessor[m_unique]['m_date'] = datetest
						if debug:
							print(emailproccessor[m_unique]['m_date'])

					elif header.strip().lower().startswith("return-path:"):
						emailproccessor[m_unique]['m_returnpath'] = header.strip().lower().strip('return-path:').lstrip(' ')
						if debug:
							print(emailproccessor[m_unique]['m_returnpath'] )

					try:
						x = emailproccessor[m_unique]['m_replyto']
					except KeyError:
						emailproccessor[m_unique]['m_replyto'] = "null"
						continue
					try:
						x = emailproccessor[m_unique]['m_importance']
					except KeyError:
						emailproccessor[m_unique]['m_importance'] = "null"
						continue
					try:
						x = emailproccessor[m_unique]['m_xmailer']
					except KeyError:
						emailproccessor[m_unique]['m_xmailer'] = "null"
						continue
					try:
						x = emailproccessor[m_unique]['m_client']
					except KeyError:
						emailproccessor[m_unique]['m_client'] = "null"
						continue
					try:
						x = emailproccessor[m_unique]['m_returnpath']
					except KeyError:
						emailproccessor[m_unique]['m_returnpath'] = "null"
						continue
			except AttributeError:
				continue
			i="2"
			try:
				if message.number_of_attachments > 0:
					emailproccessor[m_unique]['m_attachment_count'] = message.number_of_attachments
				else:
					emailproccessor[m_unique]['m_attachment_count'] = "0"

				if message.plain_text_body!= None:
					i="0"
					emailproccessor[m_unique]['m_body'] = message.plain_text_body.decode('utf-8')
				
				else:
					i="1"
					emailproccessor[m_unique]['m_body'] = "--No Body Message--- "
					
			except AttributeError:
				continue


			print(i)
			print("------------------------ "+ str(emailproccessor[m_unique]['m_to']) )
			print(emailproccessor[m_unique]['m_body'])
			save(emailproccessor[m_unique])
			if int(emailproccessor[m_unique]['m_attachment_count']) > 0:
				print('++++++++++++++++')
				#print(type(message.get_attachment(i)))

def GetLeafFolder(rootfolder):
	for folder in rootfolder.sub_folders:
		if folder.number_of_sub_folders:
			GetLeafFolder(folder)	
		EndFolders.append(folder)
		print("[+]"+ folder.get_name())
	return EndFolders
#getmessages(folder)
def createdir(name=""):
	try:
		destdir  = os.getcwd()+"/MailParsed"+str(time.time())+name
		os.mkdir(destdir)
		return destdir
	except OSError:
		print ("Creation of the directory %s failed" % path)

EndFolders =[]
InterestingFolders = ["récep","suppr"]
destdir = createdir()

pst = openMailBox(filepath)
root= pst.get_root_folder()
folders = GetLeafFolder(root)

for folder in folders:
	print("[+] Analysing Folder: "+ folder.get_name())
	for pattern in InterestingFolders:
		if pattern in folder.get_name():
			getmessages(folder)
