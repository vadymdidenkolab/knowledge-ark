---
id: "TD-GOV-LEDGER"
kind: "technology"
title: "Прозрачный ресурсный журнал"
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

# Прозрачный ресурсный журнал

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-GOV-LEDGER`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-GOV-LEDGER
- **parent_id:** [[TEC TD-GOV|TD-GOV]]
- **domain:** GOVERNANCE
- **node_type:** PROCESS
- **title_ru:** Прозрачный ресурсный журнал
- **outcome:** Track stock; ration decisions; transfers and discrepancies
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-GOV-ROLES|TD-GOV-ROLES]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_REAL_TRANSACTIONS
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]]
- **measurement_acceptance:** Opening plus receipts minus use minus closing reconciles; variances signed
- **calibration_reference:** Blind count and arithmetic cross-check
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** GROUP_PRIVACY_REQUIRED
- **waste_storage:** Spoilage and waste dispositions recorded
- **stop_conditions:** Hidden allocation; unexplained loss; coercive rationing; falsified record
- **maintenance_spares:** Daily during incident; monthly otherwise
- **successor_proof:** Преемник reconciles sample period
- **evidence_required:** Ledger; counts; approvals; variances
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Two example rows do not prove an accounting system
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
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |
| REQUIRED | [[TEC TD-GOV-ROLES|TD-GOV-ROLES]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
