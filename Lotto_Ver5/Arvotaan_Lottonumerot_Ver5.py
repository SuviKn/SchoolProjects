# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:21:03 2020

@author: Suvi

ArvotaanLottoNumerot.py

Funktio arvotaan_numerot arpoo 7 satunnaista numeroa välillä 1-40 
ja tallettaa ne listaan. Tarkistetaan ettei arvotussa ole duplikaatteja ja 
tarvittaessa suoritetaan arvonta uudestaan. 

Ver3 lisätty lisanumeron arvonta ja tarkistus
Ver 4 lisätty return lottorivi, lisanumero
Ver 5 poistettu turhia kommentteja
"""
import random

def arvotaan_numerot():
    
    lottorivi_lista = []
    
    for i in range(1,8):
        lottonumero = random.randrange(1, 41)
        lottorivi_lista.append(lottonumero)
                            
    return lottorivi_lista # tarkistettava lista 

def tarkista_lottorivi_lista():
    
    while True:
        lottorivi = arvotaan_numerot() 
        if len(lottorivi) != len(set(lottorivi)):
            continue # jatketaan kunnes saadaan rivi ilman duplikaatteja
            
        else:
            return lottorivi # katkaistaan silmukka käyttämällä returnia


def arvo_lisanumero():
    
    lisanumero = random.randrange(1, 41)  
    return lisanumero

def tarkista_lisanumero_lista():
    
    lottorivi = tarkista_lottorivi_lista()
    
    while True:
        
        lisanumero = arvo_lisanumero() # arvotaan lisanumero
        
        if lisanumero in lottorivi:
            continue
                      
        else:
            return lottorivi, lisanumero