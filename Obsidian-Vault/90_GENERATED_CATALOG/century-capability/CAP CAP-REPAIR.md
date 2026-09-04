---
id: "CAP-REPAIR"
kind: "century-capability"
title: "безопасный ремонт или замена критических систем"
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

# безопасный ремонт или замена критических систем

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `CAP-REPAIR`
- **Статус:** `PLANNED`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: century-capability-register.csv -->
- **capability_id:** CAP-REPAIR
- **domain_code:** TOOL
- **subject_level:** SITE|INSTITUTION
- **service_outcome:** безопасный ремонт или замена критических систем
- **beneficiary_scope:** ALL_CRITICAL_ASSETS
- **service_unit:** RECOVERY_WITHIN_RTO
- **demand_formula:** ASSET_FAILURE_MODES
- **minimum_service_level:** manual BOM tools parts competence isolation
- **dependency_capability_ids:** [[CAP CAP-TOOLS|CAP-TOOLS]], [[CAP CAP-SKILL-SUCCESSION|CAP-SKILL-SUCCESSION]], [[CAP CAP-FIN-LIFECYCLE|CAP-FIN-LIFECYCLE]]
- **external_dependency_class:** MANUFACTURERS_WORKSHOPS
- **maximum_safe_outage:** ASSET_SPECIFIC
- **regeneration_or_replacement_method:** standardize repair fabricate permitted parts or replace
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
