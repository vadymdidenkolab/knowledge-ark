---
id: "INF-POWER"
kind: "scenario"
title: "INF-POWER"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "UNASSIGNED"
safety_class: "UNASSIGNED"
execution_gate: "DENY_UNTIL_REVIEWED"
status: "INDEX_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# INF-POWER

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `INF-POWER`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** INF-POWER
- **family:** INF
- **name_ru:** Отключение электричества
- **scope:** HOUSEHOLD_TO_REGIONAL
- **trigger_class:** SERVICE_FAILURE_OR_OFFICIAL_NOTICE
- **first_decision_class:** ASSESS_DEPENDENCIES
- **decision_sequence:** ASSESS_DEPENDENCIES>CHECK_OFFICIAL_STATUS>ISOLATE_SPECIFIC_FAILED_EQUIPMENT_IF_NEEDED
- **decision_condition_notes:** Обычный outage не равен опасному электрическому объекту; сначала люди, медзависимости, пожар/CO и официальная информация
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-ENE|ENE]], [[XW XW-FIRE|FIRE]], [[XW XW-COM|COM]], [[XW XW-MED-NCD|MED-NCD]], [[XW XW-FOOD|FOOD]]
- **spatial_need_codes:** UTILITY_ZONE|CHARGING|HEALTHCARE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** OXYGEN_OR_POWER_DEPENDENT
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** GRID_OPERATOR_ANEPC_MUNICIPAL
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** CO и холодовая цепь являются отдельными рисками
- **source_ids:** TBD
- **source_section_refs:** TBD
- **decision_provenance_state:** NOT_LINKED
- **horizon_vocabulary_version:** 0.3
- **horizon_semantics:** RECURRENT_OVER_LIFECYCLE
- **e5_review_state:** NOT_REVIEWED
- **e5_basis_refs:** не заполнено

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
