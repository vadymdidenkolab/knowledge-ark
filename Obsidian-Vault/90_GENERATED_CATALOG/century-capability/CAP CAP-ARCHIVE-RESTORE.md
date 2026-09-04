---
id: "CAP-ARCHIVE-RESTORE"
kind: "century-capability"
title: "восстановление критического корпуса без сети"
priority_tier: "P4_BLUE"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "UNASSIGNED"
safety_class: "UNASSIGNED"
execution_gate: "DENY_UNTIL_REVIEWED"
status: "PLANNED"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# восстановление критического корпуса без сети

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-ARCHIVE-RESTORE`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-ARCHIVE-RESTORE
- **domain_code:** INFO
- **subject_level:** INSTITUTION
- **service_outcome:** восстановление критического корпуса без сети
- **beneficiary_scope:** DESIGNATED_COMMUNITY
- **service_unit:** RESTORE_SUCCESS_AND_RTO
- **demand_formula:** L0_L1_COMPLETE_PLUS_SAMPLED_DEEP
- **minimum_service_level:** fixity readers copies blank-device successor test
- **dependency_capability_ids:** [[CAP CAP-ENERGY-CRITICAL|CAP-ENERGY-CRITICAL]], [[CAP CAP-SOFTWARE-READ|CAP-SOFTWARE-READ]]
- **external_dependency_class:** MEDIA_SOFTWARE_SUPPLIERS
- **maximum_safe_outage:** ANNUAL_FOR_CRITICAL
- **regeneration_or_replacement_method:** replicate verify migrate and print core
- **owner_role_id:** TBD
- **successor_role_id:** TBD
- **evidence_required:** SEE_16_AND_18
- **evidence_state:** MISSING
- **lifecycle_state:** PLANNED
- **review_due:** не заполнено
- **gate_decision:** DENY
- **notes:** Архитектурная строка; не доказанная способность

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
