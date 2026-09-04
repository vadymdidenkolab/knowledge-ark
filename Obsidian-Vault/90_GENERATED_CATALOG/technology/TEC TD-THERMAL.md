---
id: "TD-THERMAL"
kind: "technology"
title: "Безопасный тепловой режим"
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

# Безопасный тепловой режим

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-THERMAL`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-THERMAL
- **parent_id:** [[TEC TD-SHELTER|TD-SHELTER]]
- **domain:** SHELTER
- **node_type:** OUTCOME
- **title_ru:** Безопасный тепловой режим
- **outcome:** Поддержать допустимую температуру для людей; лекарств; воды and food
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_HEAT_BALANCE
- **instrument_ids:** [[INS INS-013|INS-013]], [[INS INS-014|INS-014]], [[INS INS-015|INS-015]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Measured temperature and humidity stay within person-specific and asset limits through test period
- **calibration_reference:** Two-point thermometer comparison; independent non-combustion fallback
- **drawings_bom_state:** MISSING_ZONE_PLAN
- **localization_state:** GROUP_AND_CLIMATE_REQUIRED
- **waste_storage:** Fuel and heating waste only by approved system
- **stop_conditions:** CO; fire; overheating; hypothermia; medical vulnerability; damaged heater
- **maintenance_spares:** Seasonal test; spare blankets; seals; shading
- **successor_proof:** Преемник establishes warm or cool room and records limits
- **evidence_required:** Load test; temperatures; energy use; alarms
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No combustion in living volume
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
| REQUIRED | [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
