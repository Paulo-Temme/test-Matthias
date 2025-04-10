// Browser Automation Script für Tinder / Skype
const puppeteer = require('puppeteer');

async function startAutomation(website) {
  console.log(`Starte Browser-Automation für: ${website}`);
  
  // Browser starten
  const browser = await puppeteer.launch({
    headless: false, // Browser sichtbar machen
    defaultViewport: null, // Vollständige Seite anzeigen
    args: ['--start-maximized'] // Browser-Fenster maximieren
  });

  // Neuen Tab öffnen
  const page = await browser.newPage();
  
  try {
    // Zur gewünschten Website navigieren
    console.log(`Navigiere zu ${website}...`);
    await page.goto(website, { waitUntil: 'networkidle2' });

    if (website.includes('tinder.com')) {
      await handleTinder(page);
    } else if (website.includes('skype.com')) {
      await handleSkype(page);
    } else {
      console.log('Für diese Website gibt es kein spezielles Skript. Allgemeiner Browser wird geöffnet.');
    }

    // Browser geöffnet lassen, bis der Benutzer Strg+C drückt
    console.log('\nBrowser läuft. Drücke Strg+C im Terminal, um das Programm zu beenden.');
    
  } catch (error) {
    console.error('Ein Fehler ist aufgetreten:', error);
    await browser.close();
  }
}

async function handleTinder(page) {
  console.log('Tinder-spezifische Automation wird gestartet...');
  
  // Warten auf Ladevorgang
  await page.waitForTimeout(3000);
  
  // Hier Tinder-spezifische Aktionen einfügen
  // Beispiel: Login-Button finden und klicken
  try {
    const loginButton = await page.waitForSelector('button[aria-label="Log in"]', { timeout: 5000 });
    if (loginButton) {
      await loginButton.click();
      console.log('Login-Button geklickt');
      
      // Warten auf Login-Prozess
      console.log('Warte auf Login-Prozess...');
      await page.waitForTimeout(5000);
    }
  } catch (error) {
    console.log('Login-Button nicht gefunden oder bereits eingeloggt');
  }
  
  // Nach dem Login: Starte automatisches Swipen
  console.log('Starte automatisches Swipen...');
  await autoSwipe(page);
}

// Neue Funktion für automatisches Swipen
async function autoSwipe(page) {
  // Anzahl der Swipes
  const swipeCount = 20;
  console.log(`Werde ${swipeCount} mal swipen...`);
  
  // Warten bis die Haupt-Tinder-Oberfläche geladen ist
  await page.waitForTimeout(5000);
  
  for (let i = 0; i < swipeCount; i++) {
    try {
      // Zufällig entscheiden: Links oder Rechts swipen (70% Rechts / 30% Links)
      const swipeRight = Math.random() < 0.7;
      
      if (swipeRight) {
        // Nach rechts swipen (Like)
        console.log(`Swipe ${i+1}/${swipeCount}: Nach rechts (Like) ❤️`);
        
        // Suchen und Klicken des Like-Buttons (verschiedene mögliche Selektoren)
        try {
          // Versuche mit Tastenkürzel (Pfeil rechts)
          await page.keyboard.press('ArrowRight');
        } catch (e) {
          // Alternative: Versuche Like-Button zu finden und klicken
          try {
            const likeButton = await page.waitForSelector('button[aria-label="Like"]', { timeout: 2000 });
            if (likeButton) await likeButton.click();
          } catch (err) {
            console.log('Like-Button nicht gefunden, versuche alternative Methode');
            // Alternate Methode: Position schätzen und klicken
            await page.mouse.click(document.body.clientWidth * 0.8, document.body.clientHeight * 0.5);
          }
        }
      } else {
        // Nach links swipen (Nope)
        console.log(`Swipe ${i+1}/${swipeCount}: Nach links (Nope) 👎`);
        
        try {
          // Versuche mit Tastenkürzel (Pfeil links)
          await page.keyboard.press('ArrowLeft');
        } catch (e) {
          // Alternative: Versuche Nope-Button zu finden und klicken
          try {
            const nopeButton = await page.waitForSelector('button[aria-label="Nope"]', { timeout: 2000 });
            if (nopeButton) await nopeButton.click();
          } catch (err) {
            console.log('Nope-Button nicht gefunden, versuche alternative Methode');
            // Alternate Methode: Position schätzen und klicken
            await page.mouse.click(document.body.clientWidth * 0.2, document.body.clientHeight * 0.5);
          }
        }
      }
      
      // Warten zwischen Swipes (zufällige Zeit zwischen 1-3 Sekunden)
      const waitTime = 1000 + Math.random() * 2000;
      await page.waitForTimeout(waitTime);
      
      // Popup-Dialog behandeln (falls einer erscheint)
      try {
        const popupClose = await page.waitForSelector('button[aria-label="Close"]', { timeout: 1000 });
        if (popupClose) {
          await popupClose.click();
          console.log('Popup geschlossen');
          await page.waitForTimeout(500);
        }
      } catch (e) {
        // Kein Popup gefunden, normal weitermachen
      }
      
    } catch (error) {
      console.log(`Fehler beim Swipen: ${error}`);
    }
  }
  
  console.log('Automatisches Swipen beendet!');
}

async function handleSkype(page) {
  console.log('Skype-spezifische Automation wird gestartet...');
  
  // Warten auf Ladevorgang
  await page.waitForTimeout(3000);
  
  // Hier Skype-spezifische Aktionen einfügen
  try {
    const signInButton = await page.waitForSelector('a[data-bi-name="signin"]', { timeout: 5000 });
    if (signInButton) {
      await signInButton.click();
      console.log('Anmelde-Button geklickt');
    }
  } catch (error) {
    console.log('Anmelde-Button nicht gefunden oder bereits eingeloggt');
  }
  
  console.log('Du kannst jetzt Skype im Browser verwenden');
}

// Beispielaufruf (kann später angepasst werden)
const website = process.argv[2] || 'https://tinder.com';
startAutomation(website);
