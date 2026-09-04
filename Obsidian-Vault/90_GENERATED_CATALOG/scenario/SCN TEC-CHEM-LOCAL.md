---
id: "TEC-CHEM-LOCAL"
kind: "scenario"
title: "TEC-CHEM-LOCAL"
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

# TEC-CHEM-LOCAL

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TEC-CHEM-LOCAL`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** TEC-CHEM-LOCAL
- **family:** TEC
- **name_ru:** Локальный химический разлив или непосредственная экспозиция
- **scope:** LOCAL_SCENE
- **trigger_class:** DIRECT_EXPOSURE_OR_LOCAL_RELEASE
- **first_decision_class:** REMOVE_FROM_EXPOSURE_IF_SAFE
- **decision_sequence:** REMOVE_FROM_EXPOSURE_IF_SAFE>CALL_112_OR_CIAV>DECONTAMINATION_ONLY_PER_SAFE_GUIDANCE
- **decision_condition_notes:** Не входить в облако и не ждать точной идентификации перед прекращением безопасно устранимой экспозиции
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-PPE|PPE]], [[XW XW-AIR|AIR]], [[XW XW-COM|COM]], [[XW XW-MED-ILL|MED-ILL]], [[XW XW-NAV|NAV]]
- **spatial_need_codes:** SEVESO|WIND|NO_GO|MEDICAL_ACCESS
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** INDUSTRIAL_NEARBY
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_APA_DGS_CIAV
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** Уйти или укрыться зависит от вещества и официальной команды
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
