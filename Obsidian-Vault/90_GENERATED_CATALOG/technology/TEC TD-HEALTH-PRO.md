---
id: "TD-HEALTH-PRO"
kind: "technology"
title: "Профессиональная медицинская полка"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LICENSED_PROFESSIONAL"
safety_class: "S3_LICENSED_PROFESSIONAL"
execution_gate: "BLACK_GATE_LICENSED_ONLY"
status: "ARCHITECTURE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Профессиональная медицинская полка

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HEALTH-PRO`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HEALTH-PRO
- **parent_id:** [[TEC TD-HEALTH|TD-HEALTH]]
- **domain:** HEALTH
- **node_type:** KNOWLEDGE
- **title_ru:** Профессиональная медицинская полка
- **outcome:** Preserve clinician reference for qualified personnel in resource-limited settings
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[SRC SRC-WHO-BEC|SRC-WHO-BEC]], [[PKG PSP-055|PSP-055]], [[PKG PSP-056|PSP-056]]
- **materials_tools_state:** STARTER_FILES_CANDIDATE
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Exact editions open offline; audience and section boundaries preserved
- **calibration_reference:** Publisher provenance and hash
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** CLINICIAN_SCOPE_AND_PORTUGAL_REQUIRED
- **waste_storage:** Not applicable
- **stop_conditions:** Unqualified user; obsolete guideline; missing equipment; no infection control
- **maintenance_spares:** Scheduled guideline review
- **successor_proof:** Qualified person retrieves source and documents limits
- **evidence_required:** Files; hashes; rights; content review; credentials
- **evidence_state:** LOCAL_UNREVIEWED
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** Reference availability is not permission to treat
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL1
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S3_LICENSED_PROFESSIONAL
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS
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

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
