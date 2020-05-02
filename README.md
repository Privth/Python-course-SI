# Python-course-SI


### L1
```
1) Sforkować repozytorium na Wasze konto
2) Przejść na Waszego forka
3) Ściągnąć wasze repo na dysk i powiązać z repozytorium zdalnym (remote)
4) Napisać sortowanie liczb w dwoma znanymi Wam metodami(język jak ustalaliśmy na laboratorium). Starajcie się napisać funkcje w sposób zwarty, bez żadnych komentarzy czy śmieci w kodzie, w sposób optymalny, z użyciem najlepszych, znanych Wam struktur danych i metod przeglądania ich. Tworząc rozwiązania pracujcie z gitem- dodawajcie na stage, twórzcie commity. Pracujcie na branchu, stwórzcie na potrzeby zadania brancha i nazwijcie go np SortingMethods
5) wypchnijcie zmiany lokalne na repo zdalne
6) utwórzcie merge requesta z brancha SortingMethods do brancha master mojego repo (oryginalnego repo, z którego po
```
### L2
```
1) Funkcje sortujące z listy 1 zmienić na potrzeby zadania i opakować w nowe funkcje, które mają za zadanie znaleźć 3 pierwsze wartości w strumieniu danych, które są większe niż zadana wartość progowa i zwrócić ich indeksy. 
Wartość progowa jest podana na wejściu do funkcji opakowującej. Kolejność zwracanych indeksów ma być podyktowana wielkością wartości. Większe najpierw.
Pracujcie z gitem, proponuję zrobić osobnego brancha, nazwać go Onsets i w nim pracować. Na koniec - jak poprzednio - wysłać na repozytorium remote i wystawić pull request do mojego repozytorium, z którego pierwotnie forkowaliście. Nie akceptuję plików dodanych do gita przez „upload”. Wysyłanie plików na wasze remote repo odbywa się poprzez git push.
Przykład wejścia:
([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2) 
-strumień danych, wartość progowa
Oczekiwane wyjście 8,0,7 (trzy pierwsze wartości, które przekraczają znajdują się pod indeksami 0, 7 i 8. Największą z nich wartość ma ten pod indeksem 8, następnie 0, następnie 7).
(5pkt)
2) Zoptymalizować pod kątem obliczeniowym. Jeśli jakieś obliczenia są zbędne do wykonania zadania- pominąć. (2pkt)
3) Zmierzyć czasy znajdowania tychże wartości przez poszczególne algorytmy. Porównać dla różnych zestawów danych. Wyciągnąć (dla siebie) wnioski.
(3pkt)
```
### L3
```
1. Znaleźć w internecie API ze źródłem danych o rynkach finansowych, przykłady:
https://bittrex.github.io/api/v1-1
https://bitbay.net/en/public-api
https://www.tradingview.com/rest-api-spec/#section/Authentication

Stworzyć prostą funkcję, która łączy się z danym API, pobiera listę ofert kupna oraz listę ofert sprzedaży i printuje do konsoli. (5pkt)

2. Znaleźć API z drugiego źródła - giełdy / instytucji finansowej, wybrać jeden zasób finansowy, a właściwie ich parę (bitcoin-usd / ropa-usd / złoto-usd / eur - usd) 
porównać gdzie bardziej opłaca się kupić (oferty sprzedaży są niższe), a gdzie sprzedać (oferty kupna są wyższe) (5pkt)
```
### L4
```
1. Rozszerzyć źródła danych o 2 kolejne API, porównywać wybrane wcześniej 2 pary zasobów i ich ceny kupna-sprzedaży na przestrzeni czasu. 
Tym razem na podstawie cen kupna / sprzedaży z pośród poszerzonej bazy macie za zadanie na bieżąco wyliczać czy występuje możliwość arbitrażu.
Pod pojęciem arbitrażu kryje się przeprowadzanie dwóch transakcji przeciwstawnych na dwóch różnych giełdach. 
Pisząc bardziej zrozumiale - sprawdzacie czy da się kupić taniej w miejscu 1 i sprzedać drożej w miejscu 2.
Pamiętajcie, że chcąc kupić w miejscu X musicie patrzeć na oferty sprzedaży w miejscu X, a chcąc sprzedać w miejscu Y musicie patrzeć na oferty kupna w miejscu Y.
Program, jak poprzedni, ma się automatycznie odświeżać. Wynikiem jego działania ma być print informacji(przykładowo):
Na giełdzie X można kupić 0.1 BTC za USD po kursie 6800 i sprzedać na giełdzie Y po kursie 6900, zyskując 10USD.
(5pkt)

2. Przy kalkulacjach wziąć pod uwagę prowizję kupna sprzedaży na giełdach. Pamiętajcie, żeby brać tu pod uwagę prowizję podawaną typu Taker (tę wyższą), bo bierzecie ofertę cudzą, nie składacie własnej i nie czekacie aż ktoś się na nią zdecyduje. 
(2.5pkt)

3. Założyć wirtualny budżet rozpatrywanych zasobów i w czasie rzeczywistym liczyć ile potencjalnie zarobilibyście na Waszych operacjach. Nie musicie brać pod uwagę opóźnienia w przesyłaniu środków pomiędzy giełdami.
Dla uproszczenia identyfikacji rozpatrywanego systemu zakładamy że dysponujemy środkami w każdej z rozpatrywanych walut na każdej z rozpatrywanych giełd. 
(2.5pkt)
```
### L5
```
1. Wybrać 5 zasobów w stosunku do dolara amerykańskiego. 
Zmierzyć maksymalny potencjalny zysk dzienny, czyli procentową różnicę pomiędzy najniższą a najwyższą, występującą w 24 godzin ceny.
Program ma odświeżać się w czasie rzeczywistym i printować do konsoli w 5 wierszach zasoby oraz ich wyniki, posortowane w kolejności od najlepszego do najgorszego.
Przykładowo: wybieramy BTC, DASH, ETH, LTC, LSK i co 5 minut dostajemy update w postaci:
ETH +4.30%
BTC +3.00%
DASH +0.9%
LTC +0.4%
LSK -3.5%
(5pkt)
2. Zmienić funkcję z punktu pierwszego tak, by przyjmowała jako parametr kwotę inwestycji oraz brała pod uwagę tylko te ceny, które zadowalałyby nas również ilościowo.
Czyli w dalszym ciągu szukamy najniższej i najwyższej ceny w ciągu ostatnich 24h, ale sprawdzamy również wolumen wykonanych transakcji. 
Jeśli wprowadzona jako parametr kwota inwestycji jest stosunkowo duża jest prawdopodobne, że najniższa i najwyższa cena będą składową wielu transakcji.
(5pkt)
```
