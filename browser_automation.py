#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def start_automation(website):
    """Startet die Browser-Automation für die angegebene Website"""
    print(f"Starte Browser-Automation für: {website}")
    
    # Browser-Einstellungen
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Browser-Fenster maximieren
    
    # Browser starten mit automatisch heruntergeladenem ChromeDriver
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Zur Bumble Website navigieren
        print("Navigiere zu Bumble...")
        browser.get("https://bumble.com")
        time.sleep(2)  # Kurz warten, bis die Seite geladen ist
        
        # Starte Bumble Automation
        handle_bumble(browser)
        
        print("\nBrowser läuft. Drücke Strg+C im Terminal, um das Programm zu beenden.")
        
        # Browser offen lassen bis Strg+C gedrückt wird
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nProgramm wird beendet...")
            
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        # Bei Beendigung des Programms Browser schließen
        # browser.quit()  # Auskommentiert, damit der Browser offen bleibt
        pass


def handle_tinder(browser):
    """Führt Tinder-spezifische Aktionen aus"""
    print("Tinder-spezifische Automation wird gestartet...")
    
    # Warten auf Ladevorgang
    time.sleep(3)
    
    # Login-Button finden und klicken
    try:
        login_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Log in') or contains(text(), 'Log in')]"))
        )
        login_button.click()
        print("Login-Button geklickt")
        
        # Warten auf Login-Prozess
        print("Warte auf Login-Prozess...")
        time.sleep(5)
    except (TimeoutException, NoSuchElementException) as e:
        print("Login-Button nicht gefunden oder bereits eingeloggt")
    
    # Nach dem Login: Starte automatisches Swipen
    print("Starte automatisches Swipen...")
    auto_swipe(browser)


def auto_swipe(browser):
    """Automatisches Swipen auf Tinder"""
    # Anzahl der Swipes
    swipe_count = 20
    print(f"Werde {swipe_count} mal swipen...")
    
    # Warten bis die Haupt-Tinder-Oberfläche geladen ist
    time.sleep(5)
    
    for i in range(swipe_count):
        try:
            # Zufällig entscheiden: Links oder Rechts swipen (70% Rechts / 30% Links)
            swipe_right = random.random() < 0.7
            
            if swipe_right:
                # Nach rechts swipen (Like)
                print(f"Swipe {i+1}/{swipe_count}: Nach rechts (Like) ❤️")
                
                # Verschiedene Methoden versuchen
                try:
                    # Methode 1: Tastenkürzel
                    webdriver.ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
                except Exception:
                    try:
                        # Methode 2: Like-Button finden und klicken
                        like_button = browser.find_element(By.XPATH, "//button[contains(@aria-label, 'Like') or contains(@title, 'Like')]")
                        like_button.click()
                    except NoSuchElementException:
                        # Methode 3: Position schätzen und klicken
                        print("Like-Button nicht gefunden, versuche alternative Methode")
                        window_width = browser.execute_script("return window.innerWidth")
                        window_height = browser.execute_script("return window.innerHeight")
                        webdriver.ActionChains(browser).move_by_offset(int(window_width * 0.8), int(window_height * 0.5)).click().perform()
                        webdriver.ActionChains(browser).move_by_offset(-int(window_width * 0.8), -int(window_height * 0.5)).perform()
            else:
                # Nach links swipen (Nope)
                print(f"Swipe {i+1}/{swipe_count}: Nach links (Nope) 👎")
                
                try:
                    # Methode 1: Tastenkürzel
                    webdriver.ActionChains(browser).send_keys(Keys.ARROW_LEFT).perform()
                except Exception:
                    try:
                        # Methode 2: Nope-Button finden und klicken
                        nope_button = browser.find_element(By.XPATH, "//button[contains(@aria-label, 'Nope') or contains(@title, 'Nope')]")
                        nope_button.click()
                    except NoSuchElementException:
                        # Methode 3: Position schätzen und klicken
                        print("Nope-Button nicht gefunden, versuche alternative Methode")
                        window_width = browser.execute_script("return window.innerWidth")
                        window_height = browser.execute_script("return window.innerHeight")
                        webdriver.ActionChains(browser).move_by_offset(int(window_width * 0.2), int(window_height * 0.5)).click().perform()
                        webdriver.ActionChains(browser).move_by_offset(-int(window_width * 0.2), -int(window_height * 0.5)).perform()
            
            # Warten zwischen Swipes (zufällige Zeit zwischen 1-3 Sekunden)
            wait_time = 1 + random.random() * 2
            time.sleep(wait_time)
            
            # Popup-Dialog behandeln (falls einer erscheint)
            try:
                popup_close = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Close') or contains(@title, 'Close')]"))
                )
                popup_close.click()
                print("Popup geschlossen")
                time.sleep(0.5)
            except (TimeoutException, NoSuchElementException):
                # Kein Popup gefunden, normal weitermachen
                pass
                
        except Exception as e:
            print(f"Fehler beim Swipen: {e}")
    
    print("Automatisches Swipen beendet!")


