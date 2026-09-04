---
id: "TD-FUEL-STORAGE"
kind: "technology"
title: "Хранение готового законного топлива"
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

# Хранение готового законного топлива

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FUEL-STORAGE`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FUEL-STORAGE
- **parent_id:** [[TEC TD-FUELS|TD-FUELS]]
- **domain:** ENERGY_FUELS
- **node_type:** MATERIAL
- **title_ru:** Хранение готового законного топлива
- **outcome:** Retain only permitted quantities in certified compatible containers away from people; food; water and ignition
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-FUEL-DEMAND|TD-FUEL-DEMAND]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_APPROVED_STORAGE
- **instrument_ids:** [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-024|INS-024]], [[INS INS-071|INS-071]]
- **measurement_acceptance:** Fire-code and environmental review; container compatibility; labels; secondary containment; turnover and emergency access pass
- **calibration_reference:** Manufacturer container specification; fire professional inspection
- **drawings_bom_state:** MISSING_STORAGE_PLAN
- **localization_state:** PORTUGAL_LOCAL_RULES_REQUIRED
- **waste_storage:** Licensed fuel and contaminated-absorbent disposal
- **stop_conditions:** Odor; leak; bulging; corrosion; heat; ignition source; flood; living-space storage
- **maintenance_spares:** Frequent visual check; dated rotation; spare seals only if OEM-approved
- **successor_proof:** Преемник evacuates and uses emergency route; does not improvise transfer
- **evidence_required:** Permits where needed; SDS; photos; inspections; stock log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Not a household permission to stockpile
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
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-FUEL-DEMAND|TD-FUEL-DEMAND]] | SL3 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
