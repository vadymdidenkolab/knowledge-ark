---
id: "CAP-POP-CARE"
kind: "century-capability"
title: "достаточная и добровольная мощность ухода"
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

# достаточная и добровольная мощность ухода

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-POP-CARE`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-POP-CARE
- **domain_code:** CARE
- **subject_level:** CELL|INSTITUTION
- **service_outcome:** достаточная и добровольная мощность ухода
- **beneficiary_scope:** DEPENDENTS_AND_CAREGIVERS
- **service_unit:** CARE_HOURS_PER_WEEK
- **demand_formula:** PROFILE_BASED_DEMAND
- **minimum_service_level:** demand not above proven capacity
- **dependency_capability_ids:** [[CAP CAP-MED-PRIMARY|CAP-MED-PRIMARY]], [[CAP CAP-SHELTER|CAP-SHELTER]]
- **external_dependency_class:** HEALTH_SOCIAL_NETWORK
- **maximum_safe_outage:** PROFILE_SPECIFIC
- **regeneration_or_replacement_method:** train rotate recruit and external care
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
