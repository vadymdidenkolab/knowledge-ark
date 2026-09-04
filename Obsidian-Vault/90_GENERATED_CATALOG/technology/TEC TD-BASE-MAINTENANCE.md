---
id: "TD-BASE-MAINTENANCE"
kind: "technology"
title: "Обслуживание; ремонт и запасные части"
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

# Обслуживание; ремонт и запасные части

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE-MAINTENANCE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE-MAINTENANCE
- **parent_id:** [[TEC TD-BASE|TD-BASE]]
- **domain:** BASE
- **node_type:** MAINTENANCE
- **title_ru:** Обслуживание; ремонт и запасные части
- **outcome:** Сохранять функцию после износа и отказа
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_ASSET_LIFECYCLE_RECORDS
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-003|INS-003]], [[INS INS-045|INS-045]]
- **measurement_acceptance:** Плановое обслуживание выполнено; spares доступны; отказ безопасно диагностируется
- **calibration_reference:** Тест до и после обслуживания по OEM или проверенному пакету
- **drawings_bom_state:** MISSING_PER_ASSET
- **localization_state:** EXACT_ASSET_REQUIRED
- **waste_storage:** Отходы и заменённые части по категории
- **stop_conditions:** Stored energy; сеть; давление; газ; lithium; неизвестный дефект
- **maintenance_spares:** По OEM и фактическому duty cycle
- **successor_proof:** Преемник выполняет разрешённое обслуживание и фиксирует результат
- **evidence_required:** Maintenance log; parts; before-after test
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Ремонт не должен обходить защиты
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
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-DRAWINGS|TD-BASE-DRAWINGS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
