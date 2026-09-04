---
id: "TEC-CHEM-PLUME"
kind: "scenario"
title: "TEC-CHEM-PLUME"
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

# TEC-CHEM-PLUME

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TEC-CHEM-PLUME`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** TEC-CHEM-PLUME
- **family:** TEC
- **name_ru:** Внешнее химическое облако или промышленный выброс
- **scope:** LOCAL_TO_REGIONAL
- **trigger_class:** OFFICIAL_ALERT_OR_OBSERVED_EXTERNAL_RELEASE
- **first_decision_class:** SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION
- **decision_sequence:** SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION>CONTROL_AIR_PATHS_IF_SHELTERED>REASSESS_FROM_OFFICIAL_SOURCE
- **decision_condition_notes:** Направление ухода или укрытие зависят от вещества, ветра, здания и официальной команды; не строить бытовую plume-модель
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-PPE|PPE]], [[XW XW-AIR|AIR]], [[XW XW-COM|COM]], [[XW XW-MED-ILL|MED-ILL]], [[XW XW-NAV|NAV]]
- **spatial_need_codes:** SEVESO|WIND|OFFICIAL_ZONE|NO_GO|MEDICAL_ACCESS
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** INDUSTRIAL_NEARBY|RESPIRATORY_DISEASE|MOBILITY_LIMITATION
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_APA_DGS_CIAV
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
