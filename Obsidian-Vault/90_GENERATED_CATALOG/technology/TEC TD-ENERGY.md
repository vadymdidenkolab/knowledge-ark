---
id: "TD-ENERGY"
kind: "technology"
title: "Энергия для критических функций"
priority_tier: "P1_ORANGE"
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

# Энергия для критических функций

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ENERGY`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ENERGY
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** ENERGY
- **node_type:** OUTCOME
- **title_ru:** Энергия для критических функций
- **outcome:** Питать приоритетные нагрузки с безопасным отключением and recovery
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]], [[TEC TD-ENERGY-DC|TD-ENERGY-DC]], [[TEC TD-ENERGY-GENERATION|TD-ENERGY-GENERATION]], [[TEC TD-ENERGY-STORAGE|TD-ENERGY-STORAGE]], [[TEC TD-ENERGY-PROTECTION|TD-ENERGY-PROTECTION]], [[TEC TD-ENERGY-BLACKSTART|TD-ENERGY-BLACKSTART]], [[TEC TD-ENERGY-LIGHT|TD-ENERGY-LIGHT]], [[TEC TD-ENERGY-COMMS|TD-ENERGY-COMMS]], [[TEC TD-ENERGY-MEDICAL|TD-ENERGY-MEDICAL]], [[TEC TD-ENERGY-COLD-CHAIN|TD-ENERGY-COLD-CHAIN]], [[TEC TD-ENERGY-LOAD-SHED|TD-ENERGY-LOAD-SHED]], [[TEC TD-ENERGY-FLASHLIGHT|TD-ENERGY-FLASHLIGHT]], [[TEC TD-ENERGY-BATTERY-STANDARD|TD-ENERGY-BATTERY-STANDARD]], [[TEC TD-ENERGY-POWERBANK|TD-ENERGY-POWERBANK]], [[TEC TD-ENERGY-SOURCE|TD-ENERGY-SOURCE]], [[TEC TD-ENERGY-CHARGE|TD-ENERGY-CHARGE]], [[TEC TD-ENERGY-FAILURE|TD-ENERGY-FAILURE]], [[TEC TD-ENERGY-SPARES|TD-ENERGY-SPARES]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_SYSTEM
- **instrument_ids:** [[INS INS-045|INS-045]], [[INS INS-047|INS-047]], [[INS INS-048|INS-048]], [[INS INS-052|INS-052]], [[INS INS-053|INS-053]], [[INS INS-054|INS-054]]
- **measurement_acceptance:** Measured Wh/day; autonomy; protection; isolation; thermal limits and black-start test pass
- **calibration_reference:** Reference meter; professional electrical inspection; OEM checks
- **drawings_bom_state:** MISSING_SINGLE_LINE_AND_BOM
- **localization_state:** PORTUGAL_ELECTRICAL_RULES_AND_SITE_REQUIRED
- **waste_storage:** Batteries; electronics and fuel routed legally
- **stop_conditions:** Live mains; backfeed; damaged battery; heat; smoke; unknown wiring
- **maintenance_spares:** Scheduled load test; firmware/manuals; spares; manual fallback
- **successor_proof:** Qualified successor performs authorized start and shutdown
- **evidence_required:** Single-line; BOM; inspection; logs; drill
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Household may operate only exact user controls
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P1_ORANGE
- **priority_horizon:** 3_TO_14_DAYS
- **earliest_service_level:** SL2
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P1_ORANGE
- **acquisition_priority:** P1_ORANGE
- **knowledge_priority:** P1_ORANGE
- **safety_lane:** S3_LICENSED_PROFESSIONAL
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME
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

<details>
<summary>Типизированные зависимости</summary>

| Роль | Узел | Service level | Условие / группа |
|---|---|---|---|
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-ENERGY-LOADS|TD-ENERGY-LOADS]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-DC|TD-ENERGY-DC]] | SL2 | — |
| ALTERNATIVE | [[TEC TD-ENERGY-GENERATION|TD-ENERGY-GENERATION]] | SL2 | ENERGY_SUPPLY |
| CONDITIONAL | [[TEC TD-ENERGY-STORAGE|TD-ENERGY-STORAGE]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ENERGY-PROTECTION|TD-ENERGY-PROTECTION]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-ENERGY-BLACKSTART|TD-ENERGY-BLACKSTART]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-LIGHT|TD-ENERGY-LIGHT]] | SL1 | — |
| REQUIRED | [[TEC TD-ENERGY-COMMS|TD-ENERGY-COMMS]] | SL1 | — |
| REQUIRED | [[TEC TD-ENERGY-MEDICAL|TD-ENERGY-MEDICAL]] | SL1 | — |
| REQUIRED | [[TEC TD-ENERGY-COLD-CHAIN|TD-ENERGY-COLD-CHAIN]] | SL1 | — |
| REQUIRED | [[TEC TD-ENERGY-LOAD-SHED|TD-ENERGY-LOAD-SHED]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-FLASHLIGHT|TD-ENERGY-FLASHLIGHT]] | SL1 | — |
| REQUIRED | [[TEC TD-ENERGY-BATTERY-STANDARD|TD-ENERGY-BATTERY-STANDARD]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-POWERBANK|TD-ENERGY-POWERBANK]] | SL2 | — |
| ALTERNATIVE | [[TEC TD-ENERGY-SOURCE|TD-ENERGY-SOURCE]] | SL2 | ENERGY_SUPPLY |
| REQUIRED | [[TEC TD-ENERGY-CHARGE|TD-ENERGY-CHARGE]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-FAILURE|TD-ENERGY-FAILURE]] | SL2 | — |
| REQUIRED | [[TEC TD-ENERGY-SPARES|TD-ENERGY-SPARES]] | SL2 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
