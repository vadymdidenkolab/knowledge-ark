---
id: "DATA-REGISTER-4ca398d9d545100d"
type: "generated-data-register-view"
title: "Журнал исходных научных наблюдений — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "practical-science-raw-log-template.csv"
source_sha256: "b0baac96ab84124792c97b808d19e19a28c5b6044b66b5543db1ddea27846293"
source_bytes: 1305
source_row_count: 12
source_column_count: 17
source_cell_count: 204
ignored_blank_row_count: 0
semantic_group: "PRACTICAL_SCIENCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: practical-science-raw-log-template.csv -->

# Журнал исходных научных наблюдений — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Практическая наука, приборы и безопасность
- **Записей:** 12
- **Полей в каждой записи:** 17
- **Ячеек данных, включая пустые:** 204
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `b0baac96ab84124792c97b808d19e19a28c5b6044b66b5543db1ddea27846293`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «observation» ID | <code>&quot;observation_id&quot;</code> |
| 2 | «experiment» ID | <code>&quot;experiment_id&quot;</code> |
| 3 | «timestamp» «iso8601» | <code>&quot;timestamp_iso8601&quot;</code> |
| 4 | «operator» ID | <code>&quot;operator_id&quot;</code> |
| 5 | «replicate» | <code>&quot;replicate&quot;</code> |
| 6 | Прибор ID | <code>&quot;instrument_id&quot;</code> |
| 7 | «calibration» запись ID | <code>&quot;calibration_record_id&quot;</code> |
| 8 | «independent» значение | <code>&quot;independent_value&quot;</code> |
| 9 | «independent» единица | <code>&quot;independent_unit&quot;</code> |
| 10 | «dependent» значение | <code>&quot;dependent_value&quot;</code> |
| 11 | «dependent» единица | <code>&quot;dependent_unit&quot;</code> |
| 12 | «ambient» «temperature» «c» | <code>&quot;ambient_temperature_c&quot;</code> |
| 13 | «ambient» «rh» «percent» | <code>&quot;ambient_rh_percent&quot;</code> |
| 14 | «observation» примечание | <code>&quot;observation_note&quot;</code> |
| 15 | «anomaly» «flag» | <code>&quot;anomaly_flag&quot;</code> |
| 16 | «photo» «or» файл ссылка | <code>&quot;photo_or_file_ref&quot;</code> |
| 17 | «row» «lock» состояние | <code>&quot;row_lock_state&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:17 -->
> [!abstract]- Запись 1 из 12 — OBS-TEMPLATE-01
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-01&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:2 cells:17 -->
> [!abstract]- Запись 2 из 12 — OBS-TEMPLATE-02
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-02&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:3 cells:17 -->
> [!abstract]- Запись 3 из 12 — OBS-TEMPLATE-03
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-03&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:4 cells:17 -->
> [!abstract]- Запись 4 из 12 — OBS-TEMPLATE-04
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-04&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:5 cells:17 -->
> [!abstract]- Запись 5 из 12 — OBS-TEMPLATE-05
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-05&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:6 cells:17 -->
> [!abstract]- Запись 6 из 12 — OBS-TEMPLATE-06
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-06&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:7 cells:17 -->
> [!abstract]- Запись 7 из 12 — OBS-TEMPLATE-07
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-07&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:8 cells:17 -->
> [!abstract]- Запись 8 из 12 — OBS-TEMPLATE-08
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-08&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:9 cells:17 -->
> [!abstract]- Запись 9 из 12 — OBS-TEMPLATE-09
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-09&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:10 cells:17 -->
> [!abstract]- Запись 10 из 12 — OBS-TEMPLATE-10
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-10&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:11 cells:17 -->
> [!abstract]- Запись 11 из 12 — OBS-TEMPLATE-11
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-11&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

<!-- record:12 cells:17 -->
> [!abstract]- Запись 12 из 12 — OBS-TEMPLATE-12
> - **«observation» ID** (<code>&quot;observation_id&quot;</code>): <code>&quot;OBS-TEMPLATE-12&quot;</code>
> - **«experiment» ID** (<code>&quot;experiment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«timestamp» «iso8601»** (<code>&quot;timestamp_iso8601&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» ID** (<code>&quot;operator_id&quot;</code>): <code>&quot;&quot;</code>
> - **«replicate»** (<code>&quot;replicate&quot;</code>): <code>&quot;&quot;</code>
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;&quot;</code>
> - **«calibration» запись ID** (<code>&quot;calibration_record_id&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» значение** (<code>&quot;independent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«independent» единица** (<code>&quot;independent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» значение** (<code>&quot;dependent_value&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» единица** (<code>&quot;dependent_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «temperature» «c»** (<code>&quot;ambient_temperature_c&quot;</code>): <code>&quot;&quot;</code>
> - **«ambient» «rh» «percent»** (<code>&quot;ambient_rh_percent&quot;</code>): <code>&quot;&quot;</code>
> - **«observation» примечание** (<code>&quot;observation_note&quot;</code>): <code>&quot;&quot;</code>
> - **«anomaly» «flag»** (<code>&quot;anomaly_flag&quot;</code>): <code>&quot;&quot;</code>
> - **«photo» «or» файл ссылка** (<code>&quot;photo_or_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«row» «lock» состояние** (<code>&quot;row_lock_state&quot;</code>): <code>&quot;BLANK_TEMPLATE&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
