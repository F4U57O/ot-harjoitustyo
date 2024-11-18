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
