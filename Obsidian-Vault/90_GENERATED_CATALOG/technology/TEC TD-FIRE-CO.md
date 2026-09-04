---
id: "TD-FIRE-CO"
kind: "technology"
title: "Пожар; дым и CO detection"
priority_tier: "P0_RED"
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

# Пожар; дым и CO detection

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FIRE-CO`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FIRE-CO
- **parent_id:** [[TEC TD-SHELTER|TD-SHELTER]]
- **domain:** SHELTER
- **node_type:** OUTCOME
- **title_ru:** Пожар; дым и CO detection
- **outcome:** Получить раннее предупреждение и выйти без поиска источника в опасной зоне
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** DETECTORS_MISSING
- **instrument_ids:** [[INS INS-024|INS-024]], [[INS INS-071|INS-071]]
- **measurement_acceptance:** Certified exact models; siting by manual; test button; dates; audible coverage and drill pass
- **calibration_reference:** Manufacturer test only; replacement date; independent alarm path
- **drawings_bom_state:** MISSING_SITING_PLAN
- **localization_state:** PORTUGAL_RULES_AND_BUILDING_REQUIRED
- **waste_storage:** Expired detectors and batteries handled safely
- **stop_conditions:** Alarm; smoke; symptoms; heat; unknown combustion source
- **maintenance_spares:** Test by manual; replacement by date; spare batteries if allowed
- **successor_proof:** Преемник reacts; evacuates; calls 112 and does not investigate
- **evidence_required:** Model manuals; install photos; tests; drill
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** CO example remains planned
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL0
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
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
| CONDITIONAL | [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
