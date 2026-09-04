---
id: "TD-GOV-ROLES"
kind: "technology"
title: "Функции; primary; backup и пределы полномочий"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Функции; primary; backup и пределы полномочий

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-GOV-ROLES`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-GOV-ROLES
- **parent_id:** [[TEC TD-GOV|TD-GOV]]
- **domain:** GOVERNANCE
- **node_type:** GOVERNANCE
- **title_ru:** Функции; primary; backup и пределы полномочий
- **outcome:** Ensure every critical function has an owner and safe fallback
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** PLANNED_PSEUDONYMS_ONLY
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Every real person accepts role; availability; limits and conflicts checked
- **calibration_reference:** Roster revision and consent cross-check
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** REAL_GROUP_REQUIRED
- **waste_storage:** Not applicable
- **stop_conditions:** Unaccepted role; unavailable backup; medical or legal scope missing
- **maintenance_spares:** After membership or health change
- **successor_proof:** Backup runs one shift with handoff
- **evidence_required:** Accepted roster; availability; role gates
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Current profiles are templates
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL1
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL
- **capacity_value:** TBD_PERSON_AND_SITE_PROFILE
- **capacity_unit:** TBD_BY_CAPABILITY
- **labor_hours:** TBD
- **failure_domain:** TBD_SITE_AND_IMPLEMENTATION
- **redundancy_target:** TWO_PATHS_OR_EXPLICIT_RESIDUAL_RISK
- **owner_role:** UNASSIGNED
- **backup_role:** UNASSIGNED
- **drill_id:** NOT_ASSIGNED
- **next_due:** TBD
- **human_review_state:** PROVISIONAL_AUTO_REVIEW_REQUIRED
- **release_gate:** DENY
- **release_version:** 0.5-draft

</details>

<details>
<summary>Типизированные зависимости</summary>

| Роль | Узел | Service level | Условие / группа |
|---|---|---|---|
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
