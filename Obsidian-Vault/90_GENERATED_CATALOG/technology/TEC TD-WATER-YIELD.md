---
id: "TD-WATER-YIELD"
kind: "technology"
title: "Сезонная производительность источника"
priority_tier: "P2_YELLOW"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "TRAINED_SUPERVISED"
safety_class: "S2_TRAINED_SUPERVISED"
execution_gate: "DENY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Сезонная производительность источника

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WATER-YIELD`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WATER-YIELD
- **parent_id:** [[TEC TD-WATER|TD-WATER]]
- **domain:** WATER_WASH
- **node_type:** TEST
- **title_ru:** Сезонная производительность источника
- **outcome:** Доказать сколько воды реально доступно без истощения источника
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_TEST_SETUP
- **instrument_ids:** [[INS INS-011|INS-011]], [[INS INS-026|INS-026]], [[INS INS-027|INS-027]]
- **measurement_acceptance:** Повторные измерения в сухой и влажный сезон; demand не превышает консервативный yield
- **calibration_reference:** Объёмная timed-volume проверка и независимое повторение
- **drawings_bom_state:** MISSING_METHOD
- **localization_state:** SITE_AND_SEASON_REQUIRED
- **waste_storage:** Вода теста не загрязняет источник
- **stop_conditions:** Падение уровня; мутность; подсос; опасный доступ; unknown well condition
- **maintenance_spares:** Повтор по сезону и после ремонта
- **successor_proof:** Преемник повторяет расчёт и называет uncertainty
- **evidence_required:** Raw log; dates; weather; yield model; reviewer
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Шаблон существует; измерений нет
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P2_YELLOW
- **priority_horizon:** 15_TO_90_DAYS
- **earliest_service_level:** SL3
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P2_YELLOW
- **acquisition_priority:** P2_YELLOW
- **knowledge_priority:** P2_YELLOW
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS
- **capacity_value:** TBD_PERSON_AND_SITE_PROFILE
- **capacity_unit:** TBD_BY_CAPABILITY
- **labor_hours:** TBD
- **failure_domain:** TBD_SITE_AND_IMPLEMENTATION
- **redundancy_target:** TBD_BY_SERVICE_LEVEL
- **owner_role:** UNASSIGNED
- **backup_role:** UNASSIGNED
- **drill_id:** NOT_ASSIGNED
- **next_due:** TBD
- **human_review_state:** PROVISIONAL_AUTO_REVIEW_REQUIRED
- **release_gate:** DENY
- **release_version:** 0.5-draft

</details>

<details>
<summary>Типизированные зависимости</summary>

| Роль | Узел | Service level | Условие / группа |
|---|---|---|---|
| REQUIRED | [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
