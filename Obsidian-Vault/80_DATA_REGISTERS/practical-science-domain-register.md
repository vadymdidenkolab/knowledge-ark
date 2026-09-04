---
id: "DATA-REGISTER-96392d95b38059a0"
type: "generated-data-register-view"
title: "Отрасли практической науки"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "practical-science-domain-register.csv"
source_sha256: "d2789a1933c581c5b9ef65406fa50c30c9dd09e4415504077f0da9bf41aa8e2a"
source_bytes: 298453
source_row_count: 239
source_column_count: 16
source_cell_count: 3824
ignored_blank_row_count: 0
semantic_group: "PRACTICAL_SCIENCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: practical-science-domain-register.csv -->

# Отрасли практической науки

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Практическая наука, приборы и безопасность
- **Записей:** 239
- **Полей в каждой записи:** 16
- **Ячеек данных, включая пустые:** 3824
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `d2789a1933c581c5b9ef65406fa50c30c9dd09e4415504077f0da9bf41aa8e2a`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Идентификатор отрасли | <code>&quot;domain_id&quot;</code> |
| 2 | Группа код | <code>&quot;group_code&quot;</code> |
| 3 | Группа название на русском | <code>&quot;group_title_ru&quot;</code> |
| 4 | Название отрасли на русском | <code>&quot;domain_title_ru&quot;</code> |
| 5 | «practical» «outcome» | <code>&quot;practical_outcome&quot;</code> |
| 6 | Минимальный «demonstration» | <code>&quot;minimum_demonstration&quot;</code> |
| 7 | Основной «measure» | <code>&quot;primary_measure&quot;</code> |
| 8 | Единица «or» «standard» | <code>&quot;unit_or_standard&quot;</code> |
| 9 | Класс безопасности | <code>&quot;safety_class&quot;</code> |
| 10 | Безопасность «definition» | <code>&quot;safety_definition&quot;</code> |
| 11 | «prerequisite» «domains» | <code>&quot;prerequisite_domains&quot;</code> |
| 12 | Офлайн «package» целевой | <code>&quot;offline_package_target&quot;</code> |
| 13 | «practical» «project» целевой | <code>&quot;practical_project_target&quot;</code> |
| 14 | «successor» «proof» | <code>&quot;successor_proof&quot;</code> |
| 15 | «implementation» состояние | <code>&quot;implementation_state&quot;</code> |
| 16 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:16 -->
> [!abstract]- Запись 1 из 239 — SCI-METH-01 — Постановка проверяемого вопроса и фальсифицируемость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Постановка проверяемого вопроса и фальсифицируемость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Постановка проверяемого вопроса и фальсифицируемость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;формулировка вопроса, проверяемого наблюдением&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:2 cells:16 -->
> [!abstract]- Запись 2 из 239 — SCI-METH-02 — Иерархия источников, происхождение и конфликт интересов
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Иерархия источников, происхождение и конфликт интересов&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Иерархия источников, происхождение и конфликт интересов».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;карта утверждение → первичный источник → дата → права&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:3 cells:16 -->
> [!abstract]- Запись 3 из 239 — SCI-METH-03 — Гипотеза, контроль и альтернативные объяснения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Гипотеза, контроль и альтернативные объяснения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Гипотеза, контроль и альтернативные объяснения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;таблица конкурирующих гипотез и различающих наблюдений&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-02|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:4 cells:16 -->
> [!abstract]- Запись 4 из 239 — SCI-METH-04 — Планирование эксперимента и предрегистрация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Планирование эксперимента и предрегистрация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Планирование эксперимента и предрегистрация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;заранее записанные переменные, критерий успеха и стоп-условие&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-03|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:5 cells:16 -->
> [!abstract]- Запись 5 из 239 — SCI-METH-05 — Выборка, смещение и репрезентативность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Выборка, смещение и репрезентативность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Выборка, смещение и репрезентативность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;описание рамки выборки и известных смещений&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-04|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:6 cells:16 -->
> [!abstract]- Запись 6 из 239 — SCI-METH-06 — Словарь данных, типы переменных и единицы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Словарь данных, типы переменных и единицы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Словарь данных, типы переменных и единицы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;машиночитаемый словарь поля → тип → единица → допустимый диапазон&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-05|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:7 cells:16 -->
> [!abstract]- Запись 7 из 239 — SCI-METH-07 — SI, размерностный анализ и преобразование единиц
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;SI, размерностный анализ и преобразование единиц&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «SI, размерностный анализ и преобразование единиц».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;проверка размерности и независимый пересчёт единиц&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-06|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:8 cells:16 -->
> [!abstract]- Запись 8 из 239 — SCI-METH-08 — Калибровка и метрологическая прослеживаемость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Калибровка и метрологическая прослеживаемость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Калибровка и метрологическая прослеживаемость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;запись эталона, диапазона, поправки и срока следующей проверки&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-07|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:9 cells:16 -->
> [!abstract]- Запись 9 из 239 — SCI-METH-09 — Повторяемость, воспроизводимость и стабильность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Повторяемость, воспроизводимость и стабильность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Повторяемость, воспроизводимость и стабильность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;серия повторов одним и двумя операторами&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-08|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:10 cells:16 -->
> [!abstract]- Запись 10 из 239 — SCI-METH-10 — Неопределённость и распространение ошибок
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Неопределённость и распространение ошибок&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Неопределённость и распространение ошибок».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;бюджет неопределённости с допущениями&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-09|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:11 cells:16 -->
> [!abstract]- Запись 11 из 239 — SCI-METH-11 — Разведочный анализ и визуальная проверка данных
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Разведочный анализ и визуальная проверка данных&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Разведочный анализ и визуальная проверка данных».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;график, выбросы, пропуски и сохранённые сырые данные&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-10|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:12 cells:16 -->
> [!abstract]- Запись 12 из 239 — SCI-METH-12 — Статистический вывод, корреляция и причинность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Статистический вывод, корреляция и причинность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Статистический вывод, корреляция и причинность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;явное разделение ассоциации, механизма и причинного вывода&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-11|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:13 cells:16 -->
> [!abstract]- Запись 13 из 239 — SCI-METH-13 — Лабораторный журнал, версии и отрицательные результаты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Лабораторный журнал, версии и отрицательные результаты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Лабораторный журнал, версии и отрицательные результаты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неизменяемая запись метода, версии, ошибок и исходов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-12|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:14 cells:16 -->
> [!abstract]- Запись 14 из 239 — SCI-METH-14 — Этика, риск, согласие и право остановить опыт
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-METH-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;METH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Научный метод и метрология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Этика, риск, согласие и право остановить опыт&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Этика, риск, согласие и право остановить опыт».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;предварительный риск-анализ и подписанное стоп-правило&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;протокол/неопределённость&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-13|SCI-METH-01&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:15 cells:16 -->
> [!abstract]- Запись 15 из 239 — SCI-MATH-01 — Арифметика, порядок действий и оценка порядка величины
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Арифметика, порядок действий и оценка порядка величины&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Арифметика, порядок действий и оценка порядка величины».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;ручной и независимый расчёт с оценкой сверху/снизу&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:16 cells:16 -->
> [!abstract]- Запись 16 из 239 — SCI-MATH-02 — Дроби, отношения, проценты и пропорции
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дроби, отношения, проценты и пропорции&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дроби, отношения, проценты и пропорции».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;масштабирование рецепта или ресурса с проверкой суммы&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:17 cells:16 -->
> [!abstract]- Запись 17 из 239 — SCI-MATH-03 — Единицы, приставки и перевод величин
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Единицы, приставки и перевод величин&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Единицы, приставки и перевод величин».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;двухмаршрутный перевод единиц без потери размерности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:18 cells:16 -->
> [!abstract]- Запись 18 из 239 — SCI-MATH-04 — Алгебраические выражения и уравнения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Алгебраические выражения и уравнения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Алгебраические выражения и уравнения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;решение и обратная подстановка&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:19 cells:16 -->
> [!abstract]- Запись 19 из 239 — SCI-MATH-05 — Функции, таблицы и графики
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Функции, таблицы и графики&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Функции, таблицы и графики».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;построение таблицы значений и интерпретация наклона&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:20 cells:16 -->
> [!abstract]- Запись 20 из 239 — SCI-MATH-06 — Евклидова геометрия и площадь/объём
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Евклидова геометрия и площадь/объём&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Евклидова геометрия и площадь/объём».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;измерение формы и проверка вычисленного объёма&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:21 cells:16 -->
> [!abstract]- Запись 21 из 239 — SCI-MATH-07 — Тригонометрия и непрямые измерения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Тригонометрия и непрямые измерения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Тригонометрия и непрямые измерения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;оценка высоты безопасного объекта по углу и базе&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:22 cells:16 -->
> [!abstract]- Запись 22 из 239 — SCI-MATH-08 — Координаты, векторы и аналитическая геометрия
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Координаты, векторы и аналитическая геометрия&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Координаты, векторы и аналитическая геометрия».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;переход между координатным описанием и вектором&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:23 cells:16 -->
> [!abstract]- Запись 23 из 239 — SCI-MATH-09 — Линейная алгебра и системы уравнений
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Линейная алгебра и системы уравнений&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Линейная алгебра и системы уравнений».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;решение малой системы и проверка невязки&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:24 cells:16 -->
> [!abstract]- Запись 24 из 239 — SCI-MATH-10 — Предел, производная и скорость изменения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Предел, производная и скорость изменения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Предел, производная и скорость изменения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;численная оценка производной по измеренному ряду&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:25 cells:16 -->
> [!abstract]- Запись 25 из 239 — SCI-MATH-11 — Интеграл, накопление и баланс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Интеграл, накопление и баланс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Интеграл, накопление и баланс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;оценка накопленного расхода по временным отсчётам&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:26 cells:16 -->
> [!abstract]- Запись 26 из 239 — SCI-MATH-12 — Дифференциальные уравнения и динамические модели
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дифференциальные уравнения и динамические модели&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дифференциальные уравнения и динамические модели».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение простой модели с наблюдаемой траекторией&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:27 cells:16 -->
> [!abstract]- Запись 27 из 239 — SCI-MATH-13 — Логика, множества, графы и дискретные структуры
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Логика, множества, графы и дискретные структуры&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Логика, множества, графы и дискретные структуры».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;таблица истинности или граф зависимостей&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:28 cells:16 -->
> [!abstract]- Запись 28 из 239 — SCI-MATH-14 — Вероятность и условная вероятность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Вероятность и условная вероятность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Вероятность и условная вероятность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;дерево событий и проверка суммы вероятностей&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:29 cells:16 -->
> [!abstract]- Запись 29 из 239 — SCI-MATH-15 — Описательная статистика и устойчивые меры
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Описательная статистика и устойчивые меры&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Описательная статистика и устойчивые меры».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;среднее, медиана, разброс и квартильный размах&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:30 cells:16 -->
> [!abstract]- Запись 30 из 239 — SCI-MATH-16 — Доверительные интервалы и проверка гипотез
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Доверительные интервалы и проверка гипотез&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Доверительные интервалы и проверка гипотез».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;интервал с явно указанными предпосылками&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:31 cells:16 -->
> [!abstract]- Запись 31 из 239 — SCI-MATH-17 — Временные ряды, сезонность и контрольные карты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-17&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Временные ряды, сезонность и контрольные карты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Временные ряды, сезонность и контрольные карты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;график тренда, сезонности и контрольных границ&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-16|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:32 cells:16 -->
> [!abstract]- Запись 32 из 239 — SCI-MATH-18 — Численные методы, оптимизация и исследование операций
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MATH-18&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MATH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Математика и количественное мышление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Численные методы, оптимизация и исследование операций&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Численные методы, оптимизация и исследование операций».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;решение, проверка ограничения и анализ чувствительности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;расчёт/невязка&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MATH-17|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:33 cells:16 -->
> [!abstract]- Запись 33 из 239 — SCI-PHYS-01 — Физические величины, модели и масштаб
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Физические величины, модели и масштаб&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Физические величины, модели и масштаб».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение модели с измерением и указание области применимости&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:34 cells:16 -->
> [!abstract]- Запись 34 из 239 — SCI-PHYS-02 — Кинематика: положение, скорость и ускорение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Кинематика: положение, скорость и ускорение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Кинематика: положение, скорость и ускорение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;видеоряд или секундомерный ряд движения безопасного объекта&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:35 cells:16 -->
> [!abstract]- Запись 35 из 239 — SCI-PHYS-03 — Силы, масса и законы Ньютона
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Силы, масса и законы Ньютона&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Силы, масса и законы Ньютона».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;диаграмма сил и измерение малых сил безопасным динамометром&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:36 cells:16 -->
> [!abstract]- Запись 36 из 239 — SCI-PHYS-04 — Статика, равновесие и центр масс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Статика, равновесие и центр масс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Статика, равновесие и центр масс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;безопасная настольная модель равновесия&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:37 cells:16 -->
> [!abstract]- Запись 37 из 239 — SCI-PHYS-05 — Работа, энергия, мощность и КПД
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Работа, энергия, мощность и КПД&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Работа, энергия, мощность и КПД».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;энергетический баланс маломощной системы&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:38 cells:16 -->
> [!abstract]- Запись 38 из 239 — SCI-PHYS-06 — Импульс и столкновения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Импульс и столкновения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Импульс и столкновения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;видеоанализ малых тел без людей и хрупких предметов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:39 cells:16 -->
> [!abstract]- Запись 39 из 239 — SCI-PHYS-07 — Давление, плавучесть и гидростатика
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Давление, плавучесть и гидростатика&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Давление, плавучесть и гидростатика».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;зависимость давления/плавучести на безопасной водной модели&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:40 cells:16 -->
> [!abstract]- Запись 40 из 239 — SCI-PHYS-08 — Поток, расход, сопротивление и насосы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Поток, расход, сопротивление и насосы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Поток, расход, сопротивление и насосы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;измерение расхода воды при безопасном низком давлении&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:41 cells:16 -->
> [!abstract]- Запись 41 из 239 — SCI-PHYS-09 — Температура, теплоёмкость и фазовые переходы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Температура, теплоёмкость и фазовые переходы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Температура, теплоёмкость и фазовые переходы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;температурно-временной ряд без открытого огня&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:42 cells:16 -->
> [!abstract]- Запись 42 из 239 — SCI-PHYS-10 — Теплопередача, изоляция и тепловой баланс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Теплопередача, изоляция и тепловой баланс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Теплопередача, изоляция и тепловой баланс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение охлаждения двух одинаковых ёмкостей&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:43 cells:16 -->
> [!abstract]- Запись 43 из 239 — SCI-PHYS-11 — Колебания, волны и резонанс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Колебания, волны и резонанс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Колебания, волны и резонанс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;период и амплитуда безопасного маятника&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:44 cells:16 -->
> [!abstract]- Запись 44 из 239 — SCI-PHYS-12 — Акустика, шум и вибрация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Акустика, шум и вибрация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Акустика, шум и вибрация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;уровень/спектр относительного сигнала с оговоркой о некалиброванности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:45 cells:16 -->
> [!abstract]- Запись 45 из 239 — SCI-PHYS-13 — Геометрическая оптика и освещённость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Геометрическая оптика и освещённость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Геометрическая оптика и освещённость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;фокусное расстояние безопасной линзы без наблюдения Солнца&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:46 cells:16 -->
> [!abstract]- Запись 46 из 239 — SCI-PHYS-14 — Электрический заряд, поле и потенциал
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Электрический заряд, поле и потенциал&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Электрический заряд, поле и потенциал».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;электростатическое наблюдение на безопасной малой энергии&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:47 cells:16 -->
> [!abstract]- Запись 47 из 239 — SCI-PHYS-15 — Постоянный ток, напряжение и сопротивление
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Постоянный ток, напряжение и сопротивление&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Постоянный ток, напряжение и сопротивление».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только учебная цепь от сертифицированного USB-источника 5 V с аппаратным ограничением тока ≤100 mA; автомобильные, тяговые, свинцовые и литиевые батареи исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:48 cells:16 -->
> [!abstract]- Запись 48 из 239 — SCI-PHYS-16 — Магнетизм и электромагнитная индукция
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Магнетизм и электромагнитная индукция&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Магнетизм и электромагнитная индукция».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;катушка только от сертифицированного USB-источника 5 V с аппаратным ограничением тока ≤100 mA; STOP при любом нагреве; мощные магниты и батарейные packs исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:49 cells:16 -->
> [!abstract]- Запись 49 из 239 — SCI-PHYS-17 — Свойства материалов, упругость и разрушение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PHYS-17&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PHYS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Физика&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Свойства материалов, упругость и разрушение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Свойства материалов, упругость и разрушение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неразрушающее сравнение деформации малых образцов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;SI-измерение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PHYS-16|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:50 cells:16 -->
> [!abstract]- Запись 50 из 239 — SCI-CHEM-01 — Строение вещества и периодические закономерности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Строение вещества и периодические закономерности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Строение вещества и периодические закономерности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;объяснение свойства через состав и структуру&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:51 cells:16 -->
> [!abstract]- Запись 51 из 239 — SCI-CHEM-02 — Количество вещества, формулы и стехиометрия
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Количество вещества, формулы и стехиометрия&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Количество вещества, формулы и стехиометрия».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;массовый баланс на безопасной учебной задаче&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:52 cells:16 -->
> [!abstract]- Запись 52 из 239 — SCI-CHEM-03 — Растворы, концентрации и безопасное разбавление
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Растворы, концентрации и безопасное разбавление&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Растворы, концентрации и безопасное разбавление».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;расчёт концентрации без реактивных/токсичных веществ&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:53 cells:16 -->
> [!abstract]- Запись 53 из 239 — SCI-CHEM-04 — Кислотность, pH и буферные системы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Кислотность, pH и буферные системы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Кислотность, pH и буферные системы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;готовая тест-полоска только для питьевой воды, столового уксуса или пищевого сока в отдельной одноразовой ёмкости; cleaners, неизвестные жидкости, смешивание и tasting запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:54 cells:16 -->
> [!abstract]- Запись 54 из 239 — SCI-CHEM-05 — Газы, давление и температурные зависимости
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Газы, давление и температурные зависимости&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Газы, давление и температурные зависимости».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;анализ опубликованных данных; герметичные нагреваемые сосуды запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только справочное знание и распознавание опасности; бытовое выполнение запрещено.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:55 cells:16 -->
> [!abstract]- Запись 55 из 239 — SCI-CHEM-06 — Химическая термодинамика и фазовые равновесия
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Химическая термодинамика и фазовые равновесия&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Химическая термодинамика и фазовые равновесия».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;диаграмма состояния и энергетический баланс по данным&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:56 cells:16 -->
> [!abstract]- Запись 56 из 239 — SCI-CHEM-07 — Равновесие, растворимость и кристаллизация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Равновесие, растворимость и кристаллизация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Равновесие, растворимость и кристаллизация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;безопасное наблюдение кристаллизации пищевой соли&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:57 cells:16 -->
> [!abstract]- Запись 57 из 239 — SCI-CHEM-08 — Скорость реакции и влияние условий
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Скорость реакции и влияние условий&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Скорость реакции и влияние условий».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдение безопасного пищевого/ферментного процесса без герметизации&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:58 cells:16 -->
> [!abstract]- Запись 58 из 239 — SCI-CHEM-09 — Электрохимия, батареи и коррозия
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Электрохимия, батареи и коррозия&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Электрохимия, батареи и коррозия».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;визуальная/массовая оценка коррозии безопасных образцов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:59 cells:16 -->
> [!abstract]- Запись 59 из 239 — SCI-CHEM-10 — Аналитическая химия и контроль качества
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Аналитическая химия и контроль качества&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Аналитическая химия и контроль качества».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только после item-level SDS review: заводской водный учебный стандарт известного состава/концентрации и утверждённый путь отходов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:60 cells:16 -->
> [!abstract]- Запись 60 из 239 — SCI-CHEM-11 — Металлы, сплавы, полимеры, стекло и керамика
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Металлы, сплавы, полимеры, стекло и керамика&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Металлы, сплавы, полимеры, стекло и керамика».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идентификация материала по неразрушаемым признакам&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:61 cells:16 -->
> [!abstract]- Запись 61 из 239 — SCI-CHEM-12 — Клеи, покрытия и совместимость материалов
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Клеи, покрытия и совместимость материалов&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Клеи, покрытия и совместимость материалов».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только после item-level review конкретного consumer product, SDS, hazard statements, перчаток, вентиляции, количества и утилизации; двухкомпонентные, растворные и изоцианатные системы исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:62 cells:16 -->
> [!abstract]- Запись 62 из 239 — SCI-CHEM-13 — Топливо, горение и продукты сгорания
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Топливо, горение и продукты сгорания&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Топливо, горение и продукты сгорания».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только распознавание рисков CO/пожара; бытовые опыты запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только справочное знание и распознавание опасности; бытовое выполнение запрещено.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:63 cells:16 -->
> [!abstract]- Запись 63 из 239 — SCI-CHEM-14 — Химия воды и ограничения бытовой обработки
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Химия воды и ограничения бытовой обработки&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Химия воды и ограничения бытовой обработки».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;чтение лабораторного отчёта и разделение биологических/химических рисков&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:64 cells:16 -->
> [!abstract]- Запись 64 из 239 — SCI-CHEM-15 — Химия пищи и изменения при хранении
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Химия пищи и изменения при хранении&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Химия пищи и изменения при хранении».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;масса, температура и наблюдение без употребления сомнительных образцов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:65 cells:16 -->
> [!abstract]- Запись 65 из 239 — SCI-CHEM-16 — SDS, маркировка, совместное хранение и отходы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CHEM-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CHEM&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Химия и материалы&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;SDS, маркировка, совместное хранение и отходы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «SDS, маркировка, совместное хранение и отходы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;поиск опасностей, СИЗ, несовместимостей и пути утилизации&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;состав/концентрация&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CHEM-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:66 cells:16 -->
> [!abstract]- Запись 66 из 239 — SCI-LIFE-01 — Клетка, мембраны и обмен веществ
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Клетка, мембраны и обмен веществ&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Клетка, мембраны и обмен веществ».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аннотированная схема и анализ готового микроснимка&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:67 cells:16 -->
> [!abstract]- Запись 67 из 239 — SCI-LIFE-02 — ДНК, наследование и вариация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;ДНК, наследование и вариация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «ДНК, наследование и вариация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;родословная учебного признака без медицинской интерпретации&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:68 cells:16 -->
> [!abstract]- Запись 68 из 239 — SCI-LIFE-03 — Эволюция, отбор и филогенетика
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Эволюция, отбор и филогенетика&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Эволюция, отбор и филогенетика».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;дерево признаков с указанием неопределённости&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:69 cells:16 -->
> [!abstract]- Запись 69 из 239 — SCI-LIFE-04 — Ботаника и морфология растений
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Ботаника и морфология растений&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Ботаника и морфология растений».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;фотопротокол безопасного известного растения&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:70 cells:16 -->
> [!abstract]- Запись 70 из 239 — SCI-LIFE-05 — Физиология растений и фотосинтез
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Физиология растений и фотосинтез&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Физиология растений и фотосинтез».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неразрушающий ростовой/световой ряд&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:71 cells:16 -->
> [!abstract]- Запись 71 из 239 — SCI-LIFE-06 — Зоология, поведение и благополучие
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Зоология, поведение и благополучие&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Зоология, поведение и благополучие».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неинвазивное наблюдение без кормления дикой фауны&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:72 cells:16 -->
> [!abstract]- Запись 72 из 239 — SCI-LIFE-07 — Микробиология и биобезопасность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Микробиология и биобезопасность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Микробиология и биобезопасность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;работа только с опубликованными данными; культивирование неизвестных организмов запрещено&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только справочное знание и распознавание опасности; бытовое выполнение запрещено.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:73 cells:16 -->
> [!abstract]- Запись 73 из 239 — SCI-LIFE-08 — Микроскопия готовых безопасных препаратов
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Микроскопия готовых безопасных препаратов&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Микроскопия готовых безопасных препаратов».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;фокус, масштаб и рисунок готового слайда&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:74 cells:16 -->
> [!abstract]- Запись 74 из 239 — SCI-LIFE-09 — Систематика и определение видов
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Систематика и определение видов&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Систематика и определение видов».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;определение по нескольким признакам с фото и географией&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:75 cells:16 -->
> [!abstract]- Запись 75 из 239 — SCI-LIFE-10 — Популяции, пищевые сети и экосистемные связи
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Популяции, пищевые сети и экосистемные связи&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Популяции, пищевые сети и экосистемные связи».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдательный маршрут с повторяемыми точками&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:76 cells:16 -->
> [!abstract]- Запись 76 из 239 — SCI-LIFE-11 — Опыление и взаимодействия растение–животное
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Опыление и взаимодействия растение–животное&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Опыление и взаимодействия растение–животное».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;счёт посещений без вмешательства в гнёзда&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:77 cells:16 -->
> [!abstract]- Запись 77 из 239 — SCI-LIFE-12 — Разложение, почвенная биота и круговороты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Разложение, почвенная биота и круговороты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Разложение, почвенная биота и круговороты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;закрытый наблюдательный журнал без выращивания неизвестных культур&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:78 cells:16 -->
> [!abstract]- Запись 78 из 239 — SCI-LIFE-13 — Биоразнообразие и мониторинг участка
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Биоразнообразие и мониторинг участка&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Биоразнообразие и мониторинг участка».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;фиксированный маршрут, фото-точки и список видов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:79 cells:16 -->
> [!abstract]- Запись 79 из 239 — SCI-LIFE-14 — Биостатистика и экологическое моделирование
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Биостатистика и экологическое моделирование&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Биостатистика и экологическое моделирование».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;повторный анализ открытого набора данных&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:80 cells:16 -->
> [!abstract]- Запись 80 из 239 — SCI-LIFE-15 — Биоинформатика и работа с открытыми последовательностями
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Биоинформатика и работа с открытыми последовательностями&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Биоинформатика и работа с открытыми последовательностями».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;воспроизводимый поиск по публичной базе без персональных данных&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:81 cells:16 -->
> [!abstract]- Запись 81 из 239 — SCI-LIFE-16 — Охрана природы, инвазивные виды и правовые границы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-LIFE-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;LIFE&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Биология и экология&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Охрана природы, инвазивные виды и правовые границы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Охрана природы, инвазивные виды и правовые границы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;карта наблюдений и передача компетентному органу&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;наблюдение/счёт&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-LIFE-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:82 cells:16 -->
> [!abstract]- Запись 82 из 239 — SCI-HEALTH-01 — Анатомия, физиология и медицинская терминология
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Анатомия, физиология и медицинская терминология&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Анатомия, физиология и медицинская терминология».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;объяснение нормальной функции без постановки диагноза&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:83 cells:16 -->
> [!abstract]- Запись 83 из 239 — SCI-HEALTH-02 — Навигация по системе здравоохранения и красные флаги
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Навигация по системе здравоохранения и красные флаги&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Навигация по системе здравоохранения и красные флаги».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;правильный маршрут 112/SNS24/профильная служба по учебному сценарию&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:84 cells:16 -->
> [!abstract]- Запись 84 из 239 — SCI-HEALTH-03 — Безопасное измерение температуры, пульса и частоты дыхания
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Безопасное измерение температуры, пульса и частоты дыхания&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Безопасное измерение температуры, пульса и частоты дыхания».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;повтор измерения согласно инструкции прибора без диагностики&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:85 cells:16 -->
> [!abstract]- Запись 85 из 239 — SCI-HEALTH-04 — Первая помощь, BLS/AED и удушье
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Первая помощь, BLS/AED и удушье&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Первая помощь, BLS/AED и удушье».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только сертифицированное обучение и манекен&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:86 cells:16 -->
> [!abstract]- Запись 86 из 239 — SCI-HEALTH-05 — Инфекционный контроль, руки, поверхности и вентиляция
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Инфекционный контроль, руки, поверхности и вентиляция&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Инфекционный контроль, руки, поверхности и вентиляция».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аудит процесса без культивирования микроорганизмов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:87 cells:16 -->
> [!abstract]- Запись 87 из 239 — SCI-HEALTH-06 — Эпидемиология и интерпретация риска
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Эпидемиология и интерпретация риска&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Эпидемиология и интерпретация риска».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;расчёт показателей по обезличенным опубликованным данным&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:88 cells:16 -->
> [!abstract]- Запись 88 из 239 — SCI-HEALTH-07 — Питание, пищевой дневник и дефициты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Питание, пищевой дневник и дефициты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Питание, пищевой дневник и дефициты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сбалансированный рацион по официальным рекомендациям без лечебной диеты&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:89 cells:16 -->
> [!abstract]- Запись 89 из 239 — SCI-HEALTH-08 — Психологическая первая помощь и поддерживающее общение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Психологическая первая помощь и поддерживающее общение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Психологическая первая помощь и поддерживающее общение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сценарий слушания, безопасности и направления за помощью&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:90 cells:16 -->
> [!abstract]- Запись 90 из 239 — SCI-HEALTH-09 — Непрерывность хронического лечения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Непрерывность хронического лечения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Непрерывность хронического лечения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сверенный с врачом/фармацевтом личный план без изменения доз&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:91 cells:16 -->
> [!abstract]- Запись 91 из 239 — SCI-HEALTH-10 — Материнство, ребёнок и развитие
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Материнство, ребёнок и развитие&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Материнство, ребёнок и развитие».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;распознавание повода для профессиональной помощи&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:92 cells:16 -->
> [!abstract]- Запись 92 из 239 — SCI-HEALTH-11 — Старение, инвалидность и доступность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Старение, инвалидность и доступность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Старение, инвалидность и доступность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аудит барьеров и безопасной поддержки без подъёма человека в одиночку&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:93 cells:16 -->
> [!abstract]- Запись 93 из 239 — SCI-HEALTH-12 — Профилактическая стоматология
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Профилактическая стоматология&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Профилактическая стоматология».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;гигиена и распознавание срочности; процедуры запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:94 cells:16 -->
> [!abstract]- Запись 94 из 239 — SCI-HEALTH-13 — Эргономика, усталость и профессиональные риски
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Эргономика, усталость и профессиональные риски&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Эргономика, усталость и профессиональные риски».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдение рабочей позы, нагрузки и отдыха&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:95 cells:16 -->
> [!abstract]- Запись 95 из 239 — SCI-HEALTH-14 — Токсикологическая информация и обращение в CIAV
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Токсикологическая информация и обращение в CIAV&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Токсикологическая информация и обращение в CIAV».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идентификация продукта и подготовка точных данных; лечение не импровизируется&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:96 cells:16 -->
> [!abstract]- Запись 96 из 239 — SCI-HEALTH-15 — Ветеринарное общественное здоровье и благополучие животных
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Ветеринарное общественное здоровье и благополучие животных&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Ветеринарное общественное здоровье и благополучие животных».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;маршрут к ветеринару и наблюдательный журнал без процедур&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:97 cells:16 -->
> [!abstract]- Запись 97 из 239 — SCI-HEALTH-16 — Медицинские записи, приватность и передача информации
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-HEALTH-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Здоровье и общественное здоровье&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Медицинские записи, приватность и передача информации&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Медицинские записи, приватность и передача информации».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;структурированный список лекарств/аллергий с контролем доступа&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;официальный маршрут/неинвазивное наблюдение&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-HEALTH-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:98 cells:16 -->
> [!abstract]- Запись 98 из 239 — SCI-EARTH-01 — Минералы, горные породы и геологические процессы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Минералы, горные породы и геологические процессы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Минералы, горные породы и геологические процессы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неразрушающее описание образца без шахт/обрывов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:99 cells:16 -->
> [!abstract]- Запись 99 из 239 — SCI-EARTH-02 — Рельеф, эрозия и геоморфология
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Рельеф, эрозия и геоморфология&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Рельеф, эрозия и геоморфология».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;повторная фото-точка безопасного склона/берега&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:100 cells:16 -->
> [!abstract]- Запись 100 из 239 — SCI-EARTH-03 — Почва: горизонты, текстура и структура
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Почва: горизонты, текстура и структура&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Почва: горизонты, текстура и структура».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;полевое описание неглубокой безопасной пробы&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:101 cells:16 -->
> [!abstract]- Запись 101 из 239 — SCI-EARTH-04 — Поверхностная вода, водосбор и сток
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Поверхностная вода, водосбор и сток&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Поверхностная вода, водосбор и сток».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;карта водосбора и наблюдение потока без входа в паводковую воду&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:102 cells:16 -->
> [!abstract]- Запись 102 из 239 — SCI-EARTH-05 — Грунтовые воды и уязвимость источников
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Грунтовые воды и уязвимость источников&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Грунтовые воды и уязвимость источников».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;интерпретация официальной гидрогеологической карты&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:103 cells:16 -->
> [!abstract]- Запись 103 из 239 — SCI-EARTH-06 — Погода, наблюдения и прогноз
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Погода, наблюдения и прогноз&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Погода, наблюдения и прогноз».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;ежедневный ряд температуры, давления и осадков&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:104 cells:16 -->
> [!abstract]- Запись 104 из 239 — SCI-EARTH-07 — Климат, нормы и экстремумы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Климат, нормы и экстремумы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Климат, нормы и экстремумы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение локального ряда с официальной климатической нормой&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:105 cells:16 -->
> [!abstract]- Запись 105 из 239 — SCI-EARTH-08 — Океан, приливы, волны и побережье
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Океан, приливы, волны и побережье&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Океан, приливы, волны и побережье».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;работа с официальными данными; наблюдение только из безопасной зоны&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:106 cells:16 -->
> [!abstract]- Запись 106 из 239 — SCI-EARTH-09 — Землетрясения, оползни, вулканы и цунами
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Землетрясения, оползни, вулканы и цунами&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Землетрясения, оползни, вулканы и цунами».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сценарная карта и официальные признаки; физическое приближение запрещено&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:107 cells:16 -->
> [!abstract]- Запись 107 из 239 — SCI-EARTH-10 — Дистанционное зондирование и спутниковые данные
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дистанционное зондирование и спутниковые данные&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дистанционное зондирование и спутниковые данные».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение двух дат открытого снимка&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:108 cells:16 -->
> [!abstract]- Запись 108 из 239 — SCI-EARTH-11 — Картография, GIS, CRS и погрешность положения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Картография, GIS, CRS и погрешность положения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Картография, GIS, CRS и погрешность положения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;репроекция слоя и контроль известной точки&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:109 cells:16 -->
> [!abstract]- Запись 109 из 239 — SCI-EARTH-12 — Мониторинг воздуха, воды, шума и света
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Мониторинг воздуха, воды, шума и света&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Мониторинг воздуха, воды, шума и света».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;протокол с оговоркой о классе и калибровке датчика&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:110 cells:16 -->
> [!abstract]- Запись 110 из 239 — SCI-EARTH-13 — Отходы, загрязнение и материальные потоки
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Отходы, загрязнение и материальные потоки&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Отходы, загрязнение и материальные потоки».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аудит входов/выходов без контакта с опасными отходами&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:111 cells:16 -->
> [!abstract]- Запись 111 из 239 — SCI-EARTH-14 — Экологическое право и сообщение о наблюдении
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EARTH-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EARTH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Науки о Земле и окружающей среде&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Экологическое право и сообщение о наблюдении&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Экологическое право и сообщение о наблюдении».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;пакет дата–место–фото–метод без обвинительного вывода&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;пространственно-временной ряд&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EARTH-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:112 cells:16 -->
> [!abstract]- Запись 112 из 239 — SCI-AGRI-01 — Полевое обследование и безопасный отбор почвы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Полевое обследование и безопасный отбор почвы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Полевое обследование и безопасный отбор почвы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;составная проба с картой точек и чистым инструментом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:113 cells:16 -->
> [!abstract]- Запись 113 из 239 — SCI-AGRI-02 — Семенная партия, происхождение и доступ
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Семенная партия, происхождение и доступ&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Семенная партия, происхождение и доступ».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;паспорт accession, условия хранения и правовой статус&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:114 cells:16 -->
> [!abstract]- Запись 114 из 239 — SCI-AGRI-03 — Тест всхожести и жизнеспособности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Тест всхожести и жизнеспособности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Тест всхожести и жизнеспособности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;контролируемый тест разрешённых семян с долей всходов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:115 cells:16 -->
> [!abstract]- Запись 115 из 239 — SCI-AGRI-04 — Севооборот, календарь и планирование площади
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Севооборот, календарь и планирование площади&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Севооборот, календарь и планирование площади».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;план культуры по воде, сезону и рискам&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:116 cells:16 -->
> [!abstract]- Запись 116 из 239 — SCI-AGRI-05 — Овощеводство и питомник
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Овощеводство и питомник&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Овощеводство и питомник».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;журнал посева, пересадки, роста и потерь&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:117 cells:16 -->
> [!abstract]- Запись 117 из 239 — SCI-AGRI-06 — Ирригация, влажность и водный баланс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Ирригация, влажность и водный баланс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Ирригация, влажность и водный баланс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;объём воды, площадь, погода и состояние растения&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:118 cells:16 -->
> [!abstract]- Запись 118 из 239 — SCI-AGRI-07 — Компостирование и санитарные границы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Компостирование и санитарные границы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Компостирование и санитарные границы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;температурный журнал растительного компоста; животные/медицинские отходы исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:119 cells:16 -->
> [!abstract]- Запись 119 из 239 — SCI-AGRI-08 — Питательность почвы и безопасное внесение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Питательность почвы и безопасное внесение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Питательность почвы и безопасное внесение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;решение по лабораторному анализу и этикетке; без самодельной химии&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:120 cells:16 -->
> [!abstract]- Запись 120 из 239 — SCI-AGRI-09 — Интегрированная защита растений
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Интегрированная защита растений&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Интегрированная защита растений».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;порог наблюдения, идентификация и минимальное законное вмешательство&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:121 cells:16 -->
> [!abstract]- Запись 121 из 239 — SCI-AGRI-10 — Болезни растений и карантин
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Болезни растений и карантин&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Болезни растений и карантин».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;фото, изоляция, очистка инструмента и обращение к официальной службе&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:122 cells:16 -->
> [!abstract]- Запись 122 из 239 — SCI-AGRI-11 — Теплица, вентиляция и микроклимат
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Теплица, вентиляция и микроклимат&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Теплица, вентиляция и микроклимат».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;температура/влажность и безопасный режим вентиляции&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:123 cells:16 -->
> [!abstract]- Запись 123 из 239 — SCI-AGRI-12 — Лес, агролесоводство и пожарный интерфейс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Лес, агролесоводство и пожарный интерфейс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Лес, агролесоводство и пожарный интерфейс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;карта топлива и легальная профилактика без самостоятельного огня&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:124 cells:16 -->
> [!abstract]- Запись 124 из 239 — SCI-AGRI-13 — Содержание животных и welfare
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Содержание животных и welfare&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Содержание животных и welfare».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;вода, корм, поведение, укрытие и вызов ветеринара&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:125 cells:16 -->
> [!abstract]- Запись 125 из 239 — SCI-AGRI-14 — Пастбище, корм и хранение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Пастбище, корм и хранение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Пастбище, корм и хранение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;инвентарный баланс и признаки порчи без кормления сомнительным материалом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:126 cells:16 -->
> [!abstract]- Запись 126 из 239 — SCI-AGRI-15 — Гигиена пищи, холодовая цепь и прослеживаемость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Гигиена пищи, холодовая цепь и прослеживаемость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Гигиена пищи, холодовая цепь и прослеживаемость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;температурный журнал и lot trace&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:127 cells:16 -->
> [!abstract]- Запись 127 из 239 — SCI-AGRI-16 — Консервирование только по валидированному процессу
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-AGRI-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;AGRI&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сельское хозяйство, вода и пища&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Консервирование только по валидированному процессу&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Консервирование только по валидированному процессу».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;следование официальному рецепту; низкокислотные продукты без валидированного pressure-canning запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;урожай/вода/почва&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-AGRI-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:128 cells:16 -->
> [!abstract]- Запись 128 из 239 — SCI-CIVIL-01 — Съёмка, уровни, координаты и исполнительная схема
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Съёмка, уровни, координаты и исполнительная схема&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Съёмка, уровни, координаты и исполнительная схема».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;замкнутый безопасный ход на участке&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:129 cells:16 -->
> [!abstract]- Запись 129 из 239 — SCI-CIVIL-02 — Технический чертёж, размеры и допуски
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Технический чертёж, размеры и допуски&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Технический чертёж, размеры и допуски».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;чертёж существующей безопасной детали&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:130 cells:16 -->
> [!abstract]- Запись 130 из 239 — SCI-CIVIL-03 — Строительная физика: тепло, воздух и влага
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Строительная физика: тепло, воздух и влага&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Строительная физика: тепло, воздух и влага».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдательный температурно-влажностный профиль&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:131 cells:16 -->
> [!abstract]- Запись 131 из 239 — SCI-CIVIL-04 — Конденсация, сырость и плесень
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Конденсация, сырость и плесень&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Конденсация, сырость и плесень».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;неинвазивная карта условий; опасное/обширное поражение — специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:132 cells:16 -->
> [!abstract]- Запись 132 из 239 — SCI-CIVIL-05 — Нагрузки, путь передачи сил и устойчивость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Нагрузки, путь передачи сил и устойчивость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Нагрузки, путь передачи сил и устойчивость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;анализ схемы; изменение несущих конструкций запрещено&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:133 cells:16 -->
> [!abstract]- Запись 133 из 239 — SCI-CIVIL-06 — Грунты, фундаменты и склоновые риски
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Грунты, фундаменты и склоновые риски&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Грунты, фундаменты и склоновые риски».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;чтение инженерного отчёта; раскопки/укрепления — специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:134 cells:16 -->
> [!abstract]- Запись 134 из 239 — SCI-CIVIL-07 — Водоснабжение, давление и защита от обратного тока
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Водоснабжение, давление и защита от обратного тока&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Водоснабжение, давление и защита от обратного тока».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;схема и визуальный аудит; изменение сети — по закону&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:135 cells:16 -->
> [!abstract]- Запись 135 из 239 — SCI-CIVIL-08 — Санитария, туалеты и безопасное разделение потоков
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Санитария, туалеты и безопасное разделение потоков&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Санитария, туалеты и безопасное разделение потоков».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;план потоков и санитарный аудит&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:136 cells:16 -->
> [!abstract]- Запись 136 из 239 — SCI-CIVIL-09 — Сточные воды и очистка
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Сточные воды и очистка&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Сточные воды и очистка».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только схема/контроль; вход в колодцы и контакт со стоками запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только справочное знание и распознавание опасности; бытовое выполнение запрещено.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:137 cells:16 -->
> [!abstract]- Запись 137 из 239 — SCI-CIVIL-10 — Дренаж, ливневый сток и паводковая устойчивость
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дренаж, ливневый сток и паводковая устойчивость&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дренаж, ливневый сток и паводковая устойчивость».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдение безопасного дождя и карта путей воды&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:138 cells:16 -->
> [!abstract]- Запись 138 из 239 — SCI-CIVIL-11 — Пожарная безопасность, эвакуация и compartmentation
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Пожарная безопасность, эвакуация и compartmentation&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Пожарная безопасность, эвакуация и compartmentation».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аудит выхода/детектора; испытания огнём запрещены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:139 cells:16 -->
> [!abstract]- Запись 139 из 239 — SCI-CIVIL-12 — Вентиляция, отопление и качество воздуха
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Вентиляция, отопление и качество воздуха&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Вентиляция, отопление и качество воздуха».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;измерительный аудит без вмешательства в газ/дымоход&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:140 cells:16 -->
> [!abstract]- Запись 140 из 239 — SCI-CIVIL-13 — Сантехника, арматура и обнаружение утечек
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Сантехника, арматура и обнаружение утечек&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Сантехника, арматура и обнаружение утечек».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;безопасная визуальная проверка и изоляция по инструкции&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:141 cells:16 -->
> [!abstract]- Запись 141 из 239 — SCI-CIVIL-14 — Дороги, мосты и транспортные сооружения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дороги, мосты и транспортные сооружения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дороги, мосты и транспортные сооружения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;визуальное распознавание дефекта без заключения о безопасности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:142 cells:16 -->
> [!abstract]- Запись 142 из 239 — SCI-CIVIL-15 — Строительные материалы и неразрушающий контроль
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Строительные материалы и неразрушающий контроль&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Строительные материалы и неразрушающий контроль».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;документированный осмотр без разрушительного испытания&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:143 cells:16 -->
> [!abstract]- Запись 143 из 239 — SCI-CIVIL-16 — Плановое обслуживание и журнал здания
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-CIVIL-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;CIVIL&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Строительство, вода и инфраструктура&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Плановое обслуживание и журнал здания&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Плановое обслуживание и журнал здания».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;паспорт узла, интервал, дефект и эскалация&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/состояние/поток&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-CIVIL-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:144 cells:16 -->
> [!abstract]- Запись 144 из 239 — SCI-MECH-01 — Ручной инструмент, подбор и безопасная работа
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Ручной инструмент, подбор и безопасная работа&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Ручной инструмент, подбор и безопасная работа».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;предпусковой осмотр и низкорисковая учебная операция&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:145 cells:16 -->
> [!abstract]- Запись 145 из 239 — SCI-MECH-02 — Линейные/угловые измерения и допуски
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Линейные/угловые измерения и допуски&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Линейные/угловые измерения и допуски».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;три повтора штангенциркулем/линейкой на безопасной детали&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:146 cells:16 -->
> [!abstract]- Запись 146 из 239 — SCI-MECH-03 — Резьба, крепёж, момент и фиксация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Резьба, крепёж, момент и фиксация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Резьба, крепёж, момент и фиксация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идентификация и сборка учебного соединения по спецификации&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:147 cells:16 -->
> [!abstract]- Запись 147 из 239 — SCI-MECH-04 — Механизмы, рычаги, передачи и кинематика
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Механизмы, рычаги, передачи и кинематика&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Механизмы, рычаги, передачи и кинематика».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;настольная безопасная модель&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:148 cells:16 -->
> [!abstract]- Запись 148 из 239 — SCI-MECH-05 — Валы, муфты, цепи, ремни и ограждения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Валы, муфты, цепи, ремни и ограждения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Валы, муфты, цепи, ремни и ограждения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;осмотр отключённой учебной системы; lockout обязателен&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:149 cells:16 -->
> [!abstract]- Запись 149 из 239 — SCI-MECH-06 — Насосы, кавитация и рабочая точка
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Насосы, кавитация и рабочая точка&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Насосы, кавитация и рабочая точка».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;измерение маломощного водяного насоса&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:150 cells:16 -->
> [!abstract]- Запись 150 из 239 — SCI-MECH-07 — Клапаны, уплотнения и утечки
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Клапаны, уплотнения и утечки&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Клапаны, уплотнения и утечки».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;осмотр безопасной разгерметизированной водной системы&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:151 cells:16 -->
> [!abstract]- Запись 151 из 239 — SCI-MECH-08 — Подшипники, смазка и загрязнение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Подшипники, смазка и загрязнение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Подшипники, смазка и загрязнение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;журнал состояния отключённого узла&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:152 cells:16 -->
> [!abstract]- Запись 152 из 239 — SCI-MECH-09 — Велосипед: осмотр, тормоза и привод
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Велосипед: осмотр, тормоза и привод&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Велосипед: осмотр, тормоза и привод».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;контрольный чек после обучения; дорожный тест в безопасной зоне&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:153 cells:16 -->
> [!abstract]- Запись 153 из 239 — SCI-MECH-10 — Двигатели внутреннего сгорания и выхлоп
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Двигатели внутреннего сгорания и выхлоп&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Двигатели внутреннего сгорания и выхлоп».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только устройство и сервисная документация; работа в помещении запрещена&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:154 cells:16 -->
> [!abstract]- Запись 154 из 239 — SCI-MECH-11 — Холодильный контур и тепловой насос
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Холодильный контур и тепловой насос&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Холодильный контур и тепловой насос».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдение температур; хладагент/давление — специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:155 cells:16 -->
> [!abstract]- Запись 155 из 239 — SCI-MECH-12 — Дерево, разметка, соединения и ремонт
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Дерево, разметка, соединения и ремонт&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Дерево, разметка, соединения и ремонт».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;малый проект ручным инструментом после инструктажа&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:156 cells:16 -->
> [!abstract]- Запись 156 из 239 — SCI-MECH-13 — Металлообработка и снятие материала
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Металлообработка и снятие материала&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Металлообработка и снятие материала».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только после обучения, ограждений и СИЗ&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:157 cells:16 -->
> [!abstract]- Запись 157 из 239 — SCI-MECH-14 — Сварка, пайка твёрдым припоем и горячие работы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Сварка, пайка твёрдым припоем и горячие работы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Сварка, пайка твёрдым припоем и горячие работы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только квалифицированная площадка и разрешение&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:158 cells:16 -->
> [!abstract]- Запись 158 из 239 — SCI-MECH-15 — Текстиль, шитьё, выкройка и ремонт
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Текстиль, шитьё, выкройка и ремонт&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Текстиль, шитьё, выкройка и ремонт».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;образец шва и проверка прочности без нагрузки на безопасность&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:159 cells:16 -->
> [!abstract]- Запись 159 из 239 — SCI-MECH-16 — Надёжность, отказ, запасные части и preventive maintenance
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-MECH-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;MECH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Механика, производство и ремонт&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Надёжность, отказ, запасные части и preventive maintenance&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Надёжность, отказ, запасные части и preventive maintenance».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;FMEA и план обслуживания одного актива&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;размер/сила/состояние&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-MECH-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:160 cells:16 -->
> [!abstract]- Запись 160 из 239 — SCI-ELEC-01 — Электробезопасность и границы низкого напряжения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Электробезопасность и границы низкого напряжения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Электробезопасность и границы низкого напряжения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только на изолированном учебном USB-стенде 5 V с аппаратным ограничением тока ≤100 mA: найти источник, защиту и штатное отключение; сеть, автомобильные/тяговые/литиевые батареи исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:161 cells:16 -->
> [!abstract]- Запись 161 из 239 — SCI-ELEC-02 — Закон Ома, мощность и энергетический баланс
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Закон Ома, мощность и энергетический баланс&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Закон Ома, мощность и энергетический баланс».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;учебная цепь 5 V с аппаратным ограничением тока ≤100 mA, негорючей площадкой и заранее рассчитанной мощностью&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:162 cells:16 -->
> [!abstract]- Запись 162 из 239 — SCI-ELEC-03 — Мультиметр: напряжение, сопротивление и непрерывность
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Мультиметр: напряжение, сопротивление и непрерывность&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Мультиметр: напряжение, сопротивление и непрерывность».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;измерение только изолированной низковольтной цепи&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:163 cells:16 -->
> [!abstract]- Запись 163 из 239 — SCI-ELEC-04 — Пассивные компоненты и схемные обозначения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Пассивные компоненты и схемные обозначения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Пассивные компоненты и схемные обозначения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идентификация и измерение безопасных компонентов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:164 cells:16 -->
> [!abstract]- Запись 164 из 239 — SCI-ELEC-05 — Диоды, транзисторы и аналоговые узлы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Диоды, транзисторы и аналоговые узлы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Диоды, транзисторы и аналоговые узлы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;маломощная макетная схема с ограничением тока&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:165 cells:16 -->
> [!abstract]- Запись 165 из 239 — SCI-ELEC-06 — Цифровая логика и уровни сигналов
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Цифровая логика и уровни сигналов&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Цифровая логика и уровни сигналов».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;таблица истинности на безопасном учебном модуле&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:166 cells:16 -->
> [!abstract]- Запись 166 из 239 — SCI-ELEC-07 — Микроконтроллеры и интерфейсы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Микроконтроллеры и интерфейсы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Микроконтроллеры и интерфейсы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;считывание безопасного датчика без управления критическим объектом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:167 cells:16 -->
> [!abstract]- Запись 167 из 239 — SCI-ELEC-08 — Датчики, преобразование и сбор данных
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Датчики, преобразование и сбор данных&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Датчики, преобразование и сбор данных».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;калибровочная проверка двух точек&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:168 cells:16 -->
> [!abstract]- Запись 168 из 239 — SCI-ELEC-09 — Обратная связь, управление и safe-state
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Обратная связь, управление и safe-state&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Обратная связь, управление и safe-state».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;симуляция или маломощный стенд с ручным отключением&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:169 cells:16 -->
> [!abstract]- Запись 169 из 239 — SCI-ELEC-10 — Двигатели, генераторы и привод
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Двигатели, генераторы и привод&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Двигатели, генераторы и привод».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;учебный маломощный мотор с ограждением&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:170 cells:16 -->
> [!abstract]- Запись 170 из 239 — SCI-ELEC-11 — Солнечная фотоэлектрика и низковольтная автономная система
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Солнечная фотоэлектрика и низковольтная автономная система&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Солнечная фотоэлектрика и низковольтная автономная система».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;энергетический бюджет; монтаж здания — специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:171 cells:16 -->
> [!abstract]- Запись 171 из 239 — SCI-ELEC-12 — Батареи, заряд, BMS и пожарный риск
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Батареи, заряд, BMS и пожарный риск&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Батареи, заряд, BMS и пожарный риск».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;учёт состояния штатных исправных модулей; разборка запрещена&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:172 cells:16 -->
> [!abstract]- Запись 172 из 239 — SCI-ELEC-13 — Энергетический аудит, ватт-часы и управление нагрузкой
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Энергетический аудит, ватт-часы и управление нагрузкой&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Энергетический аудит, ватт-часы и управление нагрузкой».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;суточный журнал безопасных потребителей&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:173 cells:16 -->
> [!abstract]- Запись 173 из 239 — SCI-ELEC-14 — Сеть 230 В, щит, защита и backfeed
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Сеть 230 В, щит, защита и backfeed&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Сеть 230 В, щит, защита и backfeed».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;только распознавание и отключение; работы — лицензированный специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:174 cells:16 -->
> [!abstract]- Запись 174 из 239 — SCI-ELEC-15 — Заземление, молниезащита и EMC
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Заземление, молниезащита и EMC&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Заземление, молниезащита и EMC».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;чтение проекта/отчёта; измерения установки — специалист&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:175 cells:16 -->
> [!abstract]- Запись 175 из 239 — SCI-ELEC-16 — Радиосвязь, спектр и антенны
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Радиосвязь, спектр и антенны&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Радиосвязь, спектр и антенны».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;приём/учебный расчёт; передача только законно и в пределах допуска&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:176 cells:16 -->
> [!abstract]- Запись 176 из 239 — SCI-ELEC-17 — Проводная/беспроводная связь и PACE
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ELEC-17&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ELEC&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Электротехника, электроника и энергия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Проводная/беспроводная связь и PACE&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Проводная/беспроводная связь и PACE».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;тест независимых каналов без нарушения спектральных правил&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;V/A/Wh/сигнал&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ELEC-16|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:177 cells:16 -->
> [!abstract]- Запись 177 из 239 — SCI-COMP-01 — Архитектура компьютера и представление данных
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Архитектура компьютера и представление данных&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Архитектура компьютера и представление данных».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;разбор пути данные–память–процессор–вывод&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:178 cells:16 -->
> [!abstract]- Запись 178 из 239 — SCI-COMP-02 — Операционные системы и Linux
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Операционные системы и Linux&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Операционные системы и Linux».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;установка в изолированную виртуальную машину&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:179 cells:16 -->
> [!abstract]- Запись 179 из 239 — SCI-COMP-03 — Файловые системы, права и контроль целостности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Файловые системы, права и контроль целостности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Файловые системы, права и контроль целостности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;создание/проверка hash и тест восстановления&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:180 cells:16 -->
> [!abstract]- Запись 180 из 239 — SCI-COMP-04 — Командная строка и автоматизация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Командная строка и автоматизация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Командная строка и автоматизация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идемпотентный безопасный скрипт в тестовом каталоге&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:181 cells:16 -->
> [!abstract]- Запись 181 из 239 — SCI-COMP-05 — Python и воспроизводимый анализ
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Python и воспроизводимый анализ&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Python и воспроизводимый анализ».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;скрипт читает CSV, считает результат и сохраняет версию&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:182 cells:16 -->
> [!abstract]- Запись 182 из 239 — SCI-COMP-06 — C и память в изолированной учебной среде
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;C и память в изолированной учебной среде&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «C и память в изолированной учебной среде».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;компиляция малого примера с предупреждениями&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:183 cells:16 -->
> [!abstract]- Запись 183 из 239 — SCI-COMP-07 — Алгоритмы и оценка сложности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Алгоритмы и оценка сложности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Алгоритмы и оценка сложности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение времени двух методов на синтетических данных&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:184 cells:16 -->
> [!abstract]- Запись 184 из 239 — SCI-COMP-08 — Структуры данных и сериализация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Структуры данных и сериализация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Структуры данных и сериализация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;round-trip с проверкой эквивалентности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:185 cells:16 -->
> [!abstract]- Запись 185 из 239 — SCI-COMP-09 — Реляционные базы, SQL и транзакции
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Реляционные базы, SQL и транзакции&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Реляционные базы, SQL и транзакции».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;создание локальной БД и проверка rollback&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:186 cells:16 -->
> [!abstract]- Запись 186 из 239 — SCI-COMP-10 — Сети, адресация, DNS и маршрутизация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Сети, адресация, DNS и маршрутизация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Сети, адресация, DNS и маршрутизация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;локальная лаборатория без сканирования чужих систем&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:187 cells:16 -->
> [!abstract]- Запись 187 из 239 — SCI-COMP-11 — Web, HTTP и автономное зеркалирование
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Web, HTTP и автономное зеркалирование&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Web, HTTP и автономное зеркалирование».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;локальный статический сайт с сохранённым происхождением&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:188 cells:16 -->
> [!abstract]- Запись 188 из 239 — SCI-COMP-12 — Версионный контроль и выпуск
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Версионный контроль и выпуск&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Версионный контроль и выпуск».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;commit, tag, changelog и проверяемая сборка&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:189 cells:16 -->
> [!abstract]- Запись 189 из 239 — SCI-COMP-13 — Защитная кибербезопасность и моделирование угроз
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-13&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Защитная кибербезопасность и моделирование угроз&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Защитная кибербезопасность и моделирование угроз».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;аудит собственных активов; offensive-операции исключены&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-12|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:190 cells:16 -->
> [!abstract]- Запись 190 из 239 — SCI-COMP-14 — Шифрование, ключи, recovery и succession
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-14&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Шифрование, ключи, recovery и succession&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Шифрование, ключи, recovery и succession».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;тест восстановления на учебном ключе без реальных секретов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-13|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:191 cells:16 -->
> [!abstract]- Запись 191 из 239 — SCI-COMP-15 — Встраиваемые системы и низкопотребляющий логгер
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-15&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Встраиваемые системы и низкопотребляющий логгер&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Встраиваемые системы и низкопотребляющий логгер».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;безопасный датчик и экспорт сырых данных&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-14|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:192 cells:16 -->
> [!abstract]- Запись 192 из 239 — SCI-COMP-16 — Научные вычисления, численная проверка и тесты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-16&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Научные вычисления, численная проверка и тесты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Научные вычисления, численная проверка и тесты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сравнение с известным эталонным результатом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-15|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:193 cells:16 -->
> [!abstract]- Запись 193 из 239 — SCI-COMP-17 — Открытые GIS/CAD/EDA-инструменты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-COMP-17&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;COMP&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Вычисления и цифровая инженерия&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Открытые GIS/CAD/EDA-инструменты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Открытые GIS/CAD/EDA-инструменты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;файл проекта, открываемый на второй машине&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;воспроизводимый файл/тест&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-COMP-16|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:194 cells:16 -->
> [!abstract]- Запись 194 из 239 — SCI-EDU-01 — Грамотность и чтение технического текста
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Грамотность и чтение технического текста&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Грамотность и чтение технического текста».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;пересказ инструкции с выделением условий и запретов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:195 cells:16 -->
> [!abstract]- Запись 195 из 239 — SCI-EDU-02 — Многоязычные словари RU/UK/PT/EN
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Многоязычные словари RU/UK/PT/EN&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Многоязычные словари RU/UK/PT/EN».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;двусторонняя карточка термин–определение–контекст&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:196 cells:16 -->
> [!abstract]- Запись 196 из 239 — SCI-EDU-03 — Числовая грамотность и бытовые расчёты
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Числовая грамотность и бытовые расчёты&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Числовая грамотность и бытовые расчёты».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;оценка, расчёт, единица и здравый контроль результата&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:197 cells:16 -->
> [!abstract]- Запись 197 из 239 — SCI-EDU-04 — Педагогика, память и интервальное повторение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Педагогика, память и интервальное повторение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Педагогика, память и интервальное повторение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;план занятия с retrieval practice&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:198 cells:16 -->
> [!abstract]- Запись 198 из 239 — SCI-EDU-05 — Карта программы и зависимости тем
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Карта программы и зависимости тем&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Карта программы и зависимости тем».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;граф prerequisite → lesson → demonstration&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:199 cells:16 -->
> [!abstract]- Запись 199 из 239 — SCI-EDU-06 — Оценивание без подсказки и критерии mastery
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Оценивание без подсказки и критерии mastery&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Оценивание без подсказки и критерии mastery».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;слепое практическое задание по рубрике&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:200 cells:16 -->
> [!abstract]- Запись 200 из 239 — SCI-EDU-07 — Ученичество, наблюдение и постепенный допуск
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Ученичество, наблюдение и постепенный допуск&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Ученичество, наблюдение и постепенный допуск».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;матрица observe → assist → supervised → independent&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:201 cells:16 -->
> [!abstract]- Запись 201 из 239 — SCI-EDU-08 — Техническое письмо, схемы и чек-листы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Техническое письмо, схемы и чек-листы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Техническое письмо, схемы и чек-листы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;однозначная инструкция, проверенная вторым человеком&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:202 cells:16 -->
> [!abstract]- Запись 202 из 239 — SCI-EDU-09 — Технический перевод и опасные неоднозначности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Технический перевод и опасные неоднозначности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Технический перевод и опасные неоднозначности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;двуязычная проверка единиц, отрицаний и стоп-условий&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:203 cells:16 -->
> [!abstract]- Запись 203 из 239 — SCI-EDU-10 — Доступность: зрение, слух, моторика и когнитивная нагрузка
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Доступность: зрение, слух, моторика и когнитивная нагрузка&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Доступность: зрение, слух, моторика и когнитивная нагрузка».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;альтернативный формат одной инструкции&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:204 cells:16 -->
> [!abstract]- Запись 204 из 239 — SCI-EDU-11 — Коммуникация в конфликте и read-back/check-back
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Коммуникация в конфликте и read-back/check-back&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Коммуникация в конфликте и read-back/check-back».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;ролевая передача задачи с подтверждением&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:205 cells:16 -->
> [!abstract]- Запись 205 из 239 — SCI-EDU-12 — Teach-back и межпоколенческий экзамен
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-EDU-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Обучение, язык и передача навыка&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Teach-back и межпоколенческий экзамен&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Teach-back и межпоколенческий экзамен».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;новичок выполняет задачу без устной помощи автора&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;демонстрация mastery&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-EDU-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:206 cells:16 -->
> [!abstract]- Запись 206 из 239 — SCI-OPS-01 — Инвентаризация, единицы учёта и фактический остаток
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Инвентаризация, единицы учёта и фактический остаток&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Инвентаризация, единицы учёта и фактический остаток».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;цикл count → discrepancy → correction&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:207 cells:16 -->
> [!abstract]- Запись 207 из 239 — SCI-OPS-02 — Бухгалтерский след и двойная запись
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Бухгалтерский след и двойная запись&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Бухгалтерский след и двойная запись».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;сверка журнала с остатком без реальных финансовых данных&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:208 cells:16 -->
> [!abstract]- Запись 208 из 239 — SCI-OPS-03 — Логистика, lead time, reorder point и резерв
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Логистика, lead time, reorder point и резерв&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Логистика, lead time, reorder point и резерв».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;расчёт точки заказа с вариацией спроса&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:209 cells:16 -->
> [!abstract]- Запись 209 из 239 — SCI-OPS-04 — План обслуживания, work order и запасные части
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;План обслуживания, work order и запасные части&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «План обслуживания, work order и запасные части».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;закрытый наряд с evidence&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:210 cells:16 -->
> [!abstract]- Запись 210 из 239 — SCI-OPS-05 — Качество, дефект, root cause и CAPA
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Качество, дефект, root cause и CAPA&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Качество, дефект, root cause и CAPA».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;разбор безопасного учебного несоответствия&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:211 cells:16 -->
> [!abstract]- Запись 211 из 239 — SCI-OPS-06 — Управление проектом, зависимости и change control
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Управление проектом, зависимости и change control&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Управление проектом, зависимости и change control».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;baseline, изменение и журнал решения&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:212 cells:16 -->
> [!abstract]- Запись 212 из 239 — SCI-OPS-07 — Emergency operations, роли и span of control
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Emergency operations, роли и span of control&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Emergency operations, роли и span of control».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;настольная тренировка без имитации опасных действий&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S1_LOW_RISK_HOUSEHOLD&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Низкорисковая бытовая практика только с заранее названными обычными материалами; для электричества — изолированный защищённый источник с заранее ограниченными током, энергией и температурой; СИЗ и стоп-условие заданы до начала.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:213 cells:16 -->
> [!abstract]- Запись 213 из 239 — SCI-OPS-08 — Human factors, усталость, чек-лист и режим ошибки
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Human factors, усталость, чек-лист и режим ошибки&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Human factors, усталость, чек-лист и режим ошибки».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;наблюдение процесса и redesign шага&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:214 cells:16 -->
> [!abstract]- Запись 214 из 239 — SCI-OPS-09 — Решение при неопределённости и premortem
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Решение при неопределённости и premortem&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Решение при неопределённости и premortem».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;варианты, вероятность, ущерб и обратимость&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:215 cells:16 -->
> [!abstract]- Запись 215 из 239 — SCI-OPS-10 — Право, полномочия и доказательство актуальности
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Право, полномочия и доказательство актуальности&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Право, полномочия и доказательство актуальности».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;jurisdiction–version–valid_at–review_due&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:216 cells:16 -->
> [!abstract]- Запись 216 из 239 — SCI-OPS-11 — Экономика ремонта, замены и стандартизации
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Экономика ремонта, замены и стандартизации&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Экономика ремонта, замены и стандартизации».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;полная стоимость жизненного цикла с чувствительностью&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:217 cells:16 -->
> [!abstract]- Запись 217 из 239 — SCI-OPS-12 — Кооперация, взаимопомощь и внешняя сеть
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-OPS-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Операции, экономика и управление&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Кооперация, взаимопомощь и внешняя сеть&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Кооперация, взаимопомощь и внешняя сеть».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;соглашение о роли, границе и прекращении&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;остаток/время/дефект&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-OPS-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:218 cells:16 -->
> [!abstract]- Запись 218 из 239 — SCI-ARCH-01 — Модель цифрового сохранения и информационный пакет
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Модель цифрового сохранения и информационный пакет&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Модель цифрового сохранения и информационный пакет».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;объект + metadata + права + fixity + reader&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:219 cells:16 -->
> [!abstract]- Запись 219 из 239 — SCI-ARCH-02 — SHA-256, fixity и регулярная проверка
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;SHA-256, fixity и регулярная проверка&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «SHA-256, fixity и регулярная проверка».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;повторная проверка и журнал неизменности&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:220 cells:16 -->
> [!abstract]- Запись 220 из 239 — SCI-ARCH-03 — BagIt/пакетирование и перенос между носителями
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;BagIt/пакетирование и перенос между носителями&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «BagIt/пакетирование и перенос между носителями».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;валидный пакет с манифестом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:221 cells:16 -->
> [!abstract]- Запись 221 из 239 — SCI-ARCH-04 — Устойчивые форматы и PRONOM-идентификация
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Устойчивые форматы и PRONOM-идентификация&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Устойчивые форматы и PRONOM-идентификация».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;идентификация формата и reader path&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:222 cells:16 -->
> [!abstract]- Запись 222 из 239 — SCI-ARCH-05 — Миграция формата и сохранение оригинала
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Миграция формата и сохранение оригинала&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Миграция формата и сохранение оригинала».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;original + migrated + сравнение содержания&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:223 cells:16 -->
> [!abstract]- Запись 223 из 239 — SCI-ARCH-06 — Описательные, технические и административные metadata
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Описательные, технические и административные metadata&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Описательные, технические и административные metadata».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;заполненный минимальный профиль&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:224 cells:16 -->
> [!abstract]- Запись 224 из 239 — SCI-ARCH-07 — OCR, качество текста и сохранение изображения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;OCR, качество текста и сохранение изображения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «OCR, качество текста и сохранение изображения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;выборочная сверка OCR с оригиналом&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:225 cells:16 -->
> [!abstract]- Запись 225 из 239 — SCI-ARCH-08 — Офлайн-индекс, поиск и controlled vocabulary
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Офлайн-индекс, поиск и controlled vocabulary&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Офлайн-индекс, поиск и controlled vocabulary».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;поиск по термину, синониму и идентификатору&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:226 cells:16 -->
> [!abstract]- Запись 226 из 239 — SCI-ARCH-09 — Печатное ядро, легенда и ручной каталог
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Печатное ядро, легенда и ручной каталог&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Печатное ядро, легенда и ручной каталог».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;поиск критической страницы без электричества&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:227 cells:16 -->
> [!abstract]- Запись 227 из 239 — SCI-ARCH-10 — Refresh носителя, независимые копии и restore-test
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Refresh носителя, независимые копии и restore-test&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Refresh носителя, независимые копии и restore-test».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;восстановление на чистое устройство&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:228 cells:16 -->
> [!abstract]- Запись 228 из 239 — SCI-ARCH-11 — Контроль доступа, приватность и раздельное хранение
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-11&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Контроль доступа, приватность и раздельное хранение&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Контроль доступа, приватность и раздельное хранение».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;public/restricted/secret gate&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-10|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:229 cells:16 -->
> [!abstract]- Запись 229 из 239 — SCI-ARCH-12 — Хранитель, succession и передача следующему
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-ARCH-12&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;ARCH&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Сохранение знаний и цифровой архив&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Хранитель, succession и передача следующему&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Хранитель, succession и передача следующему».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;новый custodian проверяет каталог и восстановление&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;hash/restore/поиск&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;SI или явно названный стандарт&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-ARCH-11|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:230 cells:16 -->
> [!abstract]- Запись 230 из 239 — SCI-PORT-01 — 112, ANEPC, муниципальные планы и официальные предупреждения
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-01&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;112, ANEPC, муниципальные планы и официальные предупреждения&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «112, ANEPC, муниципальные планы и официальные предупреждения».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;поиск актуального authority path и его офлайн-снимка&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-METH-01|SCI-METH-07|SCI-METH-14&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:231 cells:16 -->
> [!abstract]- Запись 231 из 239 — SCI-PORT-02 — SNIG/DGT/CAOP и локальные координатные системы
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-02&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;SNIG/DGT/CAOP и локальные координатные системы&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «SNIG/DGT/CAOP и локальные координатные системы».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;официальный слой, metadata, CRS и дата&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-01|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:232 cells:16 -->
> [!abstract]- Запись 232 из 239 — SCI-PORT-03 — IPMA: погода, климат, землетрясения и море
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-03&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;IPMA: погода, климат, землетрясения и море&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «IPMA: погода, климат, землетрясения и море».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;разделение текущего alert и исторического набора&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-02|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:233 cells:16 -->
> [!abstract]- Запись 233 из 239 — SCI-PORT-04 — APA/LNEG: вода, наводнения, геология и среда
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-04&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;APA/LNEG: вода, наводнения, геология и среда&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «APA/LNEG: вода, наводнения, геология и среда».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;выбор официального слоя с ограничением покрытия&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-03|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:234 cells:16 -->
> [!abstract]- Запись 234 из 239 — SCI-PORT-05 — DGAV: здоровье растений, пища и animal welfare
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-05&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;DGAV: здоровье растений, пища и animal welfare&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «DGAV: здоровье растений, пища и animal welfare».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;официальное руководство с датой и rights review&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-04|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:235 cells:16 -->
> [!abstract]- Запись 235 из 239 — SCI-PORT-06 — LNEC и национальная строительная практика
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-06&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;LNEC и национальная строительная практика&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «LNEC и национальная строительная практика».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;поиск отчёта/нормы; проектное решение остаётся у специалиста&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-05|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:236 cells:16 -->
> [!abstract]- Запись 236 из 239 — SCI-PORT-07 — DGEG/ERSE и безопасность энергетики
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-07&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;DGEG/ERSE и безопасность энергетики&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «DGEG/ERSE и безопасность энергетики».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;текущий регуляторный путь; монтаж остаётся профессиональным&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только квалифицированный/лицензированный специалист в подходящей среде и по действующим нормам.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-06|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:237 cells:16 -->
> [!abstract]- Запись 237 из 239 — SCI-PORT-08 — DGS/INFARMED и права на локальную медицинскую копию
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-08&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;DGS/INFARMED и права на локальную медицинскую копию&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «DGS/INFARMED и права на локальную медицинскую копию».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;metadata/link until reproduction rights and edition are cleared&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S2_TRAINED_SUPERVISED&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Только после обучения и под компетентным надзором; бытовая самостоятельная импровизация запрещена.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-07|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:238 cells:16 -->
> [!abstract]- Запись 238 из 239 — SCI-PORT-09 — EUR-Lex/Diário da República и актуальность права
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-09&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;EUR-Lex/Diário da República и актуальность права&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «EUR-Lex/Diário da República и актуальность права».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;официальный текст, consolidated status, valid_at и review_due&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-08|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:239 cells:16 -->
> [!abstract]- Запись 239 из 239 — SCI-PORT-10 — Португальский технический язык и двуязычные карточки
> - **Идентификатор отрасли** (<code>&quot;domain_id&quot;</code>): <code>&quot;SCI-PORT-10&quot;</code>
> - **Группа код** (<code>&quot;group_code&quot;</code>): <code>&quot;PORT&quot;</code>
> - **Группа название на русском** (<code>&quot;group_title_ru&quot;</code>): <code>&quot;Локализация Португалия / ЕС&quot;</code>
> - **Название отрасли на русском** (<code>&quot;domain_title_ru&quot;</code>): <code>&quot;Португальский технический язык и двуязычные карточки&quot;</code>
> - **«practical» «outcome»** (<code>&quot;practical_outcome&quot;</code>): <code>&quot;Объяснить базовую модель, выполнить допустимую для класса риска проверку и документировать пределы по теме «Португальский технический язык и двуязычные карточки».&quot;</code>
> - **Минимальный «demonstration»** (<code>&quot;minimum_demonstration&quot;</code>): <code>&quot;PT оригинал + RU пояснение + независимая проверка опасных терминов&quot;</code>
> - **Основной «measure»** (<code>&quot;primary_measure&quot;</code>): <code>&quot;official source/version/coverage&quot;</code>
> - **Единица «or» «standard»** (<code>&quot;unit_or_standard&quot;</code>): <code>&quot;official-version/coverage&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S0_OBSERVE_READ&quot;</code>
> - **Безопасность «definition»** (<code>&quot;safety_definition&quot;</code>): <code>&quot;Наблюдение, чтение, расчёт или работа с опубликованным набором данных; физического вмешательства нет.&quot;</code>
> - **«prerequisite» «domains»** (<code>&quot;prerequisite_domains&quot;</code>): <code>&quot;SCI-PORT-09|SCI-METH-13&quot;</code>
> - **Офлайн «package» целевой** (<code>&quot;offline_package_target&quot;</code>): <code>&quot;2&quot;</code>
> - **«practical» «project» целевой** (<code>&quot;practical_project_target&quot;</code>): <code>&quot;1&quot;</code>
> - **«successor» «proof»** (<code>&quot;successor_proof&quot;</code>): <code>&quot;Новый участник находит источник офлайн, объясняет границы, повторяет допустимую процедуру и получает результат в заранее заданном допуске.&quot;</code>
> - **«implementation» состояние** (<code>&quot;implementation_state&quot;</code>): <code>&quot;FRAMEWORK_ONLY_NOT_TRAINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
