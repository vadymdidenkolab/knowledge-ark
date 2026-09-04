---
id: "TD-FUELS"
kind: "technology"
title: "Топливо; смазки и тепловые носители"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LICENSED_PROFESSIONAL"
safety_class: "S3_LICENSED_PROFESSIONAL"
execution_gate: "BLACK_GATE_LICENSED_ONLY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Топливо; смазки и тепловые носители

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUELS`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUELS
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** ENERGY_FUELS
- **node_type:** OUTCOME
- **title_ru:** Топливо; смазки и тепловые носители
- **outcome:** Сократить спрос; законно хранить готовое топливо; сохранить промышленное знание без опасной домашней переработки
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-FUEL-DEMAND|TD-FUEL-DEMAND]], [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]], [[TEC TD-FUEL-SOLID|TD-FUEL-SOLID]], [[TEC TD-FUEL-VEGOIL|TD-FUEL-VEGOIL]], [[TEC TD-FUEL-LUBRICANTS|TD-FUEL-LUBRICANTS]], [[TEC TD-FUEL-ENGINE-COMPAT|TD-FUEL-ENGINE-COMPAT]], [[TEC TD-FUEL-PETROLEUM-REFINING|TD-FUEL-PETROLEUM-REFINING]], [[TEC TD-FUEL-ETHANOL|TD-FUEL-ETHANOL]], [[TEC TD-FUEL-BIODIESEL|TD-FUEL-BIODIESEL]], [[TEC TD-FUEL-BIOGAS|TD-FUEL-BIOGAS]], [[TEC TD-FUEL-PRODUCER-GAS|TD-FUEL-PRODUCER-GAS]], [[TEC TD-FUEL-USE-COOK|TD-FUEL-USE-COOK]], [[TEC TD-FUEL-USE-HEAT|TD-FUEL-USE-HEAT]], [[TEC TD-FUEL-USE-POWER|TD-FUEL-USE-POWER]], [[TEC TD-FUEL-USE-TRANSPORT|TD-FUEL-USE-TRANSPORT]], [[TEC TD-FUEL-PRODUCT-ID|TD-FUEL-PRODUCT-ID]], [[TEC TD-FUEL-BATCH-ACCEPT|TD-FUEL-BATCH-ACCEPT]], [[TEC TD-FUEL-ROTATION|TD-FUEL-ROTATION]], [[TEC TD-FUEL-SPILL|TD-FUEL-SPILL]], [[TEC TD-FUEL-EXHAUST|TD-FUEL-EXHAUST]], [[TEC TD-FUEL-ASH|TD-FUEL-ASH]], [[TEC TD-FUEL-CONSUMPTION|TD-FUEL-CONSUMPTION]], [[TEC TD-FUEL-ALTERNATIVE|TD-FUEL-ALTERNATIVE]], [[TEC TD-FUEL-WOODLOT|TD-FUEL-WOODLOT]], [[TEC TD-FUEL-WOOD-DRY|TD-FUEL-WOOD-DRY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_FUEL_SYSTEM_OR_STOCK
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-023|INS-023]], [[INS INS-024|INS-024]], [[INS INS-045|INS-045]], [[INS INS-053|INS-053]]
- **measurement_acceptance:** Demand; legal storage; fire separation; compatibility; turnover and professional production boundaries documented
- **calibration_reference:** Certified containers; OEM data; qualified fire and process review
- **drawings_bom_state:** MISSING_SYSTEM_LAYOUT
- **localization_state:** PORTUGAL_FIRE_ENVIRONMENT_TAX_AND_FUEL_RULES_REQUIRED
- **waste_storage:** Fuel; oils; filters; contaminated soil and containers use licensed routes
- **stop_conditions:** Leak; vapor; heat; smoke; wrong fuel; unknown mixture; pressure; confined space
- **maintenance_spares:** Stock rotation; seals; filters; spill kit; fire systems; alternative mobility
- **successor_proof:** Преемник identifies products; performs safe shutdown and refuses prohibited production
- **evidence_required:** Inventory; SDS; site plan; inspections; consumption log; professional sources
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** This branch catalogs gasoline; diesel; kerosene and alternatives without household refining recipes
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL5
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S3_LICENSED_PROFESSIONAL
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE
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
| REQUIRED | [[TEC TD-FUEL-DEMAND|TD-FUEL-DEMAND]] | SL3 | — |
| CONDITIONAL | [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]] | SL5 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-FUEL-SOLID|TD-FUEL-SOLID]] | SL3 | — |
| OPTIONAL | [[TEC TD-FUEL-VEGOIL|TD-FUEL-VEGOIL]] | SL3 | use_only_if_selected_technology_requires_it |
| REQUIRED | [[TEC TD-FUEL-LUBRICANTS|TD-FUEL-LUBRICANTS]] | SL3 | — |
| CONDITIONAL | [[TEC TD-FUEL-ENGINE-COMPAT|TD-FUEL-ENGINE-COMPAT]] | SL5 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-FUEL-PETROLEUM-REFINING|TD-FUEL-PETROLEUM-REFINING]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FUEL-ETHANOL|TD-FUEL-ETHANOL]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FUEL-BIODIESEL|TD-FUEL-BIODIESEL]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FUEL-BIOGAS|TD-FUEL-BIOGAS]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FUEL-PRODUCER-GAS|TD-FUEL-PRODUCER-GAS]] | SL1 | not_an_operational_prerequisite |
| REQUIRED | [[TEC TD-FUEL-USE-COOK|TD-FUEL-USE-COOK]] | SL3 | — |
| CONDITIONAL | [[TEC TD-FUEL-USE-HEAT|TD-FUEL-USE-HEAT]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FUEL-USE-POWER|TD-FUEL-USE-POWER]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FUEL-USE-TRANSPORT|TD-FUEL-USE-TRANSPORT]] | SL5 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-FUEL-PRODUCT-ID|TD-FUEL-PRODUCT-ID]] | SL3 | — |
| REQUIRED | [[TEC TD-FUEL-BATCH-ACCEPT|TD-FUEL-BATCH-ACCEPT]] | SL3 | — |
| REQUIRED | [[TEC TD-FUEL-ROTATION|TD-FUEL-ROTATION]] | SL3 | — |
| CONDITIONAL | [[TEC TD-FUEL-SPILL|TD-FUEL-SPILL]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FUEL-EXHAUST|TD-FUEL-EXHAUST]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FUEL-ASH|TD-FUEL-ASH]] | SL5 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-FUEL-CONSUMPTION|TD-FUEL-CONSUMPTION]] | SL3 | — |
| REQUIRED | [[TEC TD-FUEL-ALTERNATIVE|TD-FUEL-ALTERNATIVE]] | SL3 | — |
| OPTIONAL | [[TEC TD-FUEL-WOODLOT|TD-FUEL-WOODLOT]] | SL5 | use_only_if_selected_technology_requires_it |
| OPTIONAL | [[TEC TD-FUEL-WOOD-DRY|TD-FUEL-WOOD-DRY]] | SL3 | use_only_if_selected_technology_requires_it |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
