---
id: "TD-WORKSHOP-SALVAGE"
kind: "technology"
title: "Безопасный разбор доноров и повторное использование"
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

# Безопасный разбор доноров и повторное использование

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WORKSHOP-SALVAGE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WORKSHOP-SALVAGE
- **parent_id:** [[TEC TD-WORKSHOP|TD-WORKSHOP]]
- **domain:** WORKSHOP
- **node_type:** PROCESS
- **title_ru:** Безопасный разбор доноров и повторное использование
- **outcome:** Recover known standard parts without importing hidden hazards
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_DONOR_PROTOCOL
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-003|INS-003]], [[INS INS-040|INS-040]], [[INS INS-045|INS-045]]
- **measurement_acceptance:** Part identity; condition; dimensions and safe application verified before stock
- **calibration_reference:** Known part datasheet and comparison sample
- **drawings_bom_state:** MISSING_PART_MAP
- **localization_state:** WASTE_AND_OWNERSHIP_RULES_REQUIRED
- **waste_storage:** Unknown and hazardous parts routed to licensed waste
- **stop_conditions:** Lithium; capacitors; CRT; pressure; refrigerant; asbestos; contamination; stolen property
- **maintenance_spares:** Quarantine; periodic stock review
- **successor_proof:** Преемник rejects unsafe donor examples
- **evidence_required:** Provenance; photos; test; quarantine record
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Salvage is not permission to dismantle hazardous systems
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
