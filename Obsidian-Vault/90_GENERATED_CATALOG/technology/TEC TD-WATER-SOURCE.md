---
id: "TD-WATER-SOURCE"
kind: "technology"
title: "Карта законных источников воды"
priority_tier: "P2_YELLOW"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Карта законных источников воды

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WATER-SOURCE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WATER-SOURCE
- **parent_id:** [[TEC TD-WATER|TD-WATER]]
- **domain:** WATER_WASH
- **node_type:** SITE_DATA
- **title_ru:** Карта законных источников воды
- **outcome:** Определить основной и независимый резервный источники
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[PKG SUP-LEA-033|SUP-LEA-033]]
- **materials_tools_state:** MISSING_SOURCE_MAP
- **instrument_ids:** [[INS INS-040|INS-040]], [[INS INS-061|INS-061]], [[INS INS-062|INS-062]]
- **measurement_acceptance:** Источник; доступ; ownership; сезонность и загрязнители записаны; минимум два failure domain
- **calibration_reference:** Координаты cross-check; фото; официальный или лабораторный источник данных
- **drawings_bom_state:** MISSING_MAP
- **localization_state:** PORTUGAL_MUNICIPALITY_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Не входить в колодец; резервуар; затопленную или загрязнённую зону
- **maintenance_spares:** Сезонный review и после события
- **successor_proof:** Преемник находит источники и safe no-go точки
- **evidence_required:** Map; permissions; photos; season log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Адрес и муниципалитет ещё не заданы
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
- **safety_lane:** S1_LOW_RISK_HOUSEHOLD
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
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
