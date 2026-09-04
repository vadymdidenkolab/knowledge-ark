---
id: "TD-NAVIGATION"
kind: "technology"
title: "Карта; компас; GNSS и нивелирование"
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

# Карта; компас; GNSS и нивелирование

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-NAVIGATION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-NAVIGATION
- **parent_id:** [[TEC TD-MAPS-COMMS|TD-MAPS-COMMS]]
- **domain:** MAPS_COMMS
- **node_type:** TRAINING
- **title_ru:** Карта; компас; GNSS и нивелирование
- **outcome:** Maintain position and direction with independent methods
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-MAPS|TD-MAPS]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** [[PKG PSP-003|PSP-003]]
- **materials_tools_state:** INSTRUMENTS_MISSING
- **instrument_ids:** [[INS INS-061|INS-061]], [[INS INS-062|INS-062]], [[INS INS-063|INS-063]], [[INS INS-064|INS-064]]
- **measurement_acceptance:** Known-course error; closure and repeatability meet task criterion
- **calibration_reference:** Known baseline; control points; declination date; two-peg test where applicable
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** LOCAL_DECLINATION_AND_CRS_REQUIRED
- **waste_storage:** Not applicable
- **stop_conditions:** Laser misuse; unsafe terrain; GPS-only decision; magnetic interference
- **maintenance_spares:** Before trip and scheduled instrument checks
- **successor_proof:** Преемник navigates without GPS and explains uncertainty
- **evidence_required:** Course log; control points; error; evaluator
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Laser and surveying have separate safety boundaries
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
- **capacity_model:** PEOPLE_CHANNELS_COVERAGE_CHECKIN_AND_ROUTE_TIME
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
| REQUIRED | [[TEC TD-MAPS|TD-MAPS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
