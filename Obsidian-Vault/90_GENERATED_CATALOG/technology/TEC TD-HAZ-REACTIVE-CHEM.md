---
id: "TD-HAZ-REACTIVE-CHEM"
kind: "technology"
title: "Реактивная и неизвестная химия"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION"
safety_class: "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"
execution_gate: "BLACK_GATE_REFERENCE_ONLY"
status: "REFERENCE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Реактивная и неизвестная химия

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HAZ-REACTIVE-CHEM`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION`
- **Класс безопасности:** `S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD`
- **Допуск:** `BLACK_GATE_REFERENCE_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HAZ-REACTIVE-CHEM
- **parent_id:** [[TEC TD-HAZARDS|TD-HAZARDS]]
- **domain:** HAZARD
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Реактивная и неизвестная химия
- **outcome:** Prevent mixing; toxic gas; burns and contaminated food or water
- **safety_class:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **execution_policy:** REFERENCE_ONLY_NO_BUILD
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_HOME_REACTIVE_CHEMISTRY
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Unknowns remain unidentified by home experimentation; area isolated
- **calibration_reference:** Official label; SDS; CIAV or competent laboratory
- **drawings_bom_state:** NO_BUILD_DRAWINGS
- **localization_state:** PORTUGAL_CIAV_AND_WASTE_ROUTE_REQUIRED
- **waste_storage:** Licensed hazardous-waste route
- **stop_conditions:** Unknown identity; leak; odor; reaction; heat; damaged container
- **maintenance_spares:** Storage audit only
- **successor_proof:** Преемник isolates and communicates label information
- **evidence_required:** Boundary card; owned-product SDS; contact drill
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** SDS does not create a laboratory
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
- **safety_lane:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
