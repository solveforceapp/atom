# ADR-0001: ATOM Project Foundation

Date: 2025-11-12  
Status: Accepted

## Context

SolveForce requires a coherent, reusable template and conceptual architecture
for the ATOM microsite and related tooling.

## Decision

- Use a static web structure under `web/`.
- Maintain domain definitions and catalogs under `content/`.
- Keep a minimal Python package at `src/atom` for future automation.
- Use GitHub Actions for basic CI.

## Consequences

- New contributors can quickly understand where to put changes.
- ATOM can be cloned as a base for other microsites.
