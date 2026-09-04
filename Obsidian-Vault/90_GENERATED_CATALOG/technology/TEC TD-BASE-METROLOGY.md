---
id: "TD-BASE-METROLOGY"
kind: "technology"
title: "Метрологическое ядро"
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

# Метрологическое ядро

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE-METROLOGY`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE-METROLOGY
- **parent_id:** [[TEC TD-BASE|TD-BASE]]
- **domain:** BASE
- **node_type:** INSTRUMENT
- **title_ru:** Метрологическое ядро
- **outcome:** Получать числа с единицей; диапазоном; проверкой и неопределённостью
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **execution_policy:** HOUSEHOLD_S1_AFTER_GATE
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-METRO-SI|TD-METRO-SI]], [[TEC TD-METRO-LENGTH|TD-METRO-LENGTH]], [[TEC TD-METRO-MASS|TD-METRO-MASS]], [[TEC TD-METRO-TIME|TD-METRO-TIME]], [[TEC TD-METRO-TEMP|TD-METRO-TEMP]], [[TEC TD-METRO-HUMIDITY|TD-METRO-HUMIDITY]], [[TEC TD-METRO-PRESSURE|TD-METRO-PRESSURE]], [[TEC TD-METRO-FLOW|TD-METRO-FLOW]], [[TEC TD-METRO-VOLUME|TD-METRO-VOLUME]], [[TEC TD-METRO-ANGLE|TD-METRO-ANGLE]], [[TEC TD-METRO-ELECTRIC|TD-METRO-ELECTRIC]], [[TEC TD-METRO-LIGHT|TD-METRO-LIGHT]], [[TEC TD-METRO-CO-SMOKE|TD-METRO-CO-SMOKE]], [[TEC TD-METRO-PH|TD-METRO-PH]], [[TEC TD-METRO-EC|TD-METRO-EC]], [[TEC TD-METRO-TURBIDITY|TD-METRO-TURBIDITY]], [[TEC TD-METRO-CHLORINE|TD-METRO-CHLORINE]], [[TEC TD-METRO-SOIL|TD-METRO-SOIL]], [[TEC TD-METRO-MOISTURE|TD-METRO-MOISTURE]], [[TEC TD-METRO-RAIN|TD-METRO-RAIN]], [[TEC TD-METRO-WIND|TD-METRO-WIND]], [[TEC TD-METRO-POSITION|TD-METRO-POSITION]], [[TEC TD-METRO-MEDICAL|TD-METRO-MEDICAL]], [[TEC TD-METRO-REFERENCE|TD-METRO-REFERENCE]], [[TEC TD-METRO-UNCERTAINTY|TD-METRO-UNCERTAINTY]], [[TEC TD-METRO-HISTORY|TD-METRO-HISTORY]], [[TEC TD-METRO-SPARES|TD-METRO-SPARES]], [[TEC TD-METRO-FAILURE|TD-METRO-FAILURE]]
- **source_package_ids:** [[PKG PSP-002|PSP-002]], [[PKG PSP-003|PSP-003]], [[PKG PSP-006|PSP-006]], [[PKG SUP-PHY-003|SUP-PHY-003]], [[PKG SUP-PHY-004|SUP-PHY-004]]
- **materials_tools_state:** 73_CLASSES_NOT_INVENTORIED
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-003|INS-003]], [[INS INS-008|INS-008]], [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-026|INS-026]], [[INS INS-045|INS-045]]
- **measurement_acceptance:** Для каждого critical measurand выбрана модель; range; resolution; check и журнал
- **calibration_reference:** Прослеживаемый эталон; контрольная точка или документированное сравнение по методу
- **drawings_bom_state:** MISSING_PER_INSTRUMENT
- **localization_state:** PORTUGAL_AND_TASK_REQUIRED
- **waste_storage:** Не применимо
- **stop_conditions:** Прибор повреждён; вне диапазона; контрольная точка не пройдена
- **maintenance_spares:** По инструкции; после удара или ремонта; перед критическим применением
- **successor_proof:** Преемник выполняет контрольную проверку и правильно бракует неверный результат
- **evidence_required:** Asset list; calibration/check logs; uncertainty budget
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Реестр классов не равен наличию приборов
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
- **capacity_model:** OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |
| REQUIRED | [[TEC TD-METRO-SI|TD-METRO-SI]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-LENGTH|TD-METRO-LENGTH]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-MASS|TD-METRO-MASS]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-TIME|TD-METRO-TIME]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-TEMP|TD-METRO-TEMP]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-HUMIDITY|TD-METRO-HUMIDITY]] | SL3 | — |
| CONDITIONAL | [[TEC TD-METRO-PRESSURE|TD-METRO-PRESSURE]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-METRO-FLOW|TD-METRO-FLOW]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-VOLUME|TD-METRO-VOLUME]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-ANGLE|TD-METRO-ANGLE]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-ELECTRIC|TD-METRO-ELECTRIC]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-LIGHT|TD-METRO-LIGHT]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-CO-SMOKE|TD-METRO-CO-SMOKE]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-PH|TD-METRO-PH]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-EC|TD-METRO-EC]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-TURBIDITY|TD-METRO-TURBIDITY]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-CHLORINE|TD-METRO-CHLORINE]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-SOIL|TD-METRO-SOIL]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-MOISTURE|TD-METRO-MOISTURE]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-RAIN|TD-METRO-RAIN]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-WIND|TD-METRO-WIND]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-POSITION|TD-METRO-POSITION]] | SL3 | — |
| CONDITIONAL | [[TEC TD-METRO-MEDICAL|TD-METRO-MEDICAL]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-METRO-REFERENCE|TD-METRO-REFERENCE]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-UNCERTAINTY|TD-METRO-UNCERTAINTY]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-HISTORY|TD-METRO-HISTORY]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-SPARES|TD-METRO-SPARES]] | SL3 | — |
| REQUIRED | [[TEC TD-METRO-FAILURE|TD-METRO-FAILURE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