def handle_bumble(browser):
    """Führt Bumble-spezifische Aktionen aus"""
    print("Bumble-spezifische Automation wird gestartet...")
    
    # Warten auf Ladevorgang
    time.sleep(3)
    
    # Login-Button finden und klicken
    try:
        # Verschiedene mögliche Selektoren für den Login-Button auf Bumble probieren
        selectors = [
            "//button[contains(text(), 'Log in')]",
            "//span[contains(text(), 'Log in')]",
            "//div[contains(text(), 'Log in')]",
            "//button[contains(@class, 'login')]"
        ]
        
        for selector in selectors:
            try:
                login_button = WebDriverWait(browser, 2).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                login_button.click()
                print("Login-Button geklickt")
                time.sleep(5)  # Warten auf Login-Formular
                break  # Wenn erfolgreich, Schleife beenden
            except (TimeoutException, NoSuchElementException):
                continue  # Wenn dieser Selektor nicht funktioniert, nächsten probieren
                
    except Exception as e:
        print(f"Login-Button nicht gefunden oder bereits eingeloggt: {e}")
    
    # Warten auf manuelle Bestätigung des Benutzers
    print("\n-----------------------------------------------------")
    print("WICHTIG: Bitte logge dich jetzt manuell ein und akzeptiere/deaktiviere alle Cookies.")
    print("Wenn du fertig bist und bereit für das automatische Swipen bist,")
    input("drücke ENTER im Terminal, um mit dem Swipen zu beginnen... ")
    print("-----------------------------------------------------")
    
    # Nach manueller Bestätigung: Starte automatisches Swipen
    print("Starte automatisches Swipen auf Bumble...")
    auto_swipe_bumble(browser)


