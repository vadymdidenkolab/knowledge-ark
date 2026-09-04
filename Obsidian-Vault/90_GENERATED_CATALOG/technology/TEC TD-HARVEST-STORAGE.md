---
id: "TD-HARVEST-STORAGE"
kind: "technology"
title: "Уборка; сушка и хранение урожая"
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

# Уборка; сушка и хранение урожая

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HARVEST-STORAGE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HARVEST-STORAGE
- **parent_id:** [[TEC TD-FOOD|TD-FOOD]]
- **domain:** FOOD_AGRI
- **node_type:** PROCESS
- **title_ru:** Уборка; сушка и хранение урожая
- **outcome:** Снизить потери без плесени; вредителей и загрязнения
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-CROP-TRIAL|TD-CROP-TRIAL]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_STORAGE_SYSTEM
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Lot; dry target; temperature; humidity; losses and rejection recorded
- **calibration_reference:** Scale; thermometer; hygrometer checks; reference method per crop
- **drawings_bom_state:** MISSING_STORE_LAYOUT
- **localization_state:** FOOD_RULES_AND_SITE_REQUIRED
- **waste_storage:** Spoiled food isolated from feed; seed and compost decisions
- **stop_conditions:** Mold; pests; chemical contamination; unknown moisture; damaged container
- **maintenance_spares:** Scheduled inspection and rotation; spare containers
- **successor_proof:** Преемник inspects and rejects unsafe lot
- **evidence_required:** Lot log; environment; losses; photos; disposition
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No physical store or season data
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
| REQUIRED | [[TEC TD-CROP-TRIAL|TD-CROP-TRIAL]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
