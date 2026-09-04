---
id: "TD-VENTILATION"
kind: "technology"
title: "Вентиляция и качество воздуха"
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

# Вентиляция и качество воздуха

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-VENTILATION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-VENTILATION
- **parent_id:** [[TEC TD-SHELTER|TD-SHELTER]]
- **domain:** SHELTER
- **node_type:** PROCESS
- **title_ru:** Вентиляция и качество воздуха
- **outcome:** Управлять влагой; CO2; particles and heat without introducing smoke or contaminants
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_AIRFLOW_ASSESSMENT
- **instrument_ids:** [[INS INS-017|INS-017]], [[INS INS-019|INS-019]], [[INS INS-023|INS-023]], [[INS INS-025|INS-025]]
- **measurement_acceptance:** Room-specific airflow strategy; measurements; outdoor-air conditions and stop criteria recorded
- **calibration_reference:** Co-location checks; professional assessment where combustion or code applies
- **drawings_bom_state:** MISSING_AIRFLOW_DIAGRAM
- **localization_state:** PORTUGAL_BUILDING_REQUIRED
- **waste_storage:** Filter disposal by contamination class
- **stop_conditions:** CO alarm; outdoor smoke; chemical release; mold; unsafe opening
- **maintenance_spares:** Filter schedule; seasonal modes; fan spares
- **successor_proof:** Преемник selects safe mode for three scenarios
- **evidence_required:** Measurements; plan; maintenance; drill
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** CO2 monitor is not full air-safety proof
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
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
