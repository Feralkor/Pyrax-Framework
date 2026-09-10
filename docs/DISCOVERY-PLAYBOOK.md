# Pyrax Framework — Discovery Playbook

Status: CANONICAL
Version: 0.3

## Objective

Provide a repeatable discovery method for entering a new organization or problem space without assuming the solution in advance.

## Discovery tracks

### Business
Capture:
- business model;
- customers and users;
- value streams;
- revenue/cost drivers;
- critical service levels;
- constraints and risks.

### Operations
Capture:
- end-to-end process;
- queues;
- handoffs;
- bottlenecks;
- rework;
- delays;
- exceptions;
- manual decisions;
- escalation points.

### Decisions
For each candidate decision record:
- decision owner;
- trigger;
- current evidence;
- current latency;
- available actions;
- consequence of delay/error;
- frequency;
- reversibility.

Prioritize decisions that are frequent, consequential, evidence-starved and actionable.

### Data
Capture systems, files, APIs, events, telemetry and external data. Never assume a field means what its label suggests.

### Technology
Capture:
- deployment model;
- network constraints;
- authentication;
- integration mechanisms;
- supported runtimes;
- data residency;
- availability requirements;
- observability requirements.

### Governance
Capture:
- data owners;
- approvers;
- regulatory/privacy constraints;
- destructive-action restrictions;
- audit requirements;
- human-in-the-loop expectations.

## Discovery questions

1. Which decision do you wish you could make earlier?
2. Which problem is discovered only after it has already caused impact?
3. What do people manually check every day?
4. Which exceptions cause the most operational attention?
5. Which queues or handoffs accumulate aging?
6. Which KPI moves too late to be useful?
7. What action could be taken if risk were visible earlier?
8. Which system is authoritative for each fact?
9. Which important facts are only available in spreadsheets or human knowledge?
10. Which fields are ambiguous or disputed?
11. What must never be automated without approval?
12. What outcome would prove that the solution is useful?

## Output

Discovery should produce evidence-backed drafts for:
- Organization Profile;
- Product Charter;
- Source Map;
- Domain Pack;
- Signal Catalog;
- Decision Catalog;
- Evidence Contract;
- Golden Cases;
- first vertical slice.

## Stop condition

Do not start broad implementation because discovery generated many opportunities. Select one decision-support vertical with sufficient data and business value, then prove it end to end.
