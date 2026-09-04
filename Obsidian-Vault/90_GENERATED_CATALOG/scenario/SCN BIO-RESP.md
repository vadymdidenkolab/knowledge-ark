---
id: "BIO-RESP"
kind: "scenario"
title: "BIO-RESP"
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

# BIO-RESP

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `BIO-RESP`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** BIO-RESP
- **family:** BIO
- **name_ru:** Респираторная вспышка эпидемия или пандемия
- **scope:** HOUSEHOLD_TO_REGIONAL
- **trigger_class:** OFFICIAL_ALERT_OR_CLUSTER
- **first_decision_class:** OFFICIAL_DIRECTION
- **decision_sequence:** OFFICIAL_DIRECTION
- **decision_condition_notes:** Меры зависят от возбудителя и текущего guidance
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-AIR|AIR]], [[XW XW-PPE|PPE]], [[XW XW-MED-ILL|MED-ILL]], [[XW XW-INFO|INFO]], [[XW XW-SAN|SAN]]
- **spatial_need_codes:** HEALTHCARE|AIR_QUALITY|OFFICIAL_ZONES
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** IMMUNOCOMPROMISED
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** DGS_ECDC_WHO
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Меры зависят от возбудителя и текущего guidance
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
