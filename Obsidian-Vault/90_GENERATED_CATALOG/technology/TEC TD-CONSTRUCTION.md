---
id: "TD-CONSTRUCTION"
kind: "technology"
title: "Строительство; обследование и as-built обслуживание"
priority_tier: "P3_GREEN"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LICENSED_PROFESSIONAL"
safety_class: "S3_LICENSED_PROFESSIONAL"
execution_gate: "BLACK_GATE_LICENSED_ONLY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Строительство; обследование и as-built обслуживание

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-CONSTRUCTION`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-CONSTRUCTION
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** CONSTRUCTION
- **node_type:** OUTCOME
- **title_ru:** Строительство; обследование и as-built обслуживание
- **outcome:** Иметь измеримую и проверяемую способность: строительство; обследование и as-built обслуживание
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-CONSTRUCTION-SITE|TD-CONSTRUCTION-SITE]], [[TEC TD-CONSTRUCTION-EARTHWORKS|TD-CONSTRUCTION-EARTHWORKS]], [[TEC TD-CONSTRUCTION-FOUNDATION|TD-CONSTRUCTION-FOUNDATION]], [[TEC TD-CONSTRUCTION-FRAME|TD-CONSTRUCTION-FRAME]], [[TEC TD-CONSTRUCTION-WALLS|TD-CONSTRUCTION-WALLS]], [[TEC TD-CONSTRUCTION-FLOORS|TD-CONSTRUCTION-FLOORS]], [[TEC TD-CONSTRUCTION-ROOF|TD-CONSTRUCTION-ROOF]], [[TEC TD-CONSTRUCTION-WEATHER|TD-CONSTRUCTION-WEATHER]], [[TEC TD-CONSTRUCTION-WINDOWS|TD-CONSTRUCTION-WINDOWS]], [[TEC TD-CONSTRUCTION-DOORS|TD-CONSTRUCTION-DOORS]], [[TEC TD-CONSTRUCTION-INSULATION|TD-CONSTRUCTION-INSULATION]], [[TEC TD-CONSTRUCTION-MOISTURE|TD-CONSTRUCTION-MOISTURE]], [[TEC TD-CONSTRUCTION-PLUMBING|TD-CONSTRUCTION-PLUMBING]], [[TEC TD-CONSTRUCTION-SANITATION|TD-CONSTRUCTION-SANITATION]], [[TEC TD-CONSTRUCTION-ELECTRICAL|TD-CONSTRUCTION-ELECTRICAL]], [[TEC TD-CONSTRUCTION-VENTILATION|TD-CONSTRUCTION-VENTILATION]], [[TEC TD-CONSTRUCTION-HVAC|TD-CONSTRUCTION-HVAC]], [[TEC TD-CONSTRUCTION-FIRE|TD-CONSTRUCTION-FIRE]], [[TEC TD-CONSTRUCTION-SEISMIC|TD-CONSTRUCTION-SEISMIC]], [[TEC TD-CONSTRUCTION-WIND|TD-CONSTRUCTION-WIND]], [[TEC TD-CONSTRUCTION-FLOOD|TD-CONSTRUCTION-FLOOD]], [[TEC TD-CONSTRUCTION-WILDFIRE|TD-CONSTRUCTION-WILDFIRE]], [[TEC TD-CONSTRUCTION-ACCESS|TD-CONSTRUCTION-ACCESS]], [[TEC TD-CONSTRUCTION-TEMP|TD-CONSTRUCTION-TEMP]], [[TEC TD-CONSTRUCTION-PERMITS|TD-CONSTRUCTION-PERMITS]], [[TEC TD-CONSTRUCTION-INSPECTION|TD-CONSTRUCTION-INSPECTION]], [[TEC TD-CONSTRUCTION-AS-BUILT|TD-CONSTRUCTION-AS-BUILT]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING
- **instrument_ids:** не заполнено
- **measurement_acceptance:** До использования задать service level, единицу, объём, срок и критерий приёмки
- **calibration_reference:** Точный метод, прибор/reference и неопределённость TBD до исполнения
- **drawings_bom_state:** MISSING_OR_NOT_APPLICABLE
- **localization_state:** PORTUGAL_AND_SITE_REVIEW_REQUIRED
- **waste_storage:** Потоки, совместимость, хранение и законный маршрут TBD до исполнения
- **stop_conditions:** Неизвестная идентичность; отсутствующее полномочие; опасная среда; непроверенный источник; выход за подготовку
- **maintenance_spares:** Периодичность, расходники, запасные части и failure signs TBD
- **successor_proof:** Другой назначенный участник находит карточку и демонстрирует допустимую часть без устной помощи автора
- **evidence_required:** Профиль; источник; инвентарь; измерения; acceptance log; reviewer; дата
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Агрегат: обязательность дочерних узлов определяется technology-dependency-edges.csv
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL5
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S3_LICENSED_PROFESSIONAL
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** AREA_LOAD_WEATHER_WINDOW_LABOR_AND_INSPECTION
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-SITE|TD-CONSTRUCTION-SITE]] | SL5 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-EARTHWORKS|TD-CONSTRUCTION-EARTHWORKS]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-FOUNDATION|TD-CONSTRUCTION-FOUNDATION]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-FRAME|TD-CONSTRUCTION-FRAME]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-WALLS|TD-CONSTRUCTION-WALLS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-FLOORS|TD-CONSTRUCTION-FLOORS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-ROOF|TD-CONSTRUCTION-ROOF]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-WEATHER|TD-CONSTRUCTION-WEATHER]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-WINDOWS|TD-CONSTRUCTION-WINDOWS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-DOORS|TD-CONSTRUCTION-DOORS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-INSULATION|TD-CONSTRUCTION-INSULATION]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-MOISTURE|TD-CONSTRUCTION-MOISTURE]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-PLUMBING|TD-CONSTRUCTION-PLUMBING]] | SL5 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-SANITATION|TD-CONSTRUCTION-SANITATION]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-ELECTRICAL|TD-CONSTRUCTION-ELECTRICAL]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-VENTILATION|TD-CONSTRUCTION-VENTILATION]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-HVAC|TD-CONSTRUCTION-HVAC]] | SL5 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-FIRE|TD-CONSTRUCTION-FIRE]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-SEISMIC|TD-CONSTRUCTION-SEISMIC]] | SL1 | not_an_operational_prerequisite |
| HAZARD_ONLY | [[TEC TD-CONSTRUCTION-WIND|TD-CONSTRUCTION-WIND]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-FLOOD|TD-CONSTRUCTION-FLOOD]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-WILDFIRE|TD-CONSTRUCTION-WILDFIRE]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-ACCESS|TD-CONSTRUCTION-ACCESS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-TEMP|TD-CONSTRUCTION-TEMP]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-PERMITS|TD-CONSTRUCTION-PERMITS]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-INSPECTION|TD-CONSTRUCTION-INSPECTION]] | SL5 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-CONSTRUCTION-AS-BUILT|TD-CONSTRUCTION-AS-BUILT]] | SL5 | applicable_profile_site_or_qualified_role_required |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
