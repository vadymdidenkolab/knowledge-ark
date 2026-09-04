---
id: "NAT-ANIMAL"
kind: "scenario"
title: "NAT-ANIMAL"
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

# NAT-ANIMAL

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `NAT-ANIMAL`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** NAT-ANIMAL
- **family:** NAT
- **name_ru:** Контакт с опасным животным или растением, укусы и ужаления: оценка красных флагов
- **scope:** PERSON_TO_LOCAL
- **trigger_class:** DIRECT_OBSERVATION_OR_EXPOSURE
- **first_decision_class:** ASSESS_RED_FLAGS
- **decision_sequence:** ASSESS_RED_FLAGS
- **decision_condition_notes:** 112 при угрозе жизни, тяжёлой реакции или иной экстренной развилке; в остальных случаях маршрут зависит от вида контакта и официальной медицинской рекомендации; универсального антидота нет
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-MED-ILL|MED-ILL]], [[XW XW-PET|PET]], [[XW XW-PPE|PPE]], [[XW XW-INFO|INFO]]
- **spatial_need_codes:** HEALTHCARE|VET|EXPOSURE_SITE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** CHILD|PET
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** DGS_ICNF_VETERINARY
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** 112 при угрозе жизни, тяжёлой реакции или иной экстренной развилке; в остальных случаях маршрут зависит от вида контакта и официальной медицинской рекомендации; универсального антидота нет
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
