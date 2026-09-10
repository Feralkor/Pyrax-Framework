# Framework Runtime Surface

This directory is reserved for reusable runtime components that are truly domain-agnostic.

Candidate future modules:
- truth;
- quality;
- reconciliation;
- evidence;
- state;
- anticipation;
- decision;
- memory;
- observability;
- integrations.

Do not move product-specific business rules here merely to increase reuse. A component belongs in the framework only when at least two domains can use it without importing domain semantics.
