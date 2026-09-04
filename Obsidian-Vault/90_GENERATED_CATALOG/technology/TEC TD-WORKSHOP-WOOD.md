---
id: "TD-WORKSHOP-WOOD"
kind: "technology"
title: "Низкорисковая работа с древесиной"
priority_tier: "P2_YELLOW"
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

# Низкорисковая работа с древесиной

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WORKSHOP-WOOD`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WORKSHOP-WOOD
- **parent_id:** [[TEC TD-WORKSHOP|TD-WORKSHOP]]
- **domain:** WORKSHOP
- **node_type:** PROCESS
- **title_ru:** Низкорисковая работа с древесиной
- **outcome:** Repair simple non-structural items using known dry material
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]], [[TEC TD-WORKSHOP-FIXTURES|TD-WORKSHOP-FIXTURES]], [[TEC TD-WORKSHOP-MEASURE|TD-WORKSHOP-MEASURE]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]]
- **source_package_ids:** [[PKG SUP-PHY-041|SUP-PHY-041]], [[PKG SUP-PHY-038|SUP-PHY-038]]
- **materials_tools_state:** MISSING_MATERIAL_AND_PACKAGES
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-003|INS-003]], [[INS INS-005|INS-005]], [[INS INS-006|INS-006]], [[INS INS-009|INS-009]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Part dimensions; moisture suitability; joints and safe service load meet exact package
- **calibration_reference:** Known samples; measurement checks; no structural rating without professional method
- **drawings_bom_state:** MISSING
- **localization_state:** PORTUGAL_MATERIAL_AND_BUILDING_RULES_REQUIRED
- **waste_storage:** Dust collection; finishes and treated wood separated
- **stop_conditions:** Treated or unknown wood; structural task; powered machinery without guard; fire
- **maintenance_spares:** Tool care; dry storage; standard fasteners
- **successor_proof:** Преемник builds one non-structural S1 item from released package
- **evidence_required:** Drawing; BOM; measurements; load test within safe limit
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Wood handbook is reference; not a construction approval
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P2_YELLOW
- **priority_horizon:** 15_TO_90_DAYS
- **earliest_service_level:** SL3
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P2_YELLOW
- **acquisition_priority:** P2_YELLOW
- **knowledge_priority:** P2_YELLOW
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES
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
| REQUIRED | [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-FIXTURES|TD-WORKSHOP-FIXTURES]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-MEASURE|TD-WORKSHOP-MEASURE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
