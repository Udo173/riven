# Design System: Riven

## 1. Visual Theme & Atmosphere

Riven's Musik-Projekt verkörpert den Kampf des Aufstehens - von Dunkelheit zu Triumph. Das Design spiegelt diese Reise wider: von tiefem, fast schwarzem Indigo zu feurigem Gold und strahlendem Weiss. Jede Phase der Transformation hat ihren eigenen visuellen Charakter, aber alle teilen eine gemeinsame Identität: Rohheit, Entschlossenheit und schliessliche Erlösung.

Das Design ist inspiriert von Linear's Präzision, Stripe's Luxus und Vercel's technischer Eleganz - adaptiert für ein emotionales Musik-Projekt.

## 2. Color Palette & Roles

### Phase 1: Dunkelheit (0:00-33:00s)
```
Background:     #0a0a14  (Void Black)
Surface:        #12121f  (Tiefes Indigo)
Text Primary:   #d0d6e0  (Gedämpftes Silber)
Text Muted:     #62666d  (Leiser Nebel)
Border:         rgba(255,255,255,0.05)
```

### Phase 2: Kampf (33:00-57:00s)
```
Background:     #1a1a2e  (Kampf-Indigo)
Surface:        #252542  (Erhobenes Indigo)
Accent Primary: #6b5b95  (Müdes Violett)
Accent Second:  #4a3f6b  (Dunkles Lila)
Text Primary:   #f7f8f8  (Helles Weiss)
Border:         rgba(255,255,255,0.08)
```

### Phase 3: Identität (57:00-66:00s)
```
Background:     #1a1a2e  (Dunkler Grund)
Accent Warm:    #ff8c42  (Aufgehende Sonne)
Accent Gold:    #ffd166  (Goldenes Licht)
Accent Green:   #06d6a0  (Hoffnung)
Text Primary:   #ffffff  (Reines Weiss)
```

### Phase 4: Feuer (66:00-84:00s)
```
Background:     #0a0a14  (Rückkehr zur Dunkelheit)
Accent Fire:    #ef476f  (Feuer-Rot)
Accent Orange:  #ff6b35  (Flamme)
Accent Gold:    #ffd166  (Glut)
Text Primary:   #ffffff  (Weiss)
Glow:           rgba(255,107,53,0.3)
```

### Phase 5: Triumph (84:00-99:00s)
```
Background:     #0d0d1a  (Siegreiches Schwarz)
Accent Gold:    #ffd166  (Triumph-Gold)
Accent White:   #ffffff  (Weisses Licht)
Accent Green:   #06d6a0  (Erfolg)
Text Primary:   #ffffff  (Weiss)
Glow:           rgba(255,209,102,0.4)
```

### Universal Constants
```
Logo Glow:      rgba(255,209,102,0.5)  (Goldener Riven-Schimmer)
Particle Gold:  #ffd166
Particle Orange:#ff8c42
Shadow Base:    rgba(0,0,0,0.6)
```

## 3. Typography Rules

### Font Family
- **Display/Headlines**: Inter Variable (wie Linear) mit `"cv01", "ss03"`
- **Body/UI**: Inter Variable, 400-510 weight
- **Monospace/Technical**: Geist Mono (wie Vercel)
- **Fallbacks**: system-ui, -apple-system, Segoe UI, sans-serif

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Color | Notes |
|------|------|--------|-------------|----------------|-------|-------|
| Display Hero | 72px | 510 | 1.00 | -1.584px | #ffffff | Erster Songtitel |
| Section Hero | 56px | 510 | 1.05 | -1.4px | #ffffff | Lyric-Display |
| Section Large | 48px | 510 | 1.10 | -1.056px | #ffd166 | Goldene Highlights |
| Heading | 32px | 400 | 1.13 | -0.704px | #f7f8f8 | Section-Titel |
| Sub-heading | 24px | 400 | 1.33 | -0.288px | #d0d6e0 | Untertitel |
| Lyric Large | 36px | 510 | 1.20 | -0.5px | #ffffff | Haupt-Lyrics |
| Lyric Medium | 28px | 400 | 1.30 | -0.3px | #d0d6e0 | Zweite Zeile |
| Body | 18px | 400 | 1.60 | normal | #d0d6e0 | Beschreibungen |
| Caption | 14px | 510 | 1.50 | -0.182px | #8a8f98 | Metadata |
| Logo Text | 24px | 700 | 1.00 | 2px | #ffd166 | "Created by Riven" |

