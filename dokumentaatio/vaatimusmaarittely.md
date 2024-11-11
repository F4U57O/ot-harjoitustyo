# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tarjota jalkapallopelaajalle erilaisia työkaluja
seurata kehitystään, kuten harjoituspäiväkirja, pelisuoritusten seuranta ja kehityssuunnitelman luonti.
Sovellusta on mahdollista käyttää useammalla rekisteröityneellä käyttäjällä, joilla on yksilölliset alueet omiin tietoihin.

## Käyttäjät

Käyttäjärooleja sovelluksessa on alkuun normaalikäyttäjä ja mahdollisesti myöhemmin pääkäyttäjä, jolla on suuremmat oikeudet.

## Perusversion tarjoamat ominaisuudet

### Ennen kirjautumista

* Käyttäjä voi luoda käyttäjätunnuksen
  - Käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä
  - Salasanan tulee olla vähintään 8 merkkiä
* Käyttäjä voi kirjautua järjestelmään
  - Käyttäjätunnuksen ja salasanan tulee olla oikein.
  - Vääristä käyttäjätunnuksista tulee ilmoitus ja kirjautuminen epäonnistuu

### Kirjautumisen jälkeen

* Käyttäjälle tulee näkymä omista merkinnöistä, jos niitä on
  - Harjoituksille, peleille ja kehityssuunnitelmalle omat osiot
* Käyttäjä voi lisätä uuden harjoituksen ja määritellä harjoituksen tyypin
  - Käyttäjä voi tallentaa harjoituksen keston, intensiteetin ja päivämäärän
  - Käyttäjä voi kirjoittaa vapaamuotoisen tekstin päiväkirjaan
* Käyttäjä voi lisätä uuden pelin ja merkitä tilastoja
  - Käyttäjä voi merkitä tilastoja, kuten maalit, syötöt ja peliaika
  - Käyttäjä voi merkitä vastustajan nimen ja pelin ajankohdan
  - Käyttäjällä on mahdollisuus arvioida pelisuoritustaan asteikolla 1-10
  - Käyttäjällä on mahdollisuus antaa palaute omasta suorituksestaan
* Käyttäjä voi luoda tavoitteen
  - Käyttäjä voi päivittää tavoitteen tilan: käynnissä, suoritettu, ei suoritettu

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
* Mahdollisuus fysiikkaseurantaan
* Sovellus voisi esittää edistymistä visuaalisesti (esim. käyrillä) ja muuta analytiikkaa
* Mahdollisuus suodattaa esim. harjoituksia tyypin ja ajankohdan mukaan
* Kalenteri johon voisi suunnitella harjoituksia eri päiville
* Omat käyttäjäroolit pelaajalle ja valmentajalle
* Valmentajalle mahdollisuus antaa palautetta
