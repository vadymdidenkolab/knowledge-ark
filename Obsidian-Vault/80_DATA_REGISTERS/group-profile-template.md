---
id: "DATA-REGISTER-231e105a8b720ea5"
type: "generated-data-register-view"
title: "Профиль группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-profile-template.csv"
source_sha256: "ab94e7939e3ecc9f7ad29b0060fc9138034522e7d9e64a4fdf2a4e5ddb88446b"
source_bytes: 1593
source_row_count: 7
source_column_count: 12
source_cell_count: 84
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-profile-template.csv -->

# Профиль группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 7
- **Полей в каждой записи:** 12
- **Ячеек данных, включая пустые:** 84
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `ab94e7939e3ecc9f7ad29b0060fc9138034522e7d9e64a4fdf2a4e5ddb88446b`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 2 | Человеческий количество | <code>&quot;human_count&quot;</code> |
| 3 | «active» человек ID | <code>&quot;active_person_ids&quot;</code> |
| 4 | Животное «entity» ID | <code>&quot;animal_entity_ids&quot;</code> |
| 5 | Уход «load» «summary» | <code>&quot;care_load_summary&quot;</code> |
| 6 | Доступный функция мощность | <code>&quot;available_function_capacity&quot;</code> |
| 7 | Минимальный «safe» «mode» триггер | <code>&quot;minimum_safe_mode_trigger&quot;</code> |
| 8 | Профиль статус | <code>&quot;profile_status&quot;</code> |
| 9 | Владелец | <code>&quot;owner&quot;</code> |
| 10 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 11 | Примечания | <code>&quot;notes&quot;</code> |
| 12 | Профиль ревизия ID | <code>&quot;profile_revision_id&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:12 -->
> [!abstract]- Запись 1 из 7 — GP-N1
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;1&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;ONE_PERSON_SEQUENTIAL_PLUS_EXTERNAL_ESCALATION&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Любая функция вне способности/полномочия или потеря связи&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;N — люди; животные считаются отдельно&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N1-R0&quot;</code>
>

<!-- record:2 cells:12 -->
> [!abstract]- Запись 2 из 7 — GP-N2
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;2&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;BUDDY_PAIR&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Оба не способны вызвать помощь или критическая функция без владельца&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N2-R0&quot;</code>
>

<!-- record:3 cells:12 -->
> [!abstract]- Запись 3 из 7 — GP-N3
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;3&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02|P03&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;COMPACT_CELL&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Care load или одновременные задачи превышают фактическую способность&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N3-R0&quot;</code>
>

<!-- record:4 cells:12 -->
> [!abstract]- Запись 4 из 7 — GP-N4
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;4&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02|P03|P04&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;TWO_PAIRS&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Подгруппа остаётся без leadership/accountability/comms&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N4-R0&quot;</code>
>

<!-- record:5 cells:12 -->
> [!abstract]- Запись 5 из 7 — GP-N5
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;5&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02|P03|P04|P05&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;FIVE_FUNCTION_CELL&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Caregiver или critical function без backup&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N5-R0&quot;</code>
>

<!-- record:6 cells:12 -->
> [!abstract]- Запись 6 из 7 — GP-N6
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;6&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02|P03|P04|P05|P06&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;SIX_FUNCTION_CELL&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Усталость или разделение ломают succession&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N6-R0&quot;</code>
>

<!-- record:7 cells:12 -->
> [!abstract]- Запись 7 из 7 — GP-N7
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Человеческий количество** (<code>&quot;human_count&quot;</code>): <code>&quot;7&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01|P02|P03|P04|P05|P06|P07&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход «load» «summary»** (<code>&quot;care_load_summary&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступный функция мощность** (<code>&quot;available_function_capacity&quot;</code>): <code>&quot;SEVEN_FUNCTION_CONTOUR&quot;</code>
> - **Минимальный «safe» «mode» триггер** (<code>&quot;minimum_safe_mode_trigger&quot;</code>): <code>&quot;Любая critical function без пригодного primary/backup&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Профиль ревизия ID** (<code>&quot;profile_revision_id&quot;</code>): <code>&quot;GP-N7-R0&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
