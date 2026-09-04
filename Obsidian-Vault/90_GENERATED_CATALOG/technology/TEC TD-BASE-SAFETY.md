---
id: "TD-BASE-SAFETY"
kind: "technology"
title: "Safety gates и полномочия"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S0_OBSERVE_READ"
execution_gate: "DENY"
status: "ARCHITECTURE_ONLY"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Safety gates и полномочия

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE-SAFETY`
- **Статус:** `ARCHITECTURE_ONLY`
- **Приоритет:** `P0_RED`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S0_OBSERVE_READ`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE-SAFETY
- **parent_id:** [[TEC TD-BASE|TD-BASE]]
- **domain:** BASE
- **node_type:** GOVERNANCE
- **title_ru:** Safety gates и полномочия
- **outcome:** Определить допустимый класс работы и право остановки
- **safety_class:** S0_OBSERVE_READ
- **execution_policy:** HOUSEHOLD_S0
- **prerequisite_node_ids:** не заполнено
- **source_package_ids:** [[SAFE SG-01|SG-01]], [[SAFE SG-02|SG-02]], [[SAFE SG-03|SG-03]], [[SAFE SG-04|SG-04]], [[SAFE SG-05|SG-05]], [[SAFE SG-06|SG-06]], [[SAFE SG-07|SG-07]], [[SAFE SG-08|SG-08]], [[SAFE SG-09|SG-09]], [[SAFE SG-10|SG-10]], [[SAFE SG-11|SG-11]], [[SAFE SG-12|SG-12]], [[SAFE SG-13|SG-13]], [[SAFE SG-14|SG-14]], [[SAFE SG-15|SG-15]], [[SAFE SG-16|SG-16]], [[SAFE SG-17|SG-17]]
- **materials_tools_state:** LOCAL_RULES_PRESENT
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Все опасности сопоставлены S0-S4; ответственный и stop назначены
- **calibration_reference:** Текущая локальная правовая и профессиональная проверка
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_REVIEW_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Неясный риск; полномочие; площадка или аварийный маршрут
- **maintenance_spares:** Ежегодный review и после инцидента
- **successor_proof:** Другой участник правильно классифицирует пять тестовых случаев
- **evidence_required:** Review record; version; jurisdiction
- **evidence_state:** LOCAL_UNREVIEWED
- **capability_status:** ARCHITECTURE_ONLY
- **release_gate:** DENY
- **notes:** 17 no-go существуют; внешняя профессиональная проверка не выполнена
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P0_RED
- **priority_horizon:** SECONDS_TO_72_HOURS
- **earliest_service_level:** SL1
- **life_criticality:** IMMEDIATE_OR_SAFETY_BOUNDARY
- **build_sequence_tier:** P0_RED
- **acquisition_priority:** P0_RED
- **knowledge_priority:** P0_RED
- **safety_lane:** S0_OBSERVE_READ
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE
- **capacity_value:** TBD_PERSON_AND_SITE_PROFILE
- **capacity_unit:** TBD_BY_CAPABILITY
- **labor_hours:** TBD
- **failure_domain:** TBD_SITE_AND_IMPLEMENTATION
- **redundancy_target:** TWO_PATHS_OR_EXPLICIT_RESIDUAL_RISK
- **owner_role:** UNASSIGNED
- **backup_role:** UNASSIGNED
- **drill_id:** NOT_ASSIGNED
- **next_due:** TBD
- **human_review_state:** PROVISIONAL_AUTO_REVIEW_REQUIRED
- **release_gate:** DENY
- **release_version:** 0.5-draft

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
