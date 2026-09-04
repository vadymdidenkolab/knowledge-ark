---
id: "TD-FUEL-DEMAND"
kind: "technology"
title: "Топливный баланс и сокращение спроса"
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

# Топливный баланс и сокращение спроса

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-DEMAND`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-DEMAND
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** TEST
- **title_ru:** Топливный баланс и сокращение спроса
- **outcome:** Measure real liters or kilograms per service unit and prioritize non-fuel alternatives
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_CONSUMPTION_LOG
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]]
- **measurement_acceptance:** Consumption by device; task; season and reserve days reconciles to stock changes
- **calibration_reference:** Known container volume or mass check; odometer or runtime cross-check
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** EXACT_ASSETS_AND_SITE_REQUIRED
- **waste_storage:** Spills and waste recorded
- **stop_conditions:** Unknown leak; inconsistent reconciliation; unsafe measurement near ignition
- **maintenance_spares:** Each refill and monthly balance
- **successor_proof:** Преемник reconciles one period and finds a planted discrepancy
- **evidence_required:** Raw stock counts; receipts; runtime; service output; uncertainty
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Do not open fuel systems to measure consumption
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
- **capacity_model:** LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE
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
| REQUIRED | [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]] | SL2 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
