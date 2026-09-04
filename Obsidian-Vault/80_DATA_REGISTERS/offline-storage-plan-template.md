---
id: "DATA-REGISTER-bcff208dc1bab46a"
type: "generated-data-register-view"
title: "План хранения офлайн-библиотеки — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "offline-storage-plan-template.csv"
source_sha256: "a87a458491abdbebf7b8eb250420094ea762bff2ddcb5c75ebcd4e579aa9cc53"
source_bytes: 655
source_row_count: 1
source_column_count: 23
source_cell_count: 23
ignored_blank_row_count: 0
semantic_group: "OFFLINE_KNOWLEDGE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: offline-storage-plan-template.csv -->

# План хранения офлайн-библиотеки — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Источники, архив и офлайн-библиотека
- **Записей:** 1
- **Полей в каждой записи:** 23
- **Ячеек данных, включая пустые:** 23
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `a87a458491abdbebf7b8eb250420094ea762bff2ddcb5c75ebcd4e579aa9cc53`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «copy» план ID | <code>&quot;copy_plan_id&quot;</code> |
| 2 | «collection» область | <code>&quot;collection_scope&quot;</code> |
| 3 | «tier» область | <code>&quot;tier_scope&quot;</code> |
| 4 | Хранение объект ID | <code>&quot;storage_site_id&quot;</code> |
| 5 | Отказ отрасль ID | <code>&quot;failure_domain_id&quot;</code> |
| 6 | Носитель класс | <code>&quot;media_class&quot;</code> |
| 7 | «device» «or» «volume» ID | <code>&quot;device_or_volume_id&quot;</code> |
| 8 | «filesystem» | <code>&quot;filesystem&quot;</code> |
| 9 | «encryption» область | <code>&quot;encryption_scope&quot;</code> |
| 10 | «write» «protection» | <code>&quot;write_protection&quot;</code> |
| 11 | «geographic» риск класс | <code>&quot;geographic_risk_class&quot;</code> |
| 12 | «custodian» роль ID | <code>&quot;custodian_role_id&quot;</code> |
| 13 | «successor» «custodian» роль ID | <code>&quot;successor_custodian_role_id&quot;</code> |
| 14 | «sync» метод | <code>&quot;sync_method&quot;</code> |
| 15 | «fixity» «schedule» | <code>&quot;fixity_schedule&quot;</code> |
| 16 | Восстановление «schedule» | <code>&quot;restore_schedule&quot;</code> |
| 17 | Плановый носитель «retirement» время | <code>&quot;planned_media_retirement_at&quot;</code> |
| 18 | Мощность «bytes» | <code>&quot;capacity_bytes&quot;</code> |
| 19 | Фактический «bytes» | <code>&quot;actual_bytes&quot;</code> |
| 20 | «last» подтверждённый время | <code>&quot;last_verified_at&quot;</code> |
| 21 | План состояние | <code>&quot;plan_state&quot;</code> |
| 22 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 23 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:23 -->
> [!abstract]- Запись 1 из 1 — COPYPLAN-EXAMPLE-001
> - **«copy» план ID** (<code>&quot;copy_plan_id&quot;</code>): <code>&quot;COPYPLAN-EXAMPLE-001&quot;</code>
> - **«collection» область** (<code>&quot;collection_scope&quot;</code>): <code>&quot;L0_L1&quot;</code>
> - **«tier» область** (<code>&quot;tier_scope&quot;</code>): <code>&quot;RED|FIELD&quot;</code>
> - **Хранение объект ID** (<code>&quot;storage_site_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Отказ отрасль ID** (<code>&quot;failure_domain_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Носитель класс** (<code>&quot;media_class&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«device» «or» «volume» ID** (<code>&quot;device_or_volume_id&quot;</code>): <code>&quot;&quot;</code>
> - **«filesystem»** (<code>&quot;filesystem&quot;</code>): <code>&quot;&quot;</code>
> - **«encryption» область** (<code>&quot;encryption_scope&quot;</code>): <code>&quot;PUBLIC_OPEN_PRIVATE_SEPARATE&quot;</code>
> - **«write» «protection»** (<code>&quot;write_protection&quot;</code>): <code>&quot;&quot;</code>
> - **«geographic» риск класс** (<code>&quot;geographic_risk_class&quot;</code>): <code>&quot;&quot;</code>
> - **«custodian» роль ID** (<code>&quot;custodian_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» «custodian» роль ID** (<code>&quot;successor_custodian_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **«sync» метод** (<code>&quot;sync_method&quot;</code>): <code>&quot;&quot;</code>
> - **«fixity» «schedule»** (<code>&quot;fixity_schedule&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Восстановление «schedule»** (<code>&quot;restore_schedule&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Плановый носитель «retirement» время** (<code>&quot;planned_media_retirement_at&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «bytes»** (<code>&quot;capacity_bytes&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический «bytes»** (<code>&quot;actual_bytes&quot;</code>): <code>&quot;&quot;</code>
> - **«last» подтверждённый время** (<code>&quot;last_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **План состояние** (<code>&quot;plan_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Одна строка не закрывает правило 4-3-2-1-1-0&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
