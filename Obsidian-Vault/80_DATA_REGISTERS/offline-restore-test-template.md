---
id: "DATA-REGISTER-e093a17016121f0a"
type: "generated-data-register-view"
title: "Испытание восстановления офлайн-библиотеки — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "offline-restore-test-template.csv"
source_sha256: "9c5b6d962cf896e104923acf3c9cb04f9cd91dcdfb1586ba43b9a71fe0a2cd61"
source_bytes: 878
source_row_count: 1
source_column_count: 28
source_cell_count: 28
ignored_blank_row_count: 0
semantic_group: "OFFLINE_KNOWLEDGE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: offline-restore-test-template.csv -->

# Испытание восстановления офлайн-библиотеки — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Источники, архив и офлайн-библиотека
- **Записей:** 1
- **Полей в каждой записи:** 28
- **Ячеек данных, включая пустые:** 28
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `9c5b6d962cf896e104923acf3c9cb04f9cd91dcdfb1586ba43b9a71fe0a2cd61`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Восстановление испытание ID | <code>&quot;restore_test_id&quot;</code> |
| 2 | Область | <code>&quot;scope&quot;</code> |
| 3 | Источник «copy» план ID | <code>&quot;source_copy_plan_ids&quot;</code> |
| 4 | Испытание «device» ID | <code>&quot;test_device_id&quot;</code> |
| 5 | «device» «was» «clean» состояние | <code>&quot;device_was_clean_state&quot;</code> |
| 6 | «network» «disabled» состояние | <code>&quot;network_disabled_state&quot;</code> |
| 7 | «paper» «runbook» ревизия | <code>&quot;paper_runbook_revision&quot;</code> |
| 8 | «operator» человек «or» роль ID | <code>&quot;operator_person_or_role_id&quot;</code> |
| 9 | «operator» «was» «original» «creator» | <code>&quot;operator_was_original_creator&quot;</code> |
| 10 | «started» время | <code>&quot;started_at&quot;</code> |
| 11 | «completed» время | <code>&quot;completed_at&quot;</code> |
| 12 | «rto» целевой | <code>&quot;rto_target&quot;</code> |
| 13 | «rto» фактический | <code>&quot;rto_actual&quot;</code> |
| 14 | «start» «here» «restored» состояние | <code>&quot;start_here_restored_state&quot;</code> |
| 15 | «manifest» «restored» состояние | <code>&quot;manifest_restored_state&quot;</code> |
| 16 | «readers» «restored» состояние | <code>&quot;readers_restored_state&quot;</code> |
| 17 | «index» «restored» состояние | <code>&quot;index_restored_state&quot;</code> |
| 18 | «sample» «packages» «restored» состояние | <code>&quot;sample_packages_restored_state&quot;</code> |
| 19 | «fixity» результат | <code>&quot;fixity_result&quot;</code> |
| 20 | «search» «tasks» «total» | <code>&quot;search_tasks_total&quot;</code> |
| 21 | «search» «tasks» «passed» | <code>&quot;search_tasks_passed&quot;</code> |
| 22 | «energy» «used» «wh» | <code>&quot;energy_used_wh&quot;</code> |
| 23 | «errors» «and» «deviations» | <code>&quot;errors_and_deviations&quot;</code> |
| 24 | «corrective» действие ссылки | <code>&quot;corrective_action_refs&quot;</code> |
| 25 | «retest» срок | <code>&quot;retest_due&quot;</code> |
| 26 | Испытание состояние | <code>&quot;test_state&quot;</code> |
| 27 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 28 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:28 -->
> [!abstract]- Запись 1 из 1 — RESTORE-EXAMPLE-001
> - **Восстановление испытание ID** (<code>&quot;restore_test_id&quot;</code>): <code>&quot;RESTORE-EXAMPLE-001&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;L0_L1&quot;</code>
> - **Источник «copy» план ID** (<code>&quot;source_copy_plan_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Испытание «device» ID** (<code>&quot;test_device_id&quot;</code>): <code>&quot;&quot;</code>
> - **«device» «was» «clean» состояние** (<code>&quot;device_was_clean_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«network» «disabled» состояние** (<code>&quot;network_disabled_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«paper» «runbook» ревизия** (<code>&quot;paper_runbook_revision&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» человек «or» роль ID** (<code>&quot;operator_person_or_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **«operator» «was» «original» «creator»** (<code>&quot;operator_was_original_creator&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«started» время** (<code>&quot;started_at&quot;</code>): <code>&quot;&quot;</code>
> - **«completed» время** (<code>&quot;completed_at&quot;</code>): <code>&quot;&quot;</code>
> - **«rto» целевой** (<code>&quot;rto_target&quot;</code>): <code>&quot;&quot;</code>
> - **«rto» фактический** (<code>&quot;rto_actual&quot;</code>): <code>&quot;&quot;</code>
> - **«start» «here» «restored» состояние** (<code>&quot;start_here_restored_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«manifest» «restored» состояние** (<code>&quot;manifest_restored_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«readers» «restored» состояние** (<code>&quot;readers_restored_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«index» «restored» состояние** (<code>&quot;index_restored_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«sample» «packages» «restored» состояние** (<code>&quot;sample_packages_restored_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«fixity» результат** (<code>&quot;fixity_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «tasks» «total»** (<code>&quot;search_tasks_total&quot;</code>): <code>&quot;&quot;</code>
> - **«search» «tasks» «passed»** (<code>&quot;search_tasks_passed&quot;</code>): <code>&quot;&quot;</code>
> - **«energy» «used» «wh»** (<code>&quot;energy_used_wh&quot;</code>): <code>&quot;&quot;</code>
> - **«errors» «and» «deviations»** (<code>&quot;errors_and_deviations&quot;</code>): <code>&quot;&quot;</code>
> - **«corrective» действие ссылки** (<code>&quot;corrective_action_refs&quot;</code>): <code>&quot;&quot;</code>
> - **«retest» срок** (<code>&quot;retest_due&quot;</code>): <code>&quot;&quot;</code>
> - **Испытание состояние** (<code>&quot;test_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Успех требует blank-device и ручного поиска другим человеком&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
