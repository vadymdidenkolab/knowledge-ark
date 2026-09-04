---
id: "TD-FOOD-PRESERVATION"
kind: "technology"
title: "Безопасное сохранение пищи"
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

# Безопасное сохранение пищи

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FOOD-PRESERVATION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FOOD-PRESERVATION
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Безопасное сохранение пищи
- **outcome:** Использовать только валидированные процессы по типу продукта и высоте
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-HARVEST-STORAGE|TD-HARVEST-STORAGE]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[PKG PSP-046|PSP-046]], [[PKG SUP-LEA-034|SUP-LEA-034]]
- **materials_tools_state:** MISSING_EQUIPMENT_AND_METHOD
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-015|INS-015]]
- **measurement_acceptance:** Exact validated recipe; jar size; time; temperature or pressure and altitude rule met
- **calibration_reference:** Verified timer; thermometer; pressure gauge service where method requires
- **drawings_bom_state:** MISSING_PROCESS_PACKAGE
- **localization_state:** PORTUGAL_FOOD_RULES_AND_ALTITUDE_REQUIRED
- **waste_storage:** Failed or suspect batches discarded safely
- **stop_conditions:** Deviation; seal failure; unknown acidity; pressure equipment issue; spoilage
- **maintenance_spares:** Equipment inspection; seals; batch logs
- **successor_proof:** Преемник follows one validated low-risk method and rejects deviation
- **evidence_required:** Source section; batch log; instrument checks; acceptance
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Не импровизировать low-acid canning
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
| REQUIRED | [[TEC TD-HARVEST-STORAGE|TD-HARVEST-STORAGE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
