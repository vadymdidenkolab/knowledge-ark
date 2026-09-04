---
id: "SUP-MDE-039"
kind: "source-science"
title: "Nix plus signed local binary/source cache"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY_UNTIL_REVIEWED"
status: "NOT_DOWNLOADED"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Nix plus signed local binary/source cache

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SUP-MDE-039`
- **Статус:** `NOT_DOWNLOADED`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: practical-science-package-register.csv -->
- **package_id:** SUP-MDE-039
- **domain_group_codes:** COMP|ARCH
- **title:** Nix plus signed local binary/source cache
- **publisher:** nixos.org
- **content_scope:** Практический источник для групп COMP|ARCH
- **canonical_url:** https://nixos.org/
- **acquisition_url:** https://nixos.org/
- **rights_url:** https://nixos.org/
- **license_or_terms:** Current Nix COPYING applies LGPL-2.1-or-later; Nixpkgs recipes, packages and cached binaries have per-package licenses; a cache does not inherit Nix's license
- **language:** docs mostly EN
- **jurisdiction:** International/reference
- **format:** Nix source/binaries;flake.lock;derivations;store paths;NAR files;narinfo;source closures
- **offline_method:** Pin Nix and nixpkgs revisions; copy complete build and source closures into local binary cache; sign cache with documented key; rebuild/realise with substituters restricted to local cache
- **tier:** L2
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **update_class:** ANNUAL_OR_EDITION
- **criticality:** 4
- **breadth:** 4
- **actionability:** 3
- **reproducibility:** 4
- **offline_fit:** 4
- **rights_clarity:** 3
- **language_fit:** 2
- **maintainability:** 3
- **safety_penalty:** 0
- **volatility_penalty:** 2
- **storage_penalty:** 1
- **release_state:** CANDIDATE
- **acquisition_state:** NOT_DOWNLOADED
- **rights_state:** REQUIRES_ITEM_REVIEW
- **content_review_state:** NOT_REVIEWED
- **offline_open_state:** NOT_TESTED
- **sha256:** не заполнено
- **local_path:** не заполнено
- **retrieved_at:** не заполнено
- **review_due:** не заполнено
- **priority_score:** не заполнено
- **notes:** [SUPPLEMENTAL_RESEARCH] Exact source LICENSE; package licenses/unfree flags; source closure; cache-key custody; architecture; GC roots; no network proof

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
