---
id: "TD-FUEL-ENGINE-COMPAT"
kind: "technology"
title: "Совместимость топлива с двигателем или горелкой"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LICENSED_PROFESSIONAL"
safety_class: "S3_LICENSED_PROFESSIONAL"
execution_gate: "BLACK_GATE_LICENSED_ONLY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Совместимость топлива с двигателем или горелкой

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-ENGINE-COMPAT`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-ENGINE-COMPAT
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** TEST
- **title_ru:** Совместимость топлива с двигателем или горелкой
- **outcome:** Prevent damage; fire; emissions and unsafe improvisation from alternative fuel
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]], [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_ENGINE_OR_FUEL_TEST
- **instrument_ids:** [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-023|INS-023]], [[INS INS-024|INS-024]], [[INS INS-045|INS-045]]
- **measurement_acceptance:** OEM or qualified conversion approval; materials compatibility; emissions; thermal and shutdown tests pass
- **calibration_reference:** Calibrated professional instruments and manufacturer data
- **drawings_bom_state:** MISSING_ASSET_SCHEMATIC
- **localization_state:** PORTUGAL_VEHICLE_EMISSIONS_FIRE_AND_TAX_RULES_REQUIRED
- **waste_storage:** Fuel; filters; oils and contaminated parts use licensed routes
- **stop_conditions:** Wrong fuel; leak; knock; overheating; smoke; CO; warranty or legal noncompliance
- **maintenance_spares:** Qualified service; filters; seals; injectors; safe standard-fuel fallback
- **successor_proof:** Qualified successor performs only authorized inspection and shutdown
- **evidence_required:** Approval; test report; emissions; service records
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No direct vegetable-oil; homemade-fuel or improvised burner instructions
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL5
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S3_LICENSED_PROFESSIONAL
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE
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
| CONDITIONAL | [[TEC TD-FUEL-STORAGE|TD-FUEL-STORAGE]] | SL5 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]] | SL3 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
