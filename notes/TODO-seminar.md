# Piano: Workshop 2 – Agentic Loop e orchestrazione multi-agente (Roma, 1 giorno)

## Context
Seminario in presenza, 1 giornata, sillabo `resources/WORKSHOP 2 – ...doc`. Formato reale: **partecipanti senza PC, proiettore, docente in piedi**. Quindi: niente lab hands-on, niente tavola rotonda strutturata; il docente spiega, mostra **demo live**, raccoglie le domande man mano (slot "parcheggio domande" a fine blocco). Si riusa la base di `agents-course` (M5, M6, M8, M9) e dei concetti di `corso-augmented-coding` (Spec Kit, Spectral, Prism/Newman, test di regressione, costi). Runtime: Ollama `gemma4:e4b` locale, nessuna API key (AGENTS.md), con fallback registrato per le demo.

## Agenda (≈ 6h effettive)
| Ora | Blocco | Fonte |
|---|---|---|
| 09:30 | 1. Catene, workflow, agenti, multi-agente; **Agentic Loop**: definizione, stato, piano, criteri di ingresso/arresto/ripetizione | nuovo M10 + M5, M8 §3 |
| 10:45 | 2. Pattern: planner-executor, router, orchestrator-worker, **evaluator-optimizer**; ruoli (orchestratore, worker, revisore, tester, documentatore) | M5 §9-10, M6 §8, M8 §4 |
| 11:45 | 3. **Jev e i System One Model** (TypeSafe AI): decisioni tipizzate con probabilità, dove stanno nell'architettura (judge/router/guardrail), alternativa offline; HITL su bassa confidenza, costi, osservabilità | nuovo M11 |
| 13:00 | Pausa | |
| 14:00 | 4. Errori, retry, checkpoint, memoria, contesto, parallelizzazione | M6 §6, M8 §5-6 |
| 15:00 | 5. **Harness**: definizione + Spec Kit, Spectral, integration test, gate | nuovo M12 + corso-augmented-coding |
| 16:00 | 6. **Demo finale**: agente che gira, si valuta, decide | vedi sotto |
| 17:00 | Chiusura, domande aperte, "cosa c'è di nuovo" (agenti auto-ottimizzanti, A2A da M9) | |

## Nuovi moduli (seguendo AGENTS.md: un chapter per modulo, h2/h3 numerati, outline, figure numerate, lock)
- **M10 Agentic Loop**: definizione (obiettivo → piano → esecuzione → verifica → stop), anatomia (stato tipizzato, budget di iterazioni, condizioni di stop, escalation), confronto catena/workflow/agente/MAS, come impostarlo in LangGraph (ciclo con conditional edge) ed ADK `LoopAgent`.
- **M11 Jev e System One Model: giudizio, valutazione, costo**. FATTI VERIFICATI (ricerca web, 2026-11-02; sono claim del vendor, da ricontrollare prima di insegnarli): Jev di TypeSafe AI (CEO Diogo Almeida, co-inventore RLHF ex-OpenAI), lanciato il 15/09/2026; modello **non generativo**: riceve testo + domande tipizzate (bool/enum/score, cardinalità fino a 255) e restituisce risposte tipizzate **con probabilità**, mai testo libero; training RLCD (Reinforcement Learning for Calibrated Decisions) su dati sintetici; latenza dichiarata 70–500 ms, costo molto inferiore agli LLM; usi: classificazione, routing, scoring, moderazione, guardrail su trace di agenti. **Closed-weight, solo API hosted** (early access su console.typesafe.ai, SDK Python/JS, endpoint OpenAI-compatibile via Requesty/OpenRouter come `typesafe/jev-*`); nessun open-weight né self-host. Contenuto del modulo: System 1 vs System 2 (Kahneman) applicato agli agenti; Jev come judge/router/guardrail dentro il loop; "one-model" (un solo modello fa tutto) vs System One dedicato accanto all'LLM generativo; bias dei giudici LLM (self-preference, verbosità); posizione nell'evaluator-optimizer; **alternativa offline** (vedi sotto); **miglior esempio di HITL** = interrupt/approve su soglia di confidenza o azione irreversibile (riusa flight-upgrade di M6 §9.3); tabella costi (token × iterazioni × giudice); osservabilità (LangSmith/OpenTelemetry-style trace, metriche per run).
- **M12 Harness**: definizione (tutto ciò che circonda il modello: goal, tool, vincoli, test, gate, memoria, osservabilità); goal via **Spec Kit** (constitution/spec/plan/tasks), contratti con **Spectral**, **integration test automatici** (Prism/Newman) come criterio di arresto del loop; il caso guida checkout/retry di `demo-augmented-coding`.
- Aggiornare `course-structure.md` (M10-M12 + Source Inventory), homepage `site/index.html`, nav prev/next di M9→M10, `snippets-agents_v1.txt` (additivo), lock `M10-M12`.
- Pagina agenda `site/workshop2.html` (opzionale, solo link ai moduli) — da confermare.

