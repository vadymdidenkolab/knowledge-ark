---
id: "TD-HEALTH-PREVENTION"
kind: "technology"
title: "Профилактика; гигиена и наблюдение"
priority_tier: "P1_ORANGE"
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

# Профилактика; гигиена и наблюдение

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HEALTH-PREVENTION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HEALTH-PREVENTION
- **parent_id:** [[TEC TD-HEALTH|TD-HEALTH]]
- **domain:** HEALTH
- **node_type:** PROCESS
- **title_ru:** Профилактика; гигиена и наблюдение
- **outcome:** Reduce avoidable illness before advanced care is needed
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-WATER|TD-WATER]], [[TEC TD-FOOD|TD-FOOD]], [[TEC TD-SHELTER|TD-SHELTER]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[PKG SUP-LEA-027|SUP-LEA-027]], [[PKG SUP-LEA-030|SUP-LEA-030]]
- **materials_tools_state:** MISSING_PERSONAL_PLAN
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Clean water; hand hygiene; ventilation; nutrition; sleep and person-specific preventive plan logged
- **calibration_reference:** Validated devices and clinician/public-health guidance
- **drawings_bom_state:** MISSING_DAILY_CHECKLIST
- **localization_state:** GROUP_PROFILE_REQUIRED
- **waste_storage:** Household and medical waste separated
- **stop_conditions:** Outbreak; vulnerable person deterioration; unknown exposure
- **maintenance_spares:** Daily/weekly routines and scheduled care
- **successor_proof:** Преемник maintains routine and flags red signs
- **evidence_required:** Routine log; appointments; risk review
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No substitute for vaccination or professional care
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS
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
| REQUIRED | [[TEC TD-WATER|TD-WATER]] | SL3 | — |
| REQUIRED | [[TEC TD-FOOD|TD-FOOD]] | SL3 | — |
| REQUIRED | [[TEC TD-SHELTER|TD-SHELTER]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
