---
id: "TD-DRAINAGE"
kind: "technology"
title: "Кровля; водоотвод и влагозащита"
priority_tier: "P3_GREEN"
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

# Кровля; водоотвод и влагозащита

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-DRAINAGE`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-DRAINAGE
- **parent_id:** [[TEC TD-SHELTER|TD-SHELTER]]
- **domain:** SHELTER
- **node_type:** MAINTENANCE
- **title_ru:** Кровля; водоотвод и влагозащита
- **outcome:** Не допустить разрушения и плесени из-за воды
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_ROOF_AND_DRAIN_ASSESSMENT
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-006|INS-006]], [[INS INS-040|INS-040]]
- **measurement_acceptance:** Safe visual inspection; flow path; defects and maintenance plan documented
- **calibration_reference:** Known level/reversal check; professional roof or structural review
- **drawings_bom_state:** MISSING_DRAINAGE_PLAN
- **localization_state:** SITE_AND_RAINFALL_REQUIRED
- **waste_storage:** Debris and contaminated materials routed safely
- **stop_conditions:** Height; live electrical; structural damage; asbestos; storm conditions
- **maintenance_spares:** Before rainy season and after storm
- **successor_proof:** Преемник inspects from safe location and escalates defects
- **evidence_required:** Photos; plan; work orders; post-rain check
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No roof climbing in household layer
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL4
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME
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
| CONDITIONAL | [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
