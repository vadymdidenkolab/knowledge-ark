---
id: "TD-FUEL-VEGOIL"
kind: "technology"
title: "Механическое получение растительного масла"
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

# Механическое получение растительного масла

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-VEGOIL`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-VEGOIL
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** PROCESS
- **title_ru:** Механическое получение растительного масла
- **outcome:** Catalog crop; food-versus-fuel tradeoff; pressing; filtration; storage and safe non-engine uses
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-FOOD-SITE|TD-FOOD-SITE]], [[TEC TD-HARVEST-STORAGE|TD-HARVEST-STORAGE]], [[TEC TD-WORKSHOP|TD-WORKSHOP]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_PRESS_OR_CROP_EVIDENCE
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-011|INS-011]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]]
- **measurement_acceptance:** Known seed; measured oil yield; contamination controls; food allocation and storage stability reviewed
- **calibration_reference:** Scale; reference sample; crop-specific quality method
- **drawings_bom_state:** MISSING_PRESS_PACKAGE
- **localization_state:** PORTUGAL_FOOD_FEED_WASTE_AND_FUEL_RULES_REQUIRED
- **waste_storage:** Press cake; rancid oil and filters routed by intended use and contamination
- **stop_conditions:** Unknown or treated seed; mold; machinery pinch; hot bearing; solvent extraction
- **maintenance_spares:** Press inspection; food-contact cleaning; spare wear parts
- **successor_proof:** Преемник conducts only an approved low-energy mechanical demonstration
- **evidence_required:** Crop lot; yield log; machine guards; quality and allocation review
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Solvent extraction and direct engine use are not included
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
| REQUIRED | [[TEC TD-FOOD-SITE|TD-FOOD-SITE]] | SL3 | — |
| REQUIRED | [[TEC TD-HARVEST-STORAGE|TD-HARVEST-STORAGE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP|TD-WORKSHOP]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
