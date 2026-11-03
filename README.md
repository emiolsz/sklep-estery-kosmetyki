# Sklep kosmetyczny — prototyp

Pełny projekt HTML, CSS i JavaScript z grafikami. Nie jest motywem WordPress ani Shopify.

## Wgranie na GitHub
1. Rozpakuj ZIP na komputerze.
2. Utwórz nowe repozytorium na GitHub.
3. Wybierz **Add file → Upload files** (w pustym repozytorium: **uploading an existing file**).
4. Przeciągnij całą zawartość rozpakowanego folderu: index.html, style.css, app.js, assets i pozostałe pliki.
5. Zatwierdź przyciskiem **Commit changes**. Nie wgrywaj samego ZIP-a jako kodu strony.

Plik index.html ma być na głównym poziomie repozytorium, obok folderu assets.

## Opcjonalny podgląd przez GitHub Pages
Samo wgranie kodu nie uruchamia strony. Jeśli chcesz podgląd, w ustawieniach repozytorium
wybierz Pages, publikację z gałęzi main i katalog /(root). Dostępność Pages zależy od
planu i widoczności repozytorium. Nie zmieniaj repozytorium na publiczne bez świadomej decyzji.
Adres strony poda GitHub po publikacji.

## Uruchomienie lokalne
Otwórz index.html. Jeżeli przeglądarka ogranicza zapis lokalny, można użyć serwera:
python -m http.server 8000
Następnie http://localhost:8000.

## Stan funkcji
Katalog, filtry, wyszukiwanie, karta produktu, koszyk, ulubione, test zamówienia,
panel edycji produktów, zdjęć, ALT, tagów i metadanych. Układ telefonu, tabletu i desktopu.
Administrator dostępny w stopce; zapis wyłącznie w localStorage tej przeglądarki.
W formularzu zamówienia używaj fikcyjnych danych. Nie ma aktywnych płatności,
prawdziwych zamówień, wspólnej bazy, zabezpieczonego logowania ani wysyłki e-mail.
Panel lokalny nie powinien być przedstawiany jako produkcyjne zaplecze.

## Konfiguracja etapów
Edytuj store-config.json i uruchom python build-config.py. Wynikiem jest store-config.js,
który umożliwia otwieranie wersji lokalnej bez fetch.

## Wznowienie projektu
Dokumenty w katalogu dokumentacja opisują ustalenia, grafiki, ograniczenia i kolejne kroki.
Nie zawierają pełnego transkryptu rozmowy słowo w słowo. Paczka nie zawiera danych
przeglądarki użytkowniczki, haseł ani kluczy usług.

Stan: 3 listopada 2026. Wersja kodu odpowiada prototypowi v5.
Prawa i warunki dystrybucji komercyjnej wymagają osobnego ustalenia.
