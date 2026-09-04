---
id: "CAP-ENERGY-CRITICAL"
kind: "century-capability"
title: "энергия для измеренных критических нагрузок"
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

# энергия для измеренных критических нагрузок

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-ENERGY-CRITICAL`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-ENERGY-CRITICAL
- **domain_code:** ENE
- **subject_level:** SITE
- **service_outcome:** энергия для измеренных критических нагрузок
- **beneficiary_scope:** CRITICAL_SYSTEMS
- **service_unit:** WH_PER_DAY_AND_PEAK_W
- **demand_formula:** MEASURED_LOAD_PROFILE
- **minimum_service_level:** load test failover isolation replacement budget
- **dependency_capability_ids:** [[CAP CAP-REPAIR|CAP-REPAIR]], [[CAP CAP-FIN-LIFECYCLE|CAP-FIN-LIFECYCLE]]
- **external_dependency_class:** GRID_FUEL_INSTALLER
- **maximum_safe_outage:** LOAD_SPECIFIC
- **regeneration_or_replacement_method:** diverse sources storage manual alternatives replace components
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