## Demo finale proposta: "l'agente che si valuta"
Caso checkout/retry: agente LangGraph (Ollama) che implementa/ripara una funzione di retry guidato da una spec Spec Kit. Loop: **genera → harness (Spectral + pytest/Newman su Prism) → judge (rubrica) → decide: ripete / escala a umano / stop**. Il proiettore mostra in parallelo: grafo, trace per iterazione, contatore costo/token, esito dei gate. Punto HITL live: l'agente si ferma e il docente approva. Dataset di fallback pre-registrato se il modello locale è lento.

## Agenti auto-ottimizzanti: cosa sono e cosa mostrare
Agenti che migliorano **sé stessi tra un run e l'altro** (non solo dentro il loop): modificano prompt, tool, memoria o codice usando un segnale di valutazione. Famiglie: (1) prompt optimization (DSPy/GEPA, TextGrad), (2) reflexion/memoria di lezioni apprese (skill che si auto-aggiornano), (3) self-evolving code (Darwin Gödel Machine, AlphaEvolve-style), (4) offline: traccia → eval → patch del prompt.
**Demo fattibile in 10 min**: mini-ottimizzatore di prompt – 8 casi di test, il judge (M11) assegna punteggio, un "meta-agente" propone 3 varianti del system prompt, si tiene la migliore, grafico punteggio vs iterazione (+ costo). Messaggio: l'auto-ottimizzazione è un loop esterno, e funziona solo se l'harness/judge è affidabile (rischio reward hacking).

## Idee "fighe" SCELTE
1. **Model routing**: modello piccolo/veloce (`gemma4:e4b`) per il lavoro, modello più grande (gemma 12b, macchina con GPU) per i casi difficili; il **router è un System One** (Jev o equivalente locale) che decide con probabilità e passa al modello grande / all'umano sotto soglia di confidenza; grafico costo/latenza/qualità vs modello singolo. Si innesta in M11 (JEV, costi) e nella demo finale.
2. **Agente reviewer (A2A)**: il judge/reviewer esposto come agente remoto indipendente (ADK `to_a2a()` + `RemoteA2aAgent`, riuso M9 e `building-llm-applications/ch13`), con Agent Card; mostra judge separato dal worker (non self-preference) e interoperabilità. Si innesta in M11 e nella demo.
(Scartate per ora: reward hacking live, trace replay, eval-driven CI, prompt injection — eventuali bonus da domande del pubblico.)

## Requisito trasversale: LLM selezionabile (worker e JEV)
- Tutte le demo e i moduli devono funzionare con **provider a scelta** via variabile d'ambiente (es. `LLM_PROVIDER=ollama|gemini|deepseek`, `LLM_MODEL`, `JEV_PROVIDER`, `JEV_MODEL`), come negli altri agenti del corso: LangChain/LangGraph con `init_chat_model`/wrapper, ADK con `LiteLlm` (riuso `building-llm-applications/ch12/adk` e `feat/deepseek-4-support`).
- **Worker e System One (judge) configurabili in modo indipendente** (`JUDGE_BACKEND=jev|llm-local|llm-online`), così si mostra sia one-model (stesso modello) sia modello dedicato.
- **Interfaccia unica del giudice**: input = testo + schema di domande tipizzate; output = risposte tipizzate + probabilità. Tre backend dietro la stessa interfaccia: (1) **Jev online** (API TypeSafe o OpenRouter/Requesty, richiede chiave/waitlist: da verificare se disponibile per il seminario), (2) **offline in Ollama**: gemma 12b su GPU (o `gemma4:e4b`) con structured output vincolato da JSON schema e probabilità ricavate da logprobs/campionamento ripetuto — è il "pattern Jev in locale", NON Jev stesso, da dichiarare esplicitamente in aula; (3) LLM online generico (Gemini/DeepSeek) come giudice. Stesse domande e stessa rubrica → tabella confronto accuratezza/calibrazione/latenza/costo per i tre backend in M11.
- Se Jev non è accessibile in aula: registrare in anticipo le chiamate (fixture) e riprodurle; la parte live resta sul backend locale.
- Model routing e reviewer A2A usano la stessa configurazione; fallback automatico verso Ollama se manca la API key o la rete (aula!). Nessuna chiave nel repo (`.env` ignorato, esempio `.env.example`).
- Demo registrata di fallback per ciascun provider.

## Ambiente
- Macchina con GPU: Ollama con gemma 12b (verificare tag esatto con `ollama list`/`ollama pull`) + `gemma4:e4b` per il worker. Il piano va ripreso da Claude su quella macchina (file nel repo, vedi sotto).

