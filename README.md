# Repozytorium z rozwiązaniem zadania rekrutacyjnego nr 3

### Aplikacja została stworzona przy pomocy frameworku flask

## uruchomienie aplikacji:

`pip3 install -r requirements.txt`

`python3 app.py`

aplikacja domyślnie uruchamia się na localhoście pod portem 5000

## dostępne zapytania

`GET` `/repos/list` - lista publicznych repozytoriów z liczbą gwiazdek, dane zwracane w postaci jsona

`GET` `/repos/stars/sum` - suma liczby gwiazdek dla wszystkich publicznych repozytoriów allegro, zwracana liczba

## potencjalny rozwój aplikacji

Projekt można potencjalnie poszerzyć np. o zdobywanie informacji o konkretnym repozytorium, takich jak opis, czy lista
użytkowników która zostawiłą gwiazdki. Można również dodać możliwość uzyskiwania takich danych dla repozytoriów innych
organizacji, lub użytkowników.