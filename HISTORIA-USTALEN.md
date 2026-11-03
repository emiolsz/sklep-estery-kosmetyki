# Kosmetyki
Pastelowy, statyczny prototyp sklepu. Start bez intro; schemat intro otwierany ze stopki. Intro nie zawiera jeszcze docelowego filmu z twarzą i symulacją mleka.

Działające podstrony hash: /, /sklep (kategoria, tag, wyszukiwanie, sortowanie), /produkt/:id, /ulubione, /koszyk, /zamowienie, /konto, /poradnik, /poradnik/:id, /kontakt, /dostawa, /prywatnosc. Trasy hash działają po odświeżeniu bez reguł serwera. Nieznane trasy pokazują powrót do strony głównej.

Koszyk: dodawanie, usuwanie, ilości 1–99, ceny w groszowo całkowitych złotych i suma, przykładowa dostawa 12 zł/gratis od 150 zł. Stan i ulubione zapisane lokalnie, wejście walidowane. Zakończenie testu nie składa zamówienia. Dane katalogu i ceny są przykładowe; ilustracje produktów wykonano w CSS.

Formularz waliduje pola i pobiera plik tekstowy, nie wysyła wiadomości. Nie przechowuje danych kontaktowych na serwerze. Profile FB/Instagram/X kierują do informacji o braku konfiguracji; wymagają adresów właścicielki. Logowanie i prawdziwe płatności niepodłączone. Przed sprzedażą wymagane rzeczywiste produkty, dane sprzedawcy, regulamin, prywatność, dostawa, płatności i poczta.

Brak zależności i kompilacji. Pliki wdrożenia w dist/. Brak analityki i reklam. Wspierane ograniczenie ruchu, klawiatura, semantyczne linki i aria-live dla powiadomień.

Menu wielokolumnowe: pielęgnacja skóry, włosy i ciało, makijaż, higiena jamy ustnej. Dostępne po kliknięciu, obsługuje klawiaturę i Escape; zamyka się przy przejściu. Wszystkie kategorie zawierają przykładowe produkty.

Boczny koszyk jest natywnym dialogiem: otwierany z nagłówka i po dodaniu produktu, zamykany przyciskiem, Escape lub kliknięciem poza panelem; podsumowanie, usuwanie i przejście do pełnego koszyka.

Sekcja opinii nad stopką: miniatury produktów, pusty stan bez sztucznych ocen; formularz /opinie zapisuje maksymalnie 20 lokalnych recenzji testowych, prezentuje ostatnie 3. Brak publicznej publikacji i weryfikacji zakupu.

Pod opiniami sekcja społecznościowa z trzema miejscami na publikacje FB/Instagram/X. Wizualizacje są lokalnymi placeholderami, nie pobierają treści osób trzecich.

Stopka w czterech kolumnach (marka/kontakt, konto, obsługa, firma), FAQ /faq i opis sklepu /o-nas. Program poleceń i cashback nieaktywne — brak ustalonych zasad biznesowych.

Centrum obsługi klienta ma wspólne boczne menu. Strona /zwroty nosi tytuł Odstąpienie od umowy i udostępnia własny pusty formularz TXT do pobrania; nie zawiera danych sklepu referencyjnego.

Podstrony firmowe: O firmie z propozycją misji, historią do uzupełnienia i miejscem na grafikę; Kontakt z działami obsługa/oferta/media i odnośnikiem do prywatności; Regulamin i Ochrona danych z nawigacją pomocy. Brak fikcyjnych danych sprzedawcy.

Stopka dopasowana strukturalnie do ostatniego wzorca: cztery kolumny, osobny pas miejsc na Ceneo/Trustpilot (niepodłączone, bez ocen), poniżej kraj Polska/język PL/waluta PLN. Brak deklaracji obsługi innych rynków.


## Aktualny kierunek strony głównej
Różowy pasek zostaje. Nowy wzorzec: etapy pielęgnacji jak w przesłanym schemacie Koreabu, przedstawione jako pionowe pastelowe karty w duchu wcześniejszego układu Soul Decoder. Pięć kart: oczyszczanie, tonizacja, serum/esencja, maseczka i krem. Każda prowadzi do filtrowanego katalogu własnego etapu. Dodano przykładowy tonik, esencję i maskę, aby wszystkie przejścia miały wyniki. Ilustracje etapów są autorskimi grafikami SVG do dalszego dopracowania. Zachowano koszyk, ulubione, pozostałe kategorie w filtrze i centrum pomocy.

Marki: osobna strona /marki, filtr marka w katalogu (łączony z kategorią, wyszukiwaniem i sortowaniem), wyszukiwarka nagłówka uwzględnia nazwę marki, odnośniki marek przy produktach. Mizu/Nami/Sora są nazwami demonstracyjnymi, nie rzeczywistą ofertą ani deklaracją współpracy. Grafiki etapów mają przekazywać znaczenie rytuału w autorskim stylu, bez kopiowania ilustracji wzorca.

