---
id: "CAP-DOC-IDENTITY"
kind: "century-capability"
title: "восстановимая идентичность права и записи"
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

# восстановимая идентичность права и записи

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-DOC-IDENTITY`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-DOC-IDENTITY
- **domain_code:** DOC
- **subject_level:** CELL|INSTITUTION
- **service_outcome:** восстановимая идентичность права и записи
- **beneficiary_scope:** ALL_PERSONS_AND_ENTITY
- **service_unit:** RESTORABLE_RECORD_SET
- **demand_formula:** ONE_CURRENT_SET_PER_SUBJECT
- **minimum_service_level:** verified copy plus lawful recovery route
- **dependency_capability_ids:** [[CAP CAP-ARCHIVE-RESTORE|CAP-ARCHIVE-RESTORE]], [[CAP CAP-LAW-TENURE|CAP-LAW-TENURE]]
- **external_dependency_class:** STATE_REGISTRIES
- **maximum_safe_outage:** BEFORE_ADMINISTRATIVE_LOSS
- **regeneration_or_replacement_method:** renew copies and official reissue
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
