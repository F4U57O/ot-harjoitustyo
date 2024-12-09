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
* Luotu WorkoutRepository- luokka vastaamaan harjoitusten tallentamisesta ja hakemisesta.

## Viikko 5
* Sovelluksen kokoa muutettu isommaksi vastaamaan sen sisältöä
* Kirjautunut käyttäjä voi lisätä pelitilastoja
  - Vastustajan pystyy valitsemaan valmiista listasta
  - Päivämäärän saa valittua kalenterinäkymästä
  - Maalit, syötöt ja peliajan pystyy valitsemaan arvovalitsimella
  - Arvosanan pystyy valitsemaan liukusäätimellä
  - Palautteen voi kirjoittaa vapaamuotoisesti
  - Pelitilastoissa näkyy maalit, syötöt ja peliaika yhteensä
  - Pelitilastoissa näkyy arvosanojen keskiarvo
  - Pelitilastoja voi poistaa yksi kerrallaan
* Luotu GameStatsRepository- luokka vastaamaan tilastojen tallentamisesta, hakemisesta ja poistamisesta tietokannasta.

## Viikko 6
* Kirjautunut käyttäjä voi lisätä tavoitteen
  - Tavoitteen luonnin yhteydessä lisätään luonnin ajankohta
  - Tavoite menee automaattisesti tilaan "käynnissä"
* Käyttäjä voi päivittää tavoitteen tilan
  - Tilan voi päivittää "suoritettu", joka näkyy vihreällä fontilla
  - Tilan voi päivittää "ei suoritettu", joka näkyy punaisella fontilla
  - Tilan päivityksen yhteydessä lisätään päivityksen ajankohta
* Luotu GoalRepository- luokka vastaamaan tavoitteiden tallentamisesta ja tilan päivittämisestä tietokantaan.
