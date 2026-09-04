---
id: "MED-BURN"
kind: "scenario"
title: "MED-BURN"
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

# MED-BURN

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `MED-BURN`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** MED-BURN
- **family:** MED
- **name_ru:** Термический ожог: оценка красных флагов и срочности
- **scope:** PERSON_OR_MULTI
- **trigger_class:** DIRECT_OBSERVATION
- **first_decision_class:** ASSESS_RED_FLAGS
- **decision_sequence:** ASSESS_RED_FLAGS
- **decision_condition_notes:** Красные флаги или угроза жизни требуют 112; остальные маршруты определяет проверенная карточка, SNS 24 или клиницист
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[SCN MED-TRAUMA|MED-TRAUMA]], [[XW XW-WAT|WAT]], [[XW XW-PPE|PPE]]
- **spatial_need_codes:** MEDICAL_ACCESS|SAFE_EXIT
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** AGE_PROFILE
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** IFRC_ERC_PLUS_LOCAL
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Красные флаги или угроза жизни требуют 112; остальные маршруты определяет проверенная карточка, SNS 24 или клиницист
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
