---
id: "DATA-REGISTER-bb5256d6306066f1"
type: "generated-data-register-view"
title: "Снимок состава группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-composition-snapshot-template.csv"
source_sha256: "137c3cedfa797405f0580d08b68049d8a63c21ff1ac22f5457a8b00e8f8398c2"
source_bytes: 685
source_row_count: 1
source_column_count: 19
source_cell_count: 19
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-composition-snapshot-template.csv -->

# Снимок состава группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 1
- **Полей в каждой записи:** 19
- **Ячеек данных, включая пустые:** 19
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `137c3cedfa797405f0580d08b68049d8a63c21ff1ac22f5457a8b00e8f8398c2`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «composition» снимок ID | <code>&quot;composition_snapshot_id&quot;</code> |
| 2 | «event» ID | <code>&quot;event_id&quot;</code> |
| 3 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 4 | «captured» время «utc» | <code>&quot;captured_at_utc&quot;</code> |
| 5 | «active» человек ID | <code>&quot;active_person_ids&quot;</code> |
| 6 | «present» человек ID | <code>&quot;present_person_ids&quot;</code> |
| 7 | «missing» человек ID | <code>&quot;missing_person_ids&quot;</code> |
| 8 | Животное «entity» ID | <code>&quot;animal_entity_ids&quot;</code> |
| 9 | «dependent» человек ID | <code>&quot;dependent_person_ids&quot;</code> |
| 10 | Источник «roster» ревизия ID | <code>&quot;source_roster_revision_id&quot;</code> |
| 11 | Согласие граница ссылка | <code>&quot;consent_boundary_ref&quot;</code> |
| 12 | «created» кем | <code>&quot;created_by&quot;</code> |
| 13 | «immutable» запись хеш | <code>&quot;immutable_record_hash&quot;</code> |
| 14 | Снимок статус | <code>&quot;snapshot_status&quot;</code> |
| 15 | Примечания | <code>&quot;notes&quot;</code> |
| 16 | Источник «roster» «content» SHA-256 | <code>&quot;source_roster_content_sha256&quot;</code> |
| 17 | Источник группа профиль ревизия ID | <code>&quot;source_group_profile_revision_id&quot;</code> |
| 18 | Источник группа профиль «content» SHA-256 | <code>&quot;source_group_profile_content_sha256&quot;</code> |
| 19 | Источник ревизия «match» состояние | <code>&quot;source_revision_match_state&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:19 -->
> [!abstract]- Запись 1 из 1 — GP-N1
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;COMP-EXAMPLE-001&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«active» человек ID** (<code>&quot;active_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **«present» человек ID** (<code>&quot;present_person_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«missing» человек ID** (<code>&quot;missing_person_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Животное «entity» ID** (<code>&quot;animal_entity_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«dependent» человек ID** (<code>&quot;dependent_person_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «roster» ревизия ID** (<code>&quot;source_roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
> - **Согласие граница ссылка** (<code>&quot;consent_boundary_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **«immutable» запись хеш** (<code>&quot;immutable_record_hash&quot;</code>): <code>&quot;&quot;</code>
> - **Снимок статус** (<code>&quot;snapshot_status&quot;</code>): <code>&quot;DRAFT_NOT_EFFECTIVE&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример структуры; не реальный состав события&quot;</code>
> - **Источник «roster» «content» SHA-256** (<code>&quot;source_roster_content_sha256&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник группа профиль ревизия ID** (<code>&quot;source_group_profile_revision_id&quot;</code>): <code>&quot;GP-N1-R0&quot;</code>
> - **Источник группа профиль «content» SHA-256** (<code>&quot;source_group_profile_content_sha256&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник ревизия «match» состояние** (<code>&quot;source_revision_match_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
