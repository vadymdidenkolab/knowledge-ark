---
id: "TD-SEED-BANK"
kind: "technology"
title: "Семенной банк с accession-level учётом"
priority_tier: "P2_YELLOW"
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

# Семенной банк с accession-level учётом

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-SEED-BANK`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-SEED-BANK
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** MATERIAL
- **title_ru:** Семенной банк с accession-level учётом
- **outcome:** Иметь несколько сортов; резерв пересева и offsite duplicate
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-FOOD-SITE|TD-FOOD-SITE]]
- **source_package_ids:** [[PKG SUP-LEA-021|SUP-LEA-021]], [[PKG SUP-LEA-022|SUP-LEA-022]], [[PKG SUP-LEA-024|SUP-LEA-024]], [[PKG SUP-LEA-025|SUP-LEA-025]]
- **materials_tools_state:** PLANNED_NOT_PURCHASED
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-036|INS-036]]
- **measurement_acceptance:** Каждый lot имеет сорт; OP/F1; год; источник; массу; storage; germination and legal notes
- **calibration_reference:** Blind seed count; scale check; germination controls
- **drawings_bom_state:** MISSING_ACCESSION_LABELS
- **localization_state:** PORTUGAL_SEED_RULES_REQUIRED
- **waste_storage:** Moldy or infested lots isolated and disposed safely
- **stop_conditions:** Unknown treatment; damaged package; invasive or regulated seed; mold
- **maintenance_spares:** Temperature/humidity log; periodic germination; duplicate rotation
- **successor_proof:** Преемник выбирает lot; тестирует и обновляет запись
- **evidence_required:** Invoices; labels; photos; mass; germination and location
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** HTML ordering model exists; no order or receipt evidence
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS
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
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-FOOD-SITE|TD-FOOD-SITE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
