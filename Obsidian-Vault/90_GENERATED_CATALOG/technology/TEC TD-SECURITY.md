---
id: "TD-SECURITY"
kind: "technology"
title: "Безопасность людей; доступ и safeguarding"
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

# Безопасность людей; доступ и safeguarding

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-SECURITY`
- **Статус:** `MISSING`
- **Приоритет:** `P0_RED`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-SECURITY
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** SECURITY
- **node_type:** OUTCOME
- **title_ru:** Безопасность людей; доступ и safeguarding
- **outcome:** Иметь измеримую и проверяемую способность: безопасность людей; доступ и safeguarding
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-SECURITY-SAFE-DIRECTION|TD-SECURITY-SAFE-DIRECTION]], [[TEC TD-SECURITY-DEESCALATION|TD-SECURITY-DEESCALATION]], [[TEC TD-SECURITY-ACCESS|TD-SECURITY-ACCESS]], [[TEC TD-SECURITY-VISITORS|TD-SECURITY-VISITORS]], [[TEC TD-SECURITY-CHILD|TD-SECURITY-CHILD]], [[TEC TD-SECURITY-DV|TD-SECURITY-DV]], [[TEC TD-SECURITY-MISSING|TD-SECURITY-MISSING]], [[TEC TD-SECURITY-SAFE-PLACE|TD-SECURITY-SAFE-PLACE]], [[TEC TD-SECURITY-CONFLICT|TD-SECURITY-CONFLICT]], [[TEC TD-SECURITY-LIGHT|TD-SECURITY-LIGHT]], [[TEC TD-SECURITY-INCIDENT|TD-SECURITY-INCIDENT]], [[TEC TD-SECURITY-NO-OFFENSE|TD-SECURITY-NO-OFFENSE]]
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

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL1
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD
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
| REQUIRED | [[TEC TD-SECURITY-SAFE-DIRECTION|TD-SECURITY-SAFE-DIRECTION]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-DEESCALATION|TD-SECURITY-DEESCALATION]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-ACCESS|TD-SECURITY-ACCESS]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-VISITORS|TD-SECURITY-VISITORS]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-CHILD|TD-SECURITY-CHILD]] | SL1 | — |
| CONDITIONAL | [[TEC TD-SECURITY-DV|TD-SECURITY-DV]] | SL1 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-SECURITY-MISSING|TD-SECURITY-MISSING]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-SAFE-PLACE|TD-SECURITY-SAFE-PLACE]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-CONFLICT|TD-SECURITY-CONFLICT]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-LIGHT|TD-SECURITY-LIGHT]] | SL1 | — |
| REQUIRED | [[TEC TD-SECURITY-INCIDENT|TD-SECURITY-INCIDENT]] | SL1 | — |
| HAZARD_ONLY | [[TEC TD-SECURITY-NO-OFFENSE|TD-SECURITY-NO-OFFENSE]] | SL1 | not_an_operational_prerequisite |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
