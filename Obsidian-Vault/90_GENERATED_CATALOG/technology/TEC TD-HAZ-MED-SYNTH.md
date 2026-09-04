---
id: "TD-HAZ-MED-SYNTH"
kind: "technology"
title: "Синтез лекарств; анестетиков и инъекций"
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

# Синтез лекарств; анестетиков и инъекций

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HAZ-MED-SYNTH`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION`
- **Класс безопасности:** `S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD`
- **Допуск:** `BLACK_GATE_REFERENCE_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HAZ-MED-SYNTH
- **parent_id:** [[TEC TD-HAZARDS|TD-HAZARDS]]
- **domain:** HAZARD
- **node_type:** HAZARD_BOUNDARY
- **title_ru:** Синтез лекарств; анестетиков и инъекций
- **outcome:** Block unregulated manufacture and route health needs safely
- **safety_class:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **execution_policy:** REFERENCE_ONLY_NO_BUILD
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-HEALTH-MEDS|TD-HEALTH-MEDS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_SYNTHESIS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Only legitimate medicine reconciliation; storage and professional supply routes
- **calibration_reference:** Licensed pharmacist or clinician
- **drawings_bom_state:** NO_RECIPES_NO_DRAWINGS
- **localization_state:** PORTUGAL_MEDICINE_LAW_REQUIRED
- **waste_storage:** Pharmacy return or regulated disposal
- **stop_conditions:** Unknown substance; counterfeit; expired or wrong-person medicine
- **maintenance_spares:** Inventory and expiry review
- **successor_proof:** Преемник refuses synthesis and follows patient plan
- **evidence_required:** Boundary card; medication plan; contacts
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** No compounding or injectable manufacture in household layer
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
- **capacity_model:** SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD
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
| CONDITIONAL | [[TEC TD-HEALTH-MEDS|TD-HEALTH-MEDS]] | SL1 | applicable_profile_site_or_qualified_role_required |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
