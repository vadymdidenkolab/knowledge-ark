---
id: "TD-ENVIRONMENT"
kind: "technology"
title: "Среда; погода; климат и экосистемные пределы"
priority_tier: "P3_GREEN"
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

# Среда; погода; климат и экосистемные пределы

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ENVIRONMENT`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ENVIRONMENT
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** ENVIRONMENT
- **node_type:** OUTCOME
- **title_ru:** Среда; погода; климат и экосистемные пределы
- **outcome:** Иметь измеримую и проверяемую способность: среда; погода; климат и экосистемные пределы
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-ENVIRONMENT-WEATHER|TD-ENVIRONMENT-WEATHER]], [[TEC TD-ENVIRONMENT-DROUGHT|TD-ENVIRONMENT-DROUGHT]], [[TEC TD-ENVIRONMENT-HEAT|TD-ENVIRONMENT-HEAT]], [[TEC TD-ENVIRONMENT-COLD|TD-ENVIRONMENT-COLD]], [[TEC TD-ENVIRONMENT-WIND|TD-ENVIRONMENT-WIND]], [[TEC TD-ENVIRONMENT-FLOOD|TD-ENVIRONMENT-FLOOD]], [[TEC TD-ENVIRONMENT-FIRE|TD-ENVIRONMENT-FIRE]], [[TEC TD-ENVIRONMENT-COAST|TD-ENVIRONMENT-COAST]], [[TEC TD-ENVIRONMENT-SEISMIC|TD-ENVIRONMENT-SEISMIC]], [[TEC TD-ENVIRONMENT-SOIL-DEGRADE|TD-ENVIRONMENT-SOIL-DEGRADE]], [[TEC TD-ENVIRONMENT-FOREST|TD-ENVIRONMENT-FOREST]], [[TEC TD-ENVIRONMENT-BIODIVERSITY|TD-ENVIRONMENT-BIODIVERSITY]], [[TEC TD-ENVIRONMENT-CLIMATE|TD-ENVIRONMENT-CLIMATE]]
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

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL4
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** SITE_SERIES_SEASONAL_RANGE_AND_TRIGGER_THRESHOLDS
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-WEATHER|TD-ENVIRONMENT-WEATHER]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-DROUGHT|TD-ENVIRONMENT-DROUGHT]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-HEAT|TD-ENVIRONMENT-HEAT]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-COLD|TD-ENVIRONMENT-COLD]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-WIND|TD-ENVIRONMENT-WIND]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-FLOOD|TD-ENVIRONMENT-FLOOD]] | SL2 | — |
| CONDITIONAL | [[TEC TD-ENVIRONMENT-FIRE|TD-ENVIRONMENT-FIRE]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ENVIRONMENT-COAST|TD-ENVIRONMENT-COAST]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-ENVIRONMENT-SEISMIC|TD-ENVIRONMENT-SEISMIC]] | SL2 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-SOIL-DEGRADE|TD-ENVIRONMENT-SOIL-DEGRADE]] | SL4 | — |
| CONDITIONAL | [[TEC TD-ENVIRONMENT-FOREST|TD-ENVIRONMENT-FOREST]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-ENVIRONMENT-BIODIVERSITY|TD-ENVIRONMENT-BIODIVERSITY]] | SL4 | — |
| REQUIRED | [[TEC TD-ENVIRONMENT-CLIMATE|TD-ENVIRONMENT-CLIMATE]] | SL4 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