def auto_swipe_bumble(browser):
    """Automatisches Swipen auf Bumble"""
    # Anzahl der Swipes
    swipe_count = 20
    print(f"Werde {swipe_count} mal swipen...")
    
    # Warten bis die Haupt-Bumble-Oberfläche geladen ist
    time.sleep(5)
    
    for i in range(swipe_count):
        try:
            # Zufällig entscheiden: Links oder Rechts swipen (70% Rechts / 30% Links)
            swipe_right = random.random() < 0.7
            
            if swipe_right:
                # Nach rechts swipen (Like)
                print(f"Swipe {i+1}/{swipe_count}: Nach rechts (Like) ❤️")
                
                # Verschiedene Methoden versuchen
                try:
                    # Methode 1: Tastenkürzel für Bumble (Pfeil rechts)
                    webdriver.ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
                except Exception:
                    try:
                        # Methode 2: Like-Button finden und klicken (verschiedene mögliche Selektoren für Bumble)
                        like_selectors = [
                            "//button[contains(@class, 'like')]",
                            "//span[contains(@class, 'like')]",
                            "//div[contains(@class, 'like')]",
                            "//button[contains(@aria-label, 'Yes')]",
                            "//button[contains(@title, 'Like')]"
                        ]
                        
                        for selector in like_selectors:
                            try:
                                like_button = browser.find_element(By.XPATH, selector)
                                like_button.click()
                                print(f"Like-Button mit Selektor {selector} gefunden und geklickt")
                                break
                            except NoSuchElementException:
                                continue
                    except Exception:
                        # Methode 3: Position schätzen und klicken
                        print("Like-Button nicht gefunden, versuche alternative Methode")
                        window_width = browser.execute_script("return window.innerWidth")
                        window_height = browser.execute_script("return window.innerHeight")
                        webdriver.ActionChains(browser).move_by_offset(int(window_width * 0.8), int(window_height * 0.5)).click().perform()
                        webdriver.ActionChains(browser).move_by_offset(-int(window_width * 0.8), -int(window_height * 0.5)).perform()
            else:
                # Nach links swipen (Nope)
                print(f"Swipe {i+1}/{swipe_count}: Nach links (Nope) 👎")
                
                try:
                    # Methode 1: Tastenkürzel
                    webdriver.ActionChains(browser).send_keys(Keys.ARROW_LEFT).perform()
                except Exception:
                    try:
                        # Methode 2: Nope-Button finden und klicken (verschiedene mögliche Selektoren für Bumble)
                        nope_selectors = [
                            "//button[contains(@class, 'nope')]",
                            "//span[contains(@class, 'nope')]",
                            "//div[contains(@class, 'nope')]",
                            "//button[contains(@aria-label, 'No')]",
                            "//button[contains(@title, 'Nope')]"
                        ]
                        
                        for selector in nope_selectors:
                            try:
                                nope_button = browser.find_element(By.XPATH, selector)
                                nope_button.click()
                                print(f"Nope-Button mit Selektor {selector} gefunden und geklickt")
                                break
                            except NoSuchElementException:
                                continue
                    except Exception:
                        # Methode 3: Position schätzen und klicken
                        print("Nope-Button nicht gefunden, versuche alternative Methode")
                        window_width = browser.execute_script("return window.innerWidth")
                        window_height = browser.execute_script("return window.innerHeight")
                        webdriver.ActionChains(browser).move_by_offset(int(window_width * 0.2), int(window_height * 0.5)).click().perform()
                        webdriver.ActionChains(browser).move_by_offset(-int(window_width * 0.2), -int(window_height * 0.5)).perform()
            
            # Warten zwischen Swipes (zufällige Zeit zwischen 1-3 Sekunden)
            wait_time = 1 + random.random() * 2
            time.sleep(wait_time)
            
            # Popup-Dialog behandeln (falls einer erscheint)
            try:
                popup_selectors = [
                    "//button[contains(@aria-label, 'Close')]",
                    "//button[contains(@aria-label, 'Nein')]",
                    "//button[contains(@aria-label, 'Vielleicht später')]",
                    "//button[contains(text(), 'Nicht jetzt')]"
                ]
                
                for selector in popup_selectors:
                    try:
                        popup_close = WebDriverWait(browser, 1).until(
                            EC.presence_of_element_located((By.XPATH, selector))
                        )
                        popup_close.click()
                        print(f"Popup mit Selektor {selector} geschlossen")
                        time.sleep(0.5)
                        break
                    except (TimeoutException, NoSuchElementException):
                        continue
            except Exception:
                # Kein Popup gefunden oder konnte nicht geschlossen werden, normal weitermachen
                pass
                
        except Exception as e:
            print(f"Fehler beim Swipen: {e}")
    
    print("Automatisches Swipen auf Bumble beendet!")


def handle_skype(browser):
    """Führt Skype-spezifische Aktionen aus"""
    print("Skype-spezifische Automation wird gestartet...")
    
    # Warten auf Ladevorgang
    time.sleep(3)
    
    # Anmelde-Button finden und klicken
    try:
        signin_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@data-bi-name, 'signin') or contains(text(), 'Sign in')]"))
        )
        signin_button.click()
        print("Anmelde-Button geklickt")
    except (TimeoutException, NoSuchElementException) as e:
        print("Anmelde-Button nicht gefunden oder bereits eingeloggt")
    
    print("Du kannst jetzt Skype im Browser verwenden")


if __name__ == "__main__":
    # Website aus Kommandozeilenargumenten oder Standardwert 'https://tinder.com'
    website = sys.argv[1] if len(sys.argv) > 1 else "https://tinder.com"
    start_automation(website)
