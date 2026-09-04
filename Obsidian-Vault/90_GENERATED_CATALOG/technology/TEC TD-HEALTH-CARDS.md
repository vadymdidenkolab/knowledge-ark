---
id: "TD-HEALTH-CARDS"
kind: "technology"
title: "Краткие action cards"
priority_tier: "P0_RED"
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

# Краткие action cards

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HEALTH-CARDS`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HEALTH-CARDS
- **parent_id:** [[TEC TD-HEALTH|TD-HEALTH]]
- **domain:** HEALTH
- **node_type:** KNOWLEDGE
- **title_ru:** Краткие action cards
- **outcome:** Retrieve safe first actions in seconds without mixing audiences
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-HEALTH-FIRSTAID|TD-HEALTH-FIRSTAID]], [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]]
- **source_package_ids:** [[SRC SRC-IFRC-FIRST-AID-2025|SRC-IFRC-FIRST-AID-2025]], [[SRC SRC-ERC-FA-2025|SRC-ERC-FA-2025]]
- **materials_tools_state:** NO_RELEASED_CARDS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Each card has audience; source section; version; 112; stop and review; professional approval
- **calibration_reference:** Cross-check against exact current protocol
- **drawings_bom_state:** MISSING_CARD_LAYOUT
- **localization_state:** PORTUGAL_AND_LANGUAGE_REQUIRED
- **waste_storage:** Old cards superseded; not silently overwritten
- **stop_conditions:** Conflicting guideline system; expired review; untrained intervention
- **maintenance_spares:** Review after guideline change and at least annually
- **successor_proof:** User finds correct card in timed drill
- **evidence_required:** Card; provenance; reviewer; drill time
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** 133 scenarios are index only
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
- **safety_lane:** S2_TRAINED_SUPERVISED
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
| REQUIRED | [[TEC TD-HEALTH-FIRSTAID|TD-HEALTH-FIRSTAID]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
