# Käyttöohje

Lataa projektin viimeisimmän [julkaisun](https://github.com/) lähdekoodi _Assets_-osion alta kohdasta _Source code_.

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

## Kirjautuminen

Ohjelma avautuu kirjautumisnäkymään, jossa käyttäjää pyydetään syöttämään käyttäjänimi ja salasana, tai luomaan uusi käyttäjä.

## Uuden käyttäjän luonti

Käyttäjä voi luoda uuden käyttäjä painamalla "New user" - painiketta, jonka jälkeen ohjelma pyytää uutta käyttäjää syöttämään uuden käyttäjänimen, sekä salasanan.

## Uuden collectionin luominen ja muokkaaminen


