---
id: "TD-SANITATION"
kind: "technology"
title: "Санитария и отходы"
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

# Санитария и отходы

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-SANITATION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-SANITATION
- **parent_id:** [[TEC TD-WATER|TD-WATER]]
- **domain:** WATER_WASH
- **node_type:** OUTCOME
- **title_ru:** Санитария и отходы
- **outcome:** Разделить drinking-water; руки; пищу; экскременты; серые воды и мусор
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-SAN-TOILET|TD-SAN-TOILET]], [[TEC TD-SAN-HANDWASH|TD-SAN-HANDWASH]], [[TEC TD-SAN-ZONING|TD-SAN-ZONING]], [[TEC TD-SAN-SOAP|TD-SAN-SOAP]], [[TEC TD-SAN-MENSTRUAL|TD-SAN-MENSTRUAL]], [[TEC TD-SAN-DIAPERS|TD-SAN-DIAPERS]], [[TEC TD-SAN-INCONTINENCE|TD-SAN-INCONTINENCE]], [[TEC TD-SAN-BATHING|TD-SAN-BATHING]], [[TEC TD-SAN-LAUNDRY|TD-SAN-LAUNDRY]], [[TEC TD-SAN-BLACKWATER|TD-SAN-BLACKWATER]], [[TEC TD-SAN-GREYWATER|TD-SAN-GREYWATER]], [[TEC TD-SAN-HOUSEHOLD-WASTE|TD-SAN-HOUSEHOLD-WASTE]], [[TEC TD-SAN-FOOD-WASTE|TD-SAN-FOOD-WASTE]], [[TEC TD-SAN-HAZARDOUS-WASTE|TD-SAN-HAZARDOUS-WASTE]], [[TEC TD-SAN-BATTERIES|TD-SAN-BATTERIES]], [[TEC TD-SAN-OILS|TD-SAN-OILS]], [[TEC TD-SAN-SHARPS|TD-SAN-SHARPS]], [[TEC TD-SAN-MEDICAL|TD-SAN-MEDICAL]], [[TEC TD-SAN-ANIMAL|TD-SAN-ANIMAL]], [[TEC TD-SAN-CONSTRUCTION|TD-SAN-CONSTRUCTION]], [[TEC TD-SAN-DEAD-ANIMAL|TD-SAN-DEAD-ANIMAL]], [[TEC TD-SAN-HUMAN-DEATH|TD-SAN-HUMAN-DEATH]], [[TEC TD-SAN-PESTS|TD-SAN-PESTS]]
- **source_package_ids:** [[PKG SUP-LEA-030|SUP-LEA-030]]
- **materials_tools_state:** MISSING_SITE_SANITATION
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-040|INS-040]]
- **measurement_acceptance:** Потоки и зоны не пересекаются; вместимость и обслуживание измерены; legal route documented
- **calibration_reference:** Site measurements; inspection; water-risk review
- **drawings_bom_state:** MISSING
- **localization_state:** PORTUGAL_SITE_AND_WASTE_RULES_REQUIRED
- **waste_storage:** Approved excreta; greywater; solid-waste routes
- **stop_conditions:** Flooding; seepage; vector outbreak; contamination of food or source
- **maintenance_spares:** Daily inspection in emergency; spares and consumables
- **successor_proof:** Преемник устанавливает clean/dirty zoning и stop
- **evidence_required:** Site plan; capacity; inspection logs; drill
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Аварийный туалет в тексте не равен длительной системе
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
- **capacity_model:** LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS
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
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-SAN-TOILET|TD-SAN-TOILET]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-HANDWASH|TD-SAN-HANDWASH]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-ZONING|TD-SAN-ZONING]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-SOAP|TD-SAN-SOAP]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-MENSTRUAL|TD-SAN-MENSTRUAL]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-DIAPERS|TD-SAN-DIAPERS]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-INCONTINENCE|TD-SAN-INCONTINENCE]] | SL1 | — |
| REQUIRED | [[TEC TD-SAN-BATHING|TD-SAN-BATHING]] | SL2 | — |
| REQUIRED | [[TEC TD-SAN-LAUNDRY|TD-SAN-LAUNDRY]] | SL2 | — |
| HAZARD_ONLY | [[TEC TD-SAN-BLACKWATER|TD-SAN-BLACKWATER]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-SAN-GREYWATER|TD-SAN-GREYWATER]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-SAN-HOUSEHOLD-WASTE|TD-SAN-HOUSEHOLD-WASTE]] | SL2 | — |
| REQUIRED | [[TEC TD-SAN-FOOD-WASTE|TD-SAN-FOOD-WASTE]] | SL2 | — |
| HAZARD_ONLY | [[TEC TD-SAN-HAZARDOUS-WASTE|TD-SAN-HAZARDOUS-WASTE]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-SAN-BATTERIES|TD-SAN-BATTERIES]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-SAN-OILS|TD-SAN-OILS]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-SAN-SHARPS|TD-SAN-SHARPS]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-SAN-MEDICAL|TD-SAN-MEDICAL]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-SAN-ANIMAL|TD-SAN-ANIMAL]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-SAN-CONSTRUCTION|TD-SAN-CONSTRUCTION]] | SL2 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-SAN-DEAD-ANIMAL|TD-SAN-DEAD-ANIMAL]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-SAN-HUMAN-DEATH|TD-SAN-HUMAN-DEATH]] | SL1 | not_an_operational_prerequisite |
| REQUIRED | [[TEC TD-SAN-PESTS|TD-SAN-PESTS]] | SL2 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
