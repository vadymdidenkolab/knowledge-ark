---
id: "TD-TRANSPORT"
kind: "technology"
title: "Перемещение людей; грузов и критических ресурсов"
priority_tier: "P1_ORANGE"
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

# Перемещение людей; грузов и критических ресурсов

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-TRANSPORT`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-TRANSPORT
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** TRANSPORT
- **node_type:** OUTCOME
- **title_ru:** Перемещение людей; грузов и критических ресурсов
- **outcome:** Иметь измеримую и проверяемую способность: перемещение людей; грузов и критических ресурсов
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-TRANSPORT-WALK|TD-TRANSPORT-WALK]], [[TEC TD-TRANSPORT-CARRY|TD-TRANSPORT-CARRY]], [[TEC TD-TRANSPORT-CART|TD-TRANSPORT-CART]], [[TEC TD-TRANSPORT-BICYCLE|TD-TRANSPORT-BICYCLE]], [[TEC TD-TRANSPORT-VEHICLE|TD-TRANSPORT-VEHICLE]], [[TEC TD-TRANSPORT-DRIVER|TD-TRANSPORT-DRIVER]], [[TEC TD-TRANSPORT-RESTRAINT|TD-TRANSPORT-RESTRAINT]], [[TEC TD-TRANSPORT-RANGE|TD-TRANSPORT-RANGE]], [[TEC TD-TRANSPORT-PAYLOAD|TD-TRANSPORT-PAYLOAD]], [[TEC TD-TRANSPORT-TIRES|TD-TRANSPORT-TIRES]], [[TEC TD-TRANSPORT-BRAKES|TD-TRANSPORT-BRAKES]], [[TEC TD-TRANSPORT-STEERING|TD-TRANSPORT-STEERING]], [[TEC TD-TRANSPORT-PUMP|TD-TRANSPORT-PUMP]], [[TEC TD-TRANSPORT-JACK|TD-TRANSPORT-JACK]], [[TEC TD-TRANSPORT-TOW|TD-TRANSPORT-TOW]], [[TEC TD-TRANSPORT-REPAIR|TD-TRANSPORT-REPAIR]], [[TEC TD-TRANSPORT-SPARES|TD-TRANSPORT-SPARES]], [[TEC TD-TRANSPORT-ROUTE|TD-TRANSPORT-ROUTE]], [[TEC TD-TRANSPORT-ABANDON|TD-TRANSPORT-ABANDON]], [[TEC TD-TRANSPORT-ANIMAL|TD-TRANSPORT-ANIMAL]], [[TEC TD-TRANSPORT-BOAT|TD-TRANSPORT-BOAT]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING
- **instrument_ids:** не заполнено
- **measurement_acceptance:** До использования задать service level, единицу, объём, срок и критерий приёмки
- **calibration_reference:** Точный метод, прибор/reference и неопределённость TBD до исполнения
- **drawings_bom_state:** MISSING_OR_NOT_APPLICABLE
- **localization_state:** PORTUGAL_AND_SITE_REVIEW_REQUIRED
- **waste_storage:** Потоки, совместимость, хранение и законный маршрут TBD до исполнения
- **stop_conditions:** Неизвестная идентичность; отсутствующее полномочие; опасная среда; непроверенный источник; выход за подготовку
- **maintenance_spares:** Периодичность, расходники, запасные части и failure signs TBD
- **successor_proof:** Другой назначенный участник находит карточку и демонстрирует допустимую часть без устной помощи автора
- **evidence_required:** Профиль; источник; инвентарь; измерения; acceptance log; reviewer; дата
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Агрегат: обязательность дочерних узлов определяется technology-dependency-edges.csv
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P1_ORANGE
- **priority_horizon:** 3_TO_14_DAYS
- **earliest_service_level:** SL2
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P1_ORANGE
- **acquisition_priority:** P1_ORANGE
- **knowledge_priority:** P1_ORANGE
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** PEOPLE_KG_KM_RANGE_AND_TURNAROUND_TIME
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| ALTERNATIVE | [[TEC TD-TRANSPORT-WALK|TD-TRANSPORT-WALK]] | SL2 | TRANSPORT_MODE |
| REQUIRED | [[TEC TD-TRANSPORT-CARRY|TD-TRANSPORT-CARRY]] | SL2 | — |
| ALTERNATIVE | [[TEC TD-TRANSPORT-CART|TD-TRANSPORT-CART]] | SL2 | TRANSPORT_MODE |
| ALTERNATIVE | [[TEC TD-TRANSPORT-BICYCLE|TD-TRANSPORT-BICYCLE]] | SL2 | TRANSPORT_MODE |
| ALTERNATIVE | [[TEC TD-TRANSPORT-VEHICLE|TD-TRANSPORT-VEHICLE]] | SL2 | TRANSPORT_MODE |
| CONDITIONAL | [[TEC TD-TRANSPORT-DRIVER|TD-TRANSPORT-DRIVER]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-TRANSPORT-RESTRAINT|TD-TRANSPORT-RESTRAINT]] | SL2 | — |
| REQUIRED | [[TEC TD-TRANSPORT-RANGE|TD-TRANSPORT-RANGE]] | SL2 | — |
| REQUIRED | [[TEC TD-TRANSPORT-PAYLOAD|TD-TRANSPORT-PAYLOAD]] | SL2 | — |
| REQUIRED | [[TEC TD-TRANSPORT-TIRES|TD-TRANSPORT-TIRES]] | SL2 | — |
| CONDITIONAL | [[TEC TD-TRANSPORT-BRAKES|TD-TRANSPORT-BRAKES]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-TRANSPORT-STEERING|TD-TRANSPORT-STEERING]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-TRANSPORT-PUMP|TD-TRANSPORT-PUMP]] | SL2 | — |
| CONDITIONAL | [[TEC TD-TRANSPORT-JACK|TD-TRANSPORT-JACK]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-TRANSPORT-TOW|TD-TRANSPORT-TOW]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-TRANSPORT-REPAIR|TD-TRANSPORT-REPAIR]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-TRANSPORT-SPARES|TD-TRANSPORT-SPARES]] | SL2 | — |
| REQUIRED | [[TEC TD-TRANSPORT-ROUTE|TD-TRANSPORT-ROUTE]] | SL2 | — |
| REQUIRED | [[TEC TD-TRANSPORT-ABANDON|TD-TRANSPORT-ABANDON]] | SL2 | — |
| CONDITIONAL | [[TEC TD-TRANSPORT-ANIMAL|TD-TRANSPORT-ANIMAL]] | SL2 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-TRANSPORT-BOAT|TD-TRANSPORT-BOAT]] | SL1 | not_an_operational_prerequisite |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
