# Harjoitustyö

## Dokumentaatio
* [Tuntikirjanpito](https://github.com/Hogwarter/ot-harjoitustyo/blob/master/h-tyo/dokumentaatio/tuntikirjanpito.md)
* [Vaatimusmäärittely](https://github.com/Hogwarter/ot-harjoitustyo/blob/master/h-tyo/dokumentaatio/vaatimusmaarittelu.md)
* [README](https://github.com/Hogwarter/ot-harjoitustyo/blob/master/h-tyo/README.md)
* [Changelog](https://github.com/Hogwarter/ot-harjoitustyo/blob/master/h-tyo/dokumentaatio/changelog.md)
* [Käyttöohje](https://github.com/Hogwarter/ot-harjoitustyo/blob/master/h-tyo/dokumentaatio/kayttoohje.md)

## Julkaisut
[1. Viikko 5](https://github.com/Hogwarter/ot-harjoitustyo/releases/tag/viikko5)

[2. Viikko 6](https://github.com/Hogwarter/ot-harjoitustyo/releases/tag/viikko6)

## Ohjelman asennus komentoriviltä:
Lataa tarvittavat riippuvuudet terminaalin kautta komennolla:
```python
poetry install
```
Alusta ohjelma komennolla:
```python
poetry run invoke build
```
## Ohjelman käynnistäminen
Käynnistä ohjelma komennolla:
```python
poetry run invoke start
```
## Ohjelman testaus
Testataan komennolla:
```python
poetry run invoke test
```
## Ohjelman testikattavuusraportti
Testikattavuusraportti saadaan komennolla:
```python
poetry run invoke coverage-report
```
## Ohjelman Pylint-tarkastaminen
Pylint-tarkastus puolestaan saadaan komennolla:
```python
poetry run invoke lint
```
