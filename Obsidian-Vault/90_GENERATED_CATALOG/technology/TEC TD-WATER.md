---
id: "TD-WATER"
kind: "technology"
title: "Безопасная вода и санитария"
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

# Безопасная вода и санитария

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WATER`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WATER
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** WATER_WASH
- **node_type:** OUTCOME
- **title_ru:** Безопасная вода и санитария
- **outcome:** Дать измеренный объём воды и не загрязнить людей; пищу и источник
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]], [[TEC TD-WATER-YIELD|TD-WATER-YIELD]], [[TEC TD-WATER-RISK|TD-WATER-RISK]], [[TEC TD-WATER-TREATMENT|TD-WATER-TREATMENT]], [[TEC TD-WATER-STORAGE|TD-WATER-STORAGE]], [[TEC TD-WATER-MONITORING|TD-WATER-MONITORING]], [[TEC TD-SANITATION|TD-SANITATION]], [[TEC TD-WATER-P0-RESERVE|TD-WATER-P0-RESERVE]], [[TEC TD-WATER-DEMAND|TD-WATER-DEMAND]], [[TEC TD-WATER-RATION|TD-WATER-RATION]], [[TEC TD-WATER-VULNERABLE|TD-WATER-VULNERABLE]], [[TEC TD-WATER-COLLECTION|TD-WATER-COLLECTION]], [[TEC TD-WATER-CARRY|TD-WATER-CARRY]], [[TEC TD-WATER-CROSS-CONTAM|TD-WATER-CROSS-CONTAM]], [[TEC TD-WATER-LABEL|TD-WATER-LABEL]], [[TEC TD-WATER-EMERGENCY-PRODUCT|TD-WATER-EMERGENCY-PRODUCT]], [[TEC TD-WATER-CONTAINER-CLEAN|TD-WATER-CONTAINER-CLEAN]], [[TEC TD-WATER-PORTFOLIO|TD-WATER-PORTFOLIO]], [[TEC TD-WATER-RAIN|TD-WATER-RAIN]], [[TEC TD-WATER-DELIVERED|TD-WATER-DELIVERED]], [[TEC TD-WATER-WELL|TD-WATER-WELL]], [[TEC TD-WATER-SURFACE|TD-WATER-SURFACE]], [[TEC TD-WATER-GRAVITY|TD-WATER-GRAVITY]], [[TEC TD-WATER-HAND-PUMP|TD-WATER-HAND-PUMP]], [[TEC TD-WATER-LOWE-PUMP|TD-WATER-LOWE-PUMP]], [[TEC TD-WATER-DISTRIBUTION|TD-WATER-DISTRIBUTION]], [[TEC TD-WATER-BACKFLOW|TD-WATER-BACKFLOW]], [[TEC TD-WATER-LEAK|TD-WATER-LEAK]], [[TEC TD-WATER-SPARES|TD-WATER-SPARES]], [[TEC TD-WATER-LAB|TD-WATER-LAB]], [[TEC TD-WATER-REDUNDANCY|TD-WATER-REDUNDANCY]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_SITE_SYSTEM
- **instrument_ids:** [[INS INS-026|INS-026]], [[INS INS-027|INS-027]], [[INS INS-029|INS-029]], [[INS INS-030|INS-030]], [[INS INS-031|INS-031]], [[INS INS-032|INS-032]]
- **measurement_acceptance:** Объём; качество; throughput и stop соответствуют точному water safety plan
- **calibration_reference:** Laboratory plan плюс instrument checks
- **drawings_bom_state:** MISSING
- **localization_state:** PORTUGAL_SOURCE_AND_SITE_REQUIRED
- **waste_storage:** Отдельный безопасный маршрут стоков и отработанных материалов
- **stop_conditions:** Неизвестное химическое или радиологическое загрязнение; failed barrier; flood intrusion
- **maintenance_spares:** Scheduled sampling; cleaning; seals; manual fallback
- **successor_proof:** Другой участник запускает safe mode и объясняет когда воду нельзя объявлять безопасной
- **evidence_required:** Water safety plan; lab data; logs; drawings; drill
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Бытовой датчик не доказывает микробиологическую безопасность
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
| REQUIRED | [[TEC TD-BASE|TD-BASE]] | SL3 | — |
| REQUIRED | [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]] | SL3 | — |
| REQUIRED | [[TEC TD-WATER-YIELD|TD-WATER-YIELD]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WATER-RISK|TD-WATER-RISK]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WATER-TREATMENT|TD-WATER-TREATMENT]] | SL3 | — |
| REQUIRED | [[TEC TD-WATER-STORAGE|TD-WATER-STORAGE]] | SL3 | — |
| REQUIRED | [[TEC TD-WATER-MONITORING|TD-WATER-MONITORING]] | SL3 | — |
| REQUIRED | [[TEC TD-SANITATION|TD-SANITATION]] | SL2 | — |
| REQUIRED | [[TEC TD-WATER-P0-RESERVE|TD-WATER-P0-RESERVE]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-DEMAND|TD-WATER-DEMAND]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-RATION|TD-WATER-RATION]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-VULNERABLE|TD-WATER-VULNERABLE]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-COLLECTION|TD-WATER-COLLECTION]] | SL3 | — |
| REQUIRED | [[TEC TD-WATER-CARRY|TD-WATER-CARRY]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-CROSS-CONTAM|TD-WATER-CROSS-CONTAM]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-LABEL|TD-WATER-LABEL]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-EMERGENCY-PRODUCT|TD-WATER-EMERGENCY-PRODUCT]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-CONTAINER-CLEAN|TD-WATER-CONTAINER-CLEAN]] | SL1 | — |
| REQUIRED | [[TEC TD-WATER-PORTFOLIO|TD-WATER-PORTFOLIO]] | SL2 | — |
| ALTERNATIVE | [[TEC TD-WATER-RAIN|TD-WATER-RAIN]] | SL2 | WATER_SOURCE |
| ALTERNATIVE | [[TEC TD-WATER-DELIVERED|TD-WATER-DELIVERED]] | SL2 | WATER_SOURCE |
| ALTERNATIVE | [[TEC TD-WATER-WELL|TD-WATER-WELL]] | SL3 | WATER_SOURCE |
| ALTERNATIVE | [[TEC TD-WATER-SURFACE|TD-WATER-SURFACE]] | SL3 | WATER_SOURCE |
| ALTERNATIVE | [[TEC TD-WATER-GRAVITY|TD-WATER-GRAVITY]] | SL2 | WATER_DELIVERY |
| ALTERNATIVE | [[TEC TD-WATER-HAND-PUMP|TD-WATER-HAND-PUMP]] | SL2 | WATER_DELIVERY |
| ALTERNATIVE | [[TEC TD-WATER-LOWE-PUMP|TD-WATER-LOWE-PUMP]] | SL2 | WATER_DELIVERY |
| REQUIRED | [[TEC TD-WATER-DISTRIBUTION|TD-WATER-DISTRIBUTION]] | SL2 | — |
| CONDITIONAL | [[TEC TD-WATER-BACKFLOW|TD-WATER-BACKFLOW]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WATER-LEAK|TD-WATER-LEAK]] | SL2 | — |
| REQUIRED | [[TEC TD-WATER-SPARES|TD-WATER-SPARES]] | SL2 | — |
| CONDITIONAL | [[TEC TD-WATER-LAB|TD-WATER-LAB]] | SL3 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WATER-REDUNDANCY|TD-WATER-REDUNDANCY]] | SL2 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
