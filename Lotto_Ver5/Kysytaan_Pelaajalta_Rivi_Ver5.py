# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:09:38 2020

@author: Suvi


Kysytaan_Pelaajalta_Rivi.py

Pelaajalta kysytään 7 erilaista kokonaislukua väliltä 1-40, ja ne talletaan 
listaan pelaajan_rivi_lista 

Ver 2 Tarkistetaan että syöte on yksi kokonaisluku, muutoin annetaan virheilmoitus

Ver 3 Ver 4 ei muutoksia
Ver 5 poistettu turhia tulostuksia
"""

def kysytaan_numerot(): # syöte täytyy olla 1 kokonaisluku
    
    while True:
        syote = (input(" Anna numero 1-40:"))
        
        try:
            pelaajan_numero = int(syote)
            return pelaajan_numero
        
        except ValueError:
            print("\n", "Virheellinen syöte, anna yksi luku välillä 1-40")


def tarkista_pelaajan_rivi(): # toimii oikein lukuvälillä ja duplikaattien kanssa
        
    pelaajan_rivi_lista = []
               
    while len(pelaajan_rivi_lista) < 7:
        
        pelaajan_numero = kysytaan_numerot()
            
        if pelaajan_numero > 40 or pelaajan_numero < 1: 
                print("\n", "Numero", pelaajan_numero, "ei ole lukuvälillä 1-40\n Syötä uusi numero!", "\n", 
                      "Syöttämäsi numerot", pelaajan_rivi_lista)

        elif pelaajan_numero in pelaajan_rivi_lista:
            print("\n", "Olet jo antanut numeron", pelaajan_numero, "Syötä uusi numero!\n",
                  "Syöttämäsi numerot", pelaajan_rivi_lista)
            
        else:
            pelaajan_rivi_lista.append(pelaajan_numero)
            print("\n", "Syöttämäsi numerot", pelaajan_rivi_lista)

    return pelaajan_rivi_lista    
        
    

