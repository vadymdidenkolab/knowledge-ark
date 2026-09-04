---
id: "TD-FUEL-LUBRICANTS"
kind: "technology"
title: "Смазки; гидравлические и охлаждающие жидкости"
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

# Смазки; гидравлические и охлаждающие жидкости

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-LUBRICANTS`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-LUBRICANTS
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** MATERIAL
- **title_ru:** Смазки; гидравлические и охлаждающие жидкости
- **outcome:** Keep exact specifications; compatibility; shelf life; contamination control and substitutes
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]], [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_ASSET_SPECIFIC_LUBE_REGISTER
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Every asset maps to exact grade; quantity; change interval; contamination check and approved substitute
- **calibration_reference:** OEM manual; batch label; temperature range
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_CHEMICAL_AND_WASTE_RULES_REQUIRED
- **waste_storage:** Used oils and fluids via licensed collection
- **stop_conditions:** Wrong grade; water contamination; unknown mix; leak; hot system; pressure
- **maintenance_spares:** Per OEM; sealed stock rotation; filters and seals
- **successor_proof:** Преемник selects correct product and rejects unsafe substitution
- **evidence_required:** OEM refs; SDS; lot; service logs; substitute approval
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Vegetable oil is not automatically a safe machinery lubricant
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
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-INVENTORY|TD-BASE-INVENTORY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-MAINTENANCE|TD-BASE-MAINTENANCE]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
