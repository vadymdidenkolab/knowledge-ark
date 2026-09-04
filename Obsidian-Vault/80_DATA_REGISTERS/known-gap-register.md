---
id: "DATA-REGISTER-4c0a041ddff3e127"
type: "generated-data-register-view"
title: "Известные пробелы и блокеры"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "known-gap-register.csv"
source_sha256: "b389e167e35ae3598e606363dfd7f2a30e3d4b50637ab816dc9535f29301cc50"
source_bytes: 25820
source_row_count: 32
source_column_count: 16
source_cell_count: 512
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: known-gap-register.csv -->

# Известные пробелы и блокеры

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 32
- **Полей в каждой записи:** 16
- **Ячеек данных, включая пустые:** 512
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `b389e167e35ae3598e606363dfd7f2a30e3d4b50637ab816dc9535f29301cc50`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «gap» ID | <code>&quot;gap_id&quot;</code> |
| 2 | Отрасль | <code>&quot;domain&quot;</code> |
| 3 | Область «layer» | <code>&quot;scope_layer&quot;</code> |
| 4 | Приоритет | <code>&quot;priority_tier&quot;</code> |
| 5 | Самый ранний уровень сервиса | <code>&quot;earliest_service_level&quot;</code> |
| 6 | «gap» на русском | <code>&quot;gap_ru&quot;</code> |
| 7 | «blocks» сервис уровень | <code>&quot;blocks_service_level&quot;</code> |
| 8 | «blocker» | <code>&quot;blocker&quot;</code> |
| 9 | Требуемые доказательства | <code>&quot;required_evidence&quot;</code> |
| 10 | Имеющиеся доказательства | <code>&quot;current_evidence&quot;</code> |
| 11 | Статус | <code>&quot;status&quot;</code> |
| 12 | Владелец | <code>&quot;owner&quot;</code> |
| 13 | Срок | <code>&quot;due&quot;</code> |
| 14 | Допуск к применению | <code>&quot;release_gate&quot;</code> |
| 15 | Версия выпуска | <code>&quot;release_version&quot;</code> |
| 16 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:16 -->
> [!abstract]- Запись 1 из 32 — GAP-001 — Персональный профиль каждого участника: личность, возраст, язык, контакты, здоровье, аллергии, назначения, огран…
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-001&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;PEOPLE_CARE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Персональный профиль каждого участника: личность, возраст, язык, контакты, здоровье, аллергии, назначения, ограничения, согласие и зависимости&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Заполненная и датированная карточка на каждого человека; приватное хранение; подпись/подтверждение; контакт экстренного лица; журнал изменений&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Шаблон и узлы каталога; заполненных персональных карточек 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_PERSON_DATA&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PERSON_PROFILES_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Медицинские решения и расчёты мощности без этого недостоверны&quot;</code>
>

<!-- record:2 cells:16 -->
> [!abstract]- Запись 2 из 32 — GAP-002 — Профиль состава группы 1–7 человек, навыков, зависимостей, доступности и особых потребностей
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-002&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;PEOPLE_CARE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Профиль состава группы 1–7 человек, навыков, зависимостей, доступности и особых потребностей&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Актуальный roster; матрица навыков; критические зависимости; потребности детей, беременных, пожилых и людей с инвалидностью; дата проверки&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог поддерживает N1|N2|N3_TO_N7; фактический состав не задан&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_GROUP_DATA&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_GROUP_PROFILE_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не выводить количества из абстрактного максимума 7 человек&quot;</code>
>

<!-- record:3 cells:16 -->
> [!abstract]- Запись 3 из 32 — GAP-003 — Профиль конкретного адреса, здания и участка
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-003&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;BASE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Профиль конкретного адреса, здания и участка&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Адрес; план; координаты; границы; коммуникации; отключения; вода; дренаж; пожарные и природные риски; фото; дата обследования&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Объектовый слой и site-specific карты: 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_SITE_DATA&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_SITE_PROFILE_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Португальский общий слой не заменяет обследование объекта&quot;</code>
>

<!-- record:4 cells:16 -->
> [!abstract]- Запись 4 из 32 — GAP-004 — Полный физический инвентарь с количеством, состоянием, сроком, местом хранения и владельцем
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-004&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;BASE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Полный физический инвентарь с количеством, состоянием, сроком, местом хранения и владельцем&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Осмотр; фото/серийные номера; количества; сроки; условия хранения; результаты теста; расхождения; дата следующей проверки&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Подтверждённое физическое имущество: 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_PHYSICAL_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PHYSICAL_INVENTORY_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Каталожная или закупочная строка не является доказательством наличия&quot;</code>
>

