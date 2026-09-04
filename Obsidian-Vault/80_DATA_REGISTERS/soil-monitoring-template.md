---
id: "DATA-REGISTER-1f48a47f119a7b3f"
type: "generated-data-register-view"
title: "Мониторинг почвы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "soil-monitoring-template.csv"
source_sha256: "7a8a41482ae074ea383020a94022b252275d88bc7abd4c5512785e8d89b5c7eb"
source_bytes: 708
source_row_count: 1
source_column_count: 26
source_cell_count: 26
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: soil-monitoring-template.csv -->

# Мониторинг почвы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 1
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 26
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `7a8a41482ae074ea383020a94022b252275d88bc7abd4c5512785e8d89b5c7eb`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «sample» ID | <code>&quot;sample_id&quot;</code> |
| 2 | «parcel» ID | <code>&quot;parcel_id&quot;</code> |
| 3 | «plot» ID | <code>&quot;plot_id&quot;</code> |
| 4 | «sampled» время | <code>&quot;sampled_at&quot;</code> |
| 5 | «sampling» протокол ссылка | <code>&quot;sampling_protocol_ref&quot;</code> |
| 6 | «sampler» | <code>&quot;sampler&quot;</code> |
| 7 | «laboratory» | <code>&quot;laboratory&quot;</code> |
| 8 | «depth» «range» | <code>&quot;depth_range&quot;</code> |
| 9 | «ph» | <code>&quot;ph&quot;</code> |
| 10 | «organic» «matter» | <code>&quot;organic_matter&quot;</code> |
| 11 | «salinity» | <code>&quot;salinity&quot;</code> |
| 12 | «macronutrient» «results» ссылка | <code>&quot;macronutrient_results_ref&quot;</code> |
| 13 | «micronutrient» «results» ссылка | <code>&quot;micronutrient_results_ref&quot;</code> |
| 14 | «contaminant» «panel» ссылка | <code>&quot;contaminant_panel_ref&quot;</code> |
| 15 | «contaminant» результат ссылка | <code>&quot;contaminant_result_ref&quot;</code> |
| 16 | «erosion» состояние | <code>&quot;erosion_state&quot;</code> |
| 17 | «compaction» состояние | <code>&quot;compaction_state&quot;</code> |
| 18 | Вода «infiltration» результат | <code>&quot;water_infiltration_result&quot;</code> |
| 19 | «biodiversity» «observation» ссылка | <code>&quot;biodiversity_observation_ref&quot;</code> |
| 20 | «interpretation» источник ссылка | <code>&quot;interpretation_source_ref&quot;</code> |
| 21 | Профессиональный проверка состояние | <code>&quot;professional_review_state&quot;</code> |
| 22 | «corrective» действие ссылка | <code>&quot;corrective_action_ref&quot;</code> |
| 23 | Следующий «sample» срок | <code>&quot;next_sample_due&quot;</code> |
| 24 | Результат состояние | <code>&quot;result_state&quot;</code> |
| 25 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 1 — SOIL-EXAMPLE-001
> - **«sample» ID** (<code>&quot;sample_id&quot;</code>): <code>&quot;SOIL-EXAMPLE-001&quot;</code>
> - **«parcel» ID** (<code>&quot;parcel_id&quot;</code>): <code>&quot;PARCEL-EXAMPLE-001&quot;</code>
> - **«plot» ID** (<code>&quot;plot_id&quot;</code>): <code>&quot;PLOT-TBD&quot;</code>
> - **«sampled» время** (<code>&quot;sampled_at&quot;</code>): <code>&quot;&quot;</code>
> - **«sampling» протокол ссылка** (<code>&quot;sampling_protocol_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«sampler»** (<code>&quot;sampler&quot;</code>): <code>&quot;&quot;</code>
> - **«laboratory»** (<code>&quot;laboratory&quot;</code>): <code>&quot;&quot;</code>
> - **«depth» «range»** (<code>&quot;depth_range&quot;</code>): <code>&quot;&quot;</code>
> - **«ph»** (<code>&quot;ph&quot;</code>): <code>&quot;&quot;</code>
> - **«organic» «matter»** (<code>&quot;organic_matter&quot;</code>): <code>&quot;&quot;</code>
> - **«salinity»** (<code>&quot;salinity&quot;</code>): <code>&quot;&quot;</code>
> - **«macronutrient» «results» ссылка** (<code>&quot;macronutrient_results_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«micronutrient» «results» ссылка** (<code>&quot;micronutrient_results_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«contaminant» «panel» ссылка** (<code>&quot;contaminant_panel_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«contaminant» результат ссылка** (<code>&quot;contaminant_result_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«erosion» состояние** (<code>&quot;erosion_state&quot;</code>): <code>&quot;&quot;</code>
> - **«compaction» состояние** (<code>&quot;compaction_state&quot;</code>): <code>&quot;&quot;</code>
> - **Вода «infiltration» результат** (<code>&quot;water_infiltration_result&quot;</code>): <code>&quot;&quot;</code>
> - **«biodiversity» «observation» ссылка** (<code>&quot;biodiversity_observation_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«interpretation» источник ссылка** (<code>&quot;interpretation_source_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«corrective» действие ссылка** (<code>&quot;corrective_action_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий «sample» срок** (<code>&quot;next_sample_due&quot;</code>): <code>&quot;&quot;</code>
> - **Результат состояние** (<code>&quot;result_state&quot;</code>): <code>&quot;NO_SAMPLE&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Цвет запах и бытовой тест не исключают contamination&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
