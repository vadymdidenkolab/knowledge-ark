---
id: "NAT-FLD"
kind: "scenario"
title: "NAT-FLD"
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

# NAT-FLD

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `NAT-FLD`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** NAT-FLD
- **family:** NAT
- **name_ru:** Речное дождевое или прибрежное наводнение
- **scope:** LOCAL_TO_REGIONAL
- **trigger_class:** OFFICIAL_ALERT_OR_DIRECT_OBSERVATION
- **first_decision_class:** MOVE_TO_HIGH_GROUND
- **decision_sequence:** MOVE_TO_HIGH_GROUND
- **decision_condition_notes:** Не входить и не въезжать в воду
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-NAV|NAV]], [[XW XW-TRANS|TRANS]], [[XW XW-WAT|WAT]], [[XW XW-SAN|SAN]], [[XW XW-REC|REC]]
- **spatial_need_codes:** FLOOD_DEPTH|VELOCITY|ELEVATION|ROAD
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** MOBILITY_LIMITATION
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_APA_MUNICIPAL
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Не входить и не въезжать в воду
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
