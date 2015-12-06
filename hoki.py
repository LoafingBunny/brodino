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
import sys
import re
from BeautifulSoup import BeautifulSoup

#url = ('http://www.hookii.it/')
#html = urllib.urlopen(url).read()

#pagina di prova:
#scrivi = open('zuppa.txt', 'w')
#scrivi.write(html)
#estrae i contenuti che ci interessano
#html = open('zuppa.txt', 'r')


#zuppa.close()
# leggiamo il file..
#zuppa = open('zuppa.txt', 'r')

#scelgo il numero di pagine da analizzare
default_pag = int('2')  #  <<<<<<----------------<<<<<-----------<<<<<----------<<<<<-------- quante pagine esaminare - default

while True :
    max_pag = raw_input('Quante pagine vuoi farmi cuocere? (Se lasci vuoto ne preparo %i)\nq per uscire\nMeglio non andare oltre le 410: ' % default_pag)
    if max_pag == 'q' : sys.exit(0)
    if len(max_pag) < 1 : 
        max_pag = int(default_pag)
        break
    try : 
        max_pag = int(max_pag)
        break
    except : print 'Inserisci un numero!\n'

num_pag = int('0')
lista_totale = []
contatore = int('0') # e' l'id di ogni post

# carico le pagine internet
while True :
    num_pag = num_pag + 1
    if num_pag > max_pag : break
    print '\n\nPagina %i' % num_pag
    url = ('http://www.hookii.it/page/%i/' % num_pag)
    html = urllib.urlopen(url).read()
    
    soup = BeautifulSoup(html)
    
    #cerchiamo voti, commenti, dominio

    dominio = soup.findAll("div", {"class": "articolo"})
    #print dominio
    #loop per suddividere i vari articoli
    for i in dominio :
    
        #cerco il titolo
        #titolo = i('a')
        #print titolo
        #print titolo.get('title', None)
        
        #punteggio
        elenco_punti = i.p.findAll(text=True)
        for punteggio in elenco_punti :
            try : int(punteggio)
            except : continue
            print '\nPunteggio: ', punteggio.strip()
            punti_veri = int(punteggio.strip())
        
    
        #loop per cercare, all'interno degli articoli, i link giusti
        link = i.find('a', {'rel': 'bookmark'}) # seleziona i tag <a> 
        manca = bool(True)
        url_hoki = link.get('href', None) #trovo il link
        print url_hoki
        pag_hoki = urllib.urlopen(url_hoki).read()
        #pag_hoki = open('semolino.txt', 'r')
        zuppa_pag = BeautifulSoup(pag_hoki)
    
        # cerco la data
        hoki_data = zuppa_pag.find("span", {"class": "entry-date"}).string.strip()
        print hoki_data
        hoki_data_separ = hoki_data.split()    
        giorno = int(hoki_data_separ[0])
        mese = hoki_data_separ[1]
        anno = int(hoki_data_separ[2])
    
        #cerco il dominio
        hoki_cont = zuppa_pag.find("div", {"class": "single-entry-content"})
        link_dom = hoki_cont('a')[0].get('href', None) # seleziona i tag <a> e preleva il dominio PERCHE??? PERCHEEE FUNZIONIIII???
        try : 
            z = re.findall('http.*://(.*?)/', link_dom) #[w]+\.+
            manca = False
        except : z = list('vuoto')

        if manca : 
            print 'Dominio: Altro'
            dominio_vero = 'altro'
        else :
            try: 
                print 'Dominio:', z[0]
                dominio_vero = z[0]
            except : 
                print 'Dominio: Altro'
                dominio_vero = 'altro'
    
        #da qui cerca i commenti:
        link = i('a')
        for g in link :
            
            testo = g.findAll(text=True)
            for l in testo :
                commenti = re.findall('([0-9]+).comment', l)
                if len(commenti) < 1 : continue
                print 'Numero di commenti:', int(commenti[0])
                commenti_veri = int(commenti[0])
    
    #faccio la l'elenco dei 3 valori e li aggiungo alla lista
        lista_articolo = (contatore, punti_veri, commenti_veri, giorno, mese, anno, dominio_vero)
        lista_totale.append(lista_articolo)
        contatore = contatore + 1

print lista_totale
#Scrivo i 3 valori nel file
minestrone = open('minestrone_e_carote.txt', 'w')
minestrone.write('ID\tVoti\tCommenti\tGiorno\tMese\tAnno\tDominio\n')
for item in lista_totale :
    minestrone.write('%i\t%i\t%i\t%i\t%s\t%i\t%s\n' % item)

minestrone.close()

 
print len(lista_totale)


#rank = soup.find("div", {"class": "articolo"}).h6.contents
#teaminfo = soup.find("div", {"class": "team-info"})
#name = teaminfo.h4.contents
#rating = teaminfo.ul.p.span.contents
