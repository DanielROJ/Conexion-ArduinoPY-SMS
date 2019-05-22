#!/usr/bin/env python3 6b6c14d53a497be30f3f6d64bb56ad9a
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:16:55 2019

@author: Daniel Rojas - danielroj

Script encargado de  establecer comunicacion con un dispositico Arduino y obtener los datos de lectura en tiempo real, asi mismo calcula el grado de alcohol y lo envia 
Por medio de un SMS de texto a un celular destinatario
"""

from twilio.rest import Client
import serial

arduino = serial.Serial('/dev/ttyACM0',9600);



valorLimite=150;


noE =0;

siE=0;

##

while noE<20:
    value =  arduino.readline();
    
    valor = value.decode("utf-8");
    
    numero = float(valor);
    
    print(numero)
    
    if(numero<valorLimite):
        noE+=1;
    else:
        siE+=1;
    
    


if(siE>0):
    account_sid = 'AC9b5f06fd6e4b74559080bdc00b52afae'
    auth_token = 'TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body="esta Borracho, para cuando la fiesta",
                     from_='+12077627439',
                     to='+573138926061'
                 )
  
    

    print("");
    
else:
    print("mamelo")
    
        
    
    

    
    
   

arduino.close();

    
