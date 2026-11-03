# Workshop 2 – scaletta, sfoltimento e script della demo

Contesto: una giornata a Roma, in piedi, con proiettore, senza PC per i partecipanti; mattina di contenuti, domande raccolte live. I capitoli M10–M12 sono completi per il corso online: per il seminario si **dice** una parte e si **lascia sul sito** il resto. I capitoli non vengono modificati (sono bloccati): lo sfoltimento è solo una scelta di cosa presentare.

Dimensioni (parole): M10 2.801 · M11 3.366 · M12 2.237 (contro M5 5.350, M6 4.476, M8 1.997, M9 2.415).

## 1. Cosa dire e cosa saltare

Legenda: **D** = da dire, **S** = se c'è tempo, **X** = non presentare (resta nel sito).

### M10 – Agentic loop (≈ 50 min con la demo breve)
| § | Sezione | |
|---|---|---|
| 3.1 | Quattro livelli di controllo (catena → workflow → agente → multi-agente) | **D** |
| 3.2 | Definizione del loop + **Figure M10.1** | **D** (è la slide centrale) |
| 3.3 | Quando il loop è sbagliato | **D** (2 minuti) |
| 4.1 | Stato | **D** |
| 4.2 | Criteri di ingresso | S |
| 4.3 | Criteri di arresto (tabella) | **D** |
| 4.4 | Feedback e ripetizione | **D** |
| 5.1–5.4 | Planner-executor, router, orchestrator-worker, evaluator-optimizer | **D** una slide con i quattro; 5.4 un po' più a lungo |
| 5.5 | Ruoli specializzati | S (tabella da leggere in 1 minuto) |
| 6.1–6.3 | LangGraph: stato, archi condizionali, checkpoint/interrupt | **D** (mostra solo il codice di `after_harness` e `interrupt`) |
| 6.4 | ADK LoopAgent | X (basta nominarlo) |
| 7.1 | Errori e retry (tecnico vs semantico) | **D** |
| 7.2–7.3 | Parallelizzazione, memoria e contesto | S |
| 8 | Esempio guidato | sostituito dalla **demo** |
| 9 | Laboratorio | X (non ci sono PC) |

### M11 – Modelli decisionali, giudici, costi (≈ 70 min)
| § | Sezione | |
|---|---|---|
| 3.1–3.2 | Generazione vs decisione; domande tipizzate | **D** |
| 3.3 | Implementazioni (Jev, aperti, LLM come giudice) | **D** (dichiara: claim del vendor, Jev è solo API) |
| 4.1 | Quattro posizioni del giudice | **D** |
| 4.2 | Un modello o un giudice separato | **D** |
| 4.3–4.4 | Come scrivere le domande, contratto indipendente dal backend | S (mostra il codice di `decide`) |
| 5.1 | Metriche (accuratezza, ECE, Brier, accuratezza se confidente) | **D** con ECE spiegato con l'esempio a due gruppi |
| 5.2 | Il caso dei ticket (tre domande, 120 ticket, 20 difficili) | **D** (2 minuti, mostra due esempi) |
| 5.3 | Disegno del benchmark | S |
| 5.4 | Risultati sul full set | **D** (una tabella: solo `team`) |
| 5.5 | gemma-12b su 49 ticket | **D** (è il punto "locale sicuro e sbagliato") |
| 5.6 | Lettura dei risultati | **D** |
| 6 | Modello decisionale vs XGBoost | **D** (la domanda arriverà comunque) |
| 7.1 | Decisioni a tre vie | **D** |
| 7.2 | Cascate + **Figure M11.1** | **D** |
| 7.3 | Intervento umano che funziona | **D** (il "miglior esempio di HITL") |
| 7.4 | Escalation del modello worker | S |
| 8.1 | Modello di costo | **D** |
| 8.2–8.4 | Cosa tracciare, metriche, operare un giudice | S (una slide riassuntiva) |
| 9 | Laboratorio | X |

### M12 – Harness (≈ 50 min)
| § | Sezione | |
|---|---|---|
| 3.1–3.3 | Definizione, componenti, "harness prima del prompt" | **D** |
| 4.1 | Spec-driven development (Spec Kit) | **D** |
| 4.2–4.4 | Scenari di accettazione, esclusioni, tracciabilità | **D** 4.2 e 4.3; S 4.4 |
| 5.1–5.3 | Spectral, Prism/Newman, limiti dei mock | **D** 5.1 e 5.3; S 5.2 |
| 6.1 | Test che l'agente non può modificare | **D** |
| 6.2–6.3 | Regole statiche, livelli di test | **D** 6.4 prima, 6.3 solo come tabella |
| 6.4 | Reward hacking | **D** (è memorabile) |
| 7.1–7.4 | Costo dei controlli, formato del feedback, pipeline, permessi | S, tranne 7.4 (**D** in 1 minuto) |
| 8 | Esempio guidato | sostituito dalla **demo** |
| 9 | Laboratorio | X |

### Dal resto del corso (riuso)
- **M8** §3.1 (tool-use loop), §4.3 (enforcement, escalation), §5.2 (errori strutturati).
- **M6** §8.2–8.3 (generate-and-review, HITL), §9.3 (flight-upgrade come esempio di HITL).
- **M5** §6.4 (ReAct) solo se serve un ripasso.
- **M9** §3 (A2A) e §6 (deployment) come ultimo blocco "cosa c'è di nuovo".

