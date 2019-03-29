#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
from tabulate import tabulate

ledb= 3
ledr= 5
buz= 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledb,GPIO.OUT)
GPIO.setup(ledr,GPIO.OUT)
GPIO.setup(buz,GPIO.OUT)
reader = SimpleMFRC522()

cred = credentials.Certificate('/home/pi/Desktop/rfid.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
#approved_list=db.collection(u'Approved')


try:
	GPIO.output(ledb,1)
	GPIO.output(ledr,0)
	GPIO.output(buz,0)
	print("PLEASE SHOW YOUR CARD")
	id, reg_no = reader.read()
	id= str(id)
	doc_ref = db.collection(u'Approved').document(u'%s'% reg_no)
	doc = doc_ref.get().to_dict()
	print(reg_no)
	#print(doc)
	#if (u'id') in doc:
	#	if (u'id'== (u'%s'% id)):
	#		print("Approved")
	#	else:
	#		print("Not Authorised")
	#else:
	#	print("not found")
	if (doc=={u'id' : u'%s' %id}) :
		print('Approved')
		GPIO.output(ledb,1)
		GPIO.output(ledr,0)
		GPIO.output(buz,1)
		time.sleep(0.5)
		GPIO.output(ledb,0)
		GPIO.output(ledr,0)
		GPIO.output(buz,0)
		
	else:
		print("Not Authorised")
		GPIO.output(ledb,0)
		GPIO.output(ledr,1)
		GPIO.output(buz,1)
		time.sleep(1)
		GPIO.output(ledb,0)
		GPIO.output(ledr,0)
		GPIO.output(buz,0)
		

finally:
	GPIO.cleanup()
