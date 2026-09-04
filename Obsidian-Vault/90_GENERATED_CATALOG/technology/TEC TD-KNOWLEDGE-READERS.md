---
id: "TD-KNOWLEDGE-READERS"
kind: "technology"
title: "Офлайн readers и установщики"
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

# Офлайн readers и установщики

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-KNOWLEDGE-READERS`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-KNOWLEDGE-READERS
- **parent_id:** [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]]
- **domain:** KNOWLEDGE
- **node_type:** TOOL
- **title_ru:** Офлайн readers и установщики
- **outcome:** Open PDF; ZIM; EPUB; GIS; CAD and common archives without app store
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-KNOWLEDGE-CORPUS|TD-KNOWLEDGE-CORPUS]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** READERS_MISSING_OR_UNTESTED
- **instrument_ids:** [[INS INS-065|INS-065]]
- **measurement_acceptance:** Each critical format opens on primary and backup device; installer hash and license stored
- **calibration_reference:** Known sample files; OS and architecture recorded
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** ACTUAL_HARDWARE_AND_OS_REQUIRED
- **waste_storage:** Old executables quarantined rather than silently run
- **stop_conditions:** Unsigned executable; incompatible architecture; no clean device
- **maintenance_spares:** Annual offline launch and after OS change
- **successor_proof:** Преемник installs on clean backup and opens samples
- **evidence_required:** Installers; source; signatures; launch log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Kiwix reader candidate must be tested; DMG alone is not capability
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
- **capacity_model:** BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES
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
| REQUIRED | [[TEC TD-KNOWLEDGE-CORPUS|TD-KNOWLEDGE-CORPUS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
