---
id: "TD-KNOWLEDGE-TOOLCHAINS"
kind: "technology"
title: "Открытые CAD; EDA; code and data toolchains"
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

# Открытые CAD; EDA; code and data toolchains

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-KNOWLEDGE-TOOLCHAINS`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-KNOWLEDGE-TOOLCHAINS
- **parent_id:** [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]]
- **domain:** KNOWLEDGE
- **node_type:** TOOL
- **title_ru:** Открытые CAD; EDA; code and data toolchains
- **outcome:** Edit drawings; rebuild software and migrate formats offline
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** [[PKG PSP-072|PSP-072]], [[PKG PSP-074|PSP-074]], [[PKG PSP-080|PSP-080]], [[PKG PSP-081|PSP-081]], [[PKG PSP-109|PSP-109]], [[PKG SUP-MDE-023|SUP-MDE-023]], [[PKG SUP-MDE-027|SUP-MDE-027]]
- **materials_tools_state:** NOT_DOWNLOADED
- **instrument_ids:** [[INS INS-065|INS-065]], [[INS INS-066|INS-066]]
- **measurement_acceptance:** Installer/source/dependencies build or launch offline on documented platform; sample project round-trip passes
- **calibration_reference:** Known sample project and reproducible hashes where possible
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** HARDWARE_OS_AND_LICENSE_REQUIRED
- **waste_storage:** Build artifacts and old dependencies quarantined
- **stop_conditions:** Untrusted package; unsigned binary; dependency gap; unsafe hardware output
- **maintenance_spares:** Version-pinned refresh and rebuild rehearsal
- **successor_proof:** Преемник edits and exports sample without network
- **evidence_required:** Source; installer; lockfiles; build log; sample output
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** A URL to FreeCAD or KiCad is not a toolchain
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
| REQUIRED | [[TEC TD-KNOWLEDGE-READERS|TD-KNOWLEDGE-READERS]] | SL2 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
