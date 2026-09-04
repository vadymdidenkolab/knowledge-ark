---
id: "TD-KNOWLEDGE"
kind: "technology"
title: "Офлайн-знания и вычисления"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY"
status: "ARCHITECTURE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Офлайн-знания и вычисления

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-KNOWLEDGE`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-KNOWLEDGE
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** KNOWLEDGE
- **node_type:** OUTCOME
- **title_ru:** Офлайн-знания и вычисления
- **outcome:** Read; search; verify; reproduce and migrate critical knowledge without network
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-KNOWLEDGE-CORPUS|TD-KNOWLEDGE-CORPUS]], [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]], [[TEC TD-KNOWLEDGE-INDEX|TD-KNOWLEDGE-INDEX]], [[TEC TD-KNOWLEDGE-RESTORE|TD-KNOWLEDGE-RESTORE]], [[TEC TD-KNOWLEDGE-TOOLCHAINS|TD-KNOWLEDGE-TOOLCHAINS]], [[TEC TD-KNOWLEDGE-FIXITY|TD-KNOWLEDGE-FIXITY]], [[TEC TD-KNOWLEDGE-COPIES|TD-KNOWLEDGE-COPIES]], [[TEC TD-KNOWLEDGE-MIGRATION|TD-KNOWLEDGE-MIGRATION]], [[TEC TD-KNOWLEDGE-SEARCH|TD-KNOWLEDGE-SEARCH]], [[TEC TD-KNOWLEDGE-PRINT-CORE|TD-KNOWLEDGE-PRINT-CORE]], [[TEC TD-KNOWLEDGE-SOURCE-CODE|TD-KNOWLEDGE-SOURCE-CODE]], [[TEC TD-KNOWLEDGE-COMPILERS|TD-KNOWLEDGE-COMPILERS]], [[TEC TD-KNOWLEDGE-GIS|TD-KNOWLEDGE-GIS]], [[TEC TD-KNOWLEDGE-EDA-CAD|TD-KNOWLEDGE-EDA-CAD]], [[TEC TD-KNOWLEDGE-HARDWARE|TD-KNOWLEDGE-HARDWARE]], [[TEC TD-KNOWLEDGE-READERS-SPARE|TD-KNOWLEDGE-READERS-SPARE]], [[TEC TD-KNOWLEDGE-PAPER-FALLBACK|TD-KNOWLEDGE-PAPER-FALLBACK]], [[TEC TD-KNOWLEDGE-LANGUAGE|TD-KNOWLEDGE-LANGUAGE]], [[TEC TD-KNOWLEDGE-RIGHTS|TD-KNOWLEDGE-RIGHTS]], [[TEC TD-KNOWLEDGE-SUCCESSOR|TD-KNOWLEDGE-SUCCESSOR]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** STARTER_CORPUS_IN_BUILD
- **instrument_ids:** [[INS INS-065|INS-065]], [[INS INS-066|INS-066]], [[INS INS-067|INS-067]], [[INS INS-068|INS-068]], [[INS INS-069|INS-069]], [[INS INS-070|INS-070]]
- **measurement_acceptance:** Released corpus opens; hashes pass; search and blank-device restore succeed
- **calibration_reference:** Two hash tools; known test vectors; independent media
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PUBLIC_PRIVATE_RIGHTS_SPLIT_REQUIRED
- **waste_storage:** Media and personal data disposed securely
- **stop_conditions:** Single device; rights unclear; corrupted file; no reader; unreviewed candidate mixed with released
- **maintenance_spares:** Full read; restore; migration rehearsal and refresh schedule
- **successor_proof:** Преемник restores and finds assigned procedures
- **evidence_required:** Payload manifest; rights; hashes; tests; restore logs
- **evidence_state:** LOCAL_UNREVIEWED
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** Current base kit is tiny architecture only
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-CORPUS|TD-KNOWLEDGE-CORPUS]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-INDEX|TD-KNOWLEDGE-INDEX]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-RESTORE|TD-KNOWLEDGE-RESTORE]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-TOOLCHAINS|TD-KNOWLEDGE-TOOLCHAINS]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-FIXITY|TD-KNOWLEDGE-FIXITY]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-COPIES|TD-KNOWLEDGE-COPIES]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-MIGRATION|TD-KNOWLEDGE-MIGRATION]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-SEARCH|TD-KNOWLEDGE-SEARCH]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-PRINT-CORE|TD-KNOWLEDGE-PRINT-CORE]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-SOURCE-CODE|TD-KNOWLEDGE-SOURCE-CODE]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-COMPILERS|TD-KNOWLEDGE-COMPILERS]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-GIS|TD-KNOWLEDGE-GIS]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-EDA-CAD|TD-KNOWLEDGE-EDA-CAD]] | SL4 | — |
| CONDITIONAL | [[TEC TD-KNOWLEDGE-HARDWARE|TD-KNOWLEDGE-HARDWARE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-KNOWLEDGE-READERS-SPARE|TD-KNOWLEDGE-READERS-SPARE]] | SL2 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-PAPER-FALLBACK|TD-KNOWLEDGE-PAPER-FALLBACK]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-LANGUAGE|TD-KNOWLEDGE-LANGUAGE]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-RIGHTS|TD-KNOWLEDGE-RIGHTS]] | SL4 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE-SUCCESSOR|TD-KNOWLEDGE-SUCCESSOR]] | SL4 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
