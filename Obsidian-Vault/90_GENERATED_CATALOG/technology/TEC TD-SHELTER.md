---
id: "TD-SHELTER"
kind: "technology"
title: "Безопасное жильё; воздух и температурный режим"
priority_tier: "P1_ORANGE"
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

# Безопасное жильё; воздух и температурный режим

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-SHELTER`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-SHELTER
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** SHELTER
- **node_type:** OUTCOME
- **title_ru:** Безопасное жильё; воздух и температурный режим
- **outcome:** Сохранить выход; оболочку; вентиляцию; тепло или охлаждение без пожара и CO
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-EXITS-SHUTOFFS|TD-EXITS-SHUTOFFS]], [[TEC TD-FIRE-CO|TD-FIRE-CO]], [[TEC TD-VENTILATION|TD-VENTILATION]], [[TEC TD-THERMAL|TD-THERMAL]], [[TEC TD-DRAINAGE|TD-DRAINAGE]], [[TEC TD-SHELTER-SHELTER-IN-PLACE|TD-SHELTER-SHELTER-IN-PLACE]], [[TEC TD-SHELTER-SAFE-ZONE|TD-SHELTER-SAFE-ZONE]], [[TEC TD-SHELTER-ACCESSIBLE-EXIT|TD-SHELTER-ACCESSIBLE-EXIT]], [[TEC TD-SHELTER-SHUTOFF-WATER|TD-SHELTER-SHUTOFF-WATER]], [[TEC TD-SHELTER-SHUTOFF-GAS|TD-SHELTER-SHUTOFF-GAS]], [[TEC TD-SHELTER-SHUTOFF-ELECTRIC|TD-SHELTER-SHUTOFF-ELECTRIC]], [[TEC TD-SHELTER-ALARMS|TD-SHELTER-ALARMS]], [[TEC TD-SHELTER-EXTINGUISHER|TD-SHELTER-EXTINGUISHER]], [[TEC TD-SHELTER-FIRE-BLANKET|TD-SHELTER-FIRE-BLANKET]], [[TEC TD-SHELTER-DARK-EXIT|TD-SHELTER-DARK-EXIT]], [[TEC TD-SHELTER-COLLAPSE|TD-SHELTER-COLLAPSE]], [[TEC TD-SHELTER-HEAT-ZONE|TD-SHELTER-HEAT-ZONE]], [[TEC TD-SHELTER-COLD-ZONE|TD-SHELTER-COLD-ZONE]], [[TEC TD-SHELTER-COMBUSTION-AIR|TD-SHELTER-COMBUSTION-AIR]], [[TEC TD-SHELTER-LIGHT|TD-SHELTER-LIGHT]], [[TEC TD-SHELTER-DEPENDENTS|TD-SHELTER-DEPENDENTS]], [[TEC TD-SHELTER-KITCHEN|TD-SHELTER-KITCHEN]], [[TEC TD-SHELTER-PESTS|TD-SHELTER-PESTS]], [[TEC TD-CONSTRUCTION|TD-CONSTRUCTION]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_SITE_ASSETS
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-021|INS-021]], [[INS INS-023|INS-023]], [[INS INS-024|INS-024]], [[INS INS-025|INS-025]], [[INS INS-071|INS-071]], [[INS INS-072|INS-072]]
- **measurement_acceptance:** Safe zones; exits; temperature; humidity; air alarms and defects within reviewed limits
- **calibration_reference:** Certified detectors; checked thermometers; professional inspections
- **drawings_bom_state:** MISSING
- **localization_state:** ADDRESS_AND_BUILDING_REQUIRED
- **waste_storage:** Building waste by known material class
- **stop_conditions:** Structural damage; gas; CO; smoke; unknown material; flood electricity
- **maintenance_spares:** Seasonal inspection; detector replacement; envelope maintenance
- **successor_proof:** Преемник performs drill and identifies no-go defects
- **evidence_required:** Building file; inspections; logs; drills
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Generic checklist is not a building assessment
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P1_ORANGE
- **priority_horizon:** 3_TO_14_DAYS
- **earliest_service_level:** SL2
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P1_ORANGE
- **acquisition_priority:** P1_ORANGE
- **knowledge_priority:** P1_ORANGE
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| CONDITIONAL | [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-EXITS-SHUTOFFS|TD-EXITS-SHUTOFFS]] | SL0 | — |
| REQUIRED | [[TEC TD-FIRE-CO|TD-FIRE-CO]] | SL0 | — |
| REQUIRED | [[TEC TD-VENTILATION|TD-VENTILATION]] | SL2 | — |
| REQUIRED | [[TEC TD-THERMAL|TD-THERMAL]] | SL2 | — |
| REQUIRED | [[TEC TD-DRAINAGE|TD-DRAINAGE]] | SL4 | — |
| REQUIRED | [[TEC TD-SHELTER-SHELTER-IN-PLACE|TD-SHELTER-SHELTER-IN-PLACE]] | SL2 | — |
| REQUIRED | [[TEC TD-SHELTER-SAFE-ZONE|TD-SHELTER-SAFE-ZONE]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-ACCESSIBLE-EXIT|TD-SHELTER-ACCESSIBLE-EXIT]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-SHUTOFF-WATER|TD-SHELTER-SHUTOFF-WATER]] | SL1 | — |
| CONDITIONAL | [[TEC TD-SHELTER-SHUTOFF-GAS|TD-SHELTER-SHUTOFF-GAS]] | SL1 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-SHELTER-SHUTOFF-ELECTRIC|TD-SHELTER-SHUTOFF-ELECTRIC]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-ALARMS|TD-SHELTER-ALARMS]] | SL0 | — |
| REQUIRED | [[TEC TD-SHELTER-EXTINGUISHER|TD-SHELTER-EXTINGUISHER]] | SL2 | — |
| REQUIRED | [[TEC TD-SHELTER-FIRE-BLANKET|TD-SHELTER-FIRE-BLANKET]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-DARK-EXIT|TD-SHELTER-DARK-EXIT]] | SL1 | — |
| HAZARD_ONLY | [[TEC TD-SHELTER-COLLAPSE|TD-SHELTER-COLLAPSE]] | SL1 | not_an_operational_prerequisite |
| REQUIRED | [[TEC TD-SHELTER-HEAT-ZONE|TD-SHELTER-HEAT-ZONE]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-COLD-ZONE|TD-SHELTER-COLD-ZONE]] | SL1 | — |
| CONDITIONAL | [[TEC TD-SHELTER-COMBUSTION-AIR|TD-SHELTER-COMBUSTION-AIR]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-SHELTER-LIGHT|TD-SHELTER-LIGHT]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-DEPENDENTS|TD-SHELTER-DEPENDENTS]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER-KITCHEN|TD-SHELTER-KITCHEN]] | SL2 | — |
| REQUIRED | [[TEC TD-SHELTER-PESTS|TD-SHELTER-PESTS]] | SL2 | — |
| CONDITIONAL | [[TEC TD-CONSTRUCTION|TD-CONSTRUCTION]] | SL5 | applicable_profile_site_or_qualified_role_required |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
