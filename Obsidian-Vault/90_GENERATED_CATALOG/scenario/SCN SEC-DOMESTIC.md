---
id: "SEC-DOMESTIC"
kind: "scenario"
title: "SEC-DOMESTIC"
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

# SEC-DOMESTIC

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `SEC-DOMESTIC`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** SEC-DOMESTIC
- **family:** SEC
- **name_ru:** Домашнее или гендерное насилие coercive control
- **scope:** PERSON_OR_HOUSEHOLD
- **trigger_class:** DISCLOSURE_OR_DIRECT_OBSERVATION
- **first_decision_class:** DISCREET_SAFETY
- **decision_sequence:** DISCREET_SAFETY>TRUSTED_CHANNEL_IF_SAFE>CALL_112_IF_IMMEDIATE_DANGER
- **decision_condition_notes:** Не провоцировать раскрытие плана или использование контролируемого устройства; 112 при непосредственной опасности
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-SAFE|SAFE]], [[XW XW-DOC|DOC]], [[XW XW-COM|COM]], [[XW XW-SHEL|SHEL]]
- **spatial_need_codes:** SAFE_SERVICE|SHELTER|POLICE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** CHILD
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** POLICE_SOCIAL_HEALTH_SPECIALIST_SERVICES
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** План не должен быть доступен агрессору
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
