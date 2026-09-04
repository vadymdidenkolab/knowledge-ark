---
id: "TD-HAZ-MAINS"
kind: "technology"
title: "Сеть 230 V; щиты и высокое напряжение"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LICENSED_PROFESSIONAL"
safety_class: "S3_LICENSED_PROFESSIONAL"
execution_gate: "BLACK_GATE_LICENSED_ONLY"
status: "REFERENCE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Сеть 230 V; щиты и высокое напряжение

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HAZ-MAINS`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HAZ-MAINS
- **parent_id:** [[TEC TD-HAZARDS|TD-HAZARDS]]
- **domain:** HAZARD
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Сеть 230 V; щиты и высокое напряжение
- **outcome:** Recognize electrical danger; isolate only by user-operable controls and call qualified help
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_HOUSEHOLD_PANEL_WORK
- **instrument_ids:** [[INS INS-073|INS-073]]
- **measurement_acceptance:** Qualified inspection and test only
- **calibration_reference:** Calibrated jurisdiction-approved test equipment
- **drawings_bom_state:** NO_DIY_PANEL_DRAWINGS
- **localization_state:** PORTUGAL_LICENSED_ELECTRICIAN_REQUIRED
- **waste_storage:** Electrical waste route
- **stop_conditions:** Live parts; water; arcing; burning odor; unknown circuit; backfeed
- **maintenance_spares:** Professional inspection
- **successor_proof:** Household successor recognizes no-go and evacuates if needed
- **evidence_required:** Boundary card; inspection certificate; drill
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** No live work or panel opening
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
- **safety_lane:** S3_LICENSED_PROFESSIONAL
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
