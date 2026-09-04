---
id: "DATA-REGISTER-6436495698d0852e"
type: "generated-data-register-view"
title: "Снимок обеспечиваемой численности — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "population-capacity-snapshot-template.csv"
source_sha256: "a513d924b498bd8597bea181769577da07778cd4f27a901e1661e55e958a0e51"
source_bytes: 835
source_row_count: 1
source_column_count: 26
source_cell_count: 26
ignored_blank_row_count: 0
semantic_group: "CENTURY_CONTINUITY"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: population-capacity-snapshot-template.csv -->

# Снимок обеспечиваемой численности — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Преемственность и столетний горизонт
- **Записей:** 1
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 26
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `a513d924b498bd8597bea181769577da07778cd4f27a901e1661e55e958a0e51`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «population» снимок ID | <code>&quot;population_snapshot_id&quot;</code> |
| 2 | «institution» ID | <code>&quot;institution_id&quot;</code> |
| 3 | «captured» время | <code>&quot;captured_at&quot;</code> |
| 4 | «active» «cell» ID | <code>&quot;active_cell_ids&quot;</code> |
| 5 | «active» человек количество | <code>&quot;active_person_count&quot;</code> |
| 6 | «age» «band» «counts» | <code>&quot;age_band_counts&quot;</code> |
| 7 | «dependent» человек количество | <code>&quot;dependent_person_count&quot;</code> |
| 8 | Уход часы требуемый «per» «week» | <code>&quot;care_hours_required_per_week&quot;</code> |
| 9 | Уход часы доступный «per» «week» | <code>&quot;care_hours_available_per_week&quot;</code> |
| 10 | «critical» навык мощность ссылки | <code>&quot;critical_skill_capacity_refs&quot;</code> |
| 11 | «housing» мощность | <code>&quot;housing_capacity&quot;</code> |
| 12 | «safe» вода мощность | <code>&quot;safe_water_capacity&quot;</code> |
| 13 | Пища сервис мощность | <code>&quot;food_service_capacity&quot;</code> |
| 14 | «sanitation» мощность | <code>&quot;sanitation_capacity&quot;</code> |
| 15 | Здоровье «access» мощность | <code>&quot;health_access_capacity&quot;</code> |
| 16 | «education» мощность | <code>&quot;education_capacity&quot;</code> |
| 17 | «mobility» мощность | <code>&quot;mobility_capacity&quot;</code> |
| 18 | Миграция «assumptions» | <code>&quot;migration_assumptions&quot;</code> |
| 19 | Внешний «support» «assumptions» | <code>&quot;external_support_assumptions&quot;</code> |
| 20 | Сценарий горизонт | <code>&quot;scenario_horizon&quot;</code> |
| 21 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 22 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |
| 23 | «content» SHA-256 | <code>&quot;content_sha256&quot;</code> |
| 24 | Снимок состояние | <code>&quot;snapshot_state&quot;</code> |
| 25 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 1 — POPCAP-EXAMPLE-001
> - **«population» снимок ID** (<code>&quot;population_snapshot_id&quot;</code>): <code>&quot;POPCAP-EXAMPLE-001&quot;</code>
> - **«institution» ID** (<code>&quot;institution_id&quot;</code>): <code>&quot;INST-EXAMPLE-001&quot;</code>
> - **«captured» время** (<code>&quot;captured_at&quot;</code>): <code>&quot;&quot;</code>
> - **«active» «cell» ID** (<code>&quot;active_cell_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«active» человек количество** (<code>&quot;active_person_count&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«age» «band» «counts»** (<code>&quot;age_band_counts&quot;</code>): <code>&quot;&quot;</code>
> - **«dependent» человек количество** (<code>&quot;dependent_person_count&quot;</code>): <code>&quot;&quot;</code>
> - **Уход часы требуемый «per» «week»** (<code>&quot;care_hours_required_per_week&quot;</code>): <code>&quot;&quot;</code>
> - **Уход часы доступный «per» «week»** (<code>&quot;care_hours_available_per_week&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» навык мощность ссылки** (<code>&quot;critical_skill_capacity_refs&quot;</code>): <code>&quot;&quot;</code>
> - **«housing» мощность** (<code>&quot;housing_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **«safe» вода мощность** (<code>&quot;safe_water_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **Пища сервис мощность** (<code>&quot;food_service_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **«sanitation» мощность** (<code>&quot;sanitation_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **Здоровье «access» мощность** (<code>&quot;health_access_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **«education» мощность** (<code>&quot;education_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» мощность** (<code>&quot;mobility_capacity&quot;</code>): <code>&quot;&quot;</code>
> - **Миграция «assumptions»** (<code>&quot;migration_assumptions&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний «support» «assumptions»** (<code>&quot;external_support_assumptions&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий горизонт** (<code>&quot;scenario_horizon&quot;</code>): <code>&quot;E5&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;STRICTLY_RESTRICTED&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«content» SHA-256** (<code>&quot;content_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Снимок состояние** (<code>&quot;snapshot_state&quot;</code>): <code>&quot;DRAFT&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сценарии состава не являются квотами рождаемости или принуждением&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
