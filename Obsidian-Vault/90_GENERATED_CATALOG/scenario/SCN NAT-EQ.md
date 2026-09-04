---
id: "NAT-EQ"
kind: "scenario"
title: "NAT-EQ"
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

# NAT-EQ

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `NAT-EQ`
- **Статус:** `INDEX_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: scenario-register.csv -->
- **scenario_id:** NAT-EQ
- **family:** NAT
- **name_ru:** Землетрясение и афтершоки
- **scope:** LOCAL_TO_REGIONAL
- **trigger_class:** DIRECT_OBSERVATION_OR_OFFICIAL_ALERT
- **first_decision_class:** PROTECT_DURING_SHAKING
- **decision_sequence:** PROTECT_DURING_SHAKING>ASSESS_SCENE_AND_PEOPLE>EXIT_IF_UNSAFE_OR_OFFICIAL_DIRECTION
- **decision_condition_notes:** Сначала защита во время толчков; выход после прекращения толчков, если здание небезопасно или так указано официально
- **decision_sequence_status:** INDEX_ONLY_NOT_REVIEWED
- **capability_ids:** [[XW XW-SHEL|SHEL]], [[XW XW-FIRE|FIRE]], [[SCN MED-TRAUMA|MED-TRAUMA]], [[XW XW-NAV|NAV]], [[XW XW-COM|COM]]
- **spatial_need_codes:** SEISMIC|BUILDING|OPEN_AREA|ROAD
- **map_ids:** TBD
- **route_ids:** TBD
- **site_ids:** TBD
- **modifier_codes:** BUILDING_PROFILE
- **group_size_scope:** N1_TO_N7
- **horizon_scope:** E0_E4
- **source_authority_class:** ANEPC_IPMA_MUNICIPAL
- **content_review_state:** NOT_REVIEWED
- **card_status:** INDEX_ONLY
- **professional_review_required:** YES
- **professional_review_state:** NOT_STARTED
- **review_due:** не заполнено
- **notes:** После события мосты здания и газ требуют отдельной оценки
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
