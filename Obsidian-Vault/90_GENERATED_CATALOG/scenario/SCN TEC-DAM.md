---
id: "TEC-DAM"
kind: "scenario"
title: "TEC-DAM"
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

# TEC-DAM

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TEC-DAM`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** TEC-DAM
- **family:** TEC
- **name_ru:** Авария плотины или быстрый downstream flood
- **scope:** LOCAL_TO_REGIONAL
- **trigger_class:** OFFICIAL_ALERT_OR_DIRECT_OBSERVATION
- **first_decision_class:** MOVE_TO_HIGH_GROUND
- **decision_sequence:** MOVE_TO_HIGH_GROUND
- **decision_condition_notes:** Только по официальной зоне и маршруту
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-NAV|NAV]], [[XW XW-TRANS|TRANS]], [[XW XW-COM|COM]], [[XW XW-GOV|GOV]]
- **spatial_need_codes:** DAM_PLAN|DOWNSTREAM_ZONE|ELEVATION
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** DAM_DOWNSTREAM
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_APA_MUNICIPAL_OPERATOR
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Только по официальной зоне и маршруту
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
