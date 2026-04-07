# AI AGENT SYSTEM - LOKALE TRANSFORMATION

## Ziel: 100% Lokales System

### Phase 1 - AKTUELL ✅
```
Cloud:           Claude (API)
Lokal:           Ollama llama3.1
Obsidian:        Vault
Kosten:          ~0 Euro (nur Claude Cloud)
```

### Phase 2 - ZIEL 🎯
```
Cloud:            NICHTS
Lokal:           Ollama (Claude-kompatibles Modell)
Obsidian:        Vault
Kosten:          0 Euro (alles lokal)
```

## Optionen fuer lokales "Claude"

### Option A: Llama 3.1 (bereits vorhanden)
- Modell: llama3.1
- Vorteil: Bereits installiert
- Nachteil: Nicht genau wie Claude

### Option B: Andere Modelle testen
```bash
ollama list
ollama pull llama3.3
ollama pull mixtral
ollama pull codellama
```

### Option C: Selbsthosted Claude-Alternative
- https://ollama.com/library (suchen nach "claude")
- https://github.com (Self-hosted LLMs)

## Naechste Schritte

1. [ ] Teste andere Ollama-Modelle
2. [ ] Pruefe ob CodeLlama fuer Programming geeignet
3. [ ] Vergleiche Leistung llama3.1 vs andere
4. [ ] Entscheide: Welches Modell als "lokaler Claude"?

## Aktuelles Setup

```
Ollama Modelle (bereits installiert):
- llama3.1
- deepseek-coder
- gemma4:e2b
- llava (Vision)
```

---

*Erstellt: 07.04.2026*
*Ziel: 100% offline-faehiges AI-System*
