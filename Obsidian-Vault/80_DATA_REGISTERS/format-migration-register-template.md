---
id: "DATA-REGISTER-56b94428de530373"
type: "generated-data-register-view"
title: "Миграция форматов архива — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "format-migration-register-template.csv"
source_sha256: "5ca5d21955f8dc1de3ad9b376731cec56f877166013f7440022704f397e3b98e"
source_bytes: 716
source_row_count: 1
source_column_count: 24
source_cell_count: 24
ignored_blank_row_count: 0
semantic_group: "OFFLINE_KNOWLEDGE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: format-migration-register-template.csv -->

# Миграция форматов архива — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Источники, архив и офлайн-библиотека
- **Записей:** 1
- **Полей в каждой записи:** 24
- **Ячеек данных, включая пустые:** 24
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `5ca5d21955f8dc1de3ad9b376731cec56f877166013f7440022704f397e3b98e`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Миграция ID | <code>&quot;migration_id&quot;</code> |
| 2 | «package» «or» «object» ID | <code>&quot;package_or_object_id&quot;</code> |
| 3 | «event» время | <code>&quot;event_at&quot;</code> |
| 4 | «operator» | <code>&quot;operator&quot;</code> |
| 5 | Источник формат | <code>&quot;source_format&quot;</code> |
| 6 | Источник «reader» «environment» ссылка | <code>&quot;source_reader_environment_ref&quot;</code> |
| 7 | Источник контрольная сумма «algorithm» | <code>&quot;source_digest_algorithm&quot;</code> |
| 8 | Источник контрольная сумма значение | <code>&quot;source_digest_value&quot;</code> |
| 9 | Целевой формат | <code>&quot;target_format&quot;</code> |
| 10 | Целевой «reader» «environment» ссылка | <code>&quot;target_reader_environment_ref&quot;</code> |
| 11 | Целевой контрольная сумма «algorithm» | <code>&quot;target_digest_algorithm&quot;</code> |
| 12 | Целевой контрольная сумма значение | <code>&quot;target_digest_value&quot;</code> |
| 13 | Миграция инструмент | <code>&quot;migration_tool&quot;</code> |
| 14 | Миграция инструмент версия | <code>&quot;migration_tool_version&quot;</code> |
| 15 | Валидация метод | <code>&quot;validation_method&quot;</code> |
| 16 | Валидация результат | <code>&quot;validation_result&quot;</code> |
| 17 | «information» «loss» «assessment» | <code>&quot;information_loss_assessment&quot;</code> |
| 18 | «provenance» «update» ссылка | <code>&quot;provenance_update_ref&quot;</code> |
| 19 | «rollback» «possible» | <code>&quot;rollback_possible&quot;</code> |
| 20 | «reviewer» | <code>&quot;reviewer&quot;</code> |
| 21 | «event» запись SHA-256 | <code>&quot;event_record_sha256&quot;</code> |
| 22 | Миграция состояние | <code>&quot;migration_state&quot;</code> |
| 23 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 24 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:24 -->
> [!abstract]- Запись 1 из 1 — MIGRATION-EXAMPLE-001
> - **Миграция ID** (<code>&quot;migration_id&quot;</code>): <code>&quot;MIGRATION-EXAMPLE-001&quot;</code>
> - **«package» «or» «object» ID** (<code>&quot;package_or_object_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«event» время** (<code>&quot;event_at&quot;</code>): <code>&quot;&quot;</code>
> - **«operator»** (<code>&quot;operator&quot;</code>): <code>&quot;&quot;</code>
> - **Источник формат** (<code>&quot;source_format&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «reader» «environment» ссылка** (<code>&quot;source_reader_environment_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Источник контрольная сумма «algorithm»** (<code>&quot;source_digest_algorithm&quot;</code>): <code>&quot;SHA-256&quot;</code>
> - **Источник контрольная сумма значение** (<code>&quot;source_digest_value&quot;</code>): <code>&quot;&quot;</code>
> - **Целевой формат** (<code>&quot;target_format&quot;</code>): <code>&quot;&quot;</code>
> - **Целевой «reader» «environment» ссылка** (<code>&quot;target_reader_environment_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Целевой контрольная сумма «algorithm»** (<code>&quot;target_digest_algorithm&quot;</code>): <code>&quot;SHA-256&quot;</code>
> - **Целевой контрольная сумма значение** (<code>&quot;target_digest_value&quot;</code>): <code>&quot;&quot;</code>
> - **Миграция инструмент** (<code>&quot;migration_tool&quot;</code>): <code>&quot;&quot;</code>
> - **Миграция инструмент версия** (<code>&quot;migration_tool_version&quot;</code>): <code>&quot;&quot;</code>
> - **Валидация метод** (<code>&quot;validation_method&quot;</code>): <code>&quot;&quot;</code>
> - **Валидация результат** (<code>&quot;validation_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«information» «loss» «assessment»** (<code>&quot;information_loss_assessment&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **«provenance» «update» ссылка** (<code>&quot;provenance_update_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«rollback» «possible»** (<code>&quot;rollback_possible&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«reviewer»** (<code>&quot;reviewer&quot;</code>): <code>&quot;&quot;</code>
> - **«event» запись SHA-256** (<code>&quot;event_record_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Миграция состояние** (<code>&quot;migration_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Original сохраняется до успешной проверки derivative&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
