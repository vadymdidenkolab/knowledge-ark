---
id: "TD-FERT-STORAGE"
kind: "technology"
title: "Хранение готовых удобрений и почвенных добавок"
priority_tier: "P2_YELLOW"
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

# Хранение готовых удобрений и почвенных добавок

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-FERT-STORAGE`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-FERT-STORAGE
- **parent_id:** [[TEC TD-FERTILIZERS|TD-FERTILIZERS]]
- **domain:** FOOD_AGRI
- **node_type:** MATERIAL
- **title_ru:** Хранение готовых удобрений и почвенных добавок
- **outcome:** Prevent moisture; contamination; incompatible mixing; diversion and water pollution
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]], [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** NO_PRODUCTS_OR_APPROVED_STORE
- **instrument_ids:** [[INS INS-009|INS-009]], [[INS INS-013|INS-013]], [[INS INS-017|INS-017]], [[INS INS-071|INS-071]], [[INS INS-072|INS-072]]
- **measurement_acceptance:** Inventory; legal quantity; segregation; secondary containment; labels; access and fire review pass
- **calibration_reference:** Product label; SDS and qualified storage review
- **drawings_bom_state:** MISSING_STORAGE_PLAN
- **localization_state:** PORTUGAL_FERTILIZER_CHEMICAL_FIRE_AND_SECURITY_RULES_REQUIRED
- **waste_storage:** Spills and expired products via legal route
- **stop_conditions:** Unknown product; damaged bag; moisture; heat; incompatible material; drain or well proximity
- **maintenance_spares:** Frequent inspection; stock rotation; spill response
- **successor_proof:** Преемник identifies segregation and emergency route without mixing
- **evidence_required:** Inventory; labels; SDS; photos; inspections
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Oxidizing nitrate products also inherit hazardous-chemical boundaries
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
- **safety_lane:** S3_LICENSED_PROFESSIONAL
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
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-MATERIALS|TD-BASE-MATERIALS]] | SL3 | — |
| REQUIRED | [[TEC TD-FERT-NUTRIENT-BUDGET|TD-FERT-NUTRIENT-BUDGET]] | SL3 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
