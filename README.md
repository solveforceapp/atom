# ATOM — Adaptive Telecom Operations Module  
A SolveForce Infrastructure System  
Published by SolveForce  
Author: Ronald Joseph Legarski, Jr.

ATOM is a modular telecom intelligence layer within the SolveForce constellation,
designed to unify connectivity, monitoring, diagnostics, and service orchestration
using precise linguistic structuring and standardized systems logic.

This repository contains the canonical implementation for the ATOM microsite
(https://atom.solveforce.com), its documentation, architecture, and service catalogs.

---

## 1. Purpose

ATOM exists as the telecom intelligence nucleus, providing:

- Carrier and service indexing  
- Fiber, broadband, wireless, satellite, and private line cataloging  
- Edge and IoT connectivity mapping  
- API-ready lookup endpoints (future)  
- AI-assisted diagnostics and recommendations (future)  
- Standardized language and terminology across SolveForce properties  

This repo is designed as the reference template for all future SolveForce microsites.

---

## 2. Repository layout

```text
.
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ CHANGELOG.md
├─ .gitignore
├─ .editorconfig
├─ .env.example
├─ src/
│  └─ atom/
│     ├─ __init__.py
│     └─ main.py
├─ web/
│  ├─ index.html
│  ├─ styles.css
│  └─ scripts.js
├─ content/
│  ├─ atom-overview.md
│  ├─ telecom-definitions.md
│  ├─ solveforce-network-map.md
│  └─ edge-modules/
│     └─ fiber-intelligence.md
├─ docs/
│  ├─ index.md
│  ├─ architecture.md
│  └─ decisions/
│     └─ adr-0001-project-foundation.md
├─ tests/
│  └─ test_sanity.py
└─ .github/
   ├─ workflows/
   │  └─ ci.yml
   ├─ ISSUE_TEMPLATE/
   │  ├─ bug_report.md
   │  └─ feature_request.md
   └─ PULL_REQUEST_TEMPLATE.md
```

---

## 3. Getting started

```bash
git clone https://github.com/solveforceapp/atom.git
cd atom
```

### Local static preview

```bash
python -m http.server 8080 --directory web
```

Then open: [http://localhost:8080](http://localhost:8080)

---

## 4. Development

- Edit both `index.html` and `web/index.html` when changing the landing page so the root and `/web` views stay identical (note: resource paths differ—root references `web/styles.css`, `/web` references `styles.css`).
- Edit `web/styles.css` and `web/scripts.js` for presentation and interactions on the public site.
- Edit `content/*.md` for long-form descriptions, service catalogs, and playbooks.
- Use `docs/architecture.md` and ADRs to record structural decisions.

Run tests (placeholder):

```bash
pytest
```

---

## 5. Reuse as template

To use this as a template for another SolveForce microsite:

1. Fork the repo.
2. Replace `ATOM` with the new service name.
3. Adjust content under `/web` and `/content`.
4. Update docs and links.

---

## 6. License

MIT License © 2025 Ronald Joseph Legarski, Jr. / SolveForce
