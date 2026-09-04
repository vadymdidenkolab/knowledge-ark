---
id: "DATA-REGISTER-c5a77f32ee2a9ed3"
type: "generated-data-register-view"
title: "Соответствие прежних и текущих сценариев"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "legacy-scenario-map.csv"
source_sha256: "edd01b3c8f2ec6b3f9e690df2bbcd370359d0c053b30f9bbbcf3ecf08e50b513"
source_bytes: 2997
source_row_count: 25
source_column_count: 5
source_cell_count: 125
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: legacy-scenario-map.csv -->

# Соответствие прежних и текущих сценариев

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 25
- **Полей в каждой записи:** 5
- **Ячеек данных, включая пустые:** 125
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `edd01b3c8f2ec6b3f9e690df2bbcd370359d0c053b30f9bbbcf3ecf08e50b513`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Прежний ID | <code>&quot;legacy_id&quot;</code> |
| 2 | Прежний статус | <code>&quot;legacy_status&quot;</code> |
| 3 | Канонический сценарий ID | <code>&quot;canonical_scenario_ids&quot;</code> |
| 4 | Миграция тип | <code>&quot;migration_type&quot;</code> |
| 5 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:5 -->
> [!abstract]- Запись 1 из 25 — MED-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;MED-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;MED-ARREST&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:2 cells:5 -->
> [!abstract]- Запись 2 из 25 — MED-02
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;MED-02&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;MED-BLEED|MED-TRAUMA&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Выбрать по trigger и первой развилке&quot;</code>
>

<!-- record:3 cells:5 -->
> [!abstract]- Запись 3 из 25 — MED-03
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;MED-03&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;MED-AIRWAY|MED-ANAPH|MED-POISON|MED-OVERDOSE&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не взаимозаменяемые карточки&quot;</code>
>

<!-- record:4 cells:5 -->
> [!abstract]- Запись 4 из 25 — MED-04
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;MED-04&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;MED-BURN|NAT-HEAT|NAT-COLD&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Термическое воздействие и средовая угроза разделены&quot;</code>
>

<!-- record:5 cells:5 -->
> [!abstract]- Запись 5 из 25 — FIR-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;FIR-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;TEC-FIRE|TEC-CO&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:6 cells:5 -->
> [!abstract]- Запись 6 из 25 — GAS-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;GAS-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;TEC-GAS&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:7 cells:5 -->
> [!abstract]- Запись 7 из 25 — EQ-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;EQ-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;NAT-EQ&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:8 cells:5 -->
> [!abstract]- Запись 8 из 25 — TSU-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;TSU-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;NAT-TSU&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:9 cells:5 -->
> [!abstract]- Запись 9 из 25 — WIL-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;WIL-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;NAT-WIL|NAT-SMOKE&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Активный пожар и воздействие дыма различаются&quot;</code>
>

<!-- record:10 cells:5 -->
> [!abstract]- Запись 10 из 25 — FLD-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;FLD-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;NAT-FLD|NAT-FLASH&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Медленное и внезапное затопление имеют разные первые решения&quot;</code>
>

<!-- record:11 cells:5 -->
> [!abstract]- Запись 11 из 25 — WX-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;WX-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;NAT-STORM|NAT-HEAT|NAT-COLD&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:12 cells:5 -->
> [!abstract]- Запись 12 из 25 — POW-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;POW-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;INF-POWER&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:13 cells:5 -->
> [!abstract]- Запись 13 из 25 — WAT-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;WAT-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;INF-WATER-OFF|INF-WATER-CONTAM&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Отсутствие и загрязнение воды различаются&quot;</code>
>

<!-- record:14 cells:5 -->
> [!abstract]- Запись 14 из 25 — FOOD-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;FOOD-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;INF-SUPPLY|BIO-FOOD&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Дефицит и пищевое отравление различаются&quot;</code>
>

<!-- record:15 cells:5 -->
> [!abstract]- Запись 15 из 25 — TEL-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;TEL-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;INF-TEL|INF-INTERNET&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:16 cells:5 -->
> [!abstract]- Запись 16 из 25 — CYB-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;CYB-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;CYB-DEVICE|CYB-ACCOUNT|CYB-MALWARE|CYB-DATA&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:17 cells:5 -->
> [!abstract]- Запись 17 из 25 — DOC-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;DOC-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;SOC-DOC&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:18 cells:5 -->
> [!abstract]- Запись 18 из 25 — EPI-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;EPI-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;BIO-RESP&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;PARTIAL_ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Другие типы вспышек имеют отдельные BIO scenarios&quot;</code>
>

<!-- record:19 cells:5 -->
> [!abstract]- Запись 19 из 25 — CHM-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;CHM-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;TEC-CHEM-LOCAL|TEC-CHEM-PLUME|TEC-HAZMAT-TRANSPORT&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Локальная экспозиция и внешнее облако требуют разных решений&quot;</code>
>

<!-- record:20 cells:5 -->
> [!abstract]- Запись 20 из 25 — RAD-FALLOUT
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;RAD-FALLOUT&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;TEC-RAD-FALLOUT&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:21 cells:5 -->
> [!abstract]- Запись 21 из 25 — RAD-SOURCE
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;RAD-SOURCE&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;TEC-RAD-SOURCE&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;ALIAS&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:22 cells:5 -->
> [!abstract]- Запись 22 из 25 — DIS-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;DIS-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|INF-HOUSING&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:23 cells:5 -->
> [!abstract]- Запись 23 из 25 — FIN-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;FIN-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;INF-PAY|SOC-INCOME&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Платёжный отказ и потеря дохода различаются&quot;</code>
>

<!-- record:24 cells:5 -->
> [!abstract]- Запись 24 из 25 — CIV-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;CIV-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;SEC-CROWD|SEC-CRIME|SEC-MASS-VIOLENCE&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;SPLIT&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:25 cells:5 -->
> [!abstract]- Запись 25 из 25 — LON-01
> - **Прежний ID** (<code>&quot;legacy_id&quot;</code>): <code>&quot;LON-01&quot;</code>
> - **Прежний статус** (<code>&quot;legacy_status&quot;</code>): <code>&quot;DO_NOT_USE_FOR_NEW_CARD&quot;</code>
> - **Канонический сценарий ID** (<code>&quot;canonical_scenario_ids&quot;</code>): <code>&quot;ENV-RESOURCE|ENV-KNOWLEDGE|ENV-CLIMATE|INF-SUPPLY|GEN-SUCCESSION-FAIL|GEN-SKILL-LINE-BREAK|GEN-TECHNOLOGY-UNREADABLE&quot;</code>
> - **Миграция тип** (<code>&quot;migration_type&quot;</code>): <code>&quot;DECOMPOSE_AND_USE_HORIZON&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Legacy E2–E4 сохраняется; E5 добавляется только через отдельные GEN/continuity records и не означает один столетний инцидент&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
