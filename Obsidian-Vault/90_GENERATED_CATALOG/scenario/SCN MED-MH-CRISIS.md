---
id: "MED-MH-CRISIS"
kind: "scenario"
title: "MED-MH-CRISIS"
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

# MED-MH-CRISIS

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `MED-MH-CRISIS`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** MED-MH-CRISIS
- **family:** MED
- **name_ru:** Острый психический кризис или непосредственный риск самоповреждения
- **scope:** PERSON_TO_GROUP
- **trigger_class:** IMMEDIATE_SELF_HARM_OTHER_HARM_OR_ACUTE_CRISIS
- **first_decision_class:** IMMEDIATE_SAFETY
- **decision_sequence:** IMMEDIATE_SAFETY>CALL_112_IF_IMMEDIATE_DANGER>TRUSTED_CRISIS_ROUTE_AND_CONTINUITY
- **decision_condition_notes:** Не оставлять человека одного при непосредственном риске, не обещать секретность и не применять принуждение вне закона/профессиональной помощи
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-MED-MH|MED-MH]], [[XW XW-SAFE|SAFE]], [[XW XW-COM|COM]], [[XW XW-TRANS|TRANS]]
- **spatial_need_codes:** SAFE_SPACE|MEDICAL_ACCESS|TRUSTED_CONTACT
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** MENTAL_HEALTH_CONTINUITY|ALONE|CHILD|ADOLESCENT
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** SNS_DGS_MENTAL_HEALTH_EMERGENCY
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
