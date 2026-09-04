---
id: "TD-FERT-PHOSPHATE-POTASH"
kind: "technology"
title: "Добыча и промышленная переработка фосфатных и калийных материалов"
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

# Добыча и промышленная переработка фосфатных и калийных материалов

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERT-PHOSPHATE-POTASH`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERT-PHOSPHATE-POTASH
- **parent_id:** [[TEC TD-FERTILIZERS|TD-FERTILIZERS]]
- **domain:** FOOD_AGRI
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Добыча и промышленная переработка фосфатных и калийных материалов
- **outcome:** Preserve geology; resource and contamination overview without unsafe extraction or chemical processing
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_MINE_OR_PROCESS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Licensed extraction; environmental assessment and product standards only
- **calibration_reference:** Qualified mining; agronomy and environmental sources
- **drawings_bom_state:** PROFESSIONAL_ONLY
- **localization_state:** PORTUGAL_MINING_ENVIRONMENT_WATER_AND_LAND_RULES_REQUIRED
- **waste_storage:** Tailings; brine; dust and process waste under licensed system
- **stop_conditions:** Mine; slope; dust; radionuclides; acid process; brine; water contamination
- **maintenance_spares:** Professional monitoring only
- **successor_proof:** Преемник recognizes limits and relies on certified product or nutrient recycling
- **evidence_required:** Boundary; professional shelf; permits if any
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** No mining; beneficiation or acidulation instructions
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
- **capacity_model:** KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS
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
| REQUIRED | [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]] | SL3 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
