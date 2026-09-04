---
id: "TEC-CO"
kind: "scenario"
title: "TEC-CO"
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

# TEC-CO

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TEC-CO`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** TEC-CO
- **family:** TEC
- **name_ru:** Угарный газ или продукты горения
- **scope:** BUILDING_OR_VEHICLE
- **trigger_class:** ALARM_OR_SYMPTOM
- **first_decision_class:** EXIT_AND_DO_NOT_RETURN
- **decision_sequence:** EXIT_AND_DO_NOT_RETURN
- **decision_condition_notes:** Не искать источник внутри при продолжающейся опасности
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-FIRE|FIRE]], [[XW XW-AIR|AIR]], [[XW XW-MED-ILL|MED-ILL]], [[XW XW-COM|COM]]
- **spatial_need_codes:** BUILDING_EXIT|MEDICAL_ACCESS
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** GENERATOR
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_DGS_FIRE_SERVICE
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Не искать источник внутри при продолжающейся опасности
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
