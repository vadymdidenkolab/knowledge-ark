---
id: "TD-MAPS-COMMS"
kind: "technology"
title: "Карты; навигация; время и связь"
priority_tier: "P1_ORANGE"
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

# Карты; навигация; время и связь

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-MAPS-COMMS`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-MAPS-COMMS
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** MAPS_COMMS
- **node_type:** OUTCOME
- **title_ru:** Карты; навигация; время и связь
- **outcome:** Navigate and exchange verified short information without internet or GPS dependence
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-MAPS|TD-MAPS]], [[TEC TD-ROUTES|TD-ROUTES]], [[TEC TD-NAVIGATION|TD-NAVIGATION]], [[TEC TD-COMMS-RECEIVE|TD-COMMS-RECEIVE]], [[TEC TD-COMMS-PACE|TD-COMMS-PACE]], [[TEC TD-TIME|TD-TIME]], [[TEC TD-COMMS-CONTACTS-PAPER|TD-COMMS-CONTACTS-PAPER]], [[TEC TD-COMMS-WARNINGS|TD-COMMS-WARNINGS]], [[TEC TD-COMMS-CHECKIN|TD-COMMS-CHECKIN]], [[TEC TD-COMMS-MISSED|TD-COMMS-MISSED]], [[TEC TD-COMMS-ACCOUNTABILITY|TD-COMMS-ACCOUNTABILITY]], [[TEC TD-COMMS-REUNION|TD-COMMS-REUNION]], [[TEC TD-COMMS-LOCAL-SIGNAL|TD-COMMS-LOCAL-SIGNAL]], [[TEC TD-COMMS-MESSAGE|TD-COMMS-MESSAGE]], [[TEC TD-COMMS-LOG|TD-COMMS-LOG]], [[TEC TD-COMMS-BUILDING-MAP|TD-COMMS-BUILDING-MAP]], [[TEC TD-COMMS-LOCAL-MAP|TD-COMMS-LOCAL-MAP]], [[TEC TD-COMMS-SERVICE-POINTS|TD-COMMS-SERVICE-POINTS]], [[TEC TD-COMMS-HAZARD-MAP|TD-COMMS-HAZARD-MAP]], [[TEC TD-COMMS-R1-R3|TD-COMMS-R1-R3]], [[TEC TD-COMMS-SLOWEST|TD-COMMS-SLOWEST]], [[TEC TD-COMMS-PRIVACY|TD-COMMS-PRIVACY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_MAPS_RADIOS_AND_DRILLS
- **instrument_ids:** [[INS INS-011|INS-011]], [[INS INS-012|INS-012]], [[INS INS-061|INS-061]], [[INS INS-062|INS-062]], [[INS INS-063|INS-063]], [[INS INS-064|INS-064]]
- **measurement_acceptance:** Offline and paper routes; message delivery and independent time checks pass
- **calibration_reference:** Known control points; multiple time sources; field verification
- **drawings_bom_state:** MISSING_MAP_PACK
- **localization_state:** PORTUGAL_ADDRESS_REQUIRED
- **waste_storage:** Batteries and print waste handled
- **stop_conditions:** Active hazard; closed route; radio illegality; stale map; GPS disagreement
- **maintenance_spares:** Quarterly checks and after event
- **successor_proof:** Преемник navigates route and sends structured message
- **evidence_required:** Maps; hashes; print; field log; comms log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Current map register has zero actual files
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-MAPS|TD-MAPS]] | SL2 | — |
| REQUIRED | [[TEC TD-ROUTES|TD-ROUTES]] | SL2 | — |
| REQUIRED | [[TEC TD-NAVIGATION|TD-NAVIGATION]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-RECEIVE|TD-COMMS-RECEIVE]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-PACE|TD-COMMS-PACE]] | SL2 | — |
| REQUIRED | [[TEC TD-TIME|TD-TIME]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-CONTACTS-PAPER|TD-COMMS-CONTACTS-PAPER]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-WARNINGS|TD-COMMS-WARNINGS]] | SL0 | — |
| REQUIRED | [[TEC TD-COMMS-CHECKIN|TD-COMMS-CHECKIN]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-MISSED|TD-COMMS-MISSED]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-ACCOUNTABILITY|TD-COMMS-ACCOUNTABILITY]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-REUNION|TD-COMMS-REUNION]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-LOCAL-SIGNAL|TD-COMMS-LOCAL-SIGNAL]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-MESSAGE|TD-COMMS-MESSAGE]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-LOG|TD-COMMS-LOG]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-BUILDING-MAP|TD-COMMS-BUILDING-MAP]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-LOCAL-MAP|TD-COMMS-LOCAL-MAP]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-SERVICE-POINTS|TD-COMMS-SERVICE-POINTS]] | SL1 | — |
| REQUIRED | [[TEC TD-COMMS-HAZARD-MAP|TD-COMMS-HAZARD-MAP]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-R1-R3|TD-COMMS-R1-R3]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-SLOWEST|TD-COMMS-SLOWEST]] | SL2 | — |
| REQUIRED | [[TEC TD-COMMS-PRIVACY|TD-COMMS-PRIVACY]] | SL2 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
