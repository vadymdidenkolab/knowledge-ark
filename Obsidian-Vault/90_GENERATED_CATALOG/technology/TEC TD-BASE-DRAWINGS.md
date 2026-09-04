---
id: "TD-BASE-DRAWINGS"
kind: "technology"
title: "Чертежи; схемы; BOM и версии"
priority_tier: "P2_YELLOW"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S0_OBSERVE_READ"
execution_gate: "DENY"
status: "MISSING"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Чертежи; схемы; BOM и версии

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-BASE-DRAWINGS`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S0_OBSERVE_READ`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-BASE-DRAWINGS
- **parent_id:** [[TEC TD-BASE|TD-BASE]]
- **domain:** BASE
- **node_type:** DRAWING
- **title_ru:** Чертежи; схемы; BOM и версии
- **outcome:** Сделать каждую безопасную систему воспроизводимой и ремонтируемой
- **safety_class:** S0_OBSERVE_READ
- **execution_policy:** HOUSEHOLD_S0
- **prerequisite_node_ids:** [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]], [[TEC TD-BASE-SITE|TD-BASE-SITE]], [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]]
- **source_package_ids:** [[PKG PSP-080|PSP-080]], [[PKG PSP-081|PSP-081]], [[PKG PSP-109|PSP-109]]
- **materials_tools_state:** NO_PRODUCTION_PACKAGES
- **instrument_ids:** не заполнено
- **measurement_acceptance:** Каждый критический объект имеет исходник; PDF или SVG fallback; BOM; допуски и acceptance
- **calibration_reference:** Контрольные размеры связаны с проверенным прибором
- **drawings_bom_state:** MISSING
- **localization_state:** EXACT_ASSET_AND_SITE_REQUIRED
- **waste_storage:** Устаревшие версии сохраняются как superseded
- **stop_conditions:** Несогласованная revision; отсутствующая единица; неизвестный материал
- **maintenance_spares:** После изменения и ежегодный аудит ссылок
- **successor_proof:** Другой участник собирает или проверяет макет только по пакету
- **evidence_required:** Versioned drawing set; BOM; review; sample test
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Иллюстрация без размеров и приёмки не считается чертежом
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
- **safety_lane:** S0_OBSERVE_READ
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE
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
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-SITE|TD-BASE-SITE]] | SL1 | — |
| REQUIRED | [[TEC TD-BASE-METROLOGY|TD-BASE-METROLOGY]] | SL3 | — |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
