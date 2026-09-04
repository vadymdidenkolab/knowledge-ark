---
id: "TD-SEED-REGEN"
kind: "technology"
title: "Получение следующего поколения семян"
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

# Получение следующего поколения семян

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-SEED-REGEN`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-SEED-REGEN
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Получение следующего поколения семян
- **outcome:** Сохранять сортовые признаки и достаточную популяцию
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-CROP-TRIAL|TD-CROP-TRIAL]], [[TEC TD-SEED-BANK|TD-SEED-BANK]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]]
- **source_package_ids:** [[PKG SUP-LEA-021|SUP-LEA-021]], [[PKG SUP-LEA-025|SUP-LEA-025]]
- **materials_tools_state:** MISSING_CROP_SPECIFIC_PROTOCOL
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-036|INS-036]]
- **measurement_acceptance:** Crop-specific isolation; population; selection; drying; storage and germination criteria pass
- **calibration_reference:** Known parent lot; germination control; moisture method
- **drawings_bom_state:** MISSING_CROP_SPECIFIC_DIAGRAM
- **localization_state:** PORTUGAL_SEED_AND_BIOSECURITY_REQUIRED
- **waste_storage:** Diseased or unknown material excluded from exchange
- **stop_conditions:** Hybrid or unknown parentage; disease; inadequate population; wet seed
- **maintenance_spares:** Each generation and storage interval
- **successor_proof:** Преемник produces and tests one accession
- **evidence_required:** Field lineage; isolation; counts; mass; moisture; germination
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Open-pollinated label alone is insufficient
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
| REQUIRED | [[TEC TD-CROP-TRIAL|TD-CROP-TRIAL]] | SL3 | — |
| REQUIRED | [[TEC TD-SEED-BANK|TD-SEED-BANK]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
