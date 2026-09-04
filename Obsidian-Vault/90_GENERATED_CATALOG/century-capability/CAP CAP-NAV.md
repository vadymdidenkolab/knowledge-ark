---
id: "CAP-NAV"
kind: "century-capability"
title: "офлайн-навигация и проверенные маршруты"
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

# офлайн-навигация и проверенные маршруты

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-NAV`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-NAV
- **domain_code:** NAV
- **subject_level:** CELL|SITE
- **service_outcome:** офлайн-навигация и проверенные маршруты
- **beneficiary_scope:** ALL_CELLS
- **service_unit:** CURRENT_MAP_ROUTE_SET
- **demand_formula:** LOCATIONS_AND_SCENARIOS
- **minimum_service_level:** digital plus print field checks and stop criteria
- **dependency_capability_ids:** [[CAP CAP-ARCHIVE-RESTORE|CAP-ARCHIVE-RESTORE]], [[CAP CAP-TRANSPORT|CAP-TRANSPORT]]
- **external_dependency_class:** MAPPING_AUTHORITIES
- **maximum_safe_outage:** ROUTE_VALIDITY_WINDOW
- **regeneration_or_replacement_method:** update data print and field verify
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
