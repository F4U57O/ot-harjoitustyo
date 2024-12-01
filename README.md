# fBallersApp

Sovelluksen tarkoituksena on tarjota jalkapallopelaajalle erilaisia työkaluja
seurata kehitystään, kuten harjoituspäiväkirja, pelisuoritusten seuranta ja kehityssuunnitelman luonti.
Sovellusta on mahdollista käyttää useammalla rekisteröityneellä käyttäjällä, joilla on yksilölliset alueet omiin tietoihin.

## Release

[Release](https://github.com/F4U57O/ot-harjoitustyo/releases/tag/viikko5)

## Huomio Python-versiosta

Sovelluksen toiminta on testattu versiolla 3.10.12 , mutta sen tulisi toimia versiolla 3.8 tai uudemmalla.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Käyttöohjeet

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Asenna tietokanta valmiiksi:

```bash
poetry run invoke build
```

3. Käynnistä sovellus:

```bash
poetry run invoke start
```

## Testaus

Testit komennolla:

```bash
poetry run invoke test
```

Generoi html-testikattavuusraportti:

```bash
poetry run invoke coverage-report
```
