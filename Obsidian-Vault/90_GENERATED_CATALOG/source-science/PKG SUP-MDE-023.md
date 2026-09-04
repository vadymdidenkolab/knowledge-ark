---
id: "SUP-MDE-023"
kind: "source-science"
title: "Native C/C++ build and debug chain"
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

# Native C/C++ build and debug chain

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SUP-MDE-023`
- **Статус:** `NOT_DOWNLOADED`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: practical-science-package-register.csv -->
- **package_id:** SUP-MDE-023
- **domain_group_codes:** COMP|ARCH
- **title:** Native C/C++ build and debug chain
- **publisher:** gcc.gnu.org
- **content_scope:** Практический источник для групп COMP|ARCH
- **canonical_url:** https://gcc.gnu.org/|https://sourceware.org/binutils/|https://sourceware.org/gdb/|https://www.gnu.org/software/make/|https://cmake.org/|https://github.com/ninja-build/ninja
- **acquisition_url:** https://gcc.gnu.org/|https://sourceware.org/binutils/|https://sourceware.org/gdb/|https://www.gnu.org/software/make/|https://cmake.org/|https://github.com/ninja-build/ninja
- **rights_url:** https://gcc.gnu.org/|https://sourceware.org/binutils/|https://sourceware.org/gdb/|https://www.gnu.org/software/make/|https://cmake.org/|https://github.com/ninja-build/ninja
- **license_or_terms:** Mixed: GCC GPL-3+ with GCC Runtime Library Exception for specified runtime components; binutils/GDB/make GPL-family; CMake BSD-3-Clause; Ninja Apache-2.0; manuals may be GFDL
- **language:** docs mostly EN
- **jurisdiction:** International/reference
- **format:** GCC;binutils;GDB;GNU make;CMake;Ninja sources/binaries/docs;sysroot/headers/libraries
- **offline_method:** Define each component/version as its own manifest record; preserve source, bootstrap binaries, sysroot, libc/headers, build generators and tests for at least two viable architectures
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
- **notes:** [SUPPLEMENTAL_RESEARCH] Compiler bootstrap; runtime exception scope; libc/sysroot rights; target triple; binutils compatibility; no family-level blanket license

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
