---
id: "DATA-REGISTER-7027480db7d84540"
type: "generated-data-register-view"
title: "Реестр карточек действий — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "action-card-register-template.csv"
source_sha256: "5310390c765ff5ef3ae563abd11652629fbec22c8b63e759bdeaa2431f4d6474"
source_bytes: 824
source_row_count: 1
source_column_count: 27
source_cell_count: 27
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: action-card-register-template.csv -->

# Реестр карточек действий — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 1
- **Полей в каждой записи:** 27
- **Ячеек данных, включая пустые:** 27
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `5310390c765ff5ef3ae563abd11652629fbec22c8b63e759bdeaa2431f4d6474`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «card» ID | <code>&quot;card_id&quot;</code> |
| 2 | Сценарий ID | <code>&quot;scenario_id&quot;</code> |
| 3 | Название на русском | <code>&quot;title_ru&quot;</code> |
| 4 | «card» версия | <code>&quot;card_version&quot;</code> |
| 5 | Юрисдикция | <code>&quot;jurisdiction&quot;</code> |
| 6 | Язык | <code>&quot;language&quot;</code> |
| 7 | «audience» «layer» | <code>&quot;audience_layer&quot;</code> |
| 8 | «content» статус | <code>&quot;content_status&quot;</code> |
| 9 | «content» файл ссылка | <code>&quot;content_file_ref&quot;</code> |
| 10 | Идентификаторы источников | <code>&quot;source_ids&quot;</code> |
| 11 | Источник «section» ссылки | <code>&quot;source_section_refs&quot;</code> |
| 12 | Источник снимок «hashes» | <code>&quot;source_snapshot_hashes&quot;</code> |
| 13 | Профессиональный проверка запись ссылки | <code>&quot;professional_review_record_refs&quot;</code> |
| 14 | «translation» проверка запись ссылка | <code>&quot;translation_review_record_ref&quot;</code> |
| 15 | Роль допуск правило ссылка | <code>&quot;role_gate_policy_ref&quot;</code> |
| 16 | Требуемый допуск снимок «schema» | <code>&quot;required_gate_snapshot_schema&quot;</code> |
| 17 | Утверждённый кем | <code>&quot;approved_by&quot;</code> |
| 18 | Утверждённый время | <code>&quot;approved_at&quot;</code> |
| 19 | «effective» из | <code>&quot;effective_from&quot;</code> |
| 20 | «valid» до | <code>&quot;valid_until&quot;</code> |
| 21 | «supersedes» «card» ID | <code>&quot;supersedes_card_id&quot;</code> |
| 22 | Выпуск состояние | <code>&quot;release_state&quot;</code> |
| 23 | «revoked» время | <code>&quot;revoked_at&quot;</code> |
| 24 | Владелец | <code>&quot;owner&quot;</code> |
| 25 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |
| 27 | «content» SHA-256 | <code>&quot;content_sha256&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:27 -->
> [!abstract]- Запись 1 из 1 — TBD — Шаблон будущей карточки
> - **«card» ID** (<code>&quot;card_id&quot;</code>): <code>&quot;CARD-EXAMPLE-001&quot;</code>
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Название на русском** (<code>&quot;title_ru&quot;</code>): <code>&quot;Шаблон будущей карточки&quot;</code>
> - **«card» версия** (<code>&quot;card_version&quot;</code>): <code>&quot;0.0-DRAFT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Язык** (<code>&quot;language&quot;</code>): <code>&quot;RU&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«content» статус** (<code>&quot;content_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **«content» файл ссылка** (<code>&quot;content_file_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник снимок «hashes»** (<code>&quot;source_snapshot_hashes&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Профессиональный проверка запись ссылки** (<code>&quot;professional_review_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«translation» проверка запись ссылка** (<code>&quot;translation_review_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск правило ссылка** (<code>&quot;role_gate_policy_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Требуемый допуск снимок «schema»** (<code>&quot;required_gate_snapshot_schema&quot;</code>): <code>&quot;card-gate-snapshot-template.csv&quot;</code>
> - **Утверждённый кем** (<code>&quot;approved_by&quot;</code>): <code>&quot;&quot;</code>
> - **Утверждённый время** (<code>&quot;approved_at&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до** (<code>&quot;valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes» «card» ID** (<code>&quot;supersedes_card_id&quot;</code>): <code>&quot;&quot;</code>
> - **Выпуск состояние** (<code>&quot;release_state&quot;</code>): <code>&quot;NOT_RELEASED&quot;</code>
> - **«revoked» время** (<code>&quot;revoked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;ID примера не разрешает действие и не считается выпущенной карточкой&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
