---
id: "TD-CROP-PLAN"
kind: "technology"
title: "Сезонный план культур"
priority_tier: "P2_YELLOW"
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

# Сезонный план культур

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-CROP-PLAN`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-CROP-PLAN
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Сезонный план культур
- **outcome:** Связать пищевую цель с площадью; водой; трудом и риском
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-FOOD-SITE|TD-FOOD-SITE]], [[TEC TD-SEED-BANK|TD-SEED-BANK]], [[TEC TD-NUTRITION|TD-NUTRITION]]
- **source_package_ids:** [[PKG PSP-041|PSP-041]], [[PKG SUP-LEA-017|SUP-LEA-017]], [[PKG SUP-LEA-018|SUP-LEA-018]], [[PKG SUP-LEA-020|SUP-LEA-020]]
- **materials_tools_state:** MISSING_SITE_PLAN
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-009|INS-009]], [[INS INS-011|INS-011]]
- **measurement_acceptance:** План имеет area; calendar; water; expected range; reserve and failure mode
- **calibration_reference:** Historical local data plus measured site data
- **drawings_bom_state:** MISSING_BED_LAYOUT
- **localization_state:** PORTUGAL_LOCAL_CALENDAR_REQUIRED
- **waste_storage:** Crop residues and diseased material routes defined
- **stop_conditions:** Water deficit; regulated crop; unknown disease; pesticide dependence
- **maintenance_spares:** Review each season
- **successor_proof:** Преемник объясняет tradeoffs and replans failed crop
- **evidence_required:** Plan; assumptions; sensitivity; approval
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Не оптимизировать только по числу сортов
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
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
| REQUIRED | [[TEC TD-SEED-BANK|TD-SEED-BANK]] | SL3 | — |
| REQUIRED | [[TEC TD-NUTRITION|TD-NUTRITION]] | SL4 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
