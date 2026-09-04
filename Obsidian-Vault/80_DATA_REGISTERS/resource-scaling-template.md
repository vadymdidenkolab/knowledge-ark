---
id: "DATA-REGISTER-7fad39eccc60c963"
type: "generated-data-register-view"
title: "Масштабирование ресурсов для группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "resource-scaling-template.csv"
source_sha256: "1d146b922a67ef0617eba4e25061faca0e7e1b2a5a972b00e98e07378487d60d"
source_bytes: 8642
source_row_count: 10
source_column_count: 43
source_cell_count: 430
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: resource-scaling-template.csv -->

# Масштабирование ресурсов для группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 10
- **Полей в каждой записи:** 43
- **Ячеек данных, включая пустые:** 430
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `1d146b922a67ef0617eba4e25061faca0e7e1b2a5a972b00e98e07378487d60d`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Ресурс ID | <code>&quot;resource_id&quot;</code> |
| 2 | «category» | <code>&quot;category&quot;</code> |
| 3 | Описание | <code>&quot;description&quot;</code> |
| 4 | «allocation» тип | <code>&quot;allocation_type&quot;</code> |
| 5 | Единица | <code>&quot;unit&quot;</code> |
| 6 | Профиль функция | <code>&quot;profile_function&quot;</code> |
| 7 | Горизонт код | <code>&quot;horizon_code&quot;</code> |
| 8 | Сценарий «codes» | <code>&quot;scenario_codes&quot;</code> |
| 9 | «per» человек «basis» | <code>&quot;per_person_basis&quot;</code> |
| 10 | «shared» мощность «metric» | <code>&quot;shared_capacity_metric&quot;</code> |
| 11 | «concurrency» требование | <code>&quot;concurrency_requirement&quot;</code> |
| 12 | «throughput» требование | <code>&quot;throughput_requirement&quot;</code> |
| 13 | Зависимость ID | <code>&quot;dependency_ids&quot;</code> |
| 14 | Отказ отрасль | <code>&quot;failure_domain&quot;</code> |
| 15 | Резервный ресурс ID | <code>&quot;backup_resource_id&quot;</code> |
| 16 | Место основной | <code>&quot;location_primary&quot;</code> |
| 17 | Место резервный | <code>&quot;location_backup&quot;</code> |
| 18 | «n1» целевой | <code>&quot;n1_target&quot;</code> |
| 19 | «n2» целевой | <code>&quot;n2_target&quot;</code> |
| 20 | «n3» целевой | <code>&quot;n3_target&quot;</code> |
| 21 | «n4» целевой | <code>&quot;n4_target&quot;</code> |
| 22 | «n5» целевой | <code>&quot;n5_target&quot;</code> |
| 23 | «n6» целевой | <code>&quot;n6_target&quot;</code> |
| 24 | «n7» целевой | <code>&quot;n7_target&quot;</code> |
| 25 | Фактический количество | <code>&quot;actual_quantity&quot;</code> |
| 26 | «gap» | <code>&quot;gap&quot;</code> |
| 27 | Источник ID | <code>&quot;source_id&quot;</code> |
| 28 | Источник версия | <code>&quot;source_version&quot;</code> |
| 29 | Доказательство метод | <code>&quot;evidence_method&quot;</code> |
| 30 | Доказательство результат | <code>&quot;evidence_result&quot;</code> |
| 31 | Навык требуемый | <code>&quot;skill_required&quot;</code> |
| 32 | Правовой допуск требуемый | <code>&quot;legal_gate_required&quot;</code> |
| 33 | Медицинский допуск требуемый | <code>&quot;medical_gate_required&quot;</code> |
| 34 | Предмет статус | <code>&quot;item_status&quot;</code> |
| 35 | Владелец | <code>&quot;owner&quot;</code> |
| 36 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 37 | Примечания | <code>&quot;notes&quot;</code> |
| 38 | Горизонт «vocabulary» версия | <code>&quot;horizon_vocabulary_version&quot;</code> |
| 39 | Горизонт «semantics» | <code>&quot;horizon_semantics&quot;</code> |
| 40 | Физический сервис «life» ссылка | <code>&quot;physical_service_life_ref&quot;</code> |
| 41 | «continuity» «model» ссылка | <code>&quot;continuity_model_ref&quot;</code> |
| 42 | «e5» проверка состояние | <code>&quot;e5_review_state&quot;</code> |
| 43 | «e5» «basis» ссылки | <code>&quot;e5_basis_refs&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:43 -->
> [!abstract]- Запись 1 из 10 — SRC-CDC-WATER-2025
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-WAT-STORED&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Хранимая питьевая вода&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;CONSUMABLE|PERSONAL_AND_SHARED&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;L&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;SUM_OF_PERSON_SPECIFIC_DAILY_NEEDS_X_DAYS_PLUS_EXPLICIT_LOSS_MARGIN&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1|E2|E3&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSON_PROFILE_REQUIRED&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;STORAGE_VOLUME&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;ALL_MEMBERS&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;DAILY_NEED&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;CONTAINER|ROTATION&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;SINGLE_LOCATION_CONTAMINATION&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-CDC-WATER-2025&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;2025&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;COUNT|DATE|STORAGE_INSPECTION&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;WATER_HYGIENE&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не использовать универсальное среднее без климата и здоровья&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CURRENT_LOADOUT_OR_CONSUMPTION&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:2 cells:43 -->
> [!abstract]- Запись 2 из 10 — RES-WAT-TREAT
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-WAT-TREAT&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Обработка биологически сомнительной воды&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;SHARED|CAPACITY|SKILL_BOUND&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;L_PER_HOUR&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;GROUP_DAILY_NEED_DIVIDED_BY_SAFE_OPERATING_WINDOW&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E2|E3|E4&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;INF-WATER-OFF|INF-WATER-CONTAM|BIO-WATER&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;VALIDATED_L_PER_HOUR_AND_CYCLE_LIMIT&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;PEAK_REFILL_WINDOW&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;GROUP_DAILY_NEED&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;PREFILTER|FUEL_OR_POWER|CLEAN_CONTAINER&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_METHOD_OR_ONE_POWER_SOURCE&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;MANUFACTURER_TEST|OFFLINE_INSTRUCTION|PRACTICE&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;WATER_TREATMENT&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не для химического или радиологического загрязнения без профильного метода&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:3 cells:43 -->
> [!abstract]- Запись 3 из 10 — RES-MED-PERSONAL
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-MED-PERSONAL&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Индивидуальные назначенные лекарства и устройства&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;PERSONAL|CONSUMABLE&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;PERSON_PLAN&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;SUM_OF_INDIVIDUAL_CLINICIAN_APPROVED_CONTINUITY_PLANS&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E0|E1|E2|E3|E4&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;MED-CONTINUITY|INF-HEALTH|SOC-HOME-LOSS|SOC-MIGRATION&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSON_SPECIFIC_ONLY&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;INDIVIDUAL_ACCESS&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;DOSING_SCHEDULE&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;COLD_CHAIN|POWER|PRESCRIPTION&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;WRONG_PERSON_OR_SINGLE_BAG&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;ON_PERSON_OR_PERSONAL_E1&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;SECURE_BACKUP_AS_LAWFUL&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;PRESCRIPTION_RECONCILIATION|STORAGE_LOG&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;PERSON_SPECIFIC&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;YES_IF_APPLICABLE&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не является общим запасом для раздачи&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:4 cells:43 -->
> [!abstract]- Запись 4 из 10 — RES-FAK-SHARED
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-FAK-SHARED&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Общая аптечка первой помощи&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;SHARED|CONSUMABLE|SKILL_BOUND&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;MODULE&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;SCENARIO_AND_TRAINING_BASED_MODULES_PLUS_REPLENISHMENT&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1|E2|E3&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;MED-ARREST|MED-AIRWAY|MED-BLEED|MED-TRAUMA|MED-HEAD-SPINE|MED-BURN|MED-ELECTRIC|MED-DROWN|MED-ANAPH|MED-SEIZURE|MED-DEHYD|MED-POISON|MED-OVERDOSE&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;INDIVIDUAL_PPE_AND_PRESCRIPTIONS_SEPARATE&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;NUMBER_OF_SIMULTANEOUS_PATIENTS_WITHIN_PLAN&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;DEFINED_BY_RISK_PROFILE&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;REPLENISHMENT_RATE&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;TRAINING|PPE|LIGHT|LOG&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_KIT_ONE_LOCATION&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;INVENTORY|EXPIRY|PACKAGE|TRAINING_SIMULATION&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;FIRST_AID_WITHIN_SCOPE&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;ACTION_DEPENDENT&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Количество не расширяет полномочия&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CURRENT_LOADOUT_OR_CONSUMPTION&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:5 cells:43 -->
> [!abstract]- Запись 5 из 10 — RES-COMMS
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-COMMS&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;COMMUNICATIONS&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Связь и получение официальной информации&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;PERSONAL_AND_SHARED|REDUNDANT|CAPACITY&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;CHANNEL&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;AT_LEAST_TWO_INDEPENDENT_FAILURE_DOMAINS_PLUS_PERSONAL_REUNION_CARDS&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E0|E1|E2|E3|E4&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSONAL_MINIMUM_FOR_KEY_MEMBERS&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;GROUP_BROADCAST_AND_EXTERNAL_CONTACT&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;GROUP_AND_EXTERNAL&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;CHECKIN_SCHEDULE&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;POWER|NETWORK|LEGAL_AUTHORITY&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_DEVICE_ONE_OPERATOR_ONE_NETWORK&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;AIRPLANE_MODE|NETWORK_DIVERSITY|MESSAGE_DRILL&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;COMMS_PROTOCOL&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;YES_FOR_TRANSMIT_METHOD&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Потенциальное покрытие не гарантирует связь&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:6 cells:43 -->
> [!abstract]- Запись 6 из 10 — RES-LIGHT
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-LIGHT&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENERGY&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Безопасный индивидуальный и общий свет&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;PERSONAL_AND_SHARED|REDUNDANT&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;LUMEN_HOURS&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;INDIVIDUAL_EXIT_LIGHT_PLUS_SHARED_TASK_LIGHT_X_REQUIRED_HOURS&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E0|E1|E2|E3&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;INF-POWER|TEC-FIRE|TEC-CO|SOC-HOME-LOSS|SOC-MIGRATION&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;ONE_ACCESSIBLE_EXIT_LIGHT_PER_PERSON_OR_CARE_UNIT&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;TASK_AREA_COVERAGE&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;SIMULTANEOUS_EXIT&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;REQUIRED_RUNTIME&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;BATTERY|CHARGER&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_BATTERY_TYPE_OR_ONE_LOCATION&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;RUNTIME_TEST|DARK_RETRIEVAL_DRILL&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;BASIC_USE&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Открытый огонь не является резервным освещением&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CURRENT_LOADOUT_OR_CONSUMPTION&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:7 cells:43 -->
> [!abstract]- Запись 7 из 10 — RES-SLEEP
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-SLEEP&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SHELTER&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Сон и температурная защита&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;PERSONAL|SHARED_CAPACITY&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;PERSON_PLACE&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;SUM_PERSON_PROFILES_PLUS_CARE_AND_PRIVACY_SPACE&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1|E2|E3|E4&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-STORM|NAT-HEAT|NAT-COLD|SOC-HOME-LOSS|SOC-MIGRATION|INF-POWER&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSON_SPECIFIC&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;SAFE_VENTILATED_AREA&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;ALL_MEMBERS&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;OVERNIGHT&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;SHELTER|VENTILATION|TEMPERATURE&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_ROOM_OR_FIRE_EXIT&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;FIT|TEMPERATURE|EXIT|CO_CHECK&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;SHELTER_SAFETY&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Учитывать приватность и ночной уход&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:8 cells:43 -->
> [!abstract]- Запись 8 из 10 — RES-SAN
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-SAN&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SANITATION&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Туалет руки отходы и гигиена&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;CONSUMABLE|SHARED_CAPACITY&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;PERSON_DAY_AND_CYCLES&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;SUM_PERSON_SPECIFIC_NEEDS_X_DAYS_PLUS_CLEANING_CYCLES&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1|E2|E3&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;INF-SEWER|BIO-RESP|INF-WATER-OFF|INF-WATER-CONTAM|BIO-WATER&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSON_PROFILE_REQUIRED&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;TOILET_AND_HANDWASH_CYCLES&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;PEAK_QUEUE&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;DAILY_CYCLES&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;WATER|BAGS|SOAP|WASTE_ROUTE&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_TOILET_OR_NO_WASTE_ROUTE&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;SIMULATION|LEAK|HANDWASH|WASTE_PLAN&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;WASH&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;LOCAL_RULES_MAY_APPLY&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Учитывать доступность и менструальный уход&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CURRENT_LOADOUT_OR_CONSUMPTION&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:9 cells:43 -->
> [!abstract]- Запись 9 из 10 — RES-MAPS
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-MAPS&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Бумажные и офлайн карты&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;PERSONAL_AND_SHARED|REDUNDANT|SKILL_BOUND&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;COPY_OR_DEVICE&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;MASTER_PACK_PLUS_DISTRIBUTED_CRITICAL_COPIES_AND_OPERATOR_REDUNDANCY_BY_GROUP_PROFILE&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E0|E1|E2|E3|E4&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;KEY_MEMBERS_HAVE_CRITICAL_COPY&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;GROUP_MASTER_MAP&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;PROFILE_BASED_OPERATOR_REDUNDANCY&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;OFFLINE_OPEN_AND_ROUTE_READ&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;POWER|SOFTWARE|PRINT&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_DEVICE_OR_ONE_NAVIGATOR&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;OFFLINE_OPEN|PRINT_READ|FIELD_WALK&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Чувствительные слои отдельно&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:10 cells:43 -->
> [!abstract]- Запись 10 из 10 — RES-TRANS
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-TRANS&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;TRANSPORT&quot;</code>
> - **Описание** (<code>&quot;description&quot;</code>): <code>&quot;Перевозка людей воды оборудования и животных&quot;</code>
> - **«allocation» тип** (<code>&quot;allocation_type&quot;</code>): <code>&quot;CAPACITY|REDUNDANT&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;KG_M3_SEATS_RANGE&quot;</code>
> - **Профиль функция** (<code>&quot;profile_function&quot;</code>): <code>&quot;PEOPLE_PLUS_RESTRAINTS_PLUS_CARGO_WITHIN_LEGAL_PAYLOAD_AND_WALKING_FALLBACK&quot;</code>
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1|E2|E3&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **«per» человек «basis»** (<code>&quot;per_person_basis&quot;</code>): <code>&quot;PERSON_AND_MOBILITY_PROFILE&quot;</code>
> - **«shared» мощность «metric»** (<code>&quot;shared_capacity_metric&quot;</code>): <code>&quot;SEATS_PAYLOAD_VOLUME_RANGE&quot;</code>
> - **«concurrency» требование** (<code>&quot;concurrency_requirement&quot;</code>): <code>&quot;ALL_MEMBERS_OR_DEFINED_SPLIT&quot;</code>
> - **«throughput» требование** (<code>&quot;throughput_requirement&quot;</code>): <code>&quot;TRIP_CYCLES&quot;</code>
> - **Зависимость ID** (<code>&quot;dependency_ids&quot;</code>): <code>&quot;FUEL_OR_CHARGE|DRIVER|ROAD|KEYS&quot;</code>
> - **Отказ отрасль** (<code>&quot;failure_domain&quot;</code>): <code>&quot;ONE_VEHICLE_ONE_DRIVER_ONE_ROUTE&quot;</code>
> - **Резервный ресурс ID** (<code>&quot;backup_resource_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Место основной** (<code>&quot;location_primary&quot;</code>): <code>&quot;&quot;</code>
> - **Место резервный** (<code>&quot;location_backup&quot;</code>): <code>&quot;&quot;</code>
> - **«n1» целевой** (<code>&quot;n1_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n2» целевой** (<code>&quot;n2_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n3» целевой** (<code>&quot;n3_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n4» целевой** (<code>&quot;n4_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n5» целевой** (<code>&quot;n5_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n6» целевой** (<code>&quot;n6_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«n7» целевой** (<code>&quot;n7_target&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **«gap»** (<code>&quot;gap&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник версия** (<code>&quot;source_version&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство метод** (<code>&quot;evidence_method&quot;</code>): <code>&quot;PAYLOAD|RANGE|LOAD|ROUTE_DRILL&quot;</code>
> - **Доказательство результат** (<code>&quot;evidence_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **Навык требуемый** (<code>&quot;skill_required&quot;</code>): <code>&quot;LICENSED_DRIVER_OR_MODE_SKILL&quot;</code>
> - **Правовой допуск требуемый** (<code>&quot;legal_gate_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Медицинский допуск требуемый** (<code>&quot;medical_gate_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Рекламный объём не доказывает фактическую вместимость&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CURRENT_LOADOUT_OR_CONSUMPTION&quot;</code>
> - **Физический сервис «life» ссылка** (<code>&quot;physical_service_life_ref&quot;</code>): <code>&quot;TBD_PER_ITEM_OR_SYSTEM&quot;</code>
> - **«continuity» «model» ссылка** (<code>&quot;continuity_model_ref&quot;</code>): <code>&quot;century-capability-register.csv&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
