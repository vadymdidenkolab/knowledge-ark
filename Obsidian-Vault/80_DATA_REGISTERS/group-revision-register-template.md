---
id: "DATA-REGISTER-de47dd330a7781aa"
type: "generated-data-register-view"
title: "Ревизии данных группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-revision-register-template.csv"
source_sha256: "9bdb45ba9a6de64e715fffc7bb57d12461a94cb0315ec6a908f04c3c4ed97fdb"
source_bytes: 2792
source_row_count: 8
source_column_count: 16
source_cell_count: 128
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-revision-register-template.csv -->

# Ревизии данных группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 8
- **Полей в каждой записи:** 16
- **Ячеек данных, включая пустые:** 128
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `9bdb45ba9a6de64e715fffc7bb57d12461a94cb0315ec6a908f04c3c4ed97fdb`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Ревизия ID | <code>&quot;revision_id&quot;</code> |
| 2 | «artifact» тип | <code>&quot;artifact_type&quot;</code> |
| 3 | «logical» «object» ID | <code>&quot;logical_object_id&quot;</code> |
| 4 | «artifact» файл ссылка | <code>&quot;artifact_file_ref&quot;</code> |
| 5 | «artifact» версия | <code>&quot;artifact_version&quot;</code> |
| 6 | «canonicalization» «rule» | <code>&quot;canonicalization_rule&quot;</code> |
| 7 | «content» SHA-256 | <code>&quot;content_sha256&quot;</code> |
| 8 | Предыдущий ревизия ID | <code>&quot;previous_revision_id&quot;</code> |
| 9 | «created» время «utc» | <code>&quot;created_at_utc&quot;</code> |
| 10 | «effective» из «utc» | <code>&quot;effective_from_utc&quot;</code> |
| 11 | «effective» до «utc» | <code>&quot;effective_until_utc&quot;</code> |
| 12 | «approval» запись ссылка | <code>&quot;approval_record_ref&quot;</code> |
| 13 | Ревизия состояние | <code>&quot;revision_state&quot;</code> |
| 14 | Владелец | <code>&quot;owner&quot;</code> |
| 15 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 16 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:16 -->
> [!abstract]- Запись 1 из 8 — ROSTER-EXAMPLE-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_ROSTER&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;ALL&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-roster-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_AND_ROWS_IN_PERSON_ID_ORDER&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest хранится вне хешируемого roster-файла; пример не operational&quot;</code>
>

<!-- record:2 cells:16 -->
> [!abstract]- Запись 2 из 8 — GP-N1-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N1-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:3 cells:16 -->
> [!abstract]- Запись 3 из 8 — GP-N2-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N2-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:4 cells:16 -->
> [!abstract]- Запись 4 из 8 — GP-N3-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N3-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:5 cells:16 -->
> [!abstract]- Запись 5 из 8 — GP-N4-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N4-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:6 cells:16 -->
> [!abstract]- Запись 6 из 8 — GP-N5-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N5-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:7 cells:16 -->
> [!abstract]- Запись 7 из 8 — GP-N6-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N6-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

<!-- record:8 cells:16 -->
> [!abstract]- Запись 8 из 8 — GP-N7-R0
> - **Ревизия ID** (<code>&quot;revision_id&quot;</code>): <code>&quot;GP-N7-R0&quot;</code>
> - **«artifact» тип** (<code>&quot;artifact_type&quot;</code>): <code>&quot;GROUP_PROFILE_ROW&quot;</code>
> - **«logical» «object» ID** (<code>&quot;logical_object_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **«artifact» файл ссылка** (<code>&quot;artifact_file_ref&quot;</code>): <code>&quot;group-profile-template.csv&quot;</code>
> - **«artifact» версия** (<code>&quot;artifact_version&quot;</code>): <code>&quot;0-DRAFT&quot;</code>
> - **«canonicalization» «rule»** (<code>&quot;canonicalization_rule&quot;</code>): <code>&quot;CSV_UTF8_HEADER_PLUS_ROW_KEYED_BY_GROUP_PROFILE_ID&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Предыдущий ревизия ID** (<code>&quot;previous_revision_id&quot;</code>): <code>&quot;&quot;</code>
> - **«created» время «utc»** (<code>&quot;created_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из «utc»** (<code>&quot;effective_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до «utc»** (<code>&quot;effective_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«approval» запись ссылка** (<code>&quot;approval_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Ревизия состояние** (<code>&quot;revision_state&quot;</code>): <code>&quot;DRAFT_NOT_HASHED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Digest относится к канонизированной header+profile row и хранится во внешнем revision register&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
