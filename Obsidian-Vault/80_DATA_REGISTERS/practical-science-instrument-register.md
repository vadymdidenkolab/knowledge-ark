---
id: "DATA-REGISTER-f5811c874d9be81d"
type: "generated-data-register-view"
title: "Измерительные приборы практической науки"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "practical-science-instrument-register.csv"
source_sha256: "95e62aac3bdaa0db95ee8b72b0b37a390abe7820b66d3e95f4869b4463e7c186"
source_bytes: 102448
source_row_count: 73
source_column_count: 19
source_cell_count: 1387
ignored_blank_row_count: 0
semantic_group: "PRACTICAL_SCIENCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: practical-science-instrument-register.csv -->

# Измерительные приборы практической науки

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Практическая наука, приборы и безопасность
- **Записей:** 73
- **Полей в каждой записи:** 19
- **Ячеек данных, включая пустые:** 1387
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `95e62aac3bdaa0db95ee8b72b0b37a390abe7820b66d3e95f4869b4463e7c186`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Прибор ID | <code>&quot;instrument_id&quot;</code> |
| 2 | «category» | <code>&quot;category&quot;</code> |
| 3 | Прибор на русском | <code>&quot;instrument_ru&quot;</code> |
| 4 | «measures» | <code>&quot;measures&quot;</code> |
| 5 | Единица | <code>&quot;unit&quot;</code> |
| 6 | «range» «hint» | <code>&quot;range_hint&quot;</code> |
| 7 | «resolution» «hint» | <code>&quot;resolution_hint&quot;</code> |
| 8 | «calibration» метод | <code>&quot;calibration_method&quot;</code> |
| 9 | Ссылка требуемый | <code>&quot;reference_required&quot;</code> |
| 10 | Интервал | <code>&quot;interval&quot;</code> |
| 11 | Хранение | <code>&quot;storage&quot;</code> |
| 12 | Обслуживание | <code>&quot;maintenance&quot;</code> |
| 13 | Отказ «signs» | <code>&quot;failure_signs&quot;</code> |
| 14 | Класс безопасности | <code>&quot;safety_class&quot;</code> |
| 15 | Запрещённый «use» | <code>&quot;prohibited_use&quot;</code> |
| 16 | «spare» «strategy» | <code>&quot;spare_strategy&quot;</code> |
| 17 | «manual» «package» ID | <code>&quot;manual_package_id&quot;</code> |
| 18 | Статус | <code>&quot;status&quot;</code> |
| 19 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:19 -->
> [!abstract]- Запись 1 из 73 — INS-001
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;стальная линейка&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;длина&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;проверка нуля и сравнение с прослеживаемым эталоном длины&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать повреждённую кромку как режущий инструмент&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;две линейки разных производителей&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:2 cells:19 -->
> [!abstract]- Запись 2 из 73 — INS-002
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-002&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;рулетка&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;длина&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm|m&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;проверка нуля/зацепа и нескольких точек&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не отпускать ленту неконтролируемо&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;запасная рулетка и складной метр&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:3 cells:19 -->
> [!abstract]- Запись 3 из 73 — INS-003
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-003&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;штангенциркуль&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;наружный/внутренний размер&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;очистка губок, zero check, проверочный блок&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не измерять вращающиеся/электрические части&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механический плюс цифровой&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:4 cells:19 -->
> [!abstract]- Запись 4 из 73 — INS-004
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-004&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;микрометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;малый размер&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;нулевой эталон/набор мер и трещотка&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не превышать усилие и диапазон&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механический эталон&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:5 cells:19 -->
> [!abstract]- Запись 5 из 73 — INS-005
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-005&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;угольник&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;прямой угол&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;degree/pass-fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;flip test на прямой линии&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не применять как ударный инструмент&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;малый и строительный&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:6 cells:19 -->
> [!abstract]- Запись 6 из 73 — INS-006
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-006&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;уровень пузырьковый&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;наклон&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm/m&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;переворот на одной поверхности&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать на высоте без защиты&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;короткий и длинный&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:7 cells:19 -->
> [!abstract]- Запись 7 из 73 — INS-007
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-007&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;цифровой угломер/инклинометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;угол/наклон&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;degree&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;zero на проверенной поверхности и reversal test&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать как доказательство структурной безопасности&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механический транспортир&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:8 cells:19 -->
> [!abstract]- Запись 8 из 73 — INS-008
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-008&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;набор калибровочных гирь&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;масса-эталон&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;g&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сертификат/класс, чистота и контрольная карта&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не считать бытовые предметы прослеживаемым эталоном&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;две номинальные точки&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:9 cells:19 -->
> [!abstract]- Запись 9 из 73 — INS-009
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-009&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;весы кухонные&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;масса&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;g&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;zero, несколько гирь, повторяемость и corner-load&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать для лекарственных доз&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механические весы как fallback&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:10 cells:19 -->
> [!abstract]- Запись 10 из 73 — INS-010
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-010&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;METROLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;весы платформенные&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;масса&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;kg&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сертифицированные гири/сервис и repeatability&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не превышать нагрузку и не стоять под грузом&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй диапазон/сервис&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:11 cells:19 -->
> [!abstract]- Запись 11 из 73 — INS-011
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-011&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;TIME&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;механические часы/секундомер&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;время&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;s&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с двумя независимыми эталонами времени&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать один дрейфующий источник как эталон&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;кварцевые часы + ради/GNSS при наличии&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:12 cells:19 -->
> [!abstract]- Запись 12 из 73 — INS-012
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-012&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;TIME&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;RTC/частотный счётчик&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;частота/время&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;Hz|s&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с прослеживаемым частотным источником&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не подключать к опасному напряжению&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;запасной модуль и опубликованный offset&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:13 cells:19 -->
> [!abstract]- Запись 13 из 73 — INS-013
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-013&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;THERMAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;контактный цифровой термометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;температура&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;°C&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;ледяная точка/сертифицированный термостат и 2-точечная проверка&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать бытовую калибровку для клинических решений&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два датчика разных типов&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:14 cells:19 -->
> [!abstract]- Запись 14 из 73 — INS-014
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-014&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;THERMAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;макс-мин термометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;температура&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;°C&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с опорным датчиком в общей среде&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;защищать от прямого солнца и влаги&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;аналоговый резерв&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:15 cells:19 -->
> [!abstract]- Запись 15 из 73 — INS-015
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-015&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;THERMAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;термопара и считыватель&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;температура&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;°C&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;reference junction и сравнение по двум точкам&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не касаться электрически опасных/движущихся частей&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;запасные зонды&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:16 cells:19 -->
> [!abstract]- Запись 16 из 73 — INS-016
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-016&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;THERMAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;ИК-термометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;температура поверхности&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;°C&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;blackbody/сравнительная поверхность и emissivity note&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не измеряет внутреннюю температуру и воздух; лазер не направлять в глаза&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;контактный термометр&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:17 cells:19 -->
> [!abstract]- Запись 17 из 73 — INS-017
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-017&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;гигрометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;относительная влажность&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;%RH&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сертифицированная salt-point/эталонная камера&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не считать дешёвый датчик эталоном без проверки&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два датчика и психрометр&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:18 cells:19 -->
> [!abstract]- Запись 18 из 73 — INS-018
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-018&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;барометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;давление&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;hPa&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с официальной станцией с поправкой высоты&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать для прогноза без контекста&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механический и цифровой&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:19 cells:19 -->
> [!abstract]- Запись 19 из 73 — INS-019
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-019&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;анемометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;скорость воздуха&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;m/s&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сервис/сравнение в контролируемом потоке&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не измерять с крыши/у ЛЭП/в шторм&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;визуальные шкалы Beaufort как fallback&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:20 cells:19 -->
> [!abstract]- Запись 20 из 73 — INS-020
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-020&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;дождемер&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;осадки&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;объёмная проверка площади приёмника&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;устанавливать без высотной работы&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;ручной резерв&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:21 cells:19 -->
> [!abstract]- Запись 21 из 73 — INS-021
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-021&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;люксметр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;освещённость&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;lx&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с калиброванным прибором/лабораторией&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не измерять Солнце без допустимого диапазона&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два сенсора/эталонная лампа по сроку&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:22 cells:19 -->
> [!abstract]- Запись 22 из 73 — INS-022
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-022&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;шумомер класса по задаче&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;уровень звука&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;dB(A/C)&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;акустический калибратор до/после серии&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;телефон — ориентир, не юридическое измерение&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;калибратор и второй прибор&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:23 cells:19 -->
> [!abstract]- Запись 23 из 73 — INS-023
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-023&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;датчик CO2 NDIR&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;CO2&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;ppm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;fresh-air check/сертифицированный газ у специалиста&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;CO2 не заменяет датчик CO и не доказывает отсутствие инфекции&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два NDIR разных партий&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:24 cells:19 -->
> [!abstract]- Запись 24 из 73 — INS-024
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-024&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;сертифицированный бытовой CO alarm&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;CO alarm&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;ppm/alarm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;только штатная test-кнопка/замена по сроку; газовые опыты запрещены&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;никогда не тестировать выхлопом/огнём&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;несколько alarms по размещению&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:25 cells:19 -->
> [!abstract]- Запись 25 из 73 — INS-025
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-025&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENVIRONMENT&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;PM2.5 монитор&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;массовая концентрация-оценка&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;µg/m³&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;co-location с референсом/контроль нуля по инструкции&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;низкобюджетный сенсор не равен регуляторной станции&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй тип + официальный мониторинг&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:26 cells:19 -->
> [!abstract]- Запись 26 из 73 — INS-026
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-026&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;мерный цилиндр/кувшин&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;объём&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mL|L&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;гравиметрическая проверка водой при известной температуре&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не смешивать пищевую и химическую посуду&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;набор размеров&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:27 cells:19 -->
> [!abstract]- Запись 27 из 73 — INS-027
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-027&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;расходомер низкого давления&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;расход&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;L/min&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;timed-volume comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не подключать к газу/опасному давлению&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;ведро+секундомер&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:28 cells:19 -->
> [!abstract]- Запись 28 из 73 — INS-028
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-028&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;манометр воды&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;давление&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;bar|kPa&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;deadweight/service calibration or comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;разгерметизировать; не применять к газовым/высоким давлениям&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;механический резерв&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:29 cells:19 -->
> [!abstract]- Запись 29 из 73 — INS-029
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-029&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;pH-метр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;pH&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;pH&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;2–3 свежих буфера, slope/offset log&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;pH не доказывает питьевую безопасность&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;полоски как грубый fallback&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:30 cells:19 -->
> [!abstract]- Запись 30 из 73 — INS-030
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-030&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;TDS/EC-метр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;электропроводность&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;µS/cm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сертифицированный стандарт и температурная компенсация&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;TDS не выявляет конкретные токсины/патогены&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй прибор/стандарт&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:31 cells:19 -->
> [!abstract]- Запись 31 из 73 — INS-031
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-031&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;турбидиметр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;мутность&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;NTU&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сертифицированные standards и blank&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;мутность не равна микробиологической безопасности&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;визуальная tube как fallback&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:32 cells:19 -->
> [!abstract]- Запись 32 из 73 — INS-032
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-032&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;хлорный колориметр DPD&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;свободный/общий хлор&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mg/L&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;blank, standards/verification kit и срок реагента&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не импровизировать дозирование; реагенты по SDS&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;запас реагентов и второй метод&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:33 cells:19 -->
> [!abstract]- Запись 33 из 73 — INS-033
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-033&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOIL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;почвенный бур/пробоотборник&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;глубина/проба&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;cm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;разметка глубины и очистка между точками&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только ручная неглубокая проба после документированной clearance коммуникаций/загрязнения/склона; силовое бурение и неизвестная площадка запрещены&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;лопатка для неглубоких заранее разрешённых проб&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:34 cells:19 -->
> [!abstract]- Запись 34 из 73 — INS-034
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-034&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOIL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;сита для текстуры/агрегатов&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;размер частиц&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;проверка маркировки/повреждения и контрольная смесь&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;пыль — вентиляция/СИЗ; не анализировать подозрительные загрязнения&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;ручная текстурная оценка&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:35 cells:19 -->
> [!abstract]- Запись 35 из 73 — INS-035
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-035&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;тензиометр/датчик влажности почвы&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;водный потенциал/влажность&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;kPa|%&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;почвоспецифическая калибровка и gravimetric comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не принимать универсальные проценты как истину&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;ручная проба + второй датчик&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:36 cells:19 -->
> [!abstract]- Запись 36 из 73 — INS-036
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-036&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;счётчик семян и лоток всхожести&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;всхожесть&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;%&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;известное количество, blind recount и control lot&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только законные/идентифицированные семена&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;ручной пересчёт&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:37 cells:19 -->
> [!abstract]- Запись 37 из 73 — INS-037
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-037&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;leaf-area scale/grid&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;площадь листа&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;cm²&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;геометрическая проверка grid/reference&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не повреждать охраняемые растения&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;фото с масштабом&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:38 cells:19 -->
> [!abstract]- Запись 38 из 73 — INS-038
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-038&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;BIOLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;лупа 10x&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;морфология&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;dimensionless&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;проверка фокуса и scale card&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не направлять Солнце в глаза/на горючее&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;вторая лупа&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:39 cells:19 -->
> [!abstract]- Запись 39 из 73 — INS-039
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-039&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;BIOLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;оптический микроскоп для готовых слайдов&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;изображение/масштаб&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;µm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;stage micrometer и чистый known slide&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не культивировать/не исследовать неизвестные биообразцы&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;лупа+готовый атлас&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:40 cells:19 -->
> [!abstract]- Запись 40 из 73 — INS-040
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-040&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;BIOLOGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;камера/фотоаппарат с scale card&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;изображение и время&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;px|mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;clock check, color/scale card and metadata&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;приватность, геолокация чувствительных видов/людей&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два формата и печатные выборки&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:41 cells:19 -->
> [!abstract]- Запись 41 из 73 — INS-041
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-041&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;клинический цифровой термометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;температура тела&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;°C&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;штатная проверка/профессиональная поверка по назначению&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не интерпретировать вне инструкции/клинического контекста&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй одобренный прибор&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:42 cells:19 -->
> [!abstract]- Запись 42 из 73 — INS-042
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-042&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;автоматический тонометр валидированной модели&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;давление/пульс&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mmHg|bpm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;проверка модели, манжеты и периодическое сравнение в клинике&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не менять лечение по одному измерению&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;запасная манжета/клиническая сверка&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:43 cells:19 -->
> [!abstract]- Запись 43 из 73 — INS-043
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-043&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;пульсоксиметр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;SpO2/пульс&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;%|bpm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;functional check and professional comparison; limitations logged&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;плохая перфузия/движение/лак и другие факторы искажают; не откладывать помощь&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй метод клинической оценки — специалист&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:44 cells:19 -->
> [!abstract]- Запись 44 из 73 — INS-044
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-044&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;манекен BLS/AED trainer&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;навык&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;rubric/pass-fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;инструкторская проверка и расходники&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не тренироваться на человеке; trainer не является рабочим AED&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;регулярный курс/второй манекен&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:45 cells:19 -->
> [!abstract]- Запись 45 из 73 — INS-045
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-045&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;цифровой мультиметр CAT по задаче&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;V/A/Ω&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;V|A|Ω&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;proof source/service calibration; lead/fuse inspection&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;базовый kit ограничен изолированным низким напряжением; mains — специалист&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй простой meter&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:46 cells:19 -->
> [!abstract]- Запись 46 из 73 — INS-046
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-046&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;регулируемый лабораторный БП с limit&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;напряжение/ток&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;V|A&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;сравнение с калиброванным meter и проверка current limit&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не заряжать неизвестные батареи/не питать тело&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;фиксированные защищённые адаптеры&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:47 cells:19 -->
> [!abstract]- Запись 47 из 73 — INS-047
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-047&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;USB power meter&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;энергия/ток&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;Wh|A|V&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;comparison with reference load/source&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать на сети 230 V&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй meter/known load&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:48 cells:19 -->
> [!abstract]- Запись 48 из 73 — INS-048
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-048&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;DC electronic load low-power&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;нагрузка/энергия&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;A|W|Wh&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;reference meter and thermal check&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не превышать мощность; огнестойкая площадка и надзор&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;резистивные certified loads&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:49 cells:19 -->
> [!abstract]- Запись 49 из 73 — INS-049
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-049&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;осциллограф low-voltage isolated use&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;напряжение/время&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;V|s|Hz&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;internal cal output and service calibration&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не подключать ground clip к сети/неизолированным опасным цепям&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;logic analyzer/USB scope with limits&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:50 cells:19 -->
> [!abstract]- Запись 50 из 73 — INS-050
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-050&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;логический анализатор&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;цифровой сигнал&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;V logic|Hz&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known pattern generator&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только безопасные logic levels&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;software decoder and spare probes&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:51 cells:19 -->
> [!abstract]- Запись 51 из 73 — INS-051
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-051&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;LCR-метр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;R/L/C&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;Ω|H|F&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;open/short calibration and standards&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только новые известные малые низковольтные учебные компоненты; неизвестные/извлечённые capacitors, power electronics и in-circuit measurement запрещены&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;known low-energy components&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:52 cells:19 -->
> [!abstract]- Запись 52 из 73 — INS-052
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-052&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ELECTRICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;низковольтный data logger&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;сенсорный ряд&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;SI by sensor&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;reference points per channel and clock sync&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать для safety-critical control&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;бумажный журнал/второй logger&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:53 cells:19 -->
> [!abstract]- Запись 53 из 73 — INS-053
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-053&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENERGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;plug-in energy meter approved for EU socket&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;мощность/энергия&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;W|Wh&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;reference load/service check&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только штатное включение; не вскрывать и не использовать с повреждением&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;utility meter trend/second unit&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:54 cells:19 -->
> [!abstract]- Запись 54 из 73 — INS-054
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-054&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENERGY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;solar irradiance reference cell/pyranometer&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;облучённость&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;W/m²&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;manufacturer calibration and intercomparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;крыша/высота требует специалиста&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;horizontal accessible reference point&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:55 cells:19 -->
> [!abstract]- Запись 55 из 73 — INS-055
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-055&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;пружинный динамометр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;сила&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;N&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known masses within local g and range&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не поднимать людей/опасные грузы&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;две шкалы&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:56 cells:19 -->
> [!abstract]- Запись 56 из 73 — INS-056
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-056&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;динамометрический ключ&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;момент&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;N·m&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;accredited calibration and exercise/storage at minimum setting&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать как breaker bar; safety fasteners by spec&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй диапазон/service&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:57 cells:19 -->
> [!abstract]- Запись 57 из 73 — INS-057
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-057&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;тахометр оптический&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;частота вращения&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;rpm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;reflective target on safe trainer/known source&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;ограждение; не приближаться к вращающимся деталям&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;video analysis&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:58 cells:19 -->
> [!abstract]- Запись 58 из 73 — INS-058
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-058&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;виброметр&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;ускорение/скорость&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;m/s²|mm/s&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;calibrator/service and fixed mounting protocol&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не приближаться к неограждённому механизму&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;trend by same sensor&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:59 cells:19 -->
> [!abstract]- Запись 59 из 73 — INS-059
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-059&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;feeler gauge&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;зазор&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;cleanliness and comparison/reference block&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;только остановленное/изолированное оборудование&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;duplicate set&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:60 cells:19 -->
> [!abstract]- Запись 60 из 73 — INS-060
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-060&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MECHANICAL&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;thread pitch gauge&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;шаг резьбы&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm|TPI&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known fastener/reference chart&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не применять к вращающейся детали&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;printable chart/caliper&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:61 cells:19 -->
> [!abstract]- Запись 61 из 73 — INS-061
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-061&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;магнитный компас&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;азимут&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;degree&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known line/reversal, declination date and interference check&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не использовать рядом с сильными магнитами; one instrument is not route safety&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;два компаса и бумажная карта&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:62 cells:19 -->
> [!abstract]- Запись 62 из 73 — INS-062
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-062&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;GNSS receiver&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;координаты/время&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;lat/lon/height/time&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known control point and multi-fix comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;координата не доказывает проходимость/безопасность&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;phone + standalone + paper&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:63 cells:19 -->
> [!abstract]- Запись 63 из 73 — INS-063
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-063&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;лазерный дальномер Class 2 or safer&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;длина&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;m&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known baseline and battery check&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не направлять в глаза/транспорт; соблюдать класс лазера&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;рулетка&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:64 cells:19 -->
> [!abstract]- Запись 64 из 73 — INS-064
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-064&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;оптический нивелир/рейка&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;перепад высоты&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;mm|m&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;two-peg test and closure&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;штатив вне движения/краёв; не смотреть на Солнце&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;water level for small safe tasks&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:65 cells:19 -->
> [!abstract]- Запись 65 из 73 — INS-065
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-065&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;COMPUTING&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;два независимых hash-инструмента&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;fixity&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;SHA-256&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;test vectors and cross-tool comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;hash не доказывает безопасность/правдивость содержимого&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;printed checksums and alternate OS&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:66 cells:19 -->
> [!abstract]- Запись 66 из 73 — INS-066
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-066&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;COMPUTING&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;offline clock/source-of-truth appliance&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;время/version&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;UTC/ISO-8601&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;compare against multiple sources before disconnect&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не считать время юридически прослеживаемым без соответствующей службы&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;mechanical/quartz logs&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:67 cells:19 -->
> [!abstract]- Запись 67 из 73 — INS-067
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-067&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;оптический/штрихкод сканер&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;идентификатор&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;text/check digit&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known test sheet and checksum validation&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не кодировать секреты в открытые labels&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;manual typed ID&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:68 cells:19 -->
> [!abstract]- Запись 68 из 73 — INS-068
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-068&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;документ-сканер&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;изображение/OCR&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;dpi|pixel&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;resolution target, color/scale card and page-count reconciliation&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;контроль приватности и повреждения оригинала&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;camera rig + flatbed&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:69 cells:19 -->
> [!abstract]- Запись 69 из 73 — INS-069
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-069&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;USB/SATA write blocker&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;read-only acquisition&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;pass/fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;known writable test device before/after&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не считать бытовой адаптер forensic-grade без проверки&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;read-only media/copy-on-write workflow&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:70 cells:19 -->
> [!abstract]- Запись 70 из 73 — INS-070
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-070&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;printer with archival workflow&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;печатный вывод&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;dpi/page&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;test target, page count and visual comparison&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;вентиляция, расходники, персональные данные&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;второй print path/ручная копия core&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:71 cells:19 -->
> [!abstract]- Запись 71 из 73 — INS-071
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-071&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SAFETY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;штатный детектор дыма&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;smoke alarm&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;alarm/pass-fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;test button and replacement date; aerosol only if manufacturer allows&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не тестировать огнём/дымом вне инструкции&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;несколько detectors по плану&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:72 cells:19 -->
> [!abstract]- Запись 72 из 73 — INS-072
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-072&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SAFETY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;штатный детектор утечки воды&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;water alarm&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;alarm/pass-fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;test probe with clean water per manual&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не помещать электронику вне rated environment&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;несколько points + visual checks&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:73 cells:19 -->
> [!abstract]- Запись 73 из 73 — INS-073
> - **Прибор ID** (<code>&quot;instrument_id&quot;</code>): <code>&quot;INS-073&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SAFETY&quot;</code>
> - **Прибор на русском** (<code>&quot;instrument_ru&quot;</code>): <code>&quot;RCD/GFCI tester approved for jurisdiction&quot;</code>
> - **«measures»** (<code>&quot;measures&quot;</code>): <code>&quot;защитное отключение&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;ms/pass-fail&quot;</code>
> - **«range» «hint»** (<code>&quot;range_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.&quot;</code>
> - **«resolution» «hint»** (<code>&quot;resolution_hint&quot;</code>): <code>&quot;TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.&quot;</code>
> - **«calibration» метод** (<code>&quot;calibration_method&quot;</code>): <code>&quot;только штатная test function/qualified inspection&quot;</code>
> - **Ссылка требуемый** (<code>&quot;reference_required&quot;</code>): <code>&quot;TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.&quot;</code>
> - **Интервал** (<code>&quot;interval&quot;</code>): <code>&quot;BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER&quot;</code>
> - **Хранение** (<code>&quot;storage&quot;</code>): <code>&quot;чисто, сухо, защищено от удара/магнитов/температуры по manual&quot;</code>
> - **Обслуживание** (<code>&quot;maintenance&quot;</code>): <code>&quot;визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки&quot;</code>
> - **Отказ «signs»** (<code>&quot;failure_signs&quot;</code>): <code>&quot;нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;не вскрывать щит и не создавать fault; интерпретация установки — электрик&quot;</code>
> - **«spare» «strategy»** (<code>&quot;spare_strategy&quot;</code>): <code>&quot;built-in test + professional schedule&quot;</code>
> - **«manual» «package» ID** (<code>&quot;manual_package_id&quot;</code>): <code>&quot;PSP-116&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;CANDIDATE_NOT_INVENTORIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
