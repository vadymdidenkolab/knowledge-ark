---
id: "TD-WORKSHOP-MEASURE"
kind: "technology"
title: "Размерный и угловой контроль"
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

# Размерный и угловой контроль

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WORKSHOP-MEASURE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WORKSHOP-MEASURE
- **parent_id:** [[TEC TD-WORKSHOP|TD-WORKSHOP]]
- **domain:** WORKSHOP
- **node_type:** INSTRUMENT
- **title_ru:** Размерный и угловой контроль
- **outcome:** Transfer dimensions and identify out-of-tolerance parts
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]], [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** INSTRUMENTS_MISSING
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-003|INS-003]], [[INS INS-004|INS-004]], [[INS INS-005|INS-005]], [[INS INS-006|INS-006]], [[INS INS-007|INS-007]], [[INS INS-059|INS-059]], [[INS INS-060|INS-060]]
- **measurement_acceptance:** Gauge R&R appropriate to task; control points pass; unit and uncertainty recorded
- **calibration_reference:** Gauge blocks or documented reference; zero and reversal checks
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** TASK_SPECIFIC_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Dirty jaws; burr; drop; failed zero; out-of-range
- **maintenance_spares:** Clean; protect; periodic comparison
- **successor_proof:** Преемник measures blind part and reaches same decision
- **evidence_required:** Instrument IDs; checks; raw readings; decision
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Resolution is not accuracy
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
- **capacity_model:** JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES
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
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
