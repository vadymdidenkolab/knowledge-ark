---
id: "SOC-DOC"
kind: "scenario"
title: "SOC-DOC"
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

# SOC-DOC

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SOC-DOC`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** SOC-DOC
- **family:** SOC
- **name_ru:** Потеря паспорта ВНЖ рецепта страховки или ключевого документа
- **scope:** PERSON_OR_HOUSEHOLD
- **trigger_class:** DIRECT_OBSERVATION
- **first_decision_class:** PRESERVE_EVIDENCE_AND_RECOVER
- **decision_sequence:** PRESERVE_EVIDENCE_AND_RECOVER
- **decision_condition_notes:** Офлайн копия не заменяет оригинал но ускоряет восстановление
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-DOC|DOC]], [[XW XW-LEG|LEG]], [[XW XW-CYB|CYB]], [[XW XW-FIN|FIN]]
- **spatial_need_codes:** ADMIN|CONSULATE|POLICE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** ABROAD
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** GOV_CONSULATE_POLICE
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Офлайн копия не заменяет оригинал но ускоряет восстановление
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
