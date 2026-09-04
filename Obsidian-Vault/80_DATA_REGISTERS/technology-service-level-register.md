---
id: "DATA-REGISTER-8411f773718ca930"
type: "generated-data-register-view"
title: "Требования уровней сервиса"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "technology-service-level-register.csv"
source_sha256: "58e01f2a63041628ef6b36782cb957f198ce6186c7646a3ced58393adfbfdd83"
source_bytes: 21589
source_row_count: 46
source_column_count: 13
source_cell_count: 598
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: technology-service-level-register.csv -->

# Требования уровней сервиса

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 46
- **Полей в каждой записи:** 13
- **Ячеек данных, включая пустые:** 598
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `58e01f2a63041628ef6b36782cb957f198ce6186c7646a3ced58393adfbfdd83`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Сервис требование ID | <code>&quot;service_requirement_id&quot;</code> |
| 2 | Уровень сервиса | <code>&quot;service_level&quot;</code> |
| 3 | Время горизонт | <code>&quot;time_horizon&quot;</code> |
| 4 | «outcome» «node» ID | <code>&quot;outcome_node_id&quot;</code> |
| 5 | Требование роль | <code>&quot;requirement_role&quot;</code> |
| 6 | Минимально требуемый результат | <code>&quot;minimum_outcome&quot;</code> |
| 7 | Размер группы | <code>&quot;group_size_scope&quot;</code> |
| 8 | Мощность «basis» | <code>&quot;capacity_basis&quot;</code> |
| 9 | Доказательство требуемый | <code>&quot;evidence_required&quot;</code> |
| 10 | Статус | <code>&quot;status&quot;</code> |
| 11 | Человеческий проверка состояние | <code>&quot;human_review_state&quot;</code> |
| 12 | Допуск к применению | <code>&quot;release_gate&quot;</code> |
| 13 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:13 -->
> [!abstract]- Запись 1 из 46 — SR-SL0-TD-BASE — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-BASE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-BASE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:2 cells:13 -->
> [!abstract]- Запись 2 из 46 — SR-SL0-TD-PEOPLE — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-PEOPLE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-PEOPLE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PERSON_HOURS_DEPENDENCY_AND_SHIFT_CAPACITY&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:3 cells:13 -->
> [!abstract]- Запись 3 из 46 — SR-SL0-TD-HEALTH — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-HEALTH&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-HEALTH&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:4 cells:13 -->
> [!abstract]- Запись 4 из 46 — SR-SL0-TD-WATER — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-WATER&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WATER&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:5 cells:13 -->
> [!abstract]- Запись 5 из 46 — SR-SL0-TD-SHELTER — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-SHELTER&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SHELTER&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:6 cells:13 -->
> [!abstract]- Запись 6 из 46 — SR-SL0-TD-MAPS-COMMS — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-MAPS-COMMS&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-MAPS-COMMS&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PEOPLE_CHANNELS_COVERAGE_CHECKIN_AND_ROUTE_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:7 cells:13 -->
> [!abstract]- Запись 7 из 46 — SR-SL0-TD-GOV — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-GOV&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:8 cells:13 -->
> [!abstract]- Запись 8 из 46 — SR-SL0-TD-SECURITY — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-SECURITY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SECURITY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:9 cells:13 -->
> [!abstract]- Запись 9 из 46 — SR-SL0-TD-PORTUGAL — Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL0-TD-PORTUGAL&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;SECONDS_TO_12_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-PORTUGAL&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;AUTHORITY_JURISDICTION_VERSION_COVERAGE_AND_CHECKED_DATE&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:10 cells:13 -->
> [!abstract]- Запись 10 из 46 — SR-SL1-TD-WATER — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-WATER&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WATER&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:11 cells:13 -->
> [!abstract]- Запись 11 из 46 — SR-SL1-TD-FOOD — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-FOOD&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-FOOD&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:12 cells:13 -->
> [!abstract]- Запись 12 из 46 — SR-SL1-TD-SANITATION — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-SANITATION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SANITATION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:13 cells:13 -->
> [!abstract]- Запись 13 из 46 — SR-SL1-TD-SHELTER — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-SHELTER&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SHELTER&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:14 cells:13 -->
> [!abstract]- Запись 14 из 46 — SR-SL1-TD-ENERGY — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-ENERGY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-ENERGY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:15 cells:13 -->
> [!abstract]- Запись 15 из 46 — SR-SL1-TD-HEALTH — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-HEALTH&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-HEALTH&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:16 cells:13 -->
> [!abstract]- Запись 16 из 46 — SR-SL1-TD-MAPS-COMMS — Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL1-TD-MAPS-COMMS&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;12_TO_72_HOURS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-MAPS-COMMS&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PEOPLE_CHANNELS_COVERAGE_CHECKIN_AND_ROUTE_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:17 cells:13 -->
> [!abstract]- Запись 17 из 46 — SR-SL2-TD-KNOWLEDGE — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-KNOWLEDGE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-KNOWLEDGE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:18 cells:13 -->
> [!abstract]- Запись 18 из 46 — SR-SL2-TD-TRANSPORT — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-TRANSPORT&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-TRANSPORT&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PEOPLE_KG_KM_RANGE_AND_TURNAROUND_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:19 cells:13 -->
> [!abstract]- Запись 19 из 46 — SR-SL2-TD-ENVIRONMENT — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-ENVIRONMENT&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-ENVIRONMENT&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;SITE_SERIES_SEASONAL_RANGE_AND_TRIGGER_THRESHOLDS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:20 cells:13 -->
> [!abstract]- Запись 20 из 46 — SR-SL2-TD-GOV — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-GOV&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:21 cells:13 -->
> [!abstract]- Запись 21 из 46 — SR-SL2-TD-WATER — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-WATER&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WATER&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:22 cells:13 -->
> [!abstract]- Запись 22 из 46 — SR-SL2-TD-FOOD — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-FOOD&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-FOOD&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:23 cells:13 -->
> [!abstract]- Запись 23 из 46 — SR-SL2-TD-HEALTH — Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL2-TD-HEALTH&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;3_TO_14_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-HEALTH&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:24 cells:13 -->
> [!abstract]- Запись 24 из 46 — SR-SL3-TD-WORKSHOP — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-WORKSHOP&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WORKSHOP&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:25 cells:13 -->
> [!abstract]- Запись 25 из 46 — SR-SL3-TD-EDUCATION — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-EDUCATION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-EDUCATION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LEARNERS_HOURS_COMPETENCY_AND_DUPLICATES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:26 cells:13 -->
> [!abstract]- Запись 26 из 46 — SR-SL3-TD-TRANSPORT — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-TRANSPORT&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-TRANSPORT&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PEOPLE_KG_KM_RANGE_AND_TURNAROUND_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:27 cells:13 -->
> [!abstract]- Запись 27 из 46 — SR-SL3-TD-ENERGY — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-ENERGY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-ENERGY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:28 cells:13 -->
> [!abstract]- Запись 28 из 46 — SR-SL3-TD-SEED-BANK — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-SEED-BANK&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SEED-BANK&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:29 cells:13 -->
> [!abstract]- Запись 29 из 46 — SR-SL3-TD-FERTILIZERS — Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL3-TD-FERTILIZERS&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_90_DAYS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-FERTILIZERS&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:30 cells:13 -->
> [!abstract]- Запись 30 из 46 — SR-SL4-TD-WATER-YIELD — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-WATER-YIELD&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WATER-YIELD&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:31 cells:13 -->
> [!abstract]- Запись 31 из 46 — SR-SL4-TD-CROP-TRIAL — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-CROP-TRIAL&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-CROP-TRIAL&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:32 cells:13 -->
> [!abstract]- Запись 32 из 46 — SR-SL4-TD-SEED-REGEN — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-SEED-REGEN&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-SEED-REGEN&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:33 cells:13 -->
> [!abstract]- Запись 33 из 46 — SR-SL4-TD-HARVEST-STORAGE — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-HARVEST-STORAGE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-HARVEST-STORAGE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:34 cells:13 -->
> [!abstract]- Запись 34 из 46 — SR-SL4-TD-ENERGY-GENERATION — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-ENERGY-GENERATION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-ENERGY-GENERATION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:35 cells:13 -->
> [!abstract]- Запись 35 из 46 — SR-SL4-TD-KNOWLEDGE-RESTORE — Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL4-TD-KNOWLEDGE-RESTORE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL4&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_SEASON_TO_ONE_YEAR&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-KNOWLEDGE-RESTORE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:36 cells:13 -->
> [!abstract]- Запись 36 из 46 — SR-SL5-TD-MATERIALS-PRODUCTION — Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL5-TD-MATERIALS-PRODUCTION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL5&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_TO_15_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-MATERIALS-PRODUCTION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;MASS_VOLUME_THROUGHPUT_YIELD_AND_REJECT_RATE&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:37 cells:13 -->
> [!abstract]- Запись 37 из 46 — SR-SL5-TD-CONSTRUCTION — Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL5-TD-CONSTRUCTION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL5&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_TO_15_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-CONSTRUCTION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;CONDITIONAL&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;AREA_LOAD_WEATHER_WINDOW_LABOR_AND_INSPECTION&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:38 cells:13 -->
> [!abstract]- Запись 38 из 46 — SR-SL5-TD-WORKSHOP — Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL5-TD-WORKSHOP&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL5&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_TO_15_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-WORKSHOP&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:39 cells:13 -->
> [!abstract]- Запись 39 из 46 — SR-SL5-TD-KNOWLEDGE — Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL5-TD-KNOWLEDGE&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL5&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_TO_15_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-KNOWLEDGE&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:40 cells:13 -->
> [!abstract]- Запись 40 из 46 — SR-SL5-TD-GOV-COMMUNITY — Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL5-TD-GOV-COMMUNITY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL5&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;ONE_TO_15_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV-COMMUNITY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:41 cells:13 -->
> [!abstract]- Запись 41 из 46 — SR-SL6-TD-GOV-SUCCESSION — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-GOV-SUCCESSION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV-SUCCESSION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:42 cells:13 -->
> [!abstract]- Запись 42 из 46 — SR-SL6-TD-EDUCATION-INSTRUCTOR — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему по…
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-EDUCATION-INSTRUCTOR&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-EDUCATION-INSTRUCTOR&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;LEARNERS_HOURS_COMPETENCY_AND_DUPLICATES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:43 cells:13 -->
> [!abstract]- Запись 43 из 46 — SR-SL6-TD-KNOWLEDGE-MIGRATION — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему пок…
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-KNOWLEDGE-MIGRATION&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-KNOWLEDGE-MIGRATION&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:44 cells:13 -->
> [!abstract]- Запись 44 из 46 — SR-SL6-TD-PEOPLE-DEMOGRAPHY — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему покол…
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-PEOPLE-DEMOGRAPHY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-PEOPLE-DEMOGRAPHY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;PERSON_HOURS_DEPENDENCY_AND_SHIFT_CAPACITY&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:45 cells:13 -->
> [!abstract]- Запись 45 из 46 — SR-SL6-TD-GOV-LAW — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-GOV-LAW&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV-LAW&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:46 cells:13 -->
> [!abstract]- Запись 46 из 46 — SR-SL6-TD-GOV-COMMUNITY — Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению
> - **Сервис требование ID** (<code>&quot;service_requirement_id&quot;</code>): <code>&quot;SR-SL6-TD-GOV-COMMUNITY&quot;</code>
> - **Уровень сервиса** (<code>&quot;service_level&quot;</code>): <code>&quot;SL6&quot;</code>
> - **Время горизонт** (<code>&quot;time_horizon&quot;</code>): <code>&quot;15_TO_100_YEARS&quot;</code>
> - **«outcome» «node» ID** (<code>&quot;outcome_node_id&quot;</code>): <code>&quot;TD-GOV-COMMUNITY&quot;</code>
> - **Требование роль** (<code>&quot;requirement_role&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Минимально требуемый результат** (<code>&quot;minimum_outcome&quot;</code>): <code>&quot;Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1|N2|N3_TO_N7&quot;</code>
> - **Мощность «basis»** (<code>&quot;capacity_basis&quot;</code>): <code>&quot;DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;Measured capacity; duration; inventory; test; owner; backup; accepted residual risk&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CATALOG_ONLY_NOT_EVALUATED&quot;</code>
> - **Человеческий проверка состояние** (<code>&quot;human_review_state&quot;</code>): <code>&quot;PROVISIONAL_AUTO_REVIEW_REQUIRED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
