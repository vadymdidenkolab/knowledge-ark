---
id: "TD-HEALTH-MOVE-HANDOVER"
kind: "technology"
title: "Безопасное перемещение; повторная оценка и handover"
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

# Безопасное перемещение; повторная оценка и handover

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-HEALTH-MOVE-HANDOVER`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-HEALTH-MOVE-HANDOVER
- **parent_id:** [[TEC TD-HEALTH|TD-HEALTH]]
- **domain:** HEALTH
- **node_type:** TRAINING
- **title_ru:** Безопасное перемещение; повторная оценка и handover
- **outcome:** Иметь измеримую и проверяемую способность: безопасное перемещение; повторная оценка и handover
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]]
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
- **notes:** Каталожный узел; процедуры и рабочие параметры ещё не созданы
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
