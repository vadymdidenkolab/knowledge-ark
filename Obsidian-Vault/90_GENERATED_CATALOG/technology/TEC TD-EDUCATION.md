---
id: "TD-EDUCATION"
kind: "technology"
title: "Образование; подготовка и передача компетенций"
priority_tier: "P4_BLUE"
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

# Образование; подготовка и передача компетенций

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-EDUCATION`
- **Статус:** `MISSING`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-EDUCATION
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** EDUCATION
- **node_type:** OUTCOME
- **title_ru:** Образование; подготовка и передача компетенций
- **outcome:** Иметь измеримую и проверяемую способность: образование; подготовка и передача компетенций
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-EDUCATION-LITERACY|TD-EDUCATION-LITERACY]], [[TEC TD-EDUCATION-NUMERACY|TD-EDUCATION-NUMERACY]], [[TEC TD-EDUCATION-LANG|TD-EDUCATION-LANG]], [[TEC TD-EDUCATION-TECH-READ|TD-EDUCATION-TECH-READ]], [[TEC TD-EDUCATION-SKILL-MATRIX|TD-EDUCATION-SKILL-MATRIX]], [[TEC TD-EDUCATION-PREREQ|TD-EDUCATION-PREREQ]], [[TEC TD-EDUCATION-APPRENTICE|TD-EDUCATION-APPRENTICE]], [[TEC TD-EDUCATION-SUPERVISED|TD-EDUCATION-SUPERVISED]], [[TEC TD-EDUCATION-MASTERY|TD-EDUCATION-MASTERY]], [[TEC TD-EDUCATION-RECERT|TD-EDUCATION-RECERT]], [[TEC TD-EDUCATION-TEACHBACK|TD-EDUCATION-TEACHBACK]], [[TEC TD-EDUCATION-INSTRUCTOR|TD-EDUCATION-INSTRUCTOR]], [[TEC TD-EDUCATION-ACCESS|TD-EDUCATION-ACCESS]], [[TEC TD-EDUCATION-CHILD|TD-EDUCATION-CHILD]], [[TEC TD-EDUCATION-PAPER|TD-EDUCATION-PAPER]]
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

- **priority_tier:** P4_BLUE
- **priority_horizon:** 15_TO_100_YEARS
- **earliest_service_level:** SL6
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P4_BLUE
- **acquisition_priority:** P4_BLUE
- **knowledge_priority:** P4_BLUE
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** LEARNERS_HOURS_COMPETENCY_AND_DUPLICATES
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
| REQUIRED | [[TEC TD-EDUCATION-LITERACY|TD-EDUCATION-LITERACY]] | SL3 | — |
| REQUIRED | [[TEC TD-EDUCATION-NUMERACY|TD-EDUCATION-NUMERACY]] | SL3 | — |
| REQUIRED | [[TEC TD-EDUCATION-LANG|TD-EDUCATION-LANG]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-TECH-READ|TD-EDUCATION-TECH-READ]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-SKILL-MATRIX|TD-EDUCATION-SKILL-MATRIX]] | SL3 | — |
| REQUIRED | [[TEC TD-EDUCATION-PREREQ|TD-EDUCATION-PREREQ]] | SL3 | — |
| REQUIRED | [[TEC TD-EDUCATION-APPRENTICE|TD-EDUCATION-APPRENTICE]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-SUPERVISED|TD-EDUCATION-SUPERVISED]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-MASTERY|TD-EDUCATION-MASTERY]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-RECERT|TD-EDUCATION-RECERT]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-TEACHBACK|TD-EDUCATION-TEACHBACK]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-INSTRUCTOR|TD-EDUCATION-INSTRUCTOR]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-ACCESS|TD-EDUCATION-ACCESS]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-CHILD|TD-EDUCATION-CHILD]] | SL6 | — |
| REQUIRED | [[TEC TD-EDUCATION-PAPER|TD-EDUCATION-PAPER]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
