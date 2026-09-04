---
id: "TEC-CONFINED"
kind: "scenario"
title: "TEC-CONFINED"
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

# TEC-CONFINED

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TEC-CONFINED`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** TEC-CONFINED
- **family:** TEC
- **name_ru:** Застревание в лифте тоннеле колодце или замкнутом пространстве
- **scope:** PERSON_TO_GROUP
- **trigger_class:** DIRECT_OBSERVATION_OR_LOST_CONTACT
- **first_decision_class:** CALL_112
- **decision_sequence:** CALL_112>DO_NOT_ENTER_OR_IMPROVISE_RESCUE>MAINTAIN_SAFE_CONTACT_AND_ACCOUNT
- **decision_condition_notes:** Неподготовленный вход может создать нескольких пострадавших из-за газа, энергии, воды, конструкции или ограниченного выхода
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-SAFE|SAFE]], [[XW XW-COM|COM]], [[XW XW-NAV|NAV]], [[XW XW-MED-BLS|MED-BLS]]
- **spatial_need_codes:** EXACT_LOCATION|RESCUE_ACCESS|UTILITY_ZONE|NO_GO
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** UNDERGROUND|TUNNEL|MOBILITY_LIMITATION|CHILD
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** 112_FIRE_RESCUE_UTILITY
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
