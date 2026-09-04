---
id: "TD-ROOT"
kind: "technology"
title: "Автономная система жизни и знаний"
priority_tier: "P4_BLUE"
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

# Автономная система жизни и знаний

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ROOT`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S0_OBSERVE_READ`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ROOT
- **parent_id:** не заполнено
- **domain:** SYSTEM
- **node_type:** OUTCOME
- **title_ru:** Автономная система жизни и знаний
- **outcome:** Сохранять критические функции и восстанавливать их после отказа внешнего снабжения
- **safety_class:** S0_OBSERVE_READ
- **execution_policy:** HOUSEHOLD_S0
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-WATER|TD-WATER]], [[TEC TD-FOOD|TD-FOOD]], [[TEC TD-SHELTER|TD-SHELTER]], [[TEC TD-ENERGY|TD-ENERGY]], [[TEC TD-HEALTH|TD-HEALTH]], [[TEC TD-MAPS-COMMS|TD-MAPS-COMMS]], [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]], [[TEC TD-GOV|TD-GOV]], [[TEC TD-WORKSHOP|TD-WORKSHOP]], [[TEC TD-FUELS|TD-FUELS]], [[TEC TD-PEOPLE|TD-PEOPLE]], [[TEC TD-TRANSPORT|TD-TRANSPORT]], [[TEC TD-SECURITY|TD-SECURITY]], [[TEC TD-EDUCATION|TD-EDUCATION]], [[TEC TD-MATERIALS-PRODUCTION|TD-MATERIALS-PRODUCTION]], [[TEC TD-CONSTRUCTION|TD-CONSTRUCTION]], [[TEC TD-ANIMALS|TD-ANIMALS]], [[TEC TD-ENVIRONMENT|TD-ENVIRONMENT]], [[TEC TD-PORTUGAL|TD-PORTUGAL]], [[TEC TD-HAZARDS|TD-HAZARDS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NOT_APPLICABLE
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Все обязательные service-level зависимости текущего приоритета имеют TESTED или явно принятый остаточный риск
- **calibration_reference:** NOT_APPLICABLE
- **drawings_bom_state:** ARCHITECTURE_ONLY
- **localization_state:** PORTUGAL_AND_SITE_TBD
- **waste_storage:** SEE_CHILD_NODES
- **stop_conditions:** Любой обязательный дочерний DENY блокирует общий ALLOW; OPTIONAL/REFERENCE не блокируют
- **maintenance_spares:** SEE_CHILD_NODES
- **successor_proof:** Другой участник находит дерево и объясняет границы каждой функции
- **evidence_required:** Полный снимок зависимостей; edge roles; service levels и решений
- **evidence_state:** ARCHITECTURE_ONLY
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** Корневой узел не является утверждением готовности; семантика ребер хранится отдельно
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P4_BLUE
- **priority_horizon:** 15_TO_100_YEARS
- **earliest_service_level:** SL6
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P4_BLUE
- **acquisition_priority:** P4_BLUE
- **knowledge_priority:** P4_BLUE
- **safety_lane:** S0_OBSERVE_READ
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL0 | — |
| REQUIRED | [[TEC TD-WATER|TD-WATER]] | SL0 | — |
| REQUIRED | [[TEC TD-FOOD|TD-FOOD]] | SL1 | — |
| REQUIRED | [[TEC TD-SHELTER|TD-SHELTER]] | SL0 | — |
| REQUIRED | [[TEC TD-ENERGY|TD-ENERGY]] | SL1 | — |
| REQUIRED | [[TEC TD-HEALTH|TD-HEALTH]] | SL0 | — |
| REQUIRED | [[TEC TD-MAPS-COMMS|TD-MAPS-COMMS]] | SL0 | — |
| REQUIRED | [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]] | SL2 | — |
| REQUIRED | [[TEC TD-GOV|TD-GOV]] | SL0 | — |
| REQUIRED | [[TEC TD-WORKSHOP|TD-WORKSHOP]] | SL3 | — |
| CONDITIONAL | [[TEC TD-FUELS|TD-FUELS]] | SL2 | fuel_dependent_service_present |
| REQUIRED | [[TEC TD-PEOPLE|TD-PEOPLE]] | SL0 | — |
| REQUIRED | [[TEC TD-TRANSPORT|TD-TRANSPORT]] | SL2 | — |
| REQUIRED | [[TEC TD-SECURITY|TD-SECURITY]] | SL0 | — |
| REQUIRED | [[TEC TD-EDUCATION|TD-EDUCATION]] | SL3 | — |
| CONDITIONAL | [[TEC TD-MATERIALS-PRODUCTION|TD-MATERIALS-PRODUCTION]] | SL5 | household_repair_or_intergroup_production_path_selected |
| CONDITIONAL | [[TEC TD-CONSTRUCTION|TD-CONSTRUCTION]] | SL3 | construction_or_structural_work_present |
| CONDITIONAL | [[TEC TD-ANIMALS|TD-ANIMALS]] | SL3 | animals_present |
| REQUIRED | [[TEC TD-ENVIRONMENT|TD-ENVIRONMENT]] | SL2 | — |
| REQUIRED | [[TEC TD-PORTUGAL|TD-PORTUGAL]] | SL0 | — |
| HAZARD_ONLY | [[TEC TD-HAZARDS|TD-HAZARDS]] | SL0 | always_visible_as_stop_boundary |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
