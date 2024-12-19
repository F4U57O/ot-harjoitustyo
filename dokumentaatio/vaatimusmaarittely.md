# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tarjota jalkapallopelaajalle erilaisia työkaluja
seurata kehitystään, kuten harjoituspäiväkirja, pelisuoritusten seuranta ja tavotteiden luonti.
Sovellusta on mahdollista käyttää useammalla rekisteröityneellä käyttäjällä, joilla on yksilölliset alueet omiin tietoihin.

## Käyttäjät

Käyttäjärooleja sovelluksessa on alkuun normaalikäyttäjä ja mahdollisesti myöhemmin pääkäyttäjä, jolla on suuremmat oikeudet.

## Käyttöliittymä

Sovellus käynnistyy näkymään, josta voi valita "Kirjaudu" tai "Rekisteröidy". Tämän jälkeen kirjautuneelle käyttäjälle
avautuu näkymä sovelluksen etusivulle, josta on mahdollista siirtyä harjoituspäiväkirjaan, pelitilastoihin tai tavoite-osioon.
Jokaisessa ominaisuudessa on omat syötekenttänsä, sekä näkymät omiin tilastoihin ja merkintöihin. Käyttäjän on mahdollista palata etusivulle
ja kirjautua ulos sovelluksesta.  

## Perusversion tarjoamat ominaisuudet

### Ennen kirjautumista

* Käyttäjä voi luoda käyttäjätunnuksen  
  - Käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä
  - Salasanan tulee olla vähintään 8 merkkiä
* Käyttäjä voi kirjautua järjestelmään  
  - Käyttäjätunnuksen ja salasanan tulee olla oikein.
  - Vääristä käyttäjätunnuksista tulee ilmoitus ja kirjautuminen epäonnistuu

### Kirjautumisen jälkeen

- Käyttäjälle aukeaa etusivu, josta pystyy valitsemaan mihin osioon haluaa siirtyä
* Käyttäjälle tulee näkymä omista merkinnöistä, jos niitä on  
  - Harjoituksille, peleille ja tavoitteille löytyy omat osiot
* Käyttäjä voi lisätä uuden harjoituksen
  - Käyttäjä voi tallentaa harjoituksen tyypin, keston ja päivämäärän
  - Käyttäjä voi kirjoittaa harjoituksen tyypin vapaamuotoisesti päiväkirjaan
* Käyttäjä voi lisätä uuden pelin
  - Käyttäjä voi merkitä tilastoja, kuten maalit, syötöt, peliaika ja ajankohta
  - Käyttäjä voi valita vastustajan nimen valmiista listasta
  - Käyttäjällä on mahdollisuus arvioida pelisuoritustaan asteikolla 1-10
  - Käyttäjällä on mahdollisuus antaa palaute omasta suorituksestaan
  - Sovellus näyttää yhteenlasketut pelit, maalit, syötöt, peliajan sekä arvostelun keskiarvon
* Käyttäjä voi luoda tavoitteen, josta jää aikaleima
  - Käyttäjä voi päivittää tavoitteen tilan: käynnissä, suoritettu, ei suoritettu
  - Tavoitteen tilan päivittämisestä jää myös aikaleima
* Käyttäjän on mahdollista kirjautua ulos

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
* Mahdollisuus fysiikkaseurantaan
* Sovellus voisi esittää edistymistä visuaalisesti (esim. käyrillä) ja muuta analytiikkaa
* Mahdollisuus suodattaa esim. harjoituksia tyypin ja ajankohdan mukaan
* Kalenteri johon voisi suunnitella harjoituksia eri päiville
* Omat käyttäjäroolit pelaajalle ja valmentajalle
* Valmentajalle mahdollisuus antaa palautetta
