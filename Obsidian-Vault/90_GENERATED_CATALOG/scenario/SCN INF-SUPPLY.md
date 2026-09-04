---
id: "INF-SUPPLY"
kind: "scenario"
title: "INF-SUPPLY"
priority_tier: "P1_ORANGE"
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

# INF-SUPPLY

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `INF-SUPPLY`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** INF-SUPPLY
- **family:** INF
- **name_ru:** Дефицит пищи лекарств топлива или расходников
- **scope:** LOCAL_TO_SYSTEMIC
- **trigger_class:** SUPPLY_DECLINE_OR_OFFICIAL_NOTICE
- **first_decision_class:** OFFICIAL_DIRECTION
- **decision_sequence:** OFFICIAL_DIRECTION
- **decision_condition_notes:** Ротация и раннее законное пополнение
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-FOOD|FOOD]], [[XW XW-MED-NCD|MED-NCD]], [[XW XW-WAT|WAT]], [[XW XW-FIN|FIN]], [[XW XW-TRANS|TRANS]]
- **spatial_need_codes:** SUPPLY|PHARMACY|FUEL|ALT_REGION
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** не заполнено
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E2_E4
- **source_authority_class:** SECTOR_AUTHORITIES_MUNICIPAL
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Ротация и раннее законное пополнение
- **source_ids:** TBD
- **source_section_refs:** TBD
- **decision_provenance_state:** NOT_LINKED
- **horizon_vocabulary_version:** 0.3
- **horizon_semantics:** TREND_OR_STATE
- **e5_review_state:** NOT_REVIEWED
- **e5_basis_refs:** не заполнено

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
