---
id: "GEN-CARE-CAPACITY-COLLAPSE"
kind: "scenario"
title: "GEN-CARE-CAPACITY-COLLAPSE"
priority_tier: "P4_BLUE"
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

# GEN-CARE-CAPACITY-COLLAPSE

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `GEN-CARE-CAPACITY-COLLAPSE`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P4_BLUE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** GEN-CARE-CAPACITY-COLLAPSE
- **family:** GEN
- **name_ru:** Спрос на уход превышает доказанную capacity
- **scope:** CELL_TO_INSTITUTION
- **trigger_class:** CARE_GAP
- **first_decision_class:** ASSESS_DEPENDENCIES
- **decision_sequence:** ASSESS_DEPENDENCIES
- **decision_condition_notes:** Нельзя скрывать дефицит за принуждением caregiver
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-MED|MED]], [[XW XW-MED-MH|MED-MH]], [[XW XW-GOV|GOV]], [[XW XW-COMM|COMM]], [[XW XW-SHEL|SHEL]]
- **spatial_need_codes:** HEALTH_SERVICE|SOCIAL_SERVICE|ACCESSIBLE_SITE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** не заполнено
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E5
- **source_authority_class:** PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Нельзя скрывать дефицит за принуждением caregiver
- **source_ids:** TBD
- **source_section_refs:** TBD
- **decision_provenance_state:** NOT_LINKED
- **horizon_vocabulary_version:** 0.3
- **horizon_semantics:** TREND_OR_STATE
- **e5_review_state:** ARCHITECTURE_ONLY
- **e5_basis_refs:** 16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
