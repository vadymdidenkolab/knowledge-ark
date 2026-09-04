---
id: "DATA-REGISTER-a4cbc725cb3ad058"
type: "generated-data-register-view"
title: "Движение и передача ресурсов — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "resource-transaction-log-template.csv"
source_sha256: "21673395f3bd51dc5702914c901fa98d020e7919c8304c4a39f51d247b8ff1ca"
source_bytes: 749
source_row_count: 2
source_column_count: 17
source_cell_count: 34
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: resource-transaction-log-template.csv -->

# Движение и передача ресурсов — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 2
- **Полей в каждой записи:** 17
- **Ячеек данных, включая пустые:** 34
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `21673395f3bd51dc5702914c901fa98d020e7919c8304c4a39f51d247b8ff1ca`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «event» ID | <code>&quot;event_id&quot;</code> |
| 2 | Операция ID | <code>&quot;transaction_id&quot;</code> |
| 3 | «timestamp» «utc» | <code>&quot;timestamp_utc&quot;</code> |
| 4 | Ресурс ID | <code>&quot;resource_id&quot;</code> |
| 5 | Операция тип | <code>&quot;transaction_type&quot;</code> |
| 6 | Количество | <code>&quot;quantity&quot;</code> |
| 7 | Единица | <code>&quot;unit&quot;</code> |
| 8 | Из место | <code>&quot;from_location&quot;</code> |
| 9 | В место | <code>&quot;to_location&quot;</code> |
| 10 | «assigned» человек «or» «subgroup» | <code>&quot;assigned_person_or_subgroup&quot;</code> |
| 11 | Утверждённый кем человек ID | <code>&quot;approved_by_person_id&quot;</code> |
| 12 | «balance» «after» | <code>&quot;balance_after&quot;</code> |
| 13 | «balance» доказательство метод | <code>&quot;balance_evidence_method&quot;</code> |
| 14 | «contamination» «or» «damage» состояние | <code>&quot;contamination_or_damage_state&quot;</code> |
| 15 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 16 | «created» кем | <code>&quot;created_by&quot;</code> |
| 17 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:17 -->
> [!abstract]- Запись 1 из 2 — EVT-YYYYMMDD-001
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Операция ID** (<code>&quot;transaction_id&quot;</code>): <code>&quot;RTX-0001&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-WAT-STORED&quot;</code>
> - **Операция тип** (<code>&quot;transaction_type&quot;</code>): <code>&quot;COUNT_BASELINE&quot;</code>
> - **Количество** (<code>&quot;quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;L&quot;</code>
> - **Из место** (<code>&quot;from_location&quot;</code>): <code>&quot;TBD&quot;</code>
> - **В место** (<code>&quot;to_location&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«assigned» человек «or» «subgroup»** (<code>&quot;assigned_person_or_subgroup&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **Утверждённый кем человек ID** (<code>&quot;approved_by_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«balance» «after»** (<code>&quot;balance_after&quot;</code>): <code>&quot;&quot;</code>
> - **«balance» доказательство метод** (<code>&quot;balance_evidence_method&quot;</code>): <code>&quot;NOT_COUNTED&quot;</code>
> - **«contamination» «or» «damage» состояние** (<code>&quot;contamination_or_damage_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон; не фактический остаток&quot;</code>
>

<!-- record:2 cells:17 -->
> [!abstract]- Запись 2 из 2 — EVT-YYYYMMDD-001
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Операция ID** (<code>&quot;transaction_id&quot;</code>): <code>&quot;RTX-0002&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс ID** (<code>&quot;resource_id&quot;</code>): <code>&quot;RES-MED-PERSONAL&quot;</code>
> - **Операция тип** (<code>&quot;transaction_type&quot;</code>): <code>&quot;ASSIGN_PERSONAL&quot;</code>
> - **Количество** (<code>&quot;quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;PERSON_PLAN&quot;</code>
> - **Из место** (<code>&quot;from_location&quot;</code>): <code>&quot;TBD&quot;</code>
> - **В место** (<code>&quot;to_location&quot;</code>): <code>&quot;ON_PERSON&quot;</code>
> - **«assigned» человек «or» «subgroup»** (<code>&quot;assigned_person_or_subgroup&quot;</code>): <code>&quot;P01&quot;</code>
> - **Утверждённый кем человек ID** (<code>&quot;approved_by_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«balance» «after»** (<code>&quot;balance_after&quot;</code>): <code>&quot;&quot;</code>
> - **«balance» доказательство метод** (<code>&quot;balance_evidence_method&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«contamination» «or» «damage» состояние** (<code>&quot;contamination_or_damage_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Индивидуальные лекарства не становятся общим пулом&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
