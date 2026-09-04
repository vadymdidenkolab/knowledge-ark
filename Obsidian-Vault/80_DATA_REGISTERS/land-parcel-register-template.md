---
id: "DATA-REGISTER-70f16daf93b0445a"
type: "generated-data-register-view"
title: "Земельные участки — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "land-parcel-register-template.csv"
source_sha256: "be0cdd4b8798b9cac3ca69457a5f61d60476b09988bc00ee4d1b141f42e9aebc"
source_bytes: 877
source_row_count: 1
source_column_count: 32
source_cell_count: 32
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: land-parcel-register-template.csv -->

# Земельные участки — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 1
- **Полей в каждой записи:** 32
- **Ячеек данных, включая пустые:** 32
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `be0cdd4b8798b9cac3ca69457a5f61d60476b09988bc00ee4d1b141f42e9aebc`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «parcel» ID | <code>&quot;parcel_id&quot;</code> |
| 2 | Объект ID | <code>&quot;site_id&quot;</code> |
| 3 | «country» | <code>&quot;country&quot;</code> |
| 4 | «municipality» | <code>&quot;municipality&quot;</code> |
| 5 | «cadastral» ссылка | <code>&quot;cadastral_reference&quot;</code> |
| 6 | «land» «registry» ссылка | <code>&quot;land_registry_reference&quot;</code> |
| 7 | «geometry» ссылка | <code>&quot;geometry_ref&quot;</code> |
| 8 | «geometry» SHA-256 | <code>&quot;geometry_sha256&quot;</code> |
| 9 | Граница подтверждение состояние | <code>&quot;boundary_verification_state&quot;</code> |
| 10 | Название «or» «tenure» тип | <code>&quot;title_or_tenure_type&quot;</code> |
| 11 | «registered» «holder» ссылка | <code>&quot;registered_holder_ref&quot;</code> |
| 12 | «ownership» «share» | <code>&quot;ownership_share&quot;</code> |
| 13 | «acquisition» «basis» | <code>&quot;acquisition_basis&quot;</code> |
| 14 | «encumbrance» ссылки | <code>&quot;encumbrance_refs&quot;</code> |
| 15 | «easement» ссылки | <code>&quot;easement_refs&quot;</code> |
| 16 | «right» «of» «way» ссылки | <code>&quot;right_of_way_refs&quot;</code> |
| 17 | «zoning» класс | <code>&quot;zoning_class&quot;</code> |
| 18 | «permitted» «use» | <code>&quot;permitted_use&quot;</code> |
| 19 | Запрещённый «use» | <code>&quot;prohibited_use&quot;</code> |
| 20 | «protected» «area» «constraints» | <code>&quot;protected_area_constraints&quot;</code> |
| 21 | «building» «constraints» | <code>&quot;building_constraints&quot;</code> |
| 22 | Вода «right» ID | <code>&quot;water_right_ids&quot;</code> |
| 23 | «tax» «and» «fee» «obligations» | <code>&quot;tax_and_fee_obligations&quot;</code> |
| 24 | «insurance» ссылка | <code>&quot;insurance_ref&quot;</code> |
| 25 | Название «checked» кем | <code>&quot;title_checked_by&quot;</code> |
| 26 | Название «checked» время | <code>&quot;title_checked_at&quot;</code> |
| 27 | Правовой проверка срок | <code>&quot;legal_review_due&quot;</code> |
| 28 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 29 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |
| 30 | «tenure» допуск состояние | <code>&quot;tenure_gate_state&quot;</code> |
| 31 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 32 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:32 -->
> [!abstract]- Запись 1 из 1 — SITE-TBD
> - **«parcel» ID** (<code>&quot;parcel_id&quot;</code>): <code>&quot;PARCEL-EXAMPLE-001&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;SITE-TBD&quot;</code>
> - **«country»** (<code>&quot;country&quot;</code>): <code>&quot;PT&quot;</code>
> - **«municipality»** (<code>&quot;municipality&quot;</code>): <code>&quot;&quot;</code>
> - **«cadastral» ссылка** (<code>&quot;cadastral_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«land» «registry» ссылка** (<code>&quot;land_registry_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» ссылка** (<code>&quot;geometry_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Граница подтверждение состояние** (<code>&quot;boundary_verification_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Название «or» «tenure» тип** (<code>&quot;title_or_tenure_type&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«registered» «holder» ссылка** (<code>&quot;registered_holder_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ownership» «share»** (<code>&quot;ownership_share&quot;</code>): <code>&quot;&quot;</code>
> - **«acquisition» «basis»** (<code>&quot;acquisition_basis&quot;</code>): <code>&quot;&quot;</code>
> - **«encumbrance» ссылки** (<code>&quot;encumbrance_refs&quot;</code>): <code>&quot;&quot;</code>
> - **«easement» ссылки** (<code>&quot;easement_refs&quot;</code>): <code>&quot;&quot;</code>
> - **«right» «of» «way» ссылки** (<code>&quot;right_of_way_refs&quot;</code>): <code>&quot;&quot;</code>
> - **«zoning» класс** (<code>&quot;zoning_class&quot;</code>): <code>&quot;&quot;</code>
> - **«permitted» «use»** (<code>&quot;permitted_use&quot;</code>): <code>&quot;&quot;</code>
> - **Запрещённый «use»** (<code>&quot;prohibited_use&quot;</code>): <code>&quot;&quot;</code>
> - **«protected» «area» «constraints»** (<code>&quot;protected_area_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«building» «constraints»** (<code>&quot;building_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **Вода «right» ID** (<code>&quot;water_right_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«tax» «and» «fee» «obligations»** (<code>&quot;tax_and_fee_obligations&quot;</code>): <code>&quot;&quot;</code>
> - **«insurance» ссылка** (<code>&quot;insurance_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Название «checked» кем** (<code>&quot;title_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Название «checked» время** (<code>&quot;title_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Правовой проверка срок** (<code>&quot;legal_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;STRICTLY_RESTRICTED&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«tenure» допуск состояние** (<code>&quot;tenure_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не содержит реальных адресов; ownership не доказывает water rights&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
