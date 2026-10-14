cena_netto_za_godzine = 50.50
liczba_godzin = 8

wartosc_uslugi_netto = cena_netto_za_godzine * liczba_godzin
stawk_vat = 23
kwota_vat = wartosc_uslugi_netto * (23/100)
wartosc_brutto_do_zaplaty = wartosc_uslugi_netto + kwota_vat

print(f"Kwota do zapłaty z podatkiem VAT to {wartosc_brutto_do_zaplaty}")
