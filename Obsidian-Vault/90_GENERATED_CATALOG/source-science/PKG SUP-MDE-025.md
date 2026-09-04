---
id: "SUP-MDE-025"
kind: "source-science"
title: "Rust standalone toolchain and vendored crates"
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

# Rust standalone toolchain and vendored crates

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SUP-MDE-025`
- **Статус:** `NOT_DOWNLOADED`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: practical-science-package-register.csv -->
- **package_id:** SUP-MDE-025
- **domain_group_codes:** COMP|ARCH
- **title:** Rust standalone toolchain and vendored crates
- **publisher:** www.rust-lang.org
- **content_scope:** Практический источник для групп COMP|ARCH
- **canonical_url:** https://www.rust-lang.org/
- **acquisition_url:** https://www.rust-lang.org/
- **rights_url:** https://www.rust-lang.org/
- **license_or_terms:** Rust project code generally MIT OR Apache-2.0; crates, LLVM and bundled tools have independent licenses
- **language:** docs primarily EN
- **jurisdiction:** International/reference
- **format:** Standalone installers;source;rustc/cargo/rustdoc/std/docs;Cargo.lock;vendor directory;crates
- **offline_method:** Preserve official standalone installers and source for exact host/targets; cargo vendor with Cargo.lock; build using locked/offline or frozen mode; retain target std components
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
- **notes:** [SUPPLEMENTAL_RESEARCH] Target triples; rustup channel mutability avoided; crate licenses/SBOM; build scripts; native dependencies; offline tests

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
