---
id: "DATA-REGISTER-9c15c4deb67c77a9"
type: "generated-data-register-view"
title: "Реестр архивных носителей — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "archive-media-register-template.csv"
source_sha256: "ab22f74953a9a40af600a83b904ce982cff478dc391f0f6dc56e68f6c33488f4"
source_bytes: 787
source_row_count: 1
source_column_count: 27
source_cell_count: 27
ignored_blank_row_count: 0
semantic_group: "OFFLINE_KNOWLEDGE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: archive-media-register-template.csv -->

# Реестр архивных носителей — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Источники, архив и офлайн-библиотека
- **Записей:** 1
- **Полей в каждой записи:** 27
- **Ячеек данных, включая пустые:** 27
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `ab22f74953a9a40af600a83b904ce982cff478dc391f0f6dc56e68f6c33488f4`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Носитель ID | <code>&quot;media_id&quot;</code> |
| 2 | «copy» план ID | <code>&quot;copy_plan_id&quot;</code> |
| 3 | «manufacturer» | <code>&quot;manufacturer&quot;</code> |
| 4 | «model» | <code>&quot;model&quot;</code> |
| 5 | «serial» «or» «batch» | <code>&quot;serial_or_batch&quot;</code> |
| 6 | Тип носителя | <code>&quot;media_type&quot;</code> |
| 7 | «interface» | <code>&quot;interface&quot;</code> |
| 8 | Мощность «bytes» | <code>&quot;capacity_bytes&quot;</code> |
| 9 | «acquired» время | <code>&quot;acquired_at&quot;</code> |
| 10 | «commissioned» время | <code>&quot;commissioned_at&quot;</code> |
| 11 | «warranty» до | <code>&quot;warranty_until&quot;</code> |
| 12 | «environment» место ссылка | <code>&quot;environment_location_ref&quot;</code> |
| 13 | «environmental» «monitor» ссылка | <code>&quot;environmental_monitor_ref&quot;</code> |
| 14 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 15 | «key» «escrow» ссылка | <code>&quot;key_escrow_ref&quot;</code> |
| 16 | «write» «protection» состояние | <code>&quot;write_protection_state&quot;</code> |
| 17 | «last» «full» «read» время | <code>&quot;last_full_read_at&quot;</code> |
| 18 | «last» «full» «read» результат | <code>&quot;last_full_read_result&quot;</code> |
| 19 | «smart» «or» здоровье ссылка | <code>&quot;smart_or_health_ref&quot;</code> |
| 20 | «uncorrected» «error» количество | <code>&quot;uncorrected_error_count&quot;</code> |
| 21 | Плановый «retirement» время | <code>&quot;planned_retirement_at&quot;</code> |
| 22 | Фактический «retirement» время | <code>&quot;actual_retirement_at&quot;</code> |
| 23 | «destruction» «or» «reuse» доказательство ссылка | <code>&quot;destruction_or_reuse_evidence_ref&quot;</code> |
| 24 | «custodian» роль ID | <code>&quot;custodian_role_id&quot;</code> |
| 25 | Носитель состояние | <code>&quot;media_state&quot;</code> |
| 26 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 27 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:27 -->
> [!abstract]- Запись 1 из 1 — MEDIA-EXAMPLE-001
> - **Носитель ID** (<code>&quot;media_id&quot;</code>): <code>&quot;MEDIA-EXAMPLE-001&quot;</code>
> - **«copy» план ID** (<code>&quot;copy_plan_id&quot;</code>): <code>&quot;COPYPLAN-EXAMPLE-001&quot;</code>
> - **«manufacturer»** (<code>&quot;manufacturer&quot;</code>): <code>&quot;&quot;</code>
> - **«model»** (<code>&quot;model&quot;</code>): <code>&quot;&quot;</code>
> - **«serial» «or» «batch»** (<code>&quot;serial_or_batch&quot;</code>): <code>&quot;&quot;</code>
> - **Тип носителя** (<code>&quot;media_type&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«interface»** (<code>&quot;interface&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «bytes»** (<code>&quot;capacity_bytes&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«acquired» время** (<code>&quot;acquired_at&quot;</code>): <code>&quot;&quot;</code>
> - **«commissioned» время** (<code>&quot;commissioned_at&quot;</code>): <code>&quot;&quot;</code>
> - **«warranty» до** (<code>&quot;warranty_until&quot;</code>): <code>&quot;&quot;</code>
> - **«environment» место ссылка** (<code>&quot;environment_location_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«environmental» «monitor» ссылка** (<code>&quot;environmental_monitor_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;TBD_BY_DATA_CLASS&quot;</code>
> - **«key» «escrow» ссылка** (<code>&quot;key_escrow_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«write» «protection» состояние** (<code>&quot;write_protection_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«last» «full» «read» время** (<code>&quot;last_full_read_at&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «full» «read» результат** (<code>&quot;last_full_read_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«smart» «or» здоровье ссылка** (<code>&quot;smart_or_health_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«uncorrected» «error» количество** (<code>&quot;uncorrected_error_count&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Плановый «retirement» время** (<code>&quot;planned_retirement_at&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический «retirement» время** (<code>&quot;actual_retirement_at&quot;</code>): <code>&quot;&quot;</code>
> - **«destruction» «or» «reuse» доказательство ссылка** (<code>&quot;destruction_or_reuse_evidence_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«custodian» роль ID** (<code>&quot;custodian_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **Носитель состояние** (<code>&quot;media_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Ни один носитель не считается столетним без миграции&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