## Karty i produkty — 2 listopada 2026
Grafiki użytkowniczki zapisane w dist/assets: Twarz, Stopy, Włosy, Ręce oraz Oczyszczanie, Tonizacja, Serum, Maseczka, Krem. Włosy to jeden dział. Karty linkują do kategorii. Produkty mają pola nazwa marki, nazwa produktu, kategoria, pojemność, opis i cena, przycisk Do koszyka. Zachowane demonstracyjne opakowania CSS. Panel /#/panel-produkty umożliwia dodawanie i edycję, zapis lokalny oraz eksport JSON. To NIE jest produkcyjny CMS: wymaga wspólnej bazy i uwierzytelnienia przed sprzedażą.

Kafelki działów pod sekcją Odkrywaj pielęgnację po swojemu: Twarz, Ręce, Nogi, Włosy. Nogi używa grafiki stóp i filtruje preparaty do nóg i stóp. U góry wyłącznie pięć etapów twarzy.

Menu główne: wyłącznie Marki, Bestsellery, Kontakt. Usunięta sekcja Małe przyjemności pielęgnacji wraz z siatką produktów ze strony głównej. Pozostałe sekcje zachowane.

Sekcja Spotkajmy się także tutaj: wyłącznie tekst i linki FB/Instagram/X. Usunięte trzy demonstracyjne kafelki publikacji i produktów.

## Czytelność i przyciski zakupu
Kontrastowe przyciski #413c40 / #fffdf9, min. wysokość 46px. Opisy listy produktów 14px. Karta produktu zawiera przy cenie/zakupie informację o testowej dostawie 12 zł i progu 150 zł, odsyłacze do dostawy i zwrotów. Do 550px stały dolny pasek ceny i zakupu, połączony z formularzem ilości (form=buy), z bezpiecznym odstępem na dole i obsługą safe-area. Nie dodano rzeczywistych płatności.

## Nawigacja mobilna i zamówienie testowe
Do 700px dolna belka Sklep/Szukaj/Konto/Koszyk. Na produkcie do 550px zastępuje ją pasek zakupu. Kasa bez rozpraszających menu, opinii, social i stopki. Formularz gościa z polami autocomplete (podpowiedzi przeglądarki, bez zewnętrznego wyszukiwania adresów), wymaganymi polami, walidacją email i kodu. Kurier i odbiór osobisty testowy aktualizują dostawę i sumę. Zakończenie bez zapisu danych i bez płatności; koszyk pozostaje. Używać fikcyjnych danych. BLIK i Apple Pay niepodłączone.

## Responsywność i konfiguracja
Układ telefonu do 700px, tabletu 701–1100px, desktopu powyżej. Karty 2/3/auto-fit kolumn; działy 2/2/4. Hover powiększa zdjęcie do 1.02 i przesuwa CTA 4px, 300ms, tylko precyzyjny wskaźnik, wyłączony przy reduced-motion. Dolny koszyk ma licznik sumy sztuk odświeżany przez persist() po każdej zmianie.
Etapy: edytuj wyłącznie dist/store-config.json (cat, title, image), uruchom python build-config.py. Generowany store-config.js zapewnia działanie również przez file:// bez fetch. Nowy identyfikator kategorii wymaga dodania kategorii i przypisania produktów; zmiana liczby/kolejności istniejących etapów wymaga tylko JSON i regeneracji.

## Filtry i wyszukiwanie — 3 listopada 2026
Desktop: poziome filtry nad wynikami; tablet dwurzędowy układ; mobile zwinięte details Filtruj. Zobacz wszystkie jawnie ma ciemny tekst #413c40 na #f1d8df. Wyszukiwanie AND po słowach, ignoruje wielkość liter i polskie znaki; obejmuje nazwę, opis, stosowanie, markę, kategorię, tag i tablicę tags. Kategoria nadal ogranicza wyniki: maska spoza kategorii Włosy nie pojawi się w tej kategorii. Nie dodano fikcyjnych dopasowań ani zmiany produktów.

## Administrator i status szablonu — 3 listopada 2026
Stopka: Administrator i © 2026 Kosmetyki. Wszelkie prawa zastrzeżone. Panel /#/administrator (stary adres kompatybilny) obejmuje dodawanie/edycję produktu, ceny, zdjęcie JPG/PNG/WebP do 1 MB, ALT, tytuł zdjęcia, tagi zdjęcia i produktu, meta title/description, eksport. Zdjęcie data URL przechowywane lokalnie; limit localStorage może wymagać mniejszych zdjęć. Metadane aktualizowane klientowo, brak SSR SEO. Panel nie ma uwierzytelnienia i nie jest produkcyjnym zapleczem. Szablon demonstracyjny na sprzedaż nie oznacza gotowej integracji zamówień, płatności, wysyłki i magazynu.
