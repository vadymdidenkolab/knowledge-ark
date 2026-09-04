---
id: "TD-FOOD-SITE"
kind: "technology"
title: "Почва; климат; вода и площадь"
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

# Почва; климат; вода и площадь

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FOOD-SITE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FOOD-SITE
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** SITE_DATA
- **title_ru:** Почва; климат; вода и площадь
- **outcome:** Определить реальную производственную способность участка
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-WATER-YIELD|TD-WATER-YIELD]]
- **source_package_ids:** [[PKG PSP-041|PSP-041]], [[PKG PSP-045|PSP-045]], [[PKG SUP-LEA-011|SUP-LEA-011]], [[PKG SUP-LEA-012|SUP-LEA-012]], [[PKG SUP-LEA-014|SUP-LEA-014]], [[PKG SUP-LEA-016|SUP-LEA-016]]
- **materials_tools_state:** MISSING_FIELD_DATA
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-020|INS-020]], [[INS INS-033|INS-033]], [[INS INS-034|INS-034]], [[INS INS-035|INS-035]]
- **measurement_acceptance:** Площадь; slope; soil profile; water budget; frost/heat and shade measured
- **calibration_reference:** Known area geometry; weather reference; lab soil test
- **drawings_bom_state:** MISSING_MAP_AND_BEDS
- **localization_state:** PORTUGAL_PARCEL_REQUIRED
- **waste_storage:** Sampling holes closed; contaminated soil isolated
- **stop_conditions:** Unknown contamination; protected habitat; unsafe slope; insufficient water
- **maintenance_spares:** Annual and seasonal logs
- **successor_proof:** Преемник повторяет area and water calculation
- **evidence_required:** Parcel map; lab report; climate log; water budget
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Расчёт 1 ha не доказывает наличие пригодного гектара
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
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-YIELD|TD-WATER-YIELD]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
