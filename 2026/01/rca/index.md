
RCA = Root-Cause Analysis = Postmortem

- 5 Whys. Why?? Why?? [Tell me
  why!!!!](https://www.youtube.com/watch?v=yki_bWIMvIU).
- CAPAs => corrective actions, preventive actions
- Corrective: fix the issue right away. Stop the bleeding.
- Preventive: how to stop it from reoccurring?
- Is there a monitoring gap? Did we find out about the issue by ourselves or via
  the customer?
- If there was an alert, was it lost in the noise? Did it have the right
  priority? Did it have proper routing, to the relevant (oncall) teams?
- Do we have an incident management process (IRM / Requiem)?
- Who is the incident commander?
- Do we have a status page that our customers can follow? Example:
  http://status.github.com/. Uptime dashboard (UptimeKuma). Atlassian
  StatusPage.
- What is our burn rate?
- What are our SLAs (agreement, contract)? SLOs (objective)? SLIs (indicator)?
- Prometheus. PromQL. Time-series database (TRDB), time-series tracking.
  Cardinality of metrics.
- Cause: trigger of an immediate event vs contributing factor that made it
  worse.
- Blameless postmortem culture. Psychological safety!
- Grafana. Dashboard. Render.
- AlertManager. Alert routing. Silencing. Snoozing.
- Maintenance mode. Maintenance windows.
- Logs collection. Loki. Analog.
- Logging (`/var/log/`) — logging framework, or even good ol' `print(f)` /
  `echo`. stdout vs stderr. Log levels. Debugging logs vs error (panic) logs.
  Exceptions, stack traces. ThirdEye / Sentry. Error, warning, info. Logs
  collection and aggregation.
- Analytics (more product-based e.g. PM, UX are interested in them) — page views
  / hits, number of daily/weekly/monthly active users.
- Metrics. Buckets. Histograms. Counters. Gauges. Number of responses with a
  given HTTP status code. Latency in ms. Rates e.g. success / total.
- Alerts. Conditions observed during a certain time window. Surpassed a certain
  threshold. Flapping.
- (Distributed) Tracing. Life of a request. Honeycomb. Microservices.0
- Bisection (e.g. `git bisect`).
- When a bug is found, write a test to prevent it from reoccurring.
- Profiling. Function latency breakdown.
- Metrics correlation.
- Incident lifecycle: detection (alert? customer?) -> triage (P0?) -> mitigation
  (CA) -> resolution (PA) -> postmortem / RCA.
- RCAs are only useful if action items are addressed. Prioritization is
  important.
- Action items need to be...actionable! Story-sized, not epic-sized.
- Playbooks (runbooks). Manual! How to address an alert. What to do? What to
  look out for?
- Failures: technical (code, infra); observability (gaps, tooling); process
  (SOP).
- Golden metrics: latency (overloaded, preempting), traffic (e.g. spikes),
  errors (kubectl logs? / loki), saturation (e.g. disk, memory — OOM, cpu –
  thrasing)

