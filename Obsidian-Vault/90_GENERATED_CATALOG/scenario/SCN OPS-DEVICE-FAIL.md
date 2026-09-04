---
id: "OPS-DEVICE-FAIL"
kind: "scenario"
title: "OPS-DEVICE-FAIL"
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

# OPS-DEVICE-FAIL

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `OPS-DEVICE-FAIL`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** OPS-DEVICE-FAIL
- **family:** OPS
- **name_ru:** Не работает фильтр энергия связь транспорт или иное критическое устройство
- **scope:** HOUSEHOLD_OR_GROUP
- **trigger_class:** TEST_OR_RUNTIME_FAILURE
- **first_decision_class:** ISOLATE_AND_LOCKOUT
- **decision_sequence:** ISOLATE_AND_LOCKOUT
- **decision_condition_notes:** Использовать независимый fallback а не опасный ремонт
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-WAT|WAT]], [[XW XW-ENE|ENE]], [[XW XW-COM|COM]], [[XW XW-TRANS|TRANS]], [[XW XW-TOOL|TOOL]]
- **spatial_need_codes:** REPAIR|SUPPLY|ALTERNATE_ROUTE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** не заполнено
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** MANUFACTURER_SERVICE_AUTHORITY
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Использовать независимый fallback а не опасный ремонт
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
