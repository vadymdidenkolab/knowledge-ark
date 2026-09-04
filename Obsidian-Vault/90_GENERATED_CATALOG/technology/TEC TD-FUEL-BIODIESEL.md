---
id: "TD-FUEL-BIODIESEL"
kind: "technology"
title: "Биодизель и переэтерификация"
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

# Биодизель и переэтерификация

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-BIODIESEL`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION`
- **Класс безопасности:** `S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD`
- **Допуск:** `BLACK_GATE_REFERENCE_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-BIODIESEL
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Биодизель и переэтерификация
- **outcome:** Preserve industrial overview while blocking toxic; caustic and flammable home processing
- **safety_class:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **execution_policy:** REFERENCE_ONLY_NO_BUILD
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-FUEL-ENGINE-COMPAT|TD-FUEL-ENGINE-COMPAT]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_CHEMICAL_PROCESS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** No-build; finished certified product identification and compatibility only
- **calibration_reference:** Qualified chemical process; fuel standard and OEM sources
- **drawings_bom_state:** NO_REACTOR_OR_PROCESS_DRAWINGS
- **localization_state:** PORTUGAL_CHEMICAL_FUEL_ENVIRONMENT_AND_TAX_RULES_REQUIRED
- **waste_storage:** Licensed methanol; catalyst; glycerol and wash-waste routes
- **stop_conditions:** Methanol; caustic; vapor; heat; pressure; wrong fuel; contaminated wash water
- **maintenance_spares:** Industrial process controls only
- **successor_proof:** Преемник refuses home reaction and checks certified product standard
- **evidence_required:** Boundary card; professional sources; OEM compatibility
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** No proportions; reaction conditions; washing or quality shortcuts
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| CONDITIONAL | [[TEC TD-FUEL-ENGINE-COMPAT|TD-FUEL-ENGINE-COMPAT]] | SL5 | applicable_profile_site_or_qualified_role_required |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
