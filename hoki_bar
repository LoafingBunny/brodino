# Note - this code must run in Python 2.x

# This software is Copyright of LoafingBunny. LOL.
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer

lista_totale = []
data_attuale = [15, 12, 05] # anno, mese, giorno
data_limite = (15, 12, 07) # data che NON deve essere raggiunta
mesi_di_trenta = (4, 6, 9, 11)
mesi_di_trentuno = (1, 3, 5, 7, 8, 10)
data_max = True

while data_max :
    print '\nBar del:', data_attuale[0], data_attuale[1], data_attuale[2]
    url = 'http://www.hookii.it/bar-{:02d}-{:02d}{:02d}'.format(data_attuale[0], data_attuale[1], data_attuale[2])
    
    html = urllib.urlopen(url).read()

    comme = SoupStrainer('header',{'class': 'single-entry-header'})
    commenti = BeautifulSoup(html,parseOnlyThese=comme)
    commenti_veri = int( commenti.find('span', {'class': 'dsq-postid'}).contents[0].split( ' ')[0].replace('.','') )
    print 'N. commenti:', commenti_veri
    
    #faccio la l'elenco dei 3 valori e li aggiungo alla lista
    lista_articolo = (data_attuale[0], data_attuale[1], data_attuale[2], commenti_veri)
    lista_totale.append(lista_articolo)
    data_attuale[2] = data_attuale[2] + 1
    if data_attuale[0] == 14 : continue
    if data_attuale[2] == 30 and data_attuale[1] in mesi_di_trenta :
        data_attuale[2] = 1
        data_attuale[1] = data_attuale[1] + 1
    elif data_attuale[2] == 31 and data_attuale[1] in mesi_di_trentuno :
        data_attuale[2] = 1
        data_attuale[1] = data_attuale[1] + 1
    elif data_attuale[1] == 2 and data_attuale[2] == 28 :
        data_attuale[2] = 1
        data_attuale[1] = data_attuale[1] + 1
    if data_attuale[1] == 12 and data_attuale[0] == 14 :
        data_attuale[2] = 1
        data_attuale[1] = 1
        
    if data_attuale[0] == data_limite[0] and data_attuale[1] == data_limite[1] and data_attuale[2] == data_limite[2] : data_max = False

minestrone = open('minestrone_alchool.txt', 'w')
minestrone.write('Anno\tMese\tGiorno\tCommenti\n')
for item in lista_totale :
    minestrone.write('%i\t%i\t%i\t%i\n' % item)

minestrone.close()

 
print 'Trovate %i pagine' % len(lista_totale)
