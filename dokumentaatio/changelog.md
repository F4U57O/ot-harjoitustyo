# Changelog

## Viikko 3
* Käyttäjät voivat rekisteröityä luomalla käyttäjätunnuksen ja salasanan
  - Virheilmoitus vääränlaisesta käyttäjätunnuksesta ja salasanasta
* Käyttäjät voivat kirjautua sisään aiemmin luoduilla käyttäjätunnuksilla
  - Virheilmoitus vääristä käyttäjätunnuksista
* Testattu, että rekisteröinti sujuu odotetulla tavalla. (Suurimmaksi osaksi)
* Luotu erilliset tiedostot käyttöliittymälle ja sovelluslogiikalle
* Luotu tietokanta käyttämällä SQLiteä käyttäjätietojen tallentamiseen
* Luotu UserRepository- luokka vastaamaan käyttäjätietojen tallentamisesta, hakemisesta ja poistamisesta tietokannasta.

## Viikko 4
* Kirjautunut käyttäjä voi lisätä harjoituspäiväkirjaan merkintöjä
  - Päivämääräksi tulee automaattisesti se päivämäärä jolloin harjoitus lisätään
  - Päivämäärän voi muuttaa manuaalisesti
  - "Harjoitus"-kenttään voi kirjoittaa vapaamuotoisesti
  - "Kesto:"-kenttään voi kirjoittaa ajan minuutteina ja sen perään tulee teksti "min"
  - Harjoituspäiväkirja alueella on "Takaisin"-nappi, josta pääsee edelliselle sivulle
  - Harjoituspäiväkirjalle on luotu oma taulu tietokantaan
