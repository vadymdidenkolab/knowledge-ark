---
id: "DATA-REGISTER-9f9537ff3ca79b54"
type: "generated-data-register-view"
title: "Реестр климатических траекторий — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "climate-pathway-register-template.csv"
source_sha256: "7a85444b857c77f2e658e0b62037b310dd814dcd37b76acea3ad01c0e8c57f62"
source_bytes: 825
source_row_count: 1
source_column_count: 29
source_cell_count: 29
ignored_blank_row_count: 0
semantic_group: "MAPS_ENVIRONMENT"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: climate-pathway-register-template.csv -->

# Реестр климатических траекторий — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Карты, маршруты и климат
- **Записей:** 1
- **Полей в каждой записи:** 29
- **Ячеек данных, включая пустые:** 29
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `7a85444b857c77f2e658e0b62037b310dd814dcd37b76acea3ad01c0e8c57f62`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «pathway» ID | <code>&quot;pathway_id&quot;</code> |
| 2 | Объект ID | <code>&quot;site_id&quot;</code> |
| 3 | Источник ID | <code>&quot;source_id&quot;</code> |
| 4 | Источник «edition» | <code>&quot;source_edition&quot;</code> |
| 5 | Сценарий «family» | <code>&quot;scenario_family&quot;</code> |
| 6 | Сценарий «identifier» | <code>&quot;scenario_identifier&quot;</code> |
| 7 | «geographic» «resolution» | <code>&quot;geographic_resolution&quot;</code> |
| 8 | «baseline» «period» | <code>&quot;baseline_period&quot;</code> |
| 9 | Целевой горизонт | <code>&quot;target_horizon&quot;</code> |
| 10 | «temperature» «variables» ссылка | <code>&quot;temperature_variables_ref&quot;</code> |
| 11 | «precipitation» «variables» ссылка | <code>&quot;precipitation_variables_ref&quot;</code> |
| 12 | «drought» «variables» ссылка | <code>&quot;drought_variables_ref&quot;</code> |
| 13 | «fire» «variables» ссылка | <code>&quot;fire_variables_ref&quot;</code> |
| 14 | «flood» «variables» ссылка | <code>&quot;flood_variables_ref&quot;</code> |
| 15 | «coastal» «variables» ссылка | <code>&quot;coastal_variables_ref&quot;</code> |
| 16 | «uncertainty» «statement» | <code>&quot;uncertainty_statement&quot;</code> |
| 17 | «observed» «monitoring» ссылки | <code>&quot;observed_monitoring_refs&quot;</code> |
| 18 | Возможность «impacts» | <code>&quot;capability_impacts&quot;</code> |
| 19 | «adaptation» «option» ID | <code>&quot;adaptation_option_ids&quot;</code> |
| 20 | «maladaptation» риск | <code>&quot;maladaptation_risk&quot;</code> |
| 21 | «lock» «in» риск | <code>&quot;lock_in_risk&quot;</code> |
| 22 | «reversibility» класс | <code>&quot;reversibility_class&quot;</code> |
| 23 | Решение триггер ID | <code>&quot;decision_trigger_ids&quot;</code> |
| 24 | «retreat» «or» «relocation» триггер ID | <code>&quot;retreat_or_relocation_trigger_ids&quot;</code> |
| 25 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 26 | Профессиональный проверка состояние | <code>&quot;professional_review_state&quot;</code> |
| 27 | «pathway» состояние | <code>&quot;pathway_state&quot;</code> |
| 28 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 29 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:29 -->
> [!abstract]- Запись 1 из 1 — TBD
> - **«pathway» ID** (<code>&quot;pathway_id&quot;</code>): <code>&quot;CLIMATE-EXAMPLE-001&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;SITE-TBD&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «family»** (<code>&quot;scenario_family&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «identifier»** (<code>&quot;scenario_identifier&quot;</code>): <code>&quot;&quot;</code>
> - **«geographic» «resolution»** (<code>&quot;geographic_resolution&quot;</code>): <code>&quot;&quot;</code>
> - **«baseline» «period»** (<code>&quot;baseline_period&quot;</code>): <code>&quot;&quot;</code>
> - **Целевой горизонт** (<code>&quot;target_horizon&quot;</code>): <code>&quot;E5&quot;</code>
> - **«temperature» «variables» ссылка** (<code>&quot;temperature_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«precipitation» «variables» ссылка** (<code>&quot;precipitation_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«drought» «variables» ссылка** (<code>&quot;drought_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«fire» «variables» ссылка** (<code>&quot;fire_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«flood» «variables» ссылка** (<code>&quot;flood_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«coastal» «variables» ссылка** (<code>&quot;coastal_variables_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«uncertainty» «statement»** (<code>&quot;uncertainty_statement&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«observed» «monitoring» ссылки** (<code>&quot;observed_monitoring_refs&quot;</code>): <code>&quot;&quot;</code>
> - **Возможность «impacts»** (<code>&quot;capability_impacts&quot;</code>): <code>&quot;&quot;</code>
> - **«adaptation» «option» ID** (<code>&quot;adaptation_option_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«maladaptation» риск** (<code>&quot;maladaptation_risk&quot;</code>): <code>&quot;&quot;</code>
> - **«lock» «in» риск** (<code>&quot;lock_in_risk&quot;</code>): <code>&quot;&quot;</code>
> - **«reversibility» класс** (<code>&quot;reversibility_class&quot;</code>): <code>&quot;&quot;</code>
> - **Решение триггер ID** (<code>&quot;decision_trigger_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«retreat» «or» «relocation» триггер ID** (<code>&quot;retreat_or_relocation_trigger_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«pathway» состояние** (<code>&quot;pathway_state&quot;</code>): <code>&quot;CANDIDATE&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Одна projection line не является адресным прогнозом&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
