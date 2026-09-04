---
id: "TD-WORKSHOP"
kind: "technology"
title: "Мастерская; материалы и ремонт"
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

# Мастерская; материалы и ремонт

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WORKSHOP`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WORKSHOP
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** WORKSHOP
- **node_type:** OUTCOME
- **title_ru:** Мастерская; материалы и ремонт
- **outcome:** Изготавливать и восстанавливать безопасные низкоэнергетические предметы
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]], [[TEC TD-WORKSHOP-FIXTURES|TD-WORKSHOP-FIXTURES]], [[TEC TD-WORKSHOP-MEASURE|TD-WORKSHOP-MEASURE]], [[TEC TD-WORKSHOP-WOOD|TD-WORKSHOP-WOOD]], [[TEC TD-WORKSHOP-TEXTILE|TD-WORKSHOP-TEXTILE]], [[TEC TD-WORKSHOP-LOWV|TD-WORKSHOP-LOWV]], [[TEC TD-WORKSHOP-SALVAGE|TD-WORKSHOP-SALVAGE]], [[TEC TD-WORKSHOP-SPACE|TD-WORKSHOP-SPACE]], [[TEC TD-WORKSHOP-LIGHT|TD-WORKSHOP-LIGHT]], [[TEC TD-WORKSHOP-VENT|TD-WORKSHOP-VENT]], [[TEC TD-WORKSHOP-FIRE|TD-WORKSHOP-FIRE]], [[TEC TD-WORKSHOP-PPE|TD-WORKSHOP-PPE]], [[TEC TD-WORKSHOP-CUSTODY|TD-WORKSHOP-CUSTODY]], [[TEC TD-WORKSHOP-MARK|TD-WORKSHOP-MARK]], [[TEC TD-WORKSHOP-TEMPLATES|TD-WORKSHOP-TEMPLATES]], [[TEC TD-WORKSHOP-HOLD|TD-WORKSHOP-HOLD]], [[TEC TD-WORKSHOP-CUT|TD-WORKSHOP-CUT]], [[TEC TD-WORKSHOP-DRILL|TD-WORKSHOP-DRILL]], [[TEC TD-WORKSHOP-FILE|TD-WORKSHOP-FILE]], [[TEC TD-WORKSHOP-PLANE|TD-WORKSHOP-PLANE]], [[TEC TD-WORKSHOP-ABRASIVE|TD-WORKSHOP-ABRASIVE]], [[TEC TD-WORKSHOP-SHARPEN|TD-WORKSHOP-SHARPEN]], [[TEC TD-WORKSHOP-FASTEN|TD-WORKSHOP-FASTEN]], [[TEC TD-WORKSHOP-TORQUE|TD-WORKSHOP-TORQUE]], [[TEC TD-WORKSHOP-ADHESIVE|TD-WORKSHOP-ADHESIVE]], [[TEC TD-WORKSHOP-SEW|TD-WORKSHOP-SEW]], [[TEC TD-WORKSHOP-ROPE|TD-WORKSHOP-ROPE]], [[TEC TD-WORKSHOP-METAL-COLD|TD-WORKSHOP-METAL-COLD]], [[TEC TD-WORKSHOP-PLUMBING|TD-WORKSHOP-PLUMBING]], [[TEC TD-WORKSHOP-PUMPS|TD-WORKSHOP-PUMPS]], [[TEC TD-WORKSHOP-BICYCLE|TD-WORKSHOP-BICYCLE]], [[TEC TD-WORKSHOP-CART|TD-WORKSHOP-CART]], [[TEC TD-WORKSHOP-FOOTWEAR|TD-WORKSHOP-FOOTWEAR]], [[TEC TD-WORKSHOP-DONOR|TD-WORKSHOP-DONOR]], [[TEC TD-WORKSHOP-CONSUMABLES|TD-WORKSHOP-CONSUMABLES]], [[TEC TD-WORKSHOP-INTERFACES|TD-WORKSHOP-INTERFACES]], [[TEC TD-WORKSHOP-POST-TEST|TD-WORKSHOP-POST-TEST]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING_WORKSHOP
- **instrument_ids:** [[INS INS-001|INS-001]], [[INS INS-002|INS-002]], [[INS INS-003|INS-003]], [[INS INS-004|INS-004]], [[INS INS-005|INS-005]], [[INS INS-006|INS-006]], [[INS INS-007|INS-007]], [[INS INS-009|INS-009]], [[INS INS-045|INS-045]]
- **measurement_acceptance:** Exact safe task meets drawing; dimensions; fit; function and inspection criteria
- **calibration_reference:** Checked measuring tools and reference samples
- **drawings_bom_state:** MISSING_PRODUCTION_PACKAGES
- **localization_state:** SITE_AND_SKILLS_REQUIRED
- **waste_storage:** Sharps; dust; metal; electronics and oils separated
- **stop_conditions:** Unknown material; stored energy; guards removed; hot work; pressure; mains
- **maintenance_spares:** Tool inspection; sharpening by safe method; standard spares
- **successor_proof:** Преемник completes one S1 production package
- **evidence_required:** Inventory; drawings; raw measurements; acceptance and repair log
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** No verified tools or bench currently
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
- **capacity_model:** JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES
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
| REQUIRED | [[TEC TD-WORKSHOP-HANDTOOLS|TD-WORKSHOP-HANDTOOLS]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-FIXTURES|TD-WORKSHOP-FIXTURES]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-MEASURE|TD-WORKSHOP-MEASURE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-WOOD|TD-WORKSHOP-WOOD]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-TEXTILE|TD-WORKSHOP-TEXTILE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-LOWV|TD-WORKSHOP-LOWV]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-SALVAGE|TD-WORKSHOP-SALVAGE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-SPACE|TD-WORKSHOP-SPACE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-LIGHT|TD-WORKSHOP-LIGHT]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WORKSHOP-VENT|TD-WORKSHOP-VENT]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WORKSHOP-FIRE|TD-WORKSHOP-FIRE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-PPE|TD-WORKSHOP-PPE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-CUSTODY|TD-WORKSHOP-CUSTODY]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-MARK|TD-WORKSHOP-MARK]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-TEMPLATES|TD-WORKSHOP-TEMPLATES]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-HOLD|TD-WORKSHOP-HOLD]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-CUT|TD-WORKSHOP-CUT]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-DRILL|TD-WORKSHOP-DRILL]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-FILE|TD-WORKSHOP-FILE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-PLANE|TD-WORKSHOP-PLANE]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WORKSHOP-ABRASIVE|TD-WORKSHOP-ABRASIVE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WORKSHOP-SHARPEN|TD-WORKSHOP-SHARPEN]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-FASTEN|TD-WORKSHOP-FASTEN]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WORKSHOP-TORQUE|TD-WORKSHOP-TORQUE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WORKSHOP-ADHESIVE|TD-WORKSHOP-ADHESIVE]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-SEW|TD-WORKSHOP-SEW]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-ROPE|TD-WORKSHOP-ROPE]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WORKSHOP-METAL-COLD|TD-WORKSHOP-METAL-COLD]] | SL4 | applicable_profile_site_or_qualified_role_required |
| REQUIRED | [[TEC TD-WORKSHOP-PLUMBING|TD-WORKSHOP-PLUMBING]] | SL3 | — |
| CONDITIONAL | [[TEC TD-WORKSHOP-PUMPS|TD-WORKSHOP-PUMPS]] | SL4 | applicable_profile_site_or_qualified_role_required |
| OPTIONAL | [[TEC TD-WORKSHOP-BICYCLE|TD-WORKSHOP-BICYCLE]] | SL3 | use_only_if_selected_technology_requires_it |
| OPTIONAL | [[TEC TD-WORKSHOP-CART|TD-WORKSHOP-CART]] | SL3 | use_only_if_selected_technology_requires_it |
| OPTIONAL | [[TEC TD-WORKSHOP-FOOTWEAR|TD-WORKSHOP-FOOTWEAR]] | SL3 | use_only_if_selected_technology_requires_it |
| REQUIRED | [[TEC TD-WORKSHOP-DONOR|TD-WORKSHOP-DONOR]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-CONSUMABLES|TD-WORKSHOP-CONSUMABLES]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-INTERFACES|TD-WORKSHOP-INTERFACES]] | SL3 | — |
| REQUIRED | [[TEC TD-WORKSHOP-POST-TEST|TD-WORKSHOP-POST-TEST]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
