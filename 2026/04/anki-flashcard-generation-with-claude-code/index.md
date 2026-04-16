---
title: "anki: flashcard generation with claude code"
url: https://perrotta.dev/2026/04/anki-flashcard-generation-with-claude-code/
last_updated: 2026-04-16
---


[Previously]({{< ref "2026-04-13-anki-api-access" >}}).

I started to use [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
to generate flashcards for my (new) **Tech** Deck via
[AnkiConnect](https://ankiweb.net/shared/info/2055492159), covering books and
topics I'm studying for to consolidate my SWE-SRE knowledge.

The workflow: I tell Claude which book or topic to cover, it researches their
key concepts, checks my existing cards (notes) for potential overlap, and
batch-adds new ones via the AnkiConnect HTTP API:

```python
def anki_request(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    req = urllib.request.Request("http://localhost:8765", data=payload.encode(), method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["result"]

notes = [
    {
        "deckName": "Tech 💻",
        "modelName": "Basic",
        "fields": {
            "Front": "DDIA: <b>LSM-Trees vs B-Trees</b> — how do they differ?",
            "Back": "..."  # HTML-formatted answer
        },
        "tags": ["ddia"],
    },
    # ... more notes
]

anki_request("addNotes", notes=notes)
```

In a sample session, topics covered:

| Topic | Cards | Tag |
| ------- | ------: | ----- |
| SRE (Google) | 50 | `sre` |
| System Design | 40 | `system-design` |
| LeetCode / Python | 41 | `python` |
| Kubernetes | 20 | `kubernetes` |
| Production-Ready Microservices (Susan Fowler) | 28 | `microservices` |
| DDIA (Martin Kleppmann) | 25 | `ddia` |
| Building Microservices (Newman) | 16 | `microservices` |
| Fundamentals of Software Architecture (Richards & Ford) | 25 | `software-architecture` |
| Kubernetes advanced | 25 | `kubernetes` |
| Networking | 17 | `networking` |
| Linux / Systems Performance | 16 | `linux` |
| Python stdlib | 23 | `python` |
| **Total** | **~326** | |

For each book, Claude searched the web for chapter summaries and key concepts,
cross-referenced my existing cards to avoid duplication, then created a Python
script to push cards through AnkiConnect's `addNotes` action.

Cards match the existing format: Basic note type, HTML formatting (`<b>`,
`<br>`, `<code>`, `•`), one tag per topic.

Example card (front):

> **DDIA: Sloppy quorums and hinted handoff — what are they?**

Example card (back):

> In a standard quorum (w + r > n), writes/reads must reach specific replicas.
> **Problem**: during a network partition, the designated replicas may be
> unreachable. Strict quorum would reject the write → reduced availability.
> **Sloppy quorum**: Accept writes on any reachable nodes, even if they aren't
> the designated replicas (...)

The whole process took about an hour. Doing it by hand would have taken days.

I am excited to evolve this workflow. The next step is going to be to refactor
my thousands of language cards and notes.

