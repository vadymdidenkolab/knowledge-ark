---
id: "MED-OB"
kind: "scenario"
title: "MED-OB"
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

# MED-OB

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `MED-OB`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** MED-OB
- **family:** MED
- **name_ru:** Неотложное состояние при беременности или родах
- **scope:** PERSON_TO_GROUP
- **trigger_class:** PREGNANCY_RED_FLAG_OR_LABOR_COMPLICATION
- **first_decision_class:** CALL_112_OR_URGENT_MATERNITY
- **decision_sequence:** CALL_112_OR_URGENT_MATERNITY>FOLLOW_DISPATCH_AND_PERSON_PLAN
- **decision_condition_notes:** Красные флаги, срок беременности и локальный maternity-route требуют профессиональной карточки; не импровизировать акушерские процедуры
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-MED-ILL|MED-ILL]], [[XW XW-MED-NCD|MED-NCD]], [[XW XW-TRANS|TRANS]], [[XW XW-COM|COM]]
- **spatial_need_codes:** MATERNITY|MEDICAL_ACCESS|ROUTE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** PREGNANCY|ALONE|LANGUAGE_BARRIER
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** SNS_DGS_OBSTETRIC_SERVICE
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** не заполнено
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