## 2. Agenda proposta (≈ 6 h effettive)
| Ora | Blocco |
|---|---|
| 09:30 | M10: loop, stato, arresto, pattern (≈ 50 min) + domande |
| 10:35 | **Demo 1, replay (storia completa, 8 min)** |
| 10:50 | Pausa |
| 11:05 | M11: giudici, calibrazione, cascate, HITL, costi (≈ 70 min) + domande |
| 12:30 | Pranzo |
| 14:00 | M12: harness (≈ 50 min) |
| 15:00 | **Demo 2, live con modelli veri (10 min)** + domande sulla demo |
| 15:30 | Pausa |
| 15:45 | Dal corso: HITL (M6), A2A (M9), agenti auto-ottimizzanti (da idee in `TODO-seminar.md`) |
| 16:45 | Domande aperte, chiusura |

## 3. Messaggi chiave (da ripetere)
1. Il loop si ferma per **evidenza**, non per opinione del modello: harness prima, giudice poi, persona per ultima.
2. Ogni loop ha più modi di finire e un **budget**.
3. Il giudice risponde con **probabilità**; le **soglie stanno nel codice**.
4. Un giudice sicuro e sbagliato è peggio di uno incerto: misura la **calibrazione**.
5. Cheap first: cascata di giudici, persona come ultimo livello.
6. L'agente non deve poter modificare i propri controlli (**reward hacking**).
7. Un harness è software: va testato (fallisce il cattivo, passa il buono, respinge il fuori-scope).

## 4. Numeri da ricordare (dal benchmark, dati sintetici, 120 ticket)
- Jev: team 0,91 (ECE 0,032), 187 ms, USD 0,002 per 120 ticket. DeepSeek: 0,87, 2.057 ms, USD 0,020. XGBoost: 0,86.
- Jev sotto-sicuro su `urgent` (conf 0,86, acc 0,99).
- gemma-12b su 49 ticket: team acc 0,77, ECE 0,233, mai incerto; ~16 s/ticket; 2 ticket senza risposta su `refund` con negazione.
- Cascata Jev → DeepSeek → persona, soglia 0,7: 96,9% risolto in automatico, acc 0,983, USD 0,06 per 1.000 ticket.
- Avvertenze da dire: dataset sintetico e piccolo; claim di Jev sono del vendor; OpenDecider **non provato**; il worker con escalation è verificato solo dai test.

## 5. Script della demo (`building-llm-applications/ch14/demo_live.py`)
**Demo 1 – replay (nessuna rete, deterministica):**
```bash
cd ch14 && .venv/bin/python demo_live.py --mode replay --delay 0.6
```
Cosa dire a ogni passo, in ordine:
1. 🎬 Obiettivo: tre requisiti e le esclusioni. 2. 🧪 Situazione iniziale: lo starter fallisce 2 test su 3. 3. ⚙️ Configurazione: worker, giudice, soglie, budget.
4. Iter 1 ❌: un test fallisce → feedback sintetico torna al generatore, il giudice **non** viene chiamato (costa).
5. Iter 2 ⛔: i test passano ma c'è un `sleep`: regola statica fuori-scope → harness fallisce anche se i test sono verdi.
6. Iter 3 ⚖️: test verdi, il giudice dice che c'è codice in più (scope_creep 0,84) → REVISE.
7. Iter 4: giudice incerto (0,74 / 0,45) → 🙋 persona: approva.
8. 🏁 Tabella finale: 4 iterazioni, costo, tempo, diff.

**Demo 2 – live (DeepSeek + Jev, o locale):**
```bash
LLM_PROVIDER=deepseek JUDGE_BACKEND=jev JEV_MODEL=jev-1.14.0 .venv/bin/python demo_live.py --mode live --inject off-by-one,backoff
JUDGE_BACKEND=cascade CASCADE_THRESHOLD=0.7 LLM_PROVIDER=deepseek .venv/bin/python demo_live.py --mode live --human ask
```
Il primo tentativo è un difetto **piantato** (etichettato 🎭 nel log): dichiaralo. Un modello forte non sbaglia da solo.

**Piano B:** se la rete cade, `--mode replay`. Se Jev non risponde, `JUDGE_BACKEND=llm` o `cascade` con `JUDGE_FALLBACK=llm`. Registra un log in anticipo con `--log file.log`.

## 6. Domande probabili (risposte brevi)
- *Perché non usare sempre un LLM come giudice?* Costo, latenza (2 s vs 0,19 s) e probabilità non calibrate; vedi gemma.
- *Jev vs XGBoost?* XGBoost se il problema è stabile e hai etichette; Jev se le domande cambiano o l'input è testo libero.
- *Posso far girare Jev in locale?* No: solo API. In locale c'è l'alternativa generica con JSON schema; modelli decisionali aperti esistono ma non li ho misurati.
- *Come scelgo la soglia?* Dalla curva su dati tuoi: quota di umano accettabile contro accuratezza (`routing_replay.py`).
- *Cosa impedisce all'agente di barare sui test?* Test in sola lettura, copiati in cartella pulita a ogni run; regole statiche; giudice indipendente.
- *Costo di un run?* Iterazioni × (generatore + giudice) + escalation + tempo umano; il budget di iterazioni è anche un tetto di costo.

## 7. Da fare prima del giorno
- [ ] Provare `demo_live.py` su projector (dimensione font, `--delay`), anche con `--no-color`.
- [ ] Rieseguire il live una volta la sera prima e salvare un log di riserva.
- [ ] Gemma 12b: completare i 71 ticket (opzionale) e OpenDecider (opzionale), poi aggiornare le note del benchmark.
- [ ] Decidere se tagliare davvero qualcosa nei capitoli o solo non presentarlo.
