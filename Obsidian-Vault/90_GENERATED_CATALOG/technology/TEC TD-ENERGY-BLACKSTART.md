---
id: "TD-ENERGY-BLACKSTART"
kind: "technology"
title: "Black start и безопасное отключение"
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

# Black start и безопасное отключение

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ENERGY-BLACKSTART`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ENERGY-BLACKSTART
- **parent_id:** [[TEC TD-ENERGY|TD-ENERGY]]
- **domain:** ENERGY
- **node_type:** PROCESS
- **title_ru:** Black start и безопасное отключение
- **outcome:** Restore critical loads from zero without internet or original installer
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-ENERGY-PROTECTION|TD-ENERGY-PROTECTION]], [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_TEST
- **instrument_ids:** [[INS INS-011|INS-011]], [[INS INS-047|INS-047]], [[INS INS-052|INS-052]]
- **measurement_acceptance:** Cold start; priority sequence; runtime; shutdown and fault handling pass
- **calibration_reference:** Known clock; energy meter; prewritten acceptance
- **drawings_bom_state:** MISSING_ACTION_CARD
- **localization_state:** EXACT_SYSTEM_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Alarm; heat; smoke; abnormal voltage; failed isolation
- **maintenance_spares:** Quarterly or per risk; keep paper card and spares
- **successor_proof:** Authorized successor completes drill without author
- **evidence_required:** Timed drill; energy log; faults; corrective actions
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No system exists to test
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
- **capacity_model:** WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME
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
| CONDITIONAL | [[TEC TD-ENERGY-PROTECTION|TD-ENERGY-PROTECTION]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
