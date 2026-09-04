---
id: "TD-FERT-COMPOST"
kind: "technology"
title: "Компост из известных низкорисковых растительных и пищевых материалов"
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

# Компост из известных низкорисковых растительных и пищевых материалов

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERT-COMPOST`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERT-COMPOST
- **parent_id:** [[TEC TD-FERTILIZERS|TD-FERTILIZERS]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Компост из известных низкорисковых растительных и пищевых материалов
- **outcome:** Convert known organics to a stable soil amendment without contaminating food or water
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_SITE_OR_FEEDSTOCK_PROTOCOL
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Only approved inputs; site drainage; temperature or maturation method; odor; vectors; final-use limits and records pass
- **calibration_reference:** Checked thermometer; known feedstock list; crop and pathogen guidance
- **drawings_bom_state:** MISSING_COMPOST_SITE_PLAN
- **localization_state:** PORTUGAL_BIOWASTE_WATER_AND_NEIGHBOR_RULES_REQUIRED
- **waste_storage:** Rejected contaminated input and leachate managed legally
- **stop_conditions:** Unknown material; meat or manure outside method; pests; leachate; fire heat; mold exposure; flooding
- **maintenance_spares:** Routine turning only if safe; moisture; cover; site inspection
- **successor_proof:** Преемник classifies inputs and rejects prohibited material
- **evidence_required:** Input log; temperature or time record; site inspection; use record
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No universal pile recipe; exact method must be sourced and localized
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
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
