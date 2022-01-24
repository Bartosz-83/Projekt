# Import modulu unittest
import unittest
# Import webdrivera
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import Select


# DANE TESTOWE:
imie = "Marzena"
nazwisko = "Nowak"
email = "bart0.tester@gmail.com"
haslo = "Qwerty@1234"
powtorz = "Qwerty@1234"
tytul = "Prof."
plec = "Pani"
# zmienne
niepoprawny_email = "jasdhfjh.kj"
zle_powtorz = "Qwert@1234"
brak_imienia = ""


# TestCase z modulu unittest
class APRegistration(unittest.TestCase):

    # Przygotowanie do kazdego testu
    def setUp(self):
        self.driver = webdriver.Chrome()
        # Włączamy strone sixt.pl
        self.driver.get('https://www.sixt.pl/')
        self.driver.maximize_window()
        # Czekaj max 15 sekund na elementy
        self.driver.implicitly_wait(15)

    # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.driver.quit()

# Test 1 Próba rejestracji z niepoprawnym adresem email.
    def testInvalidEmail(self):
        driver = self.driver
        # KROK 1: Akceptacja cookie
        zamykanie_reklamy = driver.find_element_by_class_name('t3-cookie-agreement')
        zamykanie_reklamy.click()
        # KROK 2 Kliknij rejestracja
        kliknij_login = driver.find_element_by_xpath("//li[@class='t3-main-navi-item t3-main-navi-hd-login']")
        kliknij_login.click()
        # tutaj uzywam sleep.Strona wymagala chwile na zaladowanie
        sleep(2)
        # KROK 3. Wejdz w rejestracje
        wejdz_rejestracje = driver.find_element_by_xpath("//div[@class='modal__content__button modal__content__button--register']")
        wejdz_rejestracje.click()
        # KROK 4. Wybierz plec
        select = Select(driver.find_element_by_name("start[personal_data][salutation]"))
        select.select_by_visible_text(plec)
        #KROK 5. Wybierz tytul
        select2 = Select(driver.find_element_by_name("start[personal_data][title]"))
        select2.select_by_visible_text(tytul)
        #Krok 6. Wpisz imie
        imie_input = driver.find_element_by_name('start[personal_data][first_name]')
        imie_input.send_keys(imie)
        #Krok 7. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_name('start[personal_data][last_name]')
        nazwisko_input.send_keys(nazwisko)
        #Krok 8. Wpisz email
        email_input = driver.find_element_by_name('start[email]')
        email_input.send_keys(niepoprawny_email)
        #Krok 9. Wpisz haslo
        haslo_input = driver.find_element_by_name('start[password][pwd]')
        haslo_input.send_keys(haslo)
        #Krok 10. Powtorz haslo
        powtorz_input = driver.find_element_by_name('start[password][confirm]')
        powtorz_input.send_keys(powtorz)
        #Krok 11. Kliknij rejestroj
        rejestroj = driver.find_element_by_xpath("//button[@class='sx-gc-button-cta sx-gc-button-cta-green']")
        rejestroj.click()

        ### TEST !!! ###
        # SPRAWDZENIE OCZEKIWANEGO REZULTATU
        error_notices = driver.find_elements_by_xpath('//div[@class="sx-gc-error"]/p')
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
                # Sprawdzam, czy widoczny jest tylko jeden błąd
                assert len(visible_error_notices) == 1
                # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        self.assertEqual(error_text,"E-mail : Proszę podać poprawny adres e-mail")
        print("Błąd logowania:",error_text)

