---
id: "MED-DENTAL"
kind: "scenario"
title: "MED-DENTAL"
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

# MED-DENTAL

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `MED-DENTAL`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** MED-DENTAL
- **family:** MED
- **name_ru:** Острая стоматологическая проблема травма зуба или отёк
- **scope:** PERSON_TO_GROUP
- **trigger_class:** DENTAL_TRAUMA_SEVERE_PAIN_BLEEDING_OR_SWELLING
- **first_decision_class:** ASSESS_RED_FLAGS
- **decision_sequence:** ASSESS_RED_FLAGS>DENTAL_SERVICE_OR_112_BY_CONDITION
- **decision_condition_notes:** Нарушение дыхания, быстро растущий отёк, тяжёлая травма или кровотечение меняют маршрут на экстренный
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-MED-ILL|MED-ILL]], [[SCN MED-TRAUMA|MED-TRAUMA]], [[XW XW-COM|COM]], [[XW XW-TRANS|TRANS]]
- **spatial_need_codes:** DENTAL_SERVICE|MEDICAL_ACCESS|ROUTE
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** CHILD|ANTICOAGULATION|IMMUNOCOMPROMISED
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** SNS_DGS_DENTAL_SERVICE
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
