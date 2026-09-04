---
id: "TD-WORKSHOP-FIXTURES"
kind: "technology"
title: "Верстак; тиски и безопасная оснастка"
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

# Верстак; тиски и безопасная оснастка

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WORKSHOP-FIXTURES`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WORKSHOP-FIXTURES
- **parent_id:** [[TEC TD-WORKSHOP|TD-WORKSHOP]]
- **domain:** WORKSHOP
- **node_type:** TOOL
- **title_ru:** Верстак; тиски и безопасная оснастка
- **outcome:** Secure work and keep hands away from cutting path
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]], [[TEC TD-BASE-SITE|TD-BASE-SITE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_BENCH
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-005|INS-005]], [[INS INS-006|INS-006]]
- **measurement_acceptance:** Stability; clamping; load within reviewed limit; clear egress and lighting pass
- **calibration_reference:** Level reversal; known test workpiece; no unreviewed structural anchoring
- **drawings_bom_state:** MISSING_BENCH_DRAWING
- **localization_state:** WORKSPACE_REQUIRED
- **waste_storage:** Dust and swarf collection
- **stop_conditions:** Instability; pinch point; excessive load; structural anchoring uncertainty
- **maintenance_spares:** Periodic fastener and surface inspection
- **successor_proof:** Преемник sets up one safe workholding task
- **evidence_required:** Drawing; BOM; load assumption; inspection
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Heavy load and stored-energy work remain specialist
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
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
