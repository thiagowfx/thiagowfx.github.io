---
title: "Anki: API access"
url: https://perrotta.dev/2026/04/anki-api-access/
last_updated: 2026-04-13
---


Install [AnkiConnect](https://ankiweb.net/shared/info/2055492159):

> AnkiConnect enables external applications such as Yomichan to communicate with
> Anki over a simple HTTP API. Its capabilities include executing queries
> against the user's card deck, automatically creating new cards, and more.
> AnkiConnect is compatible with the latest stable (2.1.x) releases of Anki;
> older versions (2.0.x and below) are no longer supported.

...to be able to do incantations such as:

```shell
% curl -s localhost:8765 -X POST -d '{"action": "deckNames", "version": 6}' | python3 -m json.tool
```

```json
{
    "result": [
        "Default",
        "Languages",
        "Languages::English \ud83c\uddec\ud83c\udde7",
        "Languages::German \ud83c\udde9\ud83c\uddea",
        "Languages::Italian \ud83c\uddee\ud83c\uddf9",
        "Languages::Portuguese \ud83c\udde7\ud83c\uddf7",
        "Tech \ud83d\udcbb"
    ],
    "error": null
}
```

```shell
% curl -s localhost:8765 -X POST -d '{"action": "modelNames", "version": 6}' | python3 -m json.tool
```

```json
{
    "result": [
        "Basic",
        "Basic (and reversed card)",
        "Cloze",
        "Deutsch Grammatik Cloze \ud83c\udde9\ud83c\uddea",
        "Deutsch Language Card \ud83c\udde9\ud83c\uddea",
        "Image Occlusion",
        "Italian Grammatik Cloze \ud83c\uddee\ud83c\uddf9",
        "Italian Language Card \ud83c\uddee\ud83c\uddf9"
    ],
    "error": null
}
```

Why is this useful?

It allows me to connect my LLM to Anki via HTTP[^1].

**Prompt**: create flashcards based on the _Site Reliability Engineer_ book by
Google, published by O'Reilly, in the _Tech_ deck.

> ⏺ I'll use the Basic note type (Front/Back). The Google SRE book is
> substantial — it covers topics like SLOs, error budgets, monitoring, incident
> response, automation, release engineering, etc.
>
> How many flashcards would you like roughly? And should I cover the whole book
> broadly or focus on specific chapters/topics?

The traditional option is to import an existing [shared
deck](https://ankiweb.net/shared/decks), like [this one](https://ankiweb.net/shared/info/1014055110).

> ⏺ Done! I've created 50 flashcards in the Tech 💻 deck, all tagged with sre
> and google-sre-book. They cover the most relevant topics:
>
> - Core concepts: SRE definition, SLI/SLO/SLA, error budgets, toil, 50% rule
> - Monitoring: four golden signals, black-box vs white-box, symptom-based
>   alerting
> - Incident management: roles, mitigation vs root cause, postmortems, blameless
>   culture
> - Reliability patterns: graceful degradation, load shedding, circuit breaking,
>   retry budgets, exponential backoff
> - Cascading failures: causes, defenses, deadline propagation
> - Operations: on-call best practices, change management, canarying, capacity
>   planning
> - Distributed systems: CAP theorem, consensus, Paxos/Raft
> - Culture: simplicity, automation hierarchy, PRR, Wheel of Misfortune

Wait until I start to refactor my language notes[^2].

[^1]: Alternatively you can use [MCP](https://ankiweb.net/shared/info/124672614) if you _really_
    [want]({{< ref "2025-10-17-mcp-model-context-protocol-considered-harmful" >}}) to.

[^2]: [Anki concepts](https://docs.ankiweb.net/getting-started.html?highlight=notes#key-concepts): a note is typically a pair of cards (back and front, front and back).

