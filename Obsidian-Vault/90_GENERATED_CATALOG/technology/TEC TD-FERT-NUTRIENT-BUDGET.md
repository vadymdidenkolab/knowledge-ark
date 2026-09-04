---
id: "TD-FERT-NUTRIENT-BUDGET"
kind: "technology"
title: "Баланс N-P-K; pH; органического вещества и микроэлементов"
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

# Баланс N-P-K; pH; органического вещества и микроэлементов

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERT-NUTRIENT-BUDGET`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERT-NUTRIENT-BUDGET
- **parent_id:** [[TEC TD-FERTILIZERS|TD-FERTILIZERS]]
- **domain:** FOOD_AGRI
- **node_type:** TEST
- **title_ru:** Баланс N-P-K; pH; органического вещества и микроэлементов
- **outcome:** Identify actual deficit; surplus; removal and loss pathways before adding inputs
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-FOOD-SITE|TD-FOOD-SITE]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** [[PKG PSP-041|PSP-041]], [[PKG PSP-045|PSP-045]], [[PKG SUP-LEA-011|SUP-LEA-011]], [[PKG SUP-LEA-012|SUP-LEA-012]], [[PKG SUP-LEA-014|SUP-LEA-014]], [[PKG SUP-LEA-016|SUP-LEA-016]]
- **materials_tools_state:** NO_LAB_AND_HARVEST_DATA
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-009|INS-009]], [[INS INS-029|INS-029]], [[INS INS-030|INS-030]], [[INS INS-033|INS-033]], [[INS INS-034|INS-034]]
- **measurement_acceptance:** Representative sampling; lab results; crop removal; water balance and uncertainty yield approved range
- **calibration_reference:** Accredited lab; sample controls; verified area and mass
- **drawings_bom_state:** MISSING_SAMPLING_MAP
- **localization_state:** PORTUGAL_LAB_AND_CROP_REQUIRED
- **waste_storage:** Samples and reagents handled per lab instructions
- **stop_conditions:** Unrepresentative sample; unknown contamination; runoff risk; no crop target
- **maintenance_spares:** Before new field plan and periodically
- **successor_proof:** Преемник repeats calculation and flags unsupported result
- **evidence_required:** Sampling map; lab report; equations; reviewer
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Do not infer N-P-K needs from plant color alone
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
- **capacity_model:** KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS
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
| REQUIRED | [[TEC TD-FOOD-SITE|TD-FOOD-SITE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