## Ordine di lavoro (modulo per modulo, come da AGENTS.md)
1. `python3 scripts/non_regression_guard.py check` (baseline pulita; nota: `chapter-09.html` e lock M9 risultano modificati nel working tree).
2. M10 → review → lock → check. 3. M11 → idem. 4. M12 → idem. 5. Demo (script + registrazione di fallback) in un repo/cartella dedicata, snippets. 6. Deploy solo su richiesta.

## Verifica
- `check` del guard dopo ogni modulo; navigazione prev/next, outline, figure cliccabili.
- Demo eseguita end-to-end con `gemma4:e4b` locale, due volte, più fallback registrato; tempi cronometrati (≤ 15 min).
- Prova a secco dell'agenda con timing.

## Punti aperti (da confermare dopo approvazione)
- Hai accesso a Jev (early access/waitlist, chiave TypeSafe o OpenRouter)? Determina se la demo online è live o da fixture.
- Nota: nelle versioni precedenti di questo piano "JEV" era stato interpretato erroneamente come "Judge/Evaluator": corretto qui.
- Conferma M10-M12 nel sito corrente vs sito separato.
- Lingua delle slide (corso EN con switch IT; seminario in italiano).
- Quali 2-3 delle idee extra includere.

## Strategia sviluppo LLM (decisa)
- Sviluppo con **DeepSeek** (API) tramite **LiteLLM** (nome corretto: *LiteLLM*, non "lightllm"): una sola interfaccia, si cambia solo la stringa modello (`deepseek/...`, `gemini/...`, `ollama_chat/gemma...`). In ADK: `LiteLlm`; in LangChain/LangGraph: `init_chat_model` o `ChatLiteLLM`.
- Poi verifica su **Ollama** (macchina con GPU, gemma grande): stessa suite, cambiando solo `LLM_PROVIDER`/`LLM_MODEL`.
- Attenzione: tool calling e structured output (JSON schema) variano per modello; il giudice locale va ricalibrato, i punteggi DeepSeek non sono trasferibili 1:1.

## Nota da fonte TypeSafe (testo di lancio "Meet Jev")
- Auto-definizione: classe di modelli per uso **programmatico (dentro il codice)**: "smart if-statements". Spunto per slide M11: l'LLM generativo produce testo, il System One sostituisce i punti di decisione (if/route/gate) nel loop.
- RLCD (Reinforcement Learning for Calibrated Decisions) presentato come risposta a mode dropping, hallucinations e scarsa affidabilità attribuiti a RLHF. Sono claim del vendor ("may sound too good to be true"): in aula presentarli come tali e confrontarli con la nostra tabella di calibrazione.

## Alternative open/locali a Jev (ricerca web 2026-11-02, NON ancora provate; benchmark autodichiarati)
- **OpenDecider-small** (https://huggingface.co/blog/manjunathshiva/opendecider-beats-laya-and-jev): Qwen3-4B-Instruct + LoRA, build GGUF (Q8_0, Q4_K_M) per Ollama/LM Studio. Candidata principale per il backend offline. Dichiara di battere Jev (numeri suoi, post di ~30 giorni).
- **Ollaya** (https://medium.com/data-science-in-your-pocket/ollaya-run-jev-ai-locally-bb2102f10bba, modelli: https://huggingface.co/ollaya-dev/decider): runtime open source con API compatibile TypeSafe; permetterebbe di cambiare backend senza toccare il codice. Progetto giovane, non affiliato a Ollama/TypeSafe.
- **local-decision-model** (https://huggingface.co/Pdbz199/local-decision-model): encoder ~150M, risposta in un passaggio, pacchetto proprio (non Ollama). Gli autori sconsigliano l'uso come unico controllo di sicurezza.
- Elenco: https://github.com/AnotiaWang/awesome-decision-models
- TODO: sull'altra macchina scaricare OpenDecider-small, provarlo su Ollama e confrontarlo con gemma 12b e Jev sulle stesse domande tipizzate (accuratezza, calibrazione, latenza, costo).

## Confronto System One vs XGBoost (da usare in M11)
- Punti in comune: input -> classe + probabilità, millisecondi, nessuna generazione di testo.
- Input: XGBoost = feature tabellari progettate a mano; decision model = testo libero/JSON grezzo.
- Addestramento: XGBoost = dataset etichettato per compito, riaddestro se cambia; decision model = già addestrato, zero/few-shot, domande nuove a runtime (differenza principale).
- Domande: XGBoost = fissa nel modello; decision model = domanda e schema risposte sono parametri della chiamata.
- Calibrazione: XGBoost richiede calibrazione a parte (Platt/isotonic); Jev dichiara di ottimizzarla in training (claim del vendor, da verificare).
- XGBoost resta migliore per problemi stabili con dati etichettati: costo minimo, spiegabile (SHAP), nessuna prompt injection.
- Prova diretta proposta: stesso compito di routing con (a) XGBoost su TF-IDF, (b) decision model locale, (c) Jev; confrontare accuratezza, calibrazione (reliability diagram/ECE) e costo di preparazione.
