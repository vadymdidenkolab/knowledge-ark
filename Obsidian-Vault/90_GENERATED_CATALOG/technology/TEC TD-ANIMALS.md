---
id: "TD-ANIMALS"
kind: "technology"
title: "Животные; корма; welfare и ветеринарная непрерывность"
priority_tier: "P3_GREEN"
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

# Животные; корма; welfare и ветеринарная непрерывность

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `TD-ANIMALS`
- **Статус:** `MISSING`
- **Приоритет:** `P3_GREEN`
- **Аудитория:** `TRAINED_SUPERVISED`
- **Класс безопасности:** `S2_TRAINED_SUPERVISED`
- **Допуск:** `DENY`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: technology-dependency-register.csv -->
- **node_id:** TD-ANIMALS
- **parent_id:** [[TEC TD-ROOT|TD-ROOT]]
- **domain:** ANIMALS
- **node_type:** OUTCOME
- **title_ru:** Животные; корма; welfare и ветеринарная непрерывность
- **outcome:** Иметь измеримую и проверяемую способность: животные; корма; welfare и ветеринарная непрерывность
- **safety_class:** S2_TRAINED_SUPERVISED
- **execution_policy:** TRAINED_SUPERVISED
- **prerequisite_node_ids:** [[TEC TD-BASE|TD-BASE]], [[TEC TD-ANIMALS-WELFARE|TD-ANIMALS-WELFARE]], [[TEC TD-ANIMALS-WATER|TD-ANIMALS-WATER]], [[TEC TD-ANIMALS-FEED|TD-ANIMALS-FEED]], [[TEC TD-ANIMALS-PASTURE|TD-ANIMALS-PASTURE]], [[TEC TD-ANIMALS-SHELTER|TD-ANIMALS-SHELTER]], [[TEC TD-ANIMALS-BIOSECURITY|TD-ANIMALS-BIOSECURITY]], [[TEC TD-ANIMALS-BREEDING|TD-ANIMALS-BREEDING]], [[TEC TD-ANIMALS-VET|TD-ANIMALS-VET]], [[TEC TD-ANIMALS-WASTE|TD-ANIMALS-WASTE]], [[TEC TD-ANIMALS-EGGS|TD-ANIMALS-EGGS]], [[TEC TD-ANIMALS-MILK|TD-ANIMALS-MILK]], [[TEC TD-ANIMALS-SLAUGHTER|TD-ANIMALS-SLAUGHTER]], [[TEC TD-ANIMALS-BEES|TD-ANIMALS-BEES]], [[TEC TD-ANIMALS-AQUACULTURE|TD-ANIMALS-AQUACULTURE]], [[TEC TD-ANIMALS-HANDLER|TD-ANIMALS-HANDLER]]
- **source_package_ids:** не заполнено
- **materials_tools_state:** MISSING
- **instrument_ids:** не заполнено
- **measurement_acceptance:** До использования задать service level, единицу, объём, срок и критерий приёмки
- **calibration_reference:** Точный метод, прибор/reference и неопределённость TBD до исполнения
- **drawings_bom_state:** MISSING_OR_NOT_APPLICABLE
- **localization_state:** PORTUGAL_AND_SITE_REVIEW_REQUIRED
- **waste_storage:** Потоки, совместимость, хранение и законный маршрут TBD до исполнения
- **stop_conditions:** Неизвестная идентичность; отсутствующее полномочие; опасная среда; непроверенный источник; выход за подготовку
- **maintenance_spares:** Периодичность, расходники, запасные части и failure signs TBD
- **successor_proof:** Другой назначенный участник находит карточку и демонстрирует допустимую часть без устной помощи автора
- **evidence_required:** Профиль; источник; инвентарь; измерения; acceptance log; reviewer; дата
- **evidence_state:** MISSING
- **capability_status:** MISSING
- **release_gate:** DENY
- **notes:** Агрегат: обязательность дочерних узлов определяется technology-dependency-edges.csv
- **release_version:** 0.5-draft

</details>

<details>
<summary>Служебные поля планирования</summary>

- **priority_tier:** P3_GREEN
- **priority_horizon:** 3_MONTHS_TO_15_YEARS
- **earliest_service_level:** SL4
- **life_criticality:** DEFERRED_WITHIN_STATED_HORIZON
- **build_sequence_tier:** P3_GREEN
- **acquisition_priority:** P3_GREEN
- **knowledge_priority:** P3_GREEN
- **safety_lane:** S2_TRAINED_SUPERVISED
- **group_size_scope:** N1|N2|N3_TO_N7
- **capacity_model:** HEAD_COUNT_FEED_WATER_AREA_AND_HANDLER_HOURS
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
| CONDITIONAL | [[TEC TD-ANIMALS-WELFARE|TD-ANIMALS-WELFARE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-WATER|TD-ANIMALS-WATER]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-FEED|TD-ANIMALS-FEED]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-PASTURE|TD-ANIMALS-PASTURE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-SHELTER|TD-ANIMALS-SHELTER]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-BIOSECURITY|TD-ANIMALS-BIOSECURITY]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-BREEDING|TD-ANIMALS-BREEDING]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-VET|TD-ANIMALS-VET]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-WASTE|TD-ANIMALS-WASTE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-EGGS|TD-ANIMALS-EGGS]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-MILK|TD-ANIMALS-MILK]] | SL4 | applicable_profile_site_or_qualified_role_required |
| HAZARD_ONLY | [[TEC TD-ANIMALS-SLAUGHTER|TD-ANIMALS-SLAUGHTER]] | SL1 | not_an_operational_prerequisite |
| CONDITIONAL | [[TEC TD-ANIMALS-BEES|TD-ANIMALS-BEES]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-AQUACULTURE|TD-ANIMALS-AQUACULTURE]] | SL4 | applicable_profile_site_or_qualified_role_required |
| CONDITIONAL | [[TEC TD-ANIMALS-HANDLER|TD-ANIMALS-HANDLER]] | SL4 | applicable_profile_site_or_qualified_role_required |

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
