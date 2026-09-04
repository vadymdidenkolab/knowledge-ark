---
id: "TD-KNOWLEDGE-CORPUS"
kind: "technology"
title: "Локальный критический корпус"
priority_tier: "P1_ORANGE"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S0_OBSERVE_READ"
execution_gate: "DENY"
status: "ARCHITECTURE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Локальный критический корпус

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-KNOWLEDGE-CORPUS`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S0_OBSERVE_READ`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-KNOWLEDGE-CORPUS
- **parent_id:** [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]]
- **domain:** KNOWLEDGE
- **node_type:** KNOWLEDGE
- **title_ru:** Локальный критический корпус
- **outcome:** Materialize exact books; manuals; maps; drawings and datasets
- **safety_class:** S0_OBSERVE_READ
- **execution_policy:** HOUSEHOLD_S0
- **prerequisite_node_ids:** [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** STARTER_DOWNLOADS_CANDIDATE
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Every file has source; edition; rights; audience; local path; bytes; SHA-256; open and content-review states
- **calibration_reference:** Publisher provenance and optional upstream checksum
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_PLUS_GENERAL_SEPARATED
- **waste_storage:** Superseded and quarantined content separated
- **stop_conditions:** Rights unclear; executable unscanned; medical audience mismatch; stale law
- **maintenance_spares:** Per update class and annual manifest review
- **successor_proof:** Преемник distinguishes candidate from released
- **evidence_required:** Register; license evidence; hashes; review
- **evidence_state:** LOCAL_UNREVIEWED
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** Downloaded does not mean released
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
- **safety_lane:** S0_OBSERVE_READ
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
| REQUIRED | [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
