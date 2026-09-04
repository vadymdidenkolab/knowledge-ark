---
id: "DATA-REGISTER-ea955f444138a09d"
type: "generated-data-register-view"
title: "Горизонты автономности"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "horizon-register.csv"
source_sha256: "ea2781dc02abee4a14d3298ea6e2ea809bf501d0e3c2f5084f8625addea222b1"
source_bytes: 1971
source_row_count: 6
source_column_count: 15
source_cell_count: 90
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: horizon-register.csv -->

# Горизонты автономности

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 6
- **Полей в каждой записи:** 15
- **Ячеек данных, включая пустые:** 90
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `ea2781dc02abee4a14d3298ea6e2ea809bf501d0e3c2f5084f8625addea222b1`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Горизонт код | <code>&quot;horizon_code&quot;</code> |
| 2 | «vocabulary» версия | <code>&quot;vocabulary_version&quot;</code> |
| 3 | «ordinal» | <code>&quot;ordinal&quot;</code> |
| 4 | «label» на русском | <code>&quot;label_ru&quot;</code> |
| 5 | «lower» «bound» «iso8601» | <code>&quot;lower_bound_iso8601&quot;</code> |
| 6 | «lower» «inclusive» | <code>&quot;lower_inclusive&quot;</code> |
| 7 | «upper» «bound» «iso8601» | <code>&quot;upper_bound_iso8601&quot;</code> |
| 8 | «upper» «inclusive» | <code>&quot;upper_inclusive&quot;</code> |
| 9 | Граница «rule» | <code>&quot;boundary_rule&quot;</code> |
| 10 | «planning» «intent» | <code>&quot;planning_intent&quot;</code> |
| 11 | Физический «stock» «semantics» | <code>&quot;physical_stock_semantics&quot;</code> |
| 12 | «default» проверка «cadence» | <code>&quot;default_review_cadence&quot;</code> |
| 13 | Разрешённый «claim» | <code>&quot;allowed_claim&quot;</code> |
| 14 | Запрещённый «claim» | <code>&quot;prohibited_claim&quot;</code> |
| 15 | Статус | <code>&quot;status&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:15 -->
> [!abstract]- Запись 1 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E0&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;0&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;минуты–12 часов&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;PT0S&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;PT12H&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;ELAPSED_DURATION&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;немедленная безопасность и вызов помощи&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;PORTABLE_IMMEDIATE&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;EVENT_OR_MONTHLY&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;VERIFIED_FOR_CURRENT_EVENT&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;GUARANTEED_OUTCOME&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

<!-- record:2 cells:15 -->
> [!abstract]- Запись 2 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E1&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;1&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;свыше 12–72 часов&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;PT12H&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;NO&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;P3D&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;ELAPSED_DURATION&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;выход или первичная автономность&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;PORTABLE_ROTATED&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;VERIFIED_CURRENT_LOADOUT&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;UNIVERSAL_72H_SOLUTION&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

<!-- record:3 cells:15 -->
> [!abstract]- Запись 3 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E2&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;2&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;свыше 72 часов–14 дней&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;P3D&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;NO&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;P14D&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;ELAPSED_DURATION&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;домашняя автономность при сбое&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;ROTATED_STOCK_PLUS_SYSTEM&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;VERIFIED_CURRENT_CAPACITY&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;INDEPENDENCE_FROM_SERVICES&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

<!-- record:4 cells:15 -->
> [!abstract]- Запись 4 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E3&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;3&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;свыше 14–90 дней&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;P14D&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;NO&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;P90D&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;ELAPSED_DURATION&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;длительный сбой и ограниченное пополнение&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;ROTATED_STOCK_AND_REPAIR&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;CYCLE_TESTED_FOR_CURRENT_PROFILE&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;PERMANENT_AUTONOMY&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

<!-- record:5 cells:15 -->
> [!abstract]- Запись 5 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E4&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;4&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;свыше 90 дней–менее 15 лет&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;P90D&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;NO&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;P15Y&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;NO&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;CALENDAR_ANNIVERSARY&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;воспроизводство ремонт обучение кооперация&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY_NOT_STOCKPILE&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;ALLOW_FOR_CURRENT_REVIEW_PERIOD&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;FIFTEEN_YEAR_ITEM_LIFE&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

<!-- record:6 cells:15 -->
> [!abstract]- Запись 6 из 6
> - **Горизонт код** (<code>&quot;horizon_code&quot;</code>): <code>&quot;E5&quot;</code>
> - **«vocabulary» версия** (<code>&quot;vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **«ordinal»** (<code>&quot;ordinal&quot;</code>): <code>&quot;5&quot;</code>
> - **«label» на русском** (<code>&quot;label_ru&quot;</code>): <code>&quot;15–100 лет&quot;</code>
> - **«lower» «bound» «iso8601»** (<code>&quot;lower_bound_iso8601&quot;</code>): <code>&quot;P15Y&quot;</code>
> - **«lower» «inclusive»** (<code>&quot;lower_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **«upper» «bound» «iso8601»** (<code>&quot;upper_bound_iso8601&quot;</code>): <code>&quot;P100Y&quot;</code>
> - **«upper» «inclusive»** (<code>&quot;upper_inclusive&quot;</code>): <code>&quot;YES&quot;</code>
> - **Граница «rule»** (<code>&quot;boundary_rule&quot;</code>): <code>&quot;CALENDAR_ANNIVERSARY&quot;</code>
> - **«planning» «intent»** (<code>&quot;planning_intent&quot;</code>): <code>&quot;межпоколенческая и институциональная непрерывность&quot;</code>
> - **Физический «stock» «semantics»** (<code>&quot;physical_stock_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY_NOT_STOCKPILE&quot;</code>
> - **«default» проверка «cadence»** (<code>&quot;default_review_cadence&quot;</code>): <code>&quot;ANNUAL_PLUS_5Y_MIGRATION_25Y_HANDOFF&quot;</code>
> - **Разрешённый «claim»** (<code>&quot;allowed_claim&quot;</code>): <code>&quot;ALLOW_FOR_CURRENT_REVIEW_PERIOD&quot;</code>
> - **Запрещённый «claim»** (<code>&quot;prohibited_claim&quot;</code>): <code>&quot;100_YEAR_READY_OR_GUARANTEED&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;ACTIVE&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
