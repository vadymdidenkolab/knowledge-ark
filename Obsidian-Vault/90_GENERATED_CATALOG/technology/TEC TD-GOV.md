---
id: "TD-GOV"
kind: "technology"
title: "Управление группы; права и экономика"
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

# Управление группы; права и экономика

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-GOV`
- **Статус:** `MISSING`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-GOV
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** GOVERNANCE
- **node_type:** OUTCOME
- **title_ru:** Управление группы; права и экономика
- **outcome:** Coordinate one to seven people without single-leader failure or coercion
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-GOV-ROLES|TD-GOV-ROLES]], [[TEC TD-GOV-LEDGER|TD-GOV-LEDGER]], [[TEC TD-GOV-SAFEGUARD|TD-GOV-SAFEGUARD]], [[TEC TD-GOV-SUCCESSION|TD-GOV-SUCCESSION]], [[TEC TD-GOV-CONFLICT|TD-GOV-CONFLICT]], [[TEC TD-GOV-LIMITS|TD-GOV-LIMITS]], [[TEC TD-GOV-AUDIT|TD-GOV-AUDIT]], [[TEC TD-GOV-GRIEVANCE|TD-GOV-GRIEVANCE]], [[TEC TD-GOV-VULNERABLE|TD-GOV-VULNERABLE]], [[TEC TD-GOV-LAW|TD-GOV-LAW]], [[TEC TD-GOV-BIRTH-DEATH|TD-GOV-BIRTH-DEATH]], [[TEC TD-GOV-TRADE|TD-GOV-TRADE]], [[TEC TD-GOV-COMMUNITY|TD-GOV-COMMUNITY]], [[TEC TD-GOV-PROCUREMENT|TD-GOV-PROCUREMENT]], [[TEC TD-GOV-STOCK|TD-GOV-STOCK]], [[TEC TD-GOV-WAREHOUSE|TD-GOV-WAREHOUSE]], [[TEC TD-GOV-DISTRIBUTION|TD-GOV-DISTRIBUTION]], [[TEC TD-GOV-LABOR|TD-GOV-LABOR]], [[TEC TD-GOV-RECOVERY|TD-GOV-RECOVERY]], [[TEC TD-GOV-RELOCATION|TD-GOV-RELOCATION]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NOT_ADOPTED
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Roles accepted; rights protected; resources traceable; succession and appeal drills pass
- **calibration_reference:** Signed current version and tabletop exercises
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_LAW_AND_REAL_PEOPLE_REQUIRED
- **waste_storage:** Not applicable
- **stop_conditions:** No consent; abuse; hidden ledger; exhausted decision-maker; unresolved legal authority
- **maintenance_spares:** Monthly operational; annual charter and succession review
- **successor_proof:** Преемник assumes role lawfully and produces complete handoff
- **evidence_required:** Signed charter; roster; logs; exercises
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Templates are not agreements
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-GOV-ROLES|TD-GOV-ROLES]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-LEDGER|TD-GOV-LEDGER]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-SAFEGUARD|TD-GOV-SAFEGUARD]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-SUCCESSION|TD-GOV-SUCCESSION]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-CONFLICT|TD-GOV-CONFLICT]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-LIMITS|TD-GOV-LIMITS]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-AUDIT|TD-GOV-AUDIT]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-GRIEVANCE|TD-GOV-GRIEVANCE]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-VULNERABLE|TD-GOV-VULNERABLE]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-LAW|TD-GOV-LAW]] | SL6 | — |
| CONDITIONAL | [[TEC TD-GOV-BIRTH-DEATH|TD-GOV-BIRTH-DEATH]] | SL6 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-GOV-TRADE|TD-GOV-TRADE]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-COMMUNITY|TD-GOV-COMMUNITY]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-PROCUREMENT|TD-GOV-PROCUREMENT]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-STOCK|TD-GOV-STOCK]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-WAREHOUSE|TD-GOV-WAREHOUSE]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-DISTRIBUTION|TD-GOV-DISTRIBUTION]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-LABOR|TD-GOV-LABOR]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-RECOVERY|TD-GOV-RECOVERY]] | SL6 | — |
| REQUIRED | [[TEC TD-GOV-RELOCATION|TD-GOV-RELOCATION]] | SL6 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
