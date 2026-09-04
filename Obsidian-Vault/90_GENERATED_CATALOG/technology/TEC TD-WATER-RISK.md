---
id: "TD-WATER-RISK"
kind: "technology"
title: "Профиль опасностей сырой воды"
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

# Профиль опасностей сырой воды

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-WATER-RISK`
- **Статус:** `MISSING`
- **Приоритет:** `P2_YELLOW`
- **Аудитория:** `LICENSED_PROFESSIONAL`
- **Класс безопасности:** `S3_LICENSED_PROFESSIONAL`
- **Допуск:** `BLACK_GATE_LICENSED_ONLY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-WATER-RISK
- **parent_id:** [[TEC TD-WATER|TD-WATER]]
- **domain:** WATER_WASH
- **node_type:** KNOWLEDGE
- **title_ru:** Профиль опасностей сырой воды
- **outcome:** Выбрать барьеры по реальным микробиологическим; химическим и радиологическим рискам
- **safety_class:** S3_LICENSED_PROFESSIONAL
- **execution_policy:** LICENSED_ONLY
- **prerequisite_node_ids:** [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]], [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]]
- **source_package_ids:** [[PKG PSP-101|PSP-101]], [[PKG PSP-102|PSP-102]], [[PKG SUP-LEA-026|SUP-LEA-026]], [[PKG SUP-LEA-028|SUP-LEA-028]], [[PKG SUP-LEA-029|SUP-LEA-029]]
- **materials_tools_state:** LAB_PLAN_MISSING
- **instrument_ids:** [[INS INS-029|INS-029]], [[INS INS-030|INS-030]], [[INS INS-031|INS-031]], [[INS INS-032|INS-032]]
- **measurement_acceptance:** Аккредитованный план анализа покрывает site-specific hazards; результаты интерпретированы специалистом
- **calibration_reference:** Аккредитованная лаборатория и документированные контрольные образцы
- **drawings_bom_state:** NOT_APPLICABLE
- **localization_state:** PORTUGAL_LAB_AND_RULES_REQUIRED
- **waste_storage:** Образцы и реагенты утилизируются по методу
- **stop_conditions:** Нет лаборатории; unknown contamination; результаты вне limits
- **maintenance_spares:** По water safety plan и после событий
- **successor_proof:** Преемник умеет отобрать разрешённую пробу и передать данные; не объявляет воду безопасной
- **evidence_required:** Lab reports; chain of custody; hazard assessment
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Полная изоляция оставляет остаточный риск без лаборатории
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
| REQUIRED | [[TEC TD-WATER-SOURCE|TD-WATER-SOURCE]] | SL3 | — |
| REQUIRED | [[TEC TD-BASE-SAFETY|TD-BASE-SAFETY]] | SL1 | — |

</details>

> [!danger] Закрытая ветка
> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
