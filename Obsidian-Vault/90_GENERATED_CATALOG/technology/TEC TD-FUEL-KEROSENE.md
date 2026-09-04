---
id: "TD-FUEL-KEROSENE"
kind: "technology"
title: "Керосин и реактивные средние дистилляты"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION"
safety_class: "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"
execution_gate: "BLACK_GATE_REFERENCE_ONLY"
status: "REFERENCE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Керосин и реактивные средние дистилляты

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-KEROSENE`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION`
- **Класс безопасности:** `S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD`
- **Допуск:** `BLACK_GATE_REFERENCE_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-KEROSENE
- **parent_id:** [[TEC TD-FUEL-PETROLEUM-REFINING|TD-FUEL-PETROLEUM-REFINING]]
- **domain:** ENERGY_FUELS
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Керосин и реактивные средние дистилляты
- **outcome:** Identify exact finished product and prevent substitution; vapor; indoor combustion and contamination harm
- **safety_class:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **execution_policy:** REFERENCE_ONLY_NO_BUILD
- **prerequisite_node_ids:** [[TEC TD-FUEL-PETROLEUM-REFINING|TD-FUEL-PETROLEUM-REFINING]], [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_PRODUCTION_DATA
- **instrument_ids:** не заполнено
- **measurement_acceptance:** No-build; exact label; certified appliance or engine approval; safe storage only
- **calibration_reference:** Product SDS and OEM specification
- **drawings_bom_state:** NO_REFINING_DRAWINGS
- **localization_state:** PORTUGAL_FUEL_AND_FIRE_RULES_REQUIRED
- **waste_storage:** Licensed disposal
- **stop_conditions:** Indoor combustion; CO; leak; wrong product; ingestion; water contamination
- **maintenance_spares:** Stock inspection; qualified appliance service
- **successor_proof:** Преемник refuses unapproved substitution and follows alarm response
- **evidence_required:** Boundary card; SDS; inventory; OEM refs
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** No household distillation or fractionation
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL1
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE
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
| HAZARD_ONLY | [[TEC TD-FUEL-PETROLEUM-REFINING|TD-FUEL-PETROLEUM-REFINING]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]] | SL5 | applicable_profile_site_or_qualified_role_required |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
