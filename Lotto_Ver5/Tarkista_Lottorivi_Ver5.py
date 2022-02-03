# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:37:26 2020

@author: Suvi

Tarkista_lottorivi_Ver4.py

Tarkistetaan kuinka monta oikein ja mitkä ne numerot ovat 
Ver4 
Lisäksi tehdään voiton maksu ja tarkistetaan onko lisänumero oikein 
Ver5
Lisätty voitonmaksu ja lisänumeron tarkistus tilanteessa, 
jossa se vaikuttaa voitonmaksuun
"""

import Kysytaan_Pelaajalta_Rivi_Ver5
import Arvotaan_Lottonumerot_Ver5

def voitto_listat():

    tarkista_lottorivi = Arvotaan_Lottonumerot_Ver5.tarkista_lisanumero_lista()
    tarkista_p_rivi = Kysytaan_Pelaajalta_Rivi_Ver5.tarkista_pelaajan_rivi()
    
    lottorivi = tarkista_lottorivi[0]
    lisanumero = tarkista_lottorivi[1]
    
    print("\n€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€")
    print("\n", "ALOITETAAN TARKISTUS:")
    print("\n", "Pelaajan rivi:", tarkista_p_rivi)
    print("\n" ,"Päivän lottorivi:", lottorivi)
    print("\n", "Päivän lisänumero:", lisanumero)
        
    tarkistus_lista = []
    tarkistus_lista.extend(tarkista_p_rivi)
    tarkistus_lista.extend(lottorivi)
    
    return tarkistus_lista, lisanumero, tarkista_p_rivi
    

def tarkista_numerot():
    listat = voitto_listat()
    
    tarkistus_lista = listat[0]
    lisanumero = listat[1]
    pelaajan_rivi = listat[2]
    
    # tarkistetaan oikeat numerot      
    if len(tarkistus_lista) > len(set(tarkistus_lista)):
        numeroa_oikein = (len(tarkistus_lista)) - len(set(tarkistus_lista))
        print ("\n", "Oikein arvattujen lottonumeroiden määrä:", numeroa_oikein) # numeroa_oikein on arvattujen lukujen kplmäärä
        
        numerot  = [] # listaan tallettuvat luvut, jotka pelaaja on arvannut
        
        for numero in range(0, 41):
            if tarkistus_lista.count(numero) > 1:
                numerot.append(numero)
            else:
                continue
                             
        print("\n", "Pelaaja arvasi oikein lottonumerot:", numerot)
        return numeroa_oikein, lisanumero, pelaajan_rivi
        
    else:
        print("\n", "Ei yhtään oikein, parempi onni ensi kerralla")
        numeroa_oikein = 0
        return numeroa_oikein, lisanumero, pelaajan_rivi
        
       
def voiton_maksu():
  
    voittopotti = {7: "5 000 000",
                   6: "125 000",
                   5: "2 000",
                   4: "50"}
    
    tarkista_num = tarkista_numerot()
    numeroa_oikein = tarkista_num[0]
    lisanumero = tarkista_num[1]
    pelaajan_rivi = tarkista_num[2]

    maksu = voittopotti.get(numeroa_oikein)
    
    if numeroa_oikein == 7:
        print("\n", "Täysosuma onneksi olkoon! Voitit:", maksu, "euroa")
        
    elif numeroa_oikein == 6 and lisanumero in pelaajan_rivi:
        print("\n", "Arvasit myös lisänumeron", lisanumero, "\n", "Onneksi olkoon! Voitit: 200 000 euroa")
    
    elif numeroa_oikein == 3 and lisanumero in pelaajan_rivi:
        print("\n", "Arvasit myös lisänumeron", lisanumero, "\n", "Onneksi olkoon! Voitit: 20 euroa")
    
    elif numeroa_oikein > 3:
        print("\n", "Onneksi olkoon! Voitit:", maksu, "euroa")
        
    else:
        print("\n", "Voitit: 0 euroa")