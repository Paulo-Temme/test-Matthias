# Browser Automation für Tinder/Skype

Dieses Skript ermöglicht das automatische Interagieren mit Webseiten wie Tinder und Skype im Browser.

## Installation

### 1. Node.js installieren

Für macOS gibt es zwei einfache Möglichkeiten:

**Option A: Direkt von der Website**
1. Besuche [nodejs.org](https://nodejs.org/)
2. Lade die LTS-Version herunter und installiere sie

**Option B: Mit Homebrew (falls installiert)**
```
brew install node
```

### 2. Projektabhängigkeiten installieren

Öffne das Terminal im Projektverzeichnis und führe die folgenden Befehle aus:

```
npm init -y
npm install puppeteer
```

## Verwendung

Starte das Skript mit einem der folgenden Befehle:

```
node browser_automation.js https://tinder.com
```

oder

```
node browser_automation.js https://web.skype.com
```

## Funktionen

- Öffnet einen automatisierten Chrome-Browser
- Bei Tinder: Automatisches Swipen (70% rechts/30% links)
- Bei Skype: Unterstützung beim Login

## Hinweis

Nach dem Start des Browsers musst du dich manuell einloggen. Das Skript wartet darauf und startet dann die automatischen Aktionen.
