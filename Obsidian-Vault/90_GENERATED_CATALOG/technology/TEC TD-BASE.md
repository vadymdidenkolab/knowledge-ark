---
id: "TD-BASE"
kind: "technology"
title: "Базовая доказательная платформа"
priority_tier: "P2_YELLOW"
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

# Базовая доказательная платформа

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S0_OBSERVE_READ`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** BASE
- **node_type:** OUTCOME
- **title_ru:** Базовая доказательная платформа
- **outcome:** Безопасность; площадка; инвентарь; измерения; чертежи; архив; обучение
- **safety_class:** S0_OBSERVE_READ
- **execution_policy:** HOUSEHOLD_S0
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]], [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]], [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_MIXED
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Все девять базовых узлов закрыты
- **calibration_reference:** SEE_CHILD_NODES
- **drawings_bom_state:** ARCHITECTURE_ONLY
- **localization_state:** PORTUGAL_AND_SITE_TBD
- **waste_storage:** SEE_CHILD_NODES
- **stop_conditions:** Любой TBD или неизвестная опасность
- **maintenance_spares:** SEE_CHILD_NODES
- **successor_proof:** Преемник выполняет поиск; проверку; журнал и stop без помощи автора
- **evidence_required:** Evidence по всем дочерним узлам
- **evidence_state:** ARCHITECTURE_ONLY
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** Обязательный предок каждой практической технологии
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
- **safety_lane:** S0_OBSERVE_READ
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-TRAINING|TD-BASE-TRAINING]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
