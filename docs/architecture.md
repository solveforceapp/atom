# ATOM Architecture Overview

ATOM is implemented as:

- A static web presence under `web/` for atom.solveforce.com.
- A content library under `content/` for telecom terms and structures.
- A light Python package stub under `src/atom` for future automation.
- CI workflows in `.github/` for validation and consistency.

The long-term intent is to support:

- Automated generation of availability maps.
- Integration with SolveForce internal tools and APIs.
- Alignment with other modules (AMR, DCM, language frameworks).
