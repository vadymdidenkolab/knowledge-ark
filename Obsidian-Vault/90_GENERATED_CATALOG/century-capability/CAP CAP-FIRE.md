---
id: "CAP-FIRE"
kind: "century-capability"
title: "раннее обнаружение выход и пожарная безопасность"
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

# раннее обнаружение выход и пожарная безопасность

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-FIRE`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-FIRE
- **domain_code:** FIRE
- **subject_level:** SITE
- **service_outcome:** раннее обнаружение выход и пожарная безопасность
- **beneficiary_scope:** ALL_OCCUPANTS
- **service_unit:** VERIFIED_ESCAPE_AND_DETECTION
- **demand_formula:** BUILDING_PROFILE
- **minimum_service_level:** alarms exits drills professional systems
- **dependency_capability_ids:** [[CAP CAP-SHELTER|CAP-SHELTER]], [[CAP CAP-COMMS|CAP-COMMS]]
- **external_dependency_class:** FIRE_SERVICE_INSPECTOR
- **maximum_safe_outage:** ZERO_FOR_BLOCKED_EXIT
- **regeneration_or_replacement_method:** detect exit call service and repair
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
