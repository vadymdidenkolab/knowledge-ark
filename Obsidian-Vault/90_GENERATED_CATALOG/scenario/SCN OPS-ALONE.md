---
id: "OPS-ALONE"
kind: "scenario"
title: "OPS-ALONE"
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

# OPS-ALONE

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `OPS-ALONE`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** OPS-ALONE
- **family:** OPS
- **name_ru:** Одиночный участник не выходит на связь
- **scope:** PERSON
- **trigger_class:** MISSED_CHECKIN
- **first_decision_class:** REUNIFY_AND_ACCOUNT
- **decision_sequence:** REUNIFY_AND_ACCOUNT
- **decision_condition_notes:** Заранее заданная лестница эскалации
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-COM|COM]], [[XW XW-GOV|GOV]], [[XW XW-SAFE|SAFE]], [[XW XW-MED-ILL|MED-ILL]]
- **spatial_need_codes:** LAST_KNOWN|ROUTE|EXTERNAL_CONTACT
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** не заполнено
- **group_size_scope:** N1
- **horizon_scope:** E0_E4
- **source_authority_class:** HOUSEHOLD_POLICE_MEDICAL_AS_APPLICABLE
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Заранее заданная лестница эскалации
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
