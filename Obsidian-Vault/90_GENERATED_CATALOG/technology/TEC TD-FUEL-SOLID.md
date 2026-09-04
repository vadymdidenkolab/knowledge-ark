---
id: "TD-FUEL-SOLID"
kind: "technology"
title: "Древесное топливо; пеллеты; брикеты и древесный уголь"
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

# Древесное топливо; пеллеты; брикеты и древесный уголь

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-SOLID`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-SOLID
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** MATERIAL
- **title_ru:** Древесное топливо; пеллеты; брикеты и древесный уголь
- **outcome:** Catalog sustainable ready solid fuels; moisture; storage; combustion device and ash route
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]], [[TEC TD-FIRE-CO|TD-FIRE-CO]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_APPROVED_APPLIANCE_OR_STOCK
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-024|INS-024]]
- **measurement_acceptance:** Known fuel; dry storage; certified appliance; flue inspection; CO and fire tests; measured consumption
- **calibration_reference:** Moisture method; certified detector and professional flue check
- **drawings_bom_state:** MISSING_FUEL_STORE_AND_APPLIANCE_MANUALS
- **localization_state:** PORTUGAL_FIRE_AIR_AND_FORESTRY_RULES_REQUIRED
- **waste_storage:** Ash cooled and managed only after contamination and soil-use review
- **stop_conditions:** Indoor smoke; CO; chimney defect; treated wood; wildfire restrictions; hot ash
- **maintenance_spares:** Chimney and appliance service; dry stock; seals and detector replacement
- **successor_proof:** Преемник operates only certified appliance and completes shutdown drill
- **evidence_required:** Fuel provenance; moisture; appliance manual; inspections; consumption log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Charcoal manufacture is a separate high-CO and fire process; not authorized here
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
- **capacity_model:** LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE
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
| CONDITIONAL | [[TEC TD-SHELTER-SURVEY|TD-SHELTER-SURVEY]] | SL2 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-FIRE-CO|TD-FIRE-CO]] | SL0 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