# Test 2 Próba rejestracji z niepoprawnie powtorzonym haslem.

    def testInvalidPassword(self):
        driver = self.driver
        # KROK 1: Akceptacja cookie
        zamykanie_reklamy = driver.find_element_by_class_name('t3-cookie-agreement')
        zamykanie_reklamy.click()
        # KROK 2 Kliknij rejestracja
        kliknij_login = driver.find_element_by_xpath("//li[@class='t3-main-navi-item t3-main-navi-hd-login']")
        kliknij_login.click()
        # tutaj uzywam sleep.Strona wymagala chwile na zaladowanie
        sleep(2)
        # KROK 3. Wejdz w rejestracje
        wejdz_rejestracje = driver.find_element_by_xpath("//div[@class='modal__content__button modal__content__button--register']")
        wejdz_rejestracje.click()
        # KROK 4. Wybierz plec
        select = Select(driver.find_element_by_name("start[personal_data][salutation]"))
        select.select_by_visible_text(plec)
        #KROK 5. Wybierz tytul
        select2 = Select(driver.find_element_by_name("start[personal_data][title]"))
        select2.select_by_visible_text(tytul)
        #Krok 6. Wpisz imie
        imie_input = driver.find_element_by_name('start[personal_data][first_name]')
        imie_input.send_keys(imie)
        #Krok 7. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_name('start[personal_data][last_name]')
        nazwisko_input.send_keys(nazwisko)
        #Krok 8. Wpisz email
        email_input = driver.find_element_by_name('start[email]')
        email_input.send_keys(email)
        #Krok 9. Wpisz haslo
        haslo_input = driver.find_element_by_name('start[password][pwd]')
        haslo_input.send_keys(haslo)
        #Krok 10. Nieprawidlowo powtorz haslo
        powtorz_input = driver.find_element_by_name('start[password][confirm]')
        powtorz_input.send_keys(zle_powtorz)
        #Krok 11. Kliknij rejestruj
        rejestroj = driver.find_element_by_xpath("//button[@class='sx-gc-button-cta sx-gc-button-cta-green']")
        rejestroj.click()

        ### TEST !!! ###
        # SPRAWDZENIE OCZEKIWANEGO REZULTATU

        error_notices = driver.find_elements_by_xpath('//div[@class="sx-gc-error"]/p')
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
                # Sprawdzam, czy widoczny jest tylko jeden błąd
                assert len(visible_error_notices) == 1
                # Sprawdzam treść widocznego błędu
        error_text2 = visible_error_notices[0].get_attribute("innerText")
        self.assertEqual(error_text2,"Hasło : Hasła muszą być takie same.")
        print("Błąd logowania:",error_text2)


# Test 3 Próba rejestracji bez podania imienia w formularzu
    def testno_name(self):
        driver = self.driver
        # KROK 1: Akceptacja cookie
        zamykanie_reklamy = driver.find_element_by_class_name('t3-cookie-agreement')
        zamykanie_reklamy.click()
        # KROK 2 Kliknij rejestracja
        kliknij_login = driver.find_element_by_xpath("//li[@class='t3-main-navi-item t3-main-navi-hd-login']")
        kliknij_login.click()
        # tutaj uzywam sleep.Strona wymagala chwile na zaladowanie
        sleep(2)
        # KROK 3. Wejdz w rejestracje
        wejdz_rejestracje = driver.find_element_by_xpath("//div[@class='modal__content__button modal__content__button--register']")
        wejdz_rejestracje.click()
        # KROK 4. Wybierz plec
        select = Select(driver.find_element_by_name("start[personal_data][salutation]"))
        select.select_by_visible_text(plec)
        #KROK 5. Wybierz tytul
        select2 = Select(driver.find_element_by_name("start[personal_data][title]"))
        select2.select_by_visible_text(tytul)
        #Krok 6. Nie wpisuj imienia
        imie_input = driver.find_element_by_name('start[personal_data][first_name]')
        imie_input.send_keys(brak_imienia)
        #Krok 7. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_name('start[personal_data][last_name]')
        nazwisko_input.send_keys(nazwisko)
        #Krok 8. Wpisz email
        email_input = driver.find_element_by_name('start[email]')
        email_input.send_keys(email)
        #Krok 9. Wpisz haslo
        haslo_input = driver.find_element_by_name('start[password][pwd]')
        haslo_input.send_keys(haslo)
        #Krok 10. Powtorz haslo
        powtorz_input = driver.find_element_by_name('start[password][confirm]')
        powtorz_input.send_keys(powtorz)
        #Krok 11. Kliknij rejestruj
        rejestroj = driver.find_element_by_xpath("//button[@class='sx-gc-button-cta sx-gc-button-cta-green']")
        rejestroj.click()

        ### TEST !!! ###
        # SPRAWDZENIE OCZEKIWANEGO REZULTATU

        error_notices = driver.find_elements_by_xpath('//div[@class="sx-gc-error"]/p')
        visible_error_notices = []
        #print(visible_error_notices)
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
                # Sprawdzam, czy widoczny jest tylko jeden błąd
                assert len(visible_error_notices) == 1
                # Sprawdzam treść widocznego błędu
        error_text3 = visible_error_notices[0].get_attribute("innerText")
        self.assertEqual(error_text3,"Imię : Pole nie może być puste. Prosimy o wypełnienie tego pola.")
        print("Błąd logowania",error_text3)



# Uruchom test jesli uruchamiamy
# ten plik
if __name__ == "__main__":
    unittest.main(verbosity=2)
