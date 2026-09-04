---
id: "TD-FERTILIZERS"
kind: "technology"
title: "Плодородие; удобрения и замыкание питательных циклов"
priority_tier: "P2_YELLOW"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "TRAINED_SUPERVISED"
safety_class: "S2_TRAINED_SUPERVISED"
execution_gate: "DENY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Плодородие; удобрения и замыкание питательных циклов

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERTILIZERS`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERTILIZERS
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** OUTCOME
- **title_ru:** Плодородие; удобрения и замыкание питательных циклов
- **outcome:** Maintain soil function from measured deficits using lowest-risk lawful sources
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-FOOD-SITE|TD-FOOD-SITE]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]], [[TEC TD-FERT-CROP-ROTATION|TD-FERT-CROP-ROTATION]], [[TEC TD-FERT-COMPOST|TD-FERT-COMPOST]], [[TEC TD-FERT-MANURE|TD-FERT-MANURE]], [[TEC TD-FERT-ASH|TD-FERT-ASH]], [[TEC TD-FERT-LIME-USE|TD-FERT-LIME-USE]], [[TEC TD-FERT-STORAGE|TD-FERT-STORAGE]], [[TEC TD-FERT-INDUSTRIAL-N|TD-FERT-INDUSTRIAL-N]], [[TEC TD-FERT-PHOSPHATE-POTASH|TD-FERT-PHOSPHATE-POTASH]], [[TEC TD-FERT-BIOLOGICAL|TD-FERT-BIOLOGICAL]], [[TEC TD-FERT-CROP-REMOVAL|TD-FERT-CROP-REMOVAL]], [[TEC TD-FERT-LEGUMES|TD-FERT-LEGUMES]], [[TEC TD-FERT-RESIDUES|TD-FERT-RESIDUES]], [[TEC TD-FERT-LABELED|TD-FERT-LABELED]], [[TEC TD-FERT-MICRONUTRIENTS|TD-FERT-MICRONUTRIENTS]], [[TEC TD-FERT-RUNOFF|TD-FERT-RUNOFF]], [[TEC TD-FERT-TRACEABILITY|TD-FERT-TRACEABILITY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_SOIL_PLAN_OR_INPUTS
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-029|INS-029]], [[INS INS-030|INS-030]], [[INS INS-033|INS-033]], [[INS INS-034|INS-034]], [[INS INS-035|INS-035]]
- **measurement_acceptance:** Soil and crop-specific nutrient budget; source identity; application record; water-risk and crop response reviewed
- **calibration_reference:** Accredited soil analysis; scale; area measurement; crop-specific guidance
- **drawings_bom_state:** MISSING_FIELD_PLAN
- **localization_state:** PORTUGAL_FERTILIZER_WATER_WASTE_AND_FARM_RULES_REQUIRED
- **waste_storage:** Nutrient; packaging; manure; ash and contaminated-soil routes defined
- **stop_conditions:** Unknown material; overapplication; runoff; pathogen; heavy metal; protected water; unsafe mixing
- **maintenance_spares:** Seasonal soil and crop monitoring; storage inspection
- **successor_proof:** Преемник calculates one approved application from reviewed analysis without changing product
- **evidence_required:** Soil report; product labels; mass; area; crop and water monitoring
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** A fertilizer recipe without soil data is not a capability
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P2_YELLOW
- **priority_horizon:** 15_TO_90_DAYS
- **earliest_service_level:** SL3
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P2_YELLOW
- **acquisition_priority:** P2_YELLOW
- **knowledge_priority:** P2_YELLOW
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS
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
| REQUIRED | [[TEC TD-FOOD-SITE|TD-FOOD-SITE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]] | SL3 | — |
| ALTERNATIVE | [[TEC TD-FERT-CROP-ROTATION|TD-FERT-CROP-ROTATION]] | SL3 | FERTILITY_STRATEGY |
| ALTERNATIVE | [[TEC TD-FERT-COMPOST|TD-FERT-COMPOST]] | SL3 | FERTILITY_STRATEGY |
| ALTERNATIVE | [[TEC TD-FERT-MANURE|TD-FERT-MANURE]] | SL3 | FERTILITY_STRATEGY |
| CONDITIONAL | [[TEC TD-FERT-ASH|TD-FERT-ASH]] | SL3 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FERT-LIME-USE|TD-FERT-LIME-USE]] | SL3 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-FERT-STORAGE|TD-FERT-STORAGE]] | SL3 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-FERT-INDUSTRIAL-N|TD-FERT-INDUSTRIAL-N]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FERT-PHOSPHATE-POTASH|TD-FERT-PHOSPHATE-POTASH]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-FERT-BIOLOGICAL|TD-FERT-BIOLOGICAL]] | SL1 | not_an_operational_prerequisite |
| REQUIRED | [[TEC TD-FERT-CROP-REMOVAL|TD-FERT-CROP-REMOVAL]] | SL3 | — |
| ALTERNATIVE | [[TEC TD-FERT-LEGUMES|TD-FERT-LEGUMES]] | SL3 | FERTILITY_STRATEGY |
| ALTERNATIVE | [[TEC TD-FERT-RESIDUES|TD-FERT-RESIDUES]] | SL3 | FERTILITY_STRATEGY |
| ALTERNATIVE | [[TEC TD-FERT-LABELED|TD-FERT-LABELED]] | SL3 | FERTILITY_STRATEGY |
| CONDITIONAL | [[TEC TD-FERT-MICRONUTRIENTS|TD-FERT-MICRONUTRIENTS]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-FERT-RUNOFF|TD-FERT-RUNOFF]] | SL3 | — |
| REQUIRED | [[TEC TD-FERT-TRACEABILITY|TD-FERT-TRACEABILITY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