### Typography Principles
- **Negative Tracking**: Display-Grössen nutzen aggressives negative Letter-Spacing wie Linear (-1.5px bei 72px)
- **OpenType Features**: `"cv01", "ss03"` aktiviert für geometrischere Zeichenformen
- **Gold für Akzente**: Gold (#ffd166) nur für Logo, wichtige Worte ("RISE", "TIME")
- **Monospace für Tags**: Kleine Labels wie "Created by Riven" in monospace

## 4. Component Stylings

### Logo Treatment
```
Size:           200-300px (skaliert mit Viewport)
Position:       Unten fixiert, 10% vom unteren Rand
Glow:           0 0 40px rgba(255,209,102,0.5)
Animation:      Subtiles Pulsieren (2s ease-in-out infinite)
```

### Lyric Cards
```
Background:     Transparent mit Gradient-Overlay
Border:         rgba(255,255,255,0.1)
Radius:         12px
Padding:        24px 32px
Shadow:         0 8px 32px rgba(0,0,0,0.4)
Animation:      Fade-in + leichter Aufstieg (Y: 20px -> 0)
```

### Particle System
```
Type:           Goldene Partikel (aufsteigend)
Count:          50-100 Partikel
Size:           2-6px
Color:          #ffd166 (primär), #ff8c42 (sekundär)
Speed:          Langsam, meditativ (3-8s für vollen Durchgang)
Opacity:        0.3-0.8, fadend
```

### Progress Indicator
```
Position:       Unterer Rand, über Logo
Height:         2px
Background:     rgba(255,255,255,0.1)
Fill:           Linearer Gradient #ffd166 -> #ff8c42
```

### Buttons (falls benötigt)
```
Primary:        #ffd166 bg, #0a0a14 text, 6px radius
Ghost:          transparent bg, #ffd166 text, 1px #ffd166 border
Hover:          Leichte Aufhellung
```

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px
- Generous whitespace um Lyrics für Fokus

### Video Composition
```
Canvas:         1920x1080 (16:9)
Safe Zone:      Zentrale 80% für Content
Logo Zone:      Untere 20%
Lyric Zone:     Zentrum (60% vertikal)
```

### Whitespace Philosophy
- **Fokus durch Leere**: Viel Raum um die Lyrics für emotionalen Impact
- **Dunkelheit als Leinwand**: Schwarze Flächen lassen goldene Elemente strahlen
- **Atmung**: Sections haben 64-96px Abstand für Rhythmus

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | Kein Shadow | Hintergrund |
| Lyric Card | 0 8px 32px rgba(0,0,0,0.4) | Lyric-Text |
| Logo Glow | 0 0 40px rgba(255,209,102,0.5) | Riven Logo |
| Particle | 0 0 10px rgba(255,209,102,0.3) | Goldene Partikel |

### Depth Principles
- **Schwarze Tiefe**: Dunkle Hintergründe absorbieren Licht
- **Gold strahlt**: Goldene Akzente lepten sich vom Dunkel ab
- **Sanfte Schatten**: Keine harten Kanten - alles fliesst

## 7. Animation Principles

### Timing Functions
```css
ease-out:       cubic-bezier(0.16, 1, 0.3, 1)   /* Sanfter Ausklang */
ease-in-out:    cubic-bezier(0.65, 0, 0.35, 1)  /* Rhythmus */
spring:         cubic-bezier(0.34, 1.56, 0.64, 1) /* Lebendig */
```

### Lyric Transitions
```
Enter:          opacity 0 -> 1, translateY 20px -> 0, 600ms ease-out
Hold:           Statisch während Song-Text
Exit:           opacity 1 -> 0, 400ms ease-in
```

### Particle Animation
```
Aufstieg:       translateY: 100vh -> -100px, 5-8s, linear
Rotation:       Leichtes Wackeln, 2-4s
Fade:           Opacity 0 -> 0.8 -> 0, über Lebensdauer
```

### Logo Pulse
```
Scale:          1.0 -> 1.02 -> 1.0, 3s ease-in-out infinite
Glow:           0 0 30px -> 0 0 50px -> 0 0 30px, 3s
```

## 8. Do's and Don'ts

### Do
- Verwende Inter Variable mit cv01/ss03 für moderne, geometrische Typografie
- Setze Gold (#ffd166) als Signature-Farbe für Riven-Identität
- Nutze negatives Letter-Spacing bei grossen Headlines (-1.5px+)
- Halte Hintergründe dunkel (#0a0a14 - #1a1a2e) für Dramatik
- Animiere sanft mit ease-out Kurven
- Lasse goldene Partikel langsam aufsteigen

### Don't
- Verwende keine bunten Farben ausser Gold/Orange für Akzente
- Nutze kein reines Weiss für Body-Text (#d0d6e0 ist sanfter)
- Überschreibe 3 Farben pro Phase
- Verwende keine harten Schatten
- Setze Logo nicht in die Mitte - es gehört nach unten

## 9. Video Production Guidelines

### Lyric Sync
```
Timing:         Precise sync mit Whisper-Timestamps
Emphasis:       Worte in Grossbuchstaben bei climactic Momenten
Spacing:        Zweite Zeile erscheint 200ms nach erster
```

### Color Phasing
```
0:00-33:70      Dunkelheit - Minimal, kaum Akzente
33:70-57:98     Kampf - Violett-Töne erscheinen
57:98-66:98     Identität - Gold blitzt auf
66:98-84:98     Feuer - Orange/Feuer dominant
84:98-99:70     Triumph - Volles Gold, weisse Explosion
```

### Audio-Reactive Elements (optional)
```
Partikel:       Bewegen sich subtil mit Bass
Glow:           Pulsiert mit Beat
Lyric Scale:    Leichter "Pop" bei Betonung
```
