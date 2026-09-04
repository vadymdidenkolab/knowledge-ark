---
id: "TD-HAZARDS"
kind: "technology"
title: "Опасные технологии только как границы"
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

# Опасные технологии только как границы

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HAZARDS`
- **Статус:** `REFERENCE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION`
- **Класс безопасности:** `S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD`
- **Допуск:** `BLACK_GATE_REFERENCE_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HAZARDS
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** HAZARD
- **node_type:** OUTCOME
- **title_ru:** Опасные технологии только как границы
- **outcome:** Recognize; isolate; evacuate and obtain competent help without household fabrication
- **safety_class:** S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD
- **execution_policy:** REFERENCE_ONLY_NO_BUILD
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[SAFE SG-01|SG-01]], [[SAFE SG-02|SG-02]], [[SAFE SG-03|SG-03]], [[SAFE SG-04|SG-04]], [[SAFE SG-05|SG-05]], [[SAFE SG-06|SG-06]], [[SAFE SG-07|SG-07]], [[SAFE SG-08|SG-08]], [[SAFE SG-09|SG-09]], [[SAFE SG-10|SG-10]], [[SAFE SG-11|SG-11]], [[SAFE SG-12|SG-12]], [[SAFE SG-13|SG-13]], [[SAFE SG-14|SG-14]], [[SAFE SG-15|SG-15]], [[SAFE SG-16|SG-16]], [[SAFE SG-17|SG-17]]
- **materials_tools_state:** NO_BUILD_MATERIALS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Recognition and emergency route are documented; no synthesis or build steps exist
- **calibration_reference:** Official hazard labels; SDS; emergency authority sources
- **drawings_bom_state:** NO_BUILD_DRAWINGS
- **localization_state:** PORTUGAL_EMERGENCY_AND_WASTE_ROUTES_REQUIRED
- **waste_storage:** Competent legal disposal only
- **stop_conditions:** Any contact; mixing; heating; pressure; unknown identity or damaged container
- **maintenance_spares:** Review labels and emergency contacts
- **successor_proof:** Преемник chooses distance; isolation and 112 rather than experimenting
- **evidence_required:** Boundary card; source; drill without material
- **evidence_state:** BOUNDARY_DEFINED
- **capability_status:** REFERENCE_ONLY
- **release_gate:** REFERENCE_ONLY
- **notes:** Permanent no-build parent
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

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
