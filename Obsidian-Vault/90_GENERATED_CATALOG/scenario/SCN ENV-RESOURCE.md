---
id: "ENV-RESOURCE"
kind: "scenario"
title: "ENV-RESOURCE"
priority_tier: "P2_YELLOW"
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

# ENV-RESOURCE

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `ENV-RESOURCE`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** ENV-RESOURCE
- **family:** ENV
- **name_ru:** Истощение топлива материалов запчастей или расходников
- **scope:** HOUSEHOLD_TO_SYSTEMIC
- **trigger_class:** INVENTORY_TREND
- **first_decision_class:** PRESERVE_EVIDENCE_AND_RECOVER
- **decision_sequence:** PRESERVE_EVIDENCE_AND_RECOVER
- **decision_condition_notes:** Переход к ремонту стандартизации и обмену
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-TOOL|TOOL]], [[XW XW-ENE|ENE]], [[XW XW-FIN|FIN]], [[XW XW-COMM|COMM]], [[XW XW-AGR|AGR]]
- **spatial_need_codes:** SUPPLY|REPAIR|ALTERNATE_REGION
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** не заполнено
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E3_E4
- **source_authority_class:** SECTOR_AUTHORITIES_MANUFACTURERS
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Переход к ремонту стандартизации и обмену
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
