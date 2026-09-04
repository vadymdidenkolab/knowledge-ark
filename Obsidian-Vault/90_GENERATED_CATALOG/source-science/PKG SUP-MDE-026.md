---
id: "SUP-MDE-026"
kind: "source-science"
title: "Go toolchain and vendored modules"
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

# Go toolchain and vendored modules

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SUP-MDE-026`
- **Статус:** `NOT_DOWNLOADED`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: practical-science-package-register.csv -->
- **package_id:** SUP-MDE-026
- **domain_group_codes:** COMP|ARCH
- **title:** Go toolchain and vendored modules
- **publisher:** go.dev
- **content_scope:** Практический источник для групп COMP|ARCH
- **canonical_url:** https://go.dev/
- **acquisition_url:** https://go.dev/
- **rights_url:** https://go.dev/
- **license_or_terms:** Go distribution uses BSD-style license; module dependencies and generated/vendor content have independent rights
- **language:** docs primarily EN
- **jurisdiction:** International/reference
- **format:** Source archive;official binaries;docs;go.mod;go.sum;vendor tree;modules.txt
- **offline_method:** Preserve source plus binaries for host targets; pin toolchain; go mod vendor and retain go.mod/go.sum/vendor/modules.txt; build with vendor and network denied
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
- **notes:** [SUPPLEMENTAL_RESEARCH] Bootstrap Go version; module replacements; cgo/native libs; module licenses; sum database is not offline availability proof

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
