---
id: "DATA-REGISTER-4e0284adf2d1f56e"
type: "generated-data-register-view"
title: "Оперативный состав группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-operational-roster-template.csv"
source_sha256: "f9ef8e32d0176efb3be8b905249bcb7e90d1d2cee3e25f75cea538ec6691c203"
source_bytes: 2180
source_row_count: 7
source_column_count: 16
source_cell_count: 112
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-operational-roster-template.csv -->

# Оперативный состав группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 7
- **Полей в каждой записи:** 16
- **Ячеек данных, включая пустые:** 112
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `f9ef8e32d0176efb3be8b905249bcb7e90d1d2cee3e25f75cea538ec6691c203`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Операционный запись ID | <code>&quot;operational_record_id&quot;</code> |
| 2 | Человек ID | <code>&quot;person_id&quot;</code> |
| 3 | «display» «alias» | <code>&quot;display_alias&quot;</code> |
| 4 | «accountability» статус | <code>&quot;accountability_status&quot;</code> |
| 5 | «communication» «support» «summary» | <code>&quot;communication_support_summary&quot;</code> |
| 6 | «mobility» «support» «summary» | <code>&quot;mobility_support_summary&quot;</code> |
| 7 | «buddy» «assignments» кем группа профиль | <code>&quot;buddy_assignments_by_group_profile&quot;</code> |
| 8 | Функция назначение источник | <code>&quot;function_assignment_source&quot;</code> |
| 9 | Уход «responsibility» «summary» | <code>&quot;care_responsibility_summary&quot;</code> |
| 10 | Внешний контакт ID | <code>&quot;external_contact_id&quot;</code> |
| 11 | «restricted» профиль ссылка | <code>&quot;restricted_profile_ref&quot;</code> |
| 12 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 13 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 14 | Владелец | <code>&quot;owner&quot;</code> |
| 15 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 16 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:16 -->
> [!abstract]- Запись 1 из 7 — P01
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P01&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-01&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N1:BUD-N1-EXT|GP-N2:BUD-01|GP-N3:BUD-N3-TRIAD|GP-N4:BUD-01|GP-N5:BUD-01|GP-N6:BUD-01|GP-N7:BUD-01&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P01&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view; медицинские данные отсутствуют&quot;</code>
>

<!-- record:2 cells:16 -->
> [!abstract]- Запись 2 из 7 — P02
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P02&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-02&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N2:BUD-01|GP-N3:BUD-N3-TRIAD|GP-N4:BUD-01|GP-N5:BUD-01|GP-N6:BUD-01|GP-N7:BUD-01&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P02&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view&quot;</code>
>

<!-- record:3 cells:16 -->
> [!abstract]- Запись 3 из 7 — P03
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P03&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-03&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N3:BUD-N3-TRIAD|GP-N4:BUD-02|GP-N5:BUD-N5-TRIAD|GP-N6:BUD-02|GP-N7:BUD-02&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P03&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view&quot;</code>
>

<!-- record:4 cells:16 -->
> [!abstract]- Запись 4 из 7 — P04
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P04&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-04&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N4:BUD-02|GP-N5:BUD-N5-TRIAD|GP-N6:BUD-02|GP-N7:BUD-02&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P04&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view&quot;</code>
>

<!-- record:5 cells:16 -->
> [!abstract]- Запись 5 из 7 — P05
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P05&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-05&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N5:BUD-N5-TRIAD|GP-N6:BUD-N6-PAIR|GP-N7:BUD-03&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P05&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view&quot;</code>
>

<!-- record:6 cells:16 -->
> [!abstract]- Запись 6 из 7 — P06
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P06&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-06&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N6:BUD-N6-PAIR|GP-N7:BUD-03&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P06&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view&quot;</code>
>

<!-- record:7 cells:16 -->
> [!abstract]- Запись 7 из 7 — P07
> - **Операционный запись ID** (<code>&quot;operational_record_id&quot;</code>): <code>&quot;OPR-P07&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P07&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;ALIAS-07&quot;</code>
> - **«accountability» статус** (<code>&quot;accountability_status&quot;</code>): <code>&quot;NOT_ACTIVATED&quot;</code>
> - **«communication» «support» «summary»** (<code>&quot;communication_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«mobility» «support» «summary»** (<code>&quot;mobility_support_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» «assignments» кем группа профиль** (<code>&quot;buddy_assignments_by_group_profile&quot;</code>): <code>&quot;GP-N7:BUD-03&quot;</code>
> - **Функция назначение источник** (<code>&quot;function_assignment_source&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Уход «responsibility» «summary»** (<code>&quot;care_responsibility_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«restricted» профиль ссылка** (<code>&quot;restricted_profile_ref&quot;</code>): <code>&quot;P07&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Обезличенный operational view; триада является только шаблоном&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
