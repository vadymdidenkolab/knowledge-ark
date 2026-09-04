---
id: "TD-KNOWLEDGE-RESTORE"
kind: "technology"
title: "Blank-device restore"
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

# Blank-device restore

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-KNOWLEDGE-RESTORE`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-KNOWLEDGE-RESTORE
- **parent_id:** [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]]
- **domain:** KNOWLEDGE
- **node_type:** TEST
- **title_ru:** Blank-device restore
- **outcome:** Prove archive survival beyond current computer
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-KNOWLEDGE-CORPUS|TD-KNOWLEDGE-CORPUS]], [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]], [[TEC TD-KNOWLEDGE-INDEX|TD-KNOWLEDGE-INDEX]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_MEDIA_OR_TEST
- **instrument_ids:** [[INS INS-011|INS-011]], [[INS INS-065|INS-065]], [[INS INS-069|INS-069]]
- **measurement_acceptance:** Network disabled; different person; clean device; manifests; readers; index and samples pass within measured RTO
- **calibration_reference:** Previously recorded hashes and independent tool
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** OFFSITE_AND_PRIVATE_KEYS_REQUIRED
- **waste_storage:** Secure wipe only when authorized; preserve failed media evidence
- **stop_conditions:** Only one copy; lost key; reader absent; hash mismatch
- **maintenance_spares:** Annual and after media migration
- **successor_proof:** Преемник completes restore without author
- **evidence_required:** Full log; RTO; power used; errors; signatures
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No physical media records exist
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
| REQUIRED | [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-INDEX|TD-KNOWLEDGE-INDEX]] | SL2 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
