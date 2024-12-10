# Käyttöohje

Lataa projektin uusin [release](https://github.com/F4U57O/ot-harjoitustyo/releases/tag/viikko6) valitsemalla "Source code" joko .zip tai .tar.gz
Pura tiedosto haluamaasi hakemistoon.

## Ennen sovelluksen käynnistämistä

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Sekä alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

## Sovelluksen käynnistäminen

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Rekisteröityminen

Sovelluksen etusivulta paina "Rekisteröidy"-nappia, josta pääset seuraavaan:

![register](./kuvat/register.png)


## Kirjautuminen

"Kirjaudu"-napista pääset kirjautumaan tunnuksillasi:

![login](./kuvat/login.png)

## Etusivu

Etusivun näkymässä on vaihtoehtoina "Harjoituspäiväkirja", "Pelitilastot" ja "Tavoitteet"

![frontpage](./kuvat/frontpage.png)

## Harjoituspäiväkirja

Voit luoda omia harjoituspäiväkirja merkintöjä:

![workout](./kuvat/workout.png)

Täytä kentät ja paina "Lisää harjoitus"

## Pelitilastot

Voit luoda ja poistaa pelitilastoja:

![gamestats](./kuvat/gamestats.png)

Täytä tilastokentät ja paina "Lisää pelitilasto". Tilastoja voi poistaa
valitsemalla tilaston ja painamalla "Poista"

## Tavoitteet

Voit luoda tavoitteita ja päivittää niiden tiloja:

![goals](./kuvat/goals.png)

Täytä kentät ja paina "Lisää tavoite".
Klikkaamalla tavoitetta voit päivittää sen tilan "käynnissä", "suoritettu" ja
"ei suoritettu" valinnan jälkeen paina "Päivitä tila"
