---
id: "TD-GOV-SUCCESSION"
kind: "technology"
title: "Передача ролей; ключей и знаний"
priority_tier: "P4_BLUE"
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

# Передача ролей; ключей и знаний

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-GOV-SUCCESSION`
- **Статус:** `MISSING`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-GOV-SUCCESSION
- **parent_id:** [[TEC TD-GOV|TD-GOV]]
- **domain:** GOVERNANCE
- **node_type:** TEST
- **title_ru:** Передача ролей; ключей и знаний
- **outcome:** Continue operation when a person is absent; incapacitated or dead
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-GOV-ROLES|TD-GOV-ROLES]], [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_TESTED_SUCCESSION
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Successor receives lawful access; finds records; runs safe shift and documents handoff
- **calibration_reference:** Tabletop plus live low-risk exercise
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** REAL_PEOPLE_ASSETS_AND_LAW_REQUIRED
- **waste_storage:** Not applicable
- **stop_conditions:** Unauthorized access; missing consent; lost key; competency gap
- **maintenance_spares:** Annual and after role change
- **successor_proof:** Named successor completes blind handoff
- **evidence_required:** Succession record; access test; exercise
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Single author is current failure mode
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P4_BLUE
- **priority_horizon:** 15_TO_100_YEARS
- **earliest_service_level:** SL6
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P4_BLUE
- **acquisition_priority:** P4_BLUE
- **knowledge_priority:** P4_BLUE
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL
- **capacity_value:** TBD_PERSON_AND_SITE_PROFILE
- **capacity_unit:** TBD_BY_CAPABILITY
- **labor_hours:** TBD
- **failure_domain:** TBD_SITE_AND_IMPLEMENTATION
- **redundancy_target:** TBD_BY_SERVICE_LEVEL
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
| REQUIRED | [[TEC TD-GOV-ROLES|TD-GOV-ROLES]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
