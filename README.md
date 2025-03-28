# Real-Time Flipperkast Game

## **Overview**
Een interactieve, real-time flipperkast game ontwikkeld als herkansingsopdracht voor WP6 (SWDWER61X2) — Rotterdam Academy, Software Development.

---
## **Bestaat uit**
- Realtime physics-based flipperkast
- Bestuurbare flippers (toetsen A & L)
- Beweegbare metalen bal met natuurkundige reflectie
- Botsing met bumpers levert score op
- Scorepaneel per speler + highscore
- Realtime communicatie via MQTT
- Volledige grafische weergave met Pygame
- Test Driven Development (TDD) toegepast

---

## **Installatie**
1. Clone het project
```bash
git clone <jouw-repo-url>
cd flipperkast
```

2. Installeer dependencies
```bash
pip install -r requirements.txt
```

## **Starten van het spel**
```bash
python main.py
```

## **Besturing**
- Besturing:
```yaml
A = linkerflipper

L = rechterflipper
*Laat de bal bumpers raken om punten te scoren. Scores worden live bijgehouden bovenin het scherm.*
```

## **MQTT**
- MQTT Explorer of andere clients kunnen deze topics gebruiken om communicatie te bekijken of simuleren.
- Gebruik MQTT Explorer met broker broker.hivemq.com (poort 1883) om te zien hoe de game live berichten verstuurt op MQTT-topics.

## **Tests uitvoeren ** 
### Het project is opgezet volgens Test Driven Development (TDD).
Unit tests bevinden zich in de tests/ map.

Run alle tests via:
```bash
pytest
```
