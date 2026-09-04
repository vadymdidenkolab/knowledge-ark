---
id: "TD-ENERGY-PROTECTION"
kind: "technology"
title: "Изоляция; защита и отсутствие backfeed"
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

# Изоляция; защита и отсутствие backfeed

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ENERGY-PROTECTION`
- **Статус:** `MISSING`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ENERGY-PROTECTION
- **parent_id:** [[TEC TD-ENERGY|TD-ENERGY]]
- **domain:** ENERGY
- **node_type:** TEST
- **title_ru:** Изоляция; защита и отсутствие backfeed
- **outcome:** Prevent shock; fire and energizing external circuits
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-ENERGY-DC|TD-ENERGY-DC]], [[TEC TD-ENERGY-GENERATION|TD-ENERGY-GENERATION]], [[TEC TD-ENERGY-STORAGE|TD-ENERGY-STORAGE]]
- **source_package_ids:** [[PKG SUP-PHY-036|SUP-PHY-036]]
- **materials_tools_state:** MISSING_PROTECTION_ASSESSMENT
- **instrument_ids:** [[INS INS-045|INS-045]], [[INS INS-073|INS-073]]
- **measurement_acceptance:** Qualified inspection and documented functional tests pass
- **calibration_reference:** Calibrated tester and jurisdiction-specific method
- **drawings_bom_state:** MISSING_SINGLE_LINE
- **localization_state:** PORTUGAL_LICENSED_ELECTRICIAN_REQUIRED
- **waste_storage:** Failed protection devices disposed legally
- **stop_conditions:** Live work; unknown circuit; failed RCD; backfeed possibility
- **maintenance_spares:** Periodic test per device and regulation
- **successor_proof:** Household successor only recognizes status and calls electrician
- **evidence_required:** Inspection certificate; test records; labels
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Do not open panels
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
| REQUIRED | [[TEC TD-ENERGY-DC|TD-ENERGY-DC]] | SL2 | — |
| CONDITIONAL | [[TEC TD-ENERGY-GENERATION|TD-ENERGY-GENERATION]] | SL2 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ENERGY-STORAGE|TD-ENERGY-STORAGE]] | SL2 | applicable_profile_site_or_qualified_role_required |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
