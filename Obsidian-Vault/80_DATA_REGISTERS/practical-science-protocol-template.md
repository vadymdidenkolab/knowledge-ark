---
id: "DATA-REGISTER-8a6eba53c35ae975"
type: "generated-data-register-view"
title: "Научный протокол — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "practical-science-protocol-template.csv"
source_sha256: "fd4c6d02591ea4852b5f58280776d292bacec2e111bf597921a29a5499f5c33e"
source_bytes: 1976
source_row_count: 1
source_column_count: 24
source_cell_count: 24
ignored_blank_row_count: 0
semantic_group: "PRACTICAL_SCIENCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: practical-science-protocol-template.csv -->

# Научный протокол — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Практическая наука, приборы и безопасность
- **Записей:** 1
- **Полей в каждой записи:** 24
- **Ячеек данных, включая пустые:** 24
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `fd4c6d02591ea4852b5f58280776d292bacec2e111bf597921a29a5499f5c33e`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «experiment» ID | <code>&quot;experiment_id&quot;</code> |
| 2 | Идентификатор отрасли | <code>&quot;domain_id&quot;</code> |
| 3 | «question» | <code>&quot;question&quot;</code> |
| 4 | «hypothesis» | <code>&quot;hypothesis&quot;</code> |
| 5 | «independent» «variable» | <code>&quot;independent_variable&quot;</code> |
| 6 | «dependent» «variable» | <code>&quot;dependent_variable&quot;</code> |
| 7 | «controls» | <code>&quot;controls&quot;</code> |
| 8 | «sampling» план | <code>&quot;sampling_plan&quot;</code> |
| 9 | Измерительные приборы | <code>&quot;instrument_ids&quot;</code> |
| 10 | «calibration» запись | <code>&quot;calibration_record&quot;</code> |
| 11 | Метод версия | <code>&quot;method_version&quot;</code> |
| 12 | «preregistered» «expected» «range» | <code>&quot;preregistered_expected_range&quot;</code> |
| 13 | «raw» «data» путь | <code>&quot;raw_data_path&quot;</code> |
| 14 | «calculation» | <code>&quot;calculation&quot;</code> |
| 15 | «uncertainty» | <code>&quot;uncertainty&quot;</code> |
| 16 | «hazards» | <code>&quot;hazards&quot;</code> |
| 17 | Условия остановки | <code>&quot;stop_conditions&quot;</code> |
| 18 | Результат | <code>&quot;result&quot;</code> |
| 19 | «interpretation» | <code>&quot;interpretation&quot;</code> |
| 20 | «limitations» | <code>&quot;limitations&quot;</code> |
| 21 | «reviewer» | <code>&quot;reviewer&quot;</code> |
| 22 | Доказательство хеш | <code>&quot;evidence_hash&quot;</code> |
| 23 | Выпуск состояние | <code>&quot;release_state&quot;</code> |
| 24 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:24 -->
> [!abstract]- Запись 1 из 1 — EXP-EXAMPLE-001
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;EXP-EXAMPLE-001&quot;</code>
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-10&quot;</code>
> - **«question»** (<code>&quot;question&quot;</code>): <code>&quot;Как одинаковый объём воды 35–40 °C остывает в двух разных изоляционных оболочках?&quot;</code>
> - **«hypothesis»** (<code>&quot;hypothesis&quot;</code>): <code>&quot;Оболочка A уменьшит скорость охлаждения относительно B.&quot;</code>
> - **«independent» «variable»** (<code>&quot;independent_variable&quot;</code>): <code>&quot;тип оболочки&quot;</code>
> - **«dependent» «variable»** (<code>&quot;dependent_variable&quot;</code>): <code>&quot;температура воды, °C&quot;</code>
> - **«controls»** (<code>&quot;controls&quot;</code>): <code>&quot;одинаковые устойчивые небьющиеся ёмкости, объём, начальная температура 35–40 °C, место, время отсчёта&quot;</code>
> - **«sampling» план** (<code>&quot;sampling_plan&quot;</code>): <code>&quot;каждые 5 минут в течение 30 минут; 3 независимых повтора&quot;</code>
> - **Измерительные приборы** (<code>&quot;instrument_ids&quot;</code>): <code>&quot;INS-013|INS-011|INS-026&quot;</code>
> - **«calibration» запись** (<code>&quot;calibration_record&quot;</code>): <code>&quot;zero/2-point check per instrument register; exact result TBD before run&quot;</code>
> - **Метод версия** (<code>&quot;method_version&quot;</code>): <code>&quot;DRAFT-0.1&quot;</code>
> - **«preregistered» «expected» «range»** (<code>&quot;preregistered_expected_range&quot;</code>): <code>&quot;TBD_FROM_SOURCE_AND_PILOT&quot;</code>
> - **«raw» «data» путь** (<code>&quot;raw_data_path&quot;</code>): <code>&quot;records/science/SCI-PHYS-10/YYYY-MM-DD/raw.csv&quot;</code>
> - **«calculation»** (<code>&quot;calculation&quot;</code>): <code>&quot;температурное падение и средняя скорость °C/min; сравнить повторы&quot;</code>
> - **«uncertainty»** (<code>&quot;uncertainty&quot;</code>): <code>&quot;resolution + repeat spread + operator timing&quot;</code>
> - **«hazards»** (<code>&quot;hazards&quot;</code>): <code>&quot;небольшой пролив/скольжение; контакт с тёплой водой; опрокидывание ёмкости&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;STOP до старта, если вода &gt;40 °C; STOP при повреждении/неустойчивости ёмкости, любом проливе возле подключённого оборудования или невозможности удерживать сухую устойчивую площадку&quot;</code>
> - **Результат** (<code>&quot;result&quot;</code>): <code>&quot;NOT_RUN&quot;</code>
> - **«interpretation»** (<code>&quot;interpretation&quot;</code>): <code>&quot;NOT_RUN&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;room airflow/container differences; no claim beyond tested range&quot;</code>
> - **«reviewer»** (<code>&quot;reviewer&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство хеш** (<code>&quot;evidence_hash&quot;</code>): <code>&quot;&quot;</code>
> - **Выпуск состояние** (<code>&quot;release_state&quot;</code>): <code>&quot;TEMPLATE_EXAMPLE_NOT_EXECUTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
