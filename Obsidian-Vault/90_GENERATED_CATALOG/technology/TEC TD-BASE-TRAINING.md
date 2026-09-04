---
id: "TD-BASE-TRAINING"
kind: "technology"
title: "Навыки; роли и преемственность"
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

# Навыки; роли и преемственность

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE-TRAINING`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE-TRAINING
- **parent_id:** [[TEC TD-BASE|TD-BASE]]
- **domain:** BASE
- **node_type:** TRAINING
- **title_ru:** Навыки; роли и преемственность
- **outcome:** Не зависеть от одного автора или владельца навыка
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_ACCEPTED_TRAINING_RECORDS
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Участник демонстрирует задачу; stop; ограничения и handoff
- **calibration_reference:** Независимый evaluator или заранее утверждённый checklist
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** GROUP_PROFILE_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Нет согласия; усталость; отсутствует supervisor для S2+
- **maintenance_spares:** По интервалу метода и после длительного перерыва
- **successor_proof:** Blind repeat другим человеком
- **evidence_required:** Roster; consent; competency evidence; reassessment
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Чтение не равно навыку
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-ARCHIVE|TD-BASE-ARCHIVE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
