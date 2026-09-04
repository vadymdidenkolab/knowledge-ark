---
id: "TD-EXITS-SHUTOFFS"
kind: "technology"
title: "План выходов и штатных отключений"
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

# План выходов и штатных отключений

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-EXITS-SHUTOFFS`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-EXITS-SHUTOFFS
- **parent_id:** [[TEC TD-SHELTER|TD-SHELTER]]
- **domain:** SHELTER
- **node_type:** DRAWING
- **title_ru:** План выходов и штатных отключений
- **outcome:** Обеспечить безопасную эвакуацию и известные user-operable shutoffs
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_BUILDING_PLAN
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-040|INS-040]]
- **measurement_acceptance:** Два выхода где возможно; paths clear; labels visible; only user-authorized shutoffs identified
- **calibration_reference:** Walk-through and timed drill; no opening of panels or gas work
- **drawings_bom_state:** MISSING
- **localization_state:** HOUSEHOLD_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Smoke; gas; structural damage; blocked path; unauthorized shutoff
- **maintenance_spares:** Monthly clear-path check; semiannual drill
- **successor_proof:** Преемник exits in darkness simulation and points to safe controls
- **evidence_required:** Plan; photos; drill time; issues
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Map template has zero printed copies
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
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