<!-- record:5 cells:16 -->
> [!abstract]- Запись 5 из 32 — GAP-005 — Рецензированные P0-карточки первой помощи для неспециалиста с локальными номерами помощи и стоп-условиями
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-005&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GENERAL_PORTUGAL_PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Рецензированные P0-карточки первой помощи для неспециалиста с локальными номерами помощи и стоп-условиями&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Карточки по непосредственным угрозам жизни; источник и версия; рецензент; Portugal overlay; печатный тест; сценарная тренировка; дата пересмотра&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Медицинские узлы и учебные PDF существуют; выпущенных lay action cards 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_RELEASED_ACTION_PACKAGE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_LAY_MEDICAL_CARDS_REVIEWED_AND_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не заменять карточки большим учебником; не давать диагностику или назначения вне компетенции&quot;</code>
>

<!-- record:6 cells:16 -->
> [!abstract]- Запись 6 из 32 — GAP-006 — Непрерывность назначенных лекарств, рецептов, расходников и холодовой цепи
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-006&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Непрерывность назначенных лекарств, рецептов, расходников и холодовой цепи&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Персональный medication list; назначивший врач; законный запас и ротация; температурный журнал где нужен; резервный план; противопоказания; контакт аптеки/врача&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Персональных лекарственных данных и подтверждённого запаса 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_PERSONAL_MEDICATION_PLAN&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PRESCRIBED_MEDICATION_CONTINUITY_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не предлагать самостоятельную замену дозы, препарата или синтез лекарства&quot;</code>
>

<!-- record:7 cells:16 -->
> [!abstract]- Запись 7 из 32 — GAP-007 — Физические медицинские комплекты по месту и роли
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-007&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE_PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Физические медицинские комплекты по месту и роли&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Физический осмотр комплектов; ведомость; количество на фактическую группу; сроки и ротация; СИЗ; пломбы; место; доступность; ответственный&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Целевые категории комплектов описаны; физически подтверждённых комплектов 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_PHYSICAL_MEDICAL_KIT&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_MEDICAL_KITS_PHYSICALLY_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Целевая архитектура не означает четыре реально существующих комплекта&quot;</code>
>

<!-- record:8 cells:16 -->
> [!abstract]- Запись 8 из 32 — GAP-008 — Очное обучение первой помощи и медицинские тренировки с учётом границ компетенции
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-008&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;HEALTH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PERSON_GROUP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Очное обучение первой помощи и медицинские тренировки с учётом границ компетенции&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Сертификат/подтверждение курса; дата; программа; практическая оценка; журнал drills; наблюдатель; ошибки и корректирующие действия&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;PDF и каталог существуют; подтверждённых навыков и drills 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_TRAINING_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_MEDICAL_TRAINING_AND_DRILL_PASSED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Наличие справочника не подтверждает способность оказать помощь&quot;</code>
>

<!-- record:9 cells:16 -->
> [!abstract]- Запись 9 из 32 — GAP-009 — Карта Португалии/региона с крупными рисками, службами, дорогами и альтернативными направлениями
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-009&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;MAPS_COMMS&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PORTUGAL_REGION&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Карта Португалии/региона с крупными рисками, службами, дорогами и альтернативными направлениями&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Офлайн-вектор/растр; дата; источник; опасности; больницы и пункты помощи; печатная копия; проверка масштаба и легенды&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Готовых карт этого слоя 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_MAP_LAYER_1&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PORTUGAL_REGION_MAP_VERIFIED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Первый из трёх обязательных слоёв карт&quot;</code>
>

<!-- record:10 cells:16 -->
> [!abstract]- Запись 10 из 32 — GAP-010 — Муниципальная/локальная карта маршрутов, воды, убежищ, аптек, медицины, пожарных, полиции, зарядки и встреч
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-010&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;MAPS_COMMS&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Муниципальная/локальная карта маршрутов, воды, убежищ, аптек, медицины, пожарных, полиции, зарядки и встреч&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Офлайн-карта; координаты; часы/ограничения; два маршрута; точки встречи; печатная копия; фактический проход/проезд&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Готовых карт этого слоя 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_MAP_LAYER_2&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_LOCAL_ROUTE_MAP_FIELD_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Контакты и доступность служб должны иметь дату проверки&quot;</code>
>

<!-- record:11 cells:16 -->
> [!abstract]- Запись 11 из 32 — GAP-011 — Схема объекта/участка: выходы, отключения, вода, электричество, газ, огнетушители, аптечки, опасности и сбор
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-011&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;MAPS_COMMS&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Схема объекта/участка: выходы, отключения, вода, электричество, газ, огнетушители, аптечки, опасности и сбор&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Актуальный план с легендой; маркировка на месте; ночной тест; два пути выхода; печатные копии; дата обхода&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Готовых site-specific схем 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_MAP_LAYER_3&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_SITE_MAP_WALKED_AND_SIGNED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Третий из трёх обязательных слоёв карт&quot;</code>
>

<!-- record:12 cells:16 -->
> [!abstract]- Запись 12 из 32 — GAP-012 — Измеренный резерв питьевой и хозяйственной воды для 1, 2 и 3–7 человек
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-012&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;WATER_WASH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE_PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Измеренный резерв питьевой и хозяйственной воды для 1, 2 и 3–7 человек&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Литры; число людей; дни; тара; дата наполнения; ротация; потери; доступность; второй путь снабжения; тест выдачи&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог и формула мощности есть; физический объём 0 подтверждён&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_WATER_CAPACITY_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_WATER_RESERVE_MEASURED_AND_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Количество определяется профилями людей, климатом и официальными рекомендациями&quot;</code>
>

<!-- record:13 cells:16 -->
> [!abstract]- Запись 13 из 32 — GAP-013 — Анализ источника воды и проверенный безопасный treatment train с измерениями
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-013&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;WATER_WASH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Анализ источника воды и проверенный безопасный treatment train с измерениями&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3|SL4&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Описание источника; лабораторный/валидный тест; целевые загрязнители; оборудование; расходники; калибровка; критерии прохода; журнал качества; безопасные отходы&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Есть источники WASH и каталог; объектовых проб и испытанной линии 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_WATER_TEST_AND_PROCESS_VALIDATION&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_WATER_QUALITY_AND_TREATMENT_VALIDATED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Органолептика не доказывает микробиологическую или химическую безопасность&quot;</code>
>

<!-- record:14 cells:16 -->
> [!abstract]- Запись 14 из 32 — GAP-014 — Физический резерв пищи и проверенное меню с учётом людей, воды, топлива и медицинских ограничений
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-014&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;FOOD_AGRI&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE_PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Физический резерв пищи и проверенное меню с учётом людей, воды, топлива и медицинских ограничений&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Инвентарь; энергия и белок; аллергии/диеты; меню; вода и топливо на приготовление; сроки; ротация; тест недели; отходы&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог пищи есть; подтверждённого резерва и меню 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_FOOD_RESERVE_OR_MENU_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_FOOD_RESERVE_AND_MENU_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Считать не пачки, а рацион, срок, приготовление и потери&quot;</code>
>

<!-- record:15 cells:16 -->
> [!abstract]- Запись 15 из 32 — GAP-015 — Семенной accession-register, тест всхожести, план обновления и географически отделённый дубль
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-015&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;FOOD_AGRI&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Семенной accession-register, тест всхожести, план обновления и географически отделённый дубль&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Вид/сорт; open-pollinated или гибрид; происхождение; lot; год; число/масса; влажность/температура; всхожесть; площадь; изоляция; harvest-to-seed protocol; дубликат&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталожные и закупочные материалы есть; подтверждённых accession, germination test и duplicate store 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_VERIFIED_SEED_BANK&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_SEED_ACCESSIONS_TESTED_AND_DUPLICATED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Одна пачка не является долгосрочным семенным банком; хранение без размножения не покрывает 100 лет&quot;</code>
>

<!-- record:16 cells:16 -->
> [!abstract]- Запись 16 из 32 — GAP-016 — Физический комплект ручных/электрических инструментов, оснастки, СИЗ и запчастей
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-016&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;WORKSHOP&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Физический комплект ручных/электрических инструментов, оснастки, СИЗ и запчастей&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Осмотр; ведомость; состояние; тест под нагрузкой; расходники; СИЗ; места; резерв критических инструментов; обслуживание&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Инструменты перечислены в каталоге; подтверждённых единиц 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_TOOL_INVENTORY&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_TOOLS_PHYSICALLY_VERIFIED_AND_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Самодельный инструмент требует отдельного чертежа, материала, теста и границ нагрузки&quot;</code>
>

<!-- record:17 cells:16 -->
> [!abstract]- Запись 17 из 32 — GAP-017 — Измерительные приборы, эталоны и калибровка
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-017&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;WORKSHOP&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Измерительные приборы, эталоны и калибровка&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Серийные номера; диапазон и точность; эталон; процедура; сертификат/сравнение; дата; неопределённость; критерий браковки; запас батарей/расходников&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Реестр типов приборов есть; принадлежащих и калиброванных приборов 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_CALIBRATION_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_INSTRUMENTS_OWNED_AND_CALIBRATED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Измерение без диапазона, единиц, допуска и эталона не является доказательством&quot;</code>
>

<!-- record:18 cells:16 -->
> [!abstract]- Запись 18 из 32 — GAP-018 — Выпущенные пакеты чертёж + BOM + инструменты + измерения + испытание + обслуживание
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-018&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;CONSTRUCTION&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GENERAL_SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Выпущенные пакеты чертёж + BOM + инструменты + измерения + испытание + обслуживание&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Версионированный чертёж; размеры/допуски; BOM; материал; инструмент; безопасность; сборка; контрольные точки; нагрузочный тест; отказ; обслуживание; рецензент&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Архитектура production package есть; выпущенных пакетов 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_RELEASED_DRAWING_BOM_TEST_PACKAGE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_DRAWING_BOM_TEST_PACKAGE_REVIEWED_AND_VALIDATED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не выпускать чертёж без критериев приёмки и безопасного отказа&quot;</code>
>

<!-- record:19 cells:16 -->
> [!abstract]- Запись 19 из 32 — GAP-019 — Аудит критических электрических и тепловых нагрузок по времени и пусковой мощности
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-019&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;ENERGY&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE_PERSON&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Аудит критических электрических и тепловых нагрузок по времени и пусковой мощности&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3|SL4&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Перечень нагрузок; W/Wh; пуск; режим; приоритет отключения; профиль 24 часа; измерение; автономия; потери; защита; второй путь&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог систем есть; измеренного load profile 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_ENERGY_LOAD_AUDIT&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_CRITICAL_LOADS_MEASURED_AND_BACKED_UP&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Выбор генерации и батарей до измерения нагрузки недостоверен&quot;</code>
>

<!-- record:20 cells:16 -->
> [!abstract]- Запись 20 из 32 — GAP-020 — Проверенная PACE-связь, список контактов, окна check-in и сигналы отказа
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-020&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;MAPS_COMMS&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PERSON_GROUP_SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Проверенная PACE-связь, список контактов, окна check-in и сигналы отказа&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Primary/Alternate/Contingency/Emergency каналы; контакты; заряд; покрытие; тест из ключевых точек; расписание; кодовые фразы без двусмысленности; бумажная копия&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Архитектура связи есть; фактических каналов и тестов 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_COMMS_TEST&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_COMMS_CHANNELS_FIELD_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Радиосвязь и частоты должны соответствовать действующему праву&quot;</code>
>

<!-- record:21 cells:16 -->
> [!abstract]- Запись 21 из 32 — GAP-021 — Актуальные официальные контакты, предупреждения, право и процедуры Португалии
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-021&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;PORTUGAL&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PORTUGAL&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Актуальные официальные контакты, предупреждения, право и процедуры Португалии&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Официальный источник; точное утверждение; юрисдикция; дата проверки; срок пересмотра; португальский оригинал; понятный перевод; ответственный&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;36 Portugal-узлов и несколько payload; item-level актуальность полностью не проверена&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_PARTIAL_PORTUGAL_REFERENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PORTUGAL_CONTACTS_AND_RULES_CURRENT&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Общий справочник не должен переопределять текущие указания властей&quot;</code>
>

<!-- record:22 cells:16 -->
> [!abstract]- Запись 22 из 32 — GAP-022 — Проверка лицензий, авторских прав, условий хранения, копирования и передачи офлайн-корпуса
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-022&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;KNOWLEDGE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GENERAL_PORTUGAL&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Проверка лицензий, авторских прав, условий хранения, копирования и передачи офлайн-корпуса&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Лицензия/правовое основание по каждому payload; разрешённые действия; атрибуция; ограничения; дата; рецензент&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Файлы сохранены; полный rights review не завершён&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_RIGHTS_REVIEW&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_RIGHTS_REVIEW_DOCUMENTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Техническая возможность копирования не означает юридическое разрешение&quot;</code>
>

<!-- record:23 cells:16 -->
> [!abstract]- Запись 23 из 32 — GAP-023 — Предметная ручная проверка всех 45 фактических офлайн-файлов
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-023&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;KNOWLEDGE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GENERAL_PORTUGAL&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Предметная ручная проверка всех 45 фактических офлайн-файлов&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Рецензент; дата; язык; версия; применимые разделы; ошибки; устаревание; безопасность; локализация; решение keep/replace/quarantine&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;45/45 файлов проходят машинную целостность; визуально проверены первые страницы 43 PDF; предметная ручная рецензия остаётся неполной&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_PAYLOAD_HUMAN_REVIEW&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_PAYLOADS_HUMAN_REVIEWED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Хеш сигнатура и открытие доказывают техническую пригодность файла, не истинность содержания&quot;</code>
>

<!-- record:24 cells:16 -->
> [!abstract]- Запись 24 из 32 — GAP-024 — Запуск Kiwix на целевом устройстве и открытие сохранённого Appropedia ZIM без сети
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-024&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;KNOWLEDGE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Запуск Kiwix на целевом устройстве и открытие сохранённого Appropedia ZIM без сети&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Установка; launch; ZIM open; поиск; переход статей; перезапуск без сети; скрин/журнал; версия ОС; запасной reader&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;DMG и ZIM присутствуют и проходят машинные проверки; пользовательский end-to-end тест 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_KIWIX_ZIM_E2E_TEST&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_KIWIX_AND_ZIM_OPEN_OFFLINE&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Техническая целостность DMG не равна рабочему чтению базы&quot;</code>
>

<!-- record:25 cells:16 -->
> [!abstract]- Запись 25 из 32 — GAP-025 — Независимые резервные копии и доказанное восстановление всего кита без сети
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-025&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;KNOWLEDGE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Независимые резервные копии и доказанное восстановление всего кита без сети&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Минимум две независимые копии; одна географически отделена; manifest/hash; зашифрованные приватные данные; restore drill; время восстановления; журнал ошибок&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Фактический restore drill и независимые носители не подтверждены&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_RESTORE_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_BACKUP_RESTORE_DRILL_PASSED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Копия считается резервной только после восстановления&quot;</code>
>

<!-- record:26 cells:16 -->
> [!abstract]- Запись 26 из 32 — GAP-026 — Роли, дублёры, полномочия, журнал решений, механизм разногласий и смена управления
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-026&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;GOVERNANCE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Роли, дублёры, полномочия, журнал решений, механизм разногласий и смена управления&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Role matrix; владелец/дублёр каждой критической функции; правила экстренного решения; consent; журнал; handover drill; конфликтный процесс&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Архитектурные узлы управления есть; назначенных людей 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_GROUP_ROLES&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_GROUP_ROLES_ASSIGNED_AND_EXERCISED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Система должна работать при отсутствии одного ключевого человека&quot;</code>
>

<!-- record:27 cells:16 -->
> [!abstract]- Запись 27 из 32 — GAP-027 — Осмотр укрытия, пожарных рисков, путей выхода, вентиляции и CO
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-027&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;SHELTER&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL0&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Осмотр укрытия, пожарных рисков, путей выхода, вентиляции и CO&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL0|SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Site walk; два пути выхода; smoke/CO alarms с тестом; огнетушители по риску; отключения; вентиляция; отопление; ночная тренировка; журнал обслуживания&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог безопасности укрытия есть; объектового осмотра и теста 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_SHELTER_FIRE_CO_EVIDENCE&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_SHELTER_FIRE_CO_CONTROLS_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Горение в помещении без рассчитанного воздуха, отвода и CO-контроля запрещено&quot;</code>
>

<!-- record:28 cells:16 -->
> [!abstract]- Запись 28 из 32 — GAP-028 — Практическая система туалета, гигиены, серых вод, мусора и опасных отходов
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-028&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;WATER_WASH&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P0_RED&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Практическая система туалета, гигиены, серых вод, мусора и опасных отходов&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3|SL4&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Поток отходов; ёмкости; разделение; средства гигиены; очистка; PPE; законный вывоз/обработка; capacity; тест 72 часа; вредители; журнал&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;55 WASH-узлов и справочные PDF есть; физической системы и теста 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_SANITATION_WASTE_SYSTEM&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_SANITATION_AND_WASTE_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не смешивать человеческие, химические, медицинские и горючие отходы&quot;</code>
>

<!-- record:29 cells:16 -->
> [!abstract]- Запись 29 из 32 — GAP-029 — Сквозные тренировки всех P0/P1 сценариев и журнал корректирующих действий
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-029&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;BASE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;PERSON_GROUP_SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL2&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Сквозные тренировки всех P0/P1 сценариев и журнал корректирующих действий&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL2|SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Сценарии; участники; наблюдатель; время; результат; near misses; фото/лог; corrective action; повторный тест; следующая дата&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог сценариев есть; выполненных сквозных drills 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_INTEGRATED_DRILLS&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_P0_P1_SCENARIOS_DRILLED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Начинать с безопасных tabletop и walk-through; рискованные действия не имитировать без контроля&quot;</code>
>

<!-- record:30 cells:16 -->
> [!abstract]- Запись 30 из 32 — GAP-030 — Безопасное приготовление пищи и тепло с вентиляцией, пожарной защитой, CO-контролем и законным топливом
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-030&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;ENERGY_FUELS&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P1_ORANGE&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL1&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Безопасное приготовление пищи и тепло с вентиляцией, пожарной защитой, CO-контролем и законным топливом&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL1|SL2|SL3&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Утверждённое оборудование; совместимое топливо; хранение; вентиляция; CO alarm; пожарный контроль; тест; запас; обслуживание; инструкция производителя&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Каталог энергосистем есть; физическая система и тест 0&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_SAFE_COOKING_HEAT_PATH&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_CERTIFIED_COOKING_HEAT_PATH_TESTED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Самодельное производство бензина, дизеля или керосина не является бытовой ветвью&quot;</code>
>

<!-- record:31 cells:16 -->
> [!abstract]- Запись 31 из 32 — GAP-031 — Календарь обслуживания, ротации, калибровки, обновления источников и критических запчастей
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-031&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;BASE&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Календарь обслуживания, ротации, калибровки, обновления источников и критических запчастей&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5|SL6&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Asset/source owner; backup; interval; next_due; spare level; work log; failure history; trigger for replacement; annual review&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;Большинство owner и next_due имеют UNASSIGNED/TBD&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_NO_MAINTENANCE_OWNERSHIP&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_MAINTENANCE_CALENDAR_ASSIGNED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сто лет достигаются повторяемым обслуживанием и передачей, а не разовой закупкой&quot;</code>
>

<!-- record:32 cells:16 -->
> [!abstract]- Запись 32 из 32 — GAP-032 — Контроль доступа и правовая/профессиональная граница для S3/S4 материалов
> - **«gap» ID** (<code>&quot;gap_id&quot;</code>): <code>&quot;GAP-032&quot;</code>
> - **Отрасль** (<code>&quot;domain&quot;</code>): <code>&quot;HAZARD&quot;</code>
> - **Область «layer»** (<code>&quot;scope_layer&quot;</code>): <code>&quot;GENERAL_PORTUGAL_SITE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;P2_YELLOW&quot;</code>
> - **Самый ранний уровень сервиса** (<code>&quot;earliest_service_level&quot;</code>): <code>&quot;SL3&quot;</code>
> - **«gap» на русском** (<code>&quot;gap_ru&quot;</code>): <code>&quot;Контроль доступа и правовая/профессиональная граница для S3/S4 материалов&quot;</code>
> - **«blocks» сервис уровень** (<code>&quot;blocks_service_level&quot;</code>): <code>&quot;SL3|SL4|SL5&quot;</code>
> - **«blocker»** (<code>&quot;blocker&quot;</code>): <code>&quot;YES&quot;</code>
> - **Требуемые доказательства** (<code>&quot;required_evidence&quot;</code>): <code>&quot;Классификация; основание ограничения; доступ; предупреждение; закон; компетенция; facility controls; отходы; incident plan; ежегодный review&quot;</code>
> - **Имеющиеся доказательства** (<code>&quot;current_evidence&quot;</code>): <code>&quot;74 узла REFERENCE_ONLY; готовность контроля доступа и review не подтверждена&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN_HAZARD_GOVERNANCE_REVIEW&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;UNASSIGNED&quot;</code>
> - **Срок** (<code>&quot;due&quot;</code>): <code>&quot;TBD_NOT_SCHEDULED&quot;</code>
> - **Допуск к применению** (<code>&quot;release_gate&quot;</code>): <code>&quot;DENY_UNTIL_S3_S4_ACCESS_AND_REVIEW_CONTROLS_DEFINED&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не публиковать бытовые рецепты взрывчатых веществ, импровизированных топлив, синтеза лекарств или высокорисковой химии&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
