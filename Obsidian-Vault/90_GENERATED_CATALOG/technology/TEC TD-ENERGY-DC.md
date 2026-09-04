---
id: "TD-ENERGY-DC"
kind: "technology"
title: "Безопасная низковольтная DC архитектура"
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

# Безопасная низковольтная DC архитектура

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ENERGY-DC`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ENERGY-DC
- **parent_id:** [[TEC TD-ENERGY|TD-ENERGY]]
- **domain:** ENERGY
- **node_type:** DRAWING
- **title_ru:** Безопасная низковольтная DC архитектура
- **outcome:** Стандартизировать маломощные loads; connectors; fusing and labels
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_DESIGN
- **instrument_ids:** [[INS INS-003|INS-003]], [[INS INS-045|INS-045]], [[INS INS-046|INS-046]], [[INS INS-047|INS-047]], [[INS INS-048|INS-048]]
- **measurement_acceptance:** Voltage drop; current; polarity; fuse and thermal tests pass under reviewed load
- **calibration_reference:** Reference meter and known load; independent polarity check
- **drawings_bom_state:** MISSING_SCHEMATIC_BOM
- **localization_state:** EXACT_VOLTAGES_AND_SITE_REQUIRED
- **waste_storage:** Electronic waste and batteries separated
- **stop_conditions:** Unknown battery; overcurrent; hot connector; damaged insulation; mains coupling
- **maintenance_spares:** Connector inspection; fuse stock; cable and adapter spares
- **successor_proof:** Преемник assembles only low-energy approved branch and tests polarity
- **evidence_required:** Schematic; BOM; calculations; thermal test; review
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Does not authorize high-current battery construction
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
| REQUIRED | [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
