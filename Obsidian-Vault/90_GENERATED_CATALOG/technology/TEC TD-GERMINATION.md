---
id: "TD-GERMINATION"
kind: "technology"
title: "Тест всхожести"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY"
status: "ARCHITECTURE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Тест всхожести

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-GERMINATION`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-GERMINATION
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** TEST
- **title_ru:** Тест всхожести
- **outcome:** Оценить текущую жизнеспособность конкретной партии семян
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-SEED-BANK|TD-SEED-BANK]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** PRODUCTION_PACKAGE_CANDIDATE
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-036|INS-036]]
- **measurement_acceptance:** Заранее заданный sample; replicates; counted normal seedlings; percentage and uncertainty recorded
- **calibration_reference:** Known count; blind recount; control lot where available
- **drawings_bom_state:** CANDIDATE_PACKAGE_NOT_TESTED
- **localization_state:** CROP_SPECIFIC_METHOD_REQUIRED
- **waste_storage:** Used known seed and clean substrate bagged; mold stops test
- **stop_conditions:** Unknown biology; unusual odor; extensive mold; treated-seed exposure
- **maintenance_spares:** Per accession schedule
- **successor_proof:** Преемник повторяет с тем же lot and method
- **evidence_required:** Raw counts; photos; temperature; calculation; deviations
- **evidence_state:** LOCAL_UNREVIEWED
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** PP-002 создаётся как безопасный шаблон; нужен физический тест
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL4
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
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
| REQUIRED | [[TEC TD-SEED-BANK|TD-SEED-BANK]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
