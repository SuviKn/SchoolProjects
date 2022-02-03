# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:37:44 2020

@author: Suvi

Pelaa.py

Pelin pää funktio joka käynnistää pelin 
"""

import Tarkista_Lottorivi_Ver5
   
if __name__ == '__main__' :    
    print("\n€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€",
          "\n", "\n Tervetuloa pelaamaan lotto peliä!\n",
          "Sinun tulee valita 7 numeroa välillä 1-40.\n Tämän jälkeen arvotaan lottonumerot,",
          "\n ja selvitetään suosiiko onni sinua tällä kertaa!\n",
          "\n", "Voittosummat:", "\n",
          "7 oikein : 5 000 000 €\n",
          "6 + 1 oikein : 200 000 €\n",
          "6 oikein : 125 000 €\n",
          "5 oikein : 2 000 €\n",
          "4 oikein : 50 €\n",
          "3 + 1 oikein : 20€\n",
          "\n€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€")     
    Tarkista_Lottorivi_Ver5.voiton_maksu()
    