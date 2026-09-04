---
id: "DATA-REGISTER-2ddfdc7dacb69d50"
type: "generated-data-register-view"
title: "Журнал подотчётности — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "accountability-log-template.csv"
source_sha256: "6c674ace408e0cfc294ee9f26458f5f85f09a4c07450ea08d722a9d88a21636b"
source_bytes: 1108
source_row_count: 4
source_column_count: 20
source_cell_count: 80
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: accountability-log-template.csv -->

# Журнал подотчётности — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 4
- **Полей в каждой записи:** 20
- **Ячеек данных, включая пустые:** 80
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `6c674ace408e0cfc294ee9f26458f5f85f09a4c07450ea08d722a9d88a21636b`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «event» ID | <code>&quot;event_id&quot;</code> |
| 2 | «accountability» запись ID | <code>&quot;accountability_entry_id&quot;</code> |
| 3 | «timestamp» «utc» | <code>&quot;timestamp_utc&quot;</code> |
| 4 | Человек ID | <code>&quot;person_id&quot;</code> |
| 5 | «subgroup» ID | <code>&quot;subgroup_id&quot;</code> |
| 6 | «accountability» статус | <code>&quot;accountability_status&quot;</code> |
| 7 | Объект ID | <code>&quot;site_id&quot;</code> |
| 8 | Маршрут ID | <code>&quot;route_id&quot;</code> |
| 9 | «buddy» назначение ID | <code>&quot;buddy_assignment_id&quot;</code> |
| 10 | «observation» метод | <code>&quot;observation_method&quot;</code> |
| 11 | «observed» кем человек ID | <code>&quot;observed_by_person_id&quot;</code> |
| 12 | «last» «confirmed» контакт | <code>&quot;last_confirmed_contact&quot;</code> |
| 13 | Следующий проверка срок | <code>&quot;next_check_due&quot;</code> |
| 14 | «missing» человек «escalation» состояние | <code>&quot;missing_person_escalation_state&quot;</code> |
| 15 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 16 | «created» кем | <code>&quot;created_by&quot;</code> |
| 17 | Примечания | <code>&quot;notes&quot;</code> |
| 18 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 19 | «composition» снимок ID | <code>&quot;composition_snapshot_id&quot;</code> |
| 20 | «composition» допуск состояние | <code>&quot;composition_gate_state&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:20 -->
> [!abstract]- Запись 1 из 4 — P01
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_id&quot;</code>): <code>&quot;ACC-0001&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-01&quot;</code>
> - **«observation» метод** (<code>&quot;observation_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«observed» кем человек ID** (<code>&quot;observed_by_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«last» «confirmed» контакт** (<code>&quot;last_confirmed_contact&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка срок** (<code>&quot;next_check_due&quot;</code>): <code>&quot;&quot;</code>
> - **«missing» человек «escalation» состояние** (<code>&quot;missing_person_escalation_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон; не реальная отметка присутствия&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
>

<!-- record:2 cells:20 -->
> [!abstract]- Запись 2 из 4 — P02
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_id&quot;</code>): <code>&quot;ACC-0002&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-01&quot;</code>
> - **«observation» метод** (<code>&quot;observation_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«observed» кем человек ID** (<code>&quot;observed_by_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«last» «confirmed» контакт** (<code>&quot;last_confirmed_contact&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка срок** (<code>&quot;next_check_due&quot;</code>): <code>&quot;&quot;</code>
> - **«missing» человек «escalation» состояние** (<code>&quot;missing_person_escalation_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
>

<!-- record:3 cells:20 -->
> [!abstract]- Запись 3 из 4 — P03
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_id&quot;</code>): <code>&quot;ACC-0003&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-02&quot;</code>
> - **«observation» метод** (<code>&quot;observation_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«observed» кем человек ID** (<code>&quot;observed_by_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«last» «confirmed» контакт** (<code>&quot;last_confirmed_contact&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка срок** (<code>&quot;next_check_due&quot;</code>): <code>&quot;&quot;</code>
> - **«missing» человек «escalation» состояние** (<code>&quot;missing_person_escalation_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
>

<!-- record:4 cells:20 -->
> [!abstract]- Запись 4 из 4 — P04
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_id&quot;</code>): <code>&quot;ACC-0004&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-02&quot;</code>
> - **«observation» метод** (<code>&quot;observation_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«observed» кем человек ID** (<code>&quot;observed_by_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«last» «confirmed» контакт** (<code>&quot;last_confirmed_contact&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка срок** (<code>&quot;next_check_due&quot;</code>): <code>&quot;&quot;</code>
> - **«missing» человек «escalation» состояние** (<code>&quot;missing_person_escalation_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
