---
id: "TD-CROP-TRIAL"
kind: "technology"
title: "Полевые испытания культур"
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

# Полевые испытания культур

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-CROP-TRIAL`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-CROP-TRIAL
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Полевые испытания культур
- **outcome:** Проверить сорта на реальном участке до зависимости от них
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-CROP-PLAN|TD-CROP-PLAN]], [[TEC TD-GERMINATION|TD-GERMINATION]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_TRIALS
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-020|INS-020]], [[INS INS-035|INS-035]], [[INS INS-037|INS-037]]
- **measurement_acceptance:** Replicated plots; inputs; yield; losses and quality logged over multiple seasons
- **calibration_reference:** Area grid; scale; known count; weather cross-check
- **drawings_bom_state:** MISSING_PLOT_MAP
- **localization_state:** PORTUGAL_SITE_REQUIRED
- **waste_storage:** Diseased plants isolated according to local guidance
- **stop_conditions:** Unknown disease; protected organism; pesticide need beyond label
- **maintenance_spares:** At each trial and season
- **successor_proof:** Преемник repeats one trial without changing criteria
- **evidence_required:** Plot map; raw log; harvest weights; photos; review
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Один удачный сезон не доказывает устойчивость
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
| REQUIRED | [[TEC TD-CROP-PLAN|TD-CROP-PLAN]] | SL3 | — |
| REQUIRED | [[TEC TD-GERMINATION|TD-GERMINATION]] | SL4 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
