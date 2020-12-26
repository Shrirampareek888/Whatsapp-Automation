# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:44:18 2020

@author: shrir
"""


from twilio.rest import Client 
from Main import cont
account_sid = 'Enter your account_sid' 
auth_token = 'Enter your auth_token' 
client = Client(account_sid, auth_token) 
 
def send_sms():
    message = client.messages.create( 
                              from_='whatsapp:Enter Provided No',  
                              body=cont(),      
                              to='whatsapp:Enter Receiver No' 
                          ) 
 
    print(message.sid)