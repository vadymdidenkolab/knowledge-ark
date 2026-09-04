---
id: "TD-FERT-ASH"
kind: "technology"
title: "Зола как потенциальная почвенная добавка"
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

# Зола как потенциальная почвенная добавка

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERT-ASH`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERT-ASH
- **parent_id:** [[TEC TD-FERTILIZERS|TD-FERTILIZERS]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Зола как потенциальная почвенная добавка
- **outcome:** Determine whether clean source and measured soil need justify any use
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-FUEL-SOLID|TD-FUEL-SOLID]], [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_ASH_OR_SOIL_EVIDENCE
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-029|INS-029]], [[INS INS-033|INS-033]]
- **measurement_acceptance:** Only known untreated biomass ash; contaminant and pH risk reviewed; measured bounded application and crop response documented
- **calibration_reference:** Lab or qualified soil guidance; checked scale and area
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_WASTE_SOIL_AND_WATER_RULES_REQUIRED
- **waste_storage:** Unknown or contaminated ash disposed legally
- **stop_conditions:** Hot ash; treated wood; coal; trash; heavy metals; alkaline burn; runoff
- **maintenance_spares:** Dry sealed labeled storage; periodic soil review
- **successor_proof:** Преемник rejects unknown ash and documents decision
- **evidence_required:** Fuel provenance; ash analysis where needed; soil report; use log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Ash can harm soil and water; not a default fertilizer
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
| REQUIRED | [[TEC TD-FUEL-SOLID|TD-FUEL-SOLID]] | SL3 | — |
| REQUIRED | [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
