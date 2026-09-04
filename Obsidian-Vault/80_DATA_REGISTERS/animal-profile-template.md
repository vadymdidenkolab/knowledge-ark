---
id: "DATA-REGISTER-a172079fa2cdc20a"
type: "generated-data-register-view"
title: "Профиль животного — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "animal-profile-template.csv"
source_sha256: "7394142d2ea92506e70235e7d6ee90e74a65603a6e1ebbcfef76325af0bb5186"
source_bytes: 967
source_row_count: 1
source_column_count: 25
source_cell_count: 25
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: animal-profile-template.csv -->

# Профиль животного — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 1
- **Полей в каждой записи:** 25
- **Ячеек данных, включая пустые:** 25
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `7394142d2ea92506e70235e7d6ee90e74a65603a6e1ebbcfef76325af0bb5186`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Животное ID | <code>&quot;animal_id&quot;</code> |
| 2 | «display» «alias» | <code>&quot;display_alias&quot;</code> |
| 3 | «species» | <code>&quot;species&quot;</code> |
| 4 | Количество | <code>&quot;count&quot;</code> |
| 5 | Сервис животное состояние | <code>&quot;service_animal_state&quot;</code> |
| 6 | Основной «handler» человек ID | <code>&quot;primary_handler_person_id&quot;</code> |
| 7 | Резервный «handler» человек ID | <code>&quot;backup_handler_person_id&quot;</code> |
| 8 | «veterinary» профиль ссылка | <code>&quot;veterinary_profile_ref&quot;</code> |
| 9 | «medication» ссылка | <code>&quot;medication_ref&quot;</code> |
| 10 | Пища ресурс ссылка | <code>&quot;food_resource_ref&quot;</code> |
| 11 | Вода профиль ссылка | <code>&quot;water_profile_ref&quot;</code> |
| 12 | «carrier» «or» «restraint» ссылка | <code>&quot;carrier_or_restraint_ref&quot;</code> |
| 13 | «documents» ссылка | <code>&quot;documents_ref&quot;</code> |
| 14 | «shelter» «constraints» | <code>&quot;shelter_constraints&quot;</code> |
| 15 | «transport» «constraints» | <code>&quot;transport_constraints&quot;</code> |
| 16 | «separation» «prohibition» | <code>&quot;separation_prohibition&quot;</code> |
| 17 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 18 | Профиль статус | <code>&quot;profile_status&quot;</code> |
| 19 | Владелец | <code>&quot;owner&quot;</code> |
| 20 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 21 | Примечания | <code>&quot;notes&quot;</code> |
| 22 | Группа профиль область | <code>&quot;group_profile_scope&quot;</code> |
| 23 | Основной «handler» приёмка состояние | <code>&quot;primary_handler_acceptance_state&quot;</code> |
| 24 | Резервный «handler» приёмка состояние | <code>&quot;backup_handler_acceptance_state&quot;</code> |
| 25 | «handler» «activation» допуск состояние | <code>&quot;handler_activation_gate_state&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:25 -->
> [!abstract]- Запись 1 из 1 — ANIMAL-001
> - **Животное ID** (<code>&quot;animal_id&quot;</code>): <code>&quot;ANIMAL-001&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;PET-ALIAS-01&quot;</code>
> - **«species»** (<code>&quot;species&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Количество** (<code>&quot;count&quot;</code>): <code>&quot;1&quot;</code>
> - **Сервис животное состояние** (<code>&quot;service_animal_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Основной «handler» человек ID** (<code>&quot;primary_handler_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный «handler» человек ID** (<code>&quot;backup_handler_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«veterinary» профиль ссылка** (<code>&quot;veterinary_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«medication» ссылка** (<code>&quot;medication_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Пища ресурс ссылка** (<code>&quot;food_resource_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Вода профиль ссылка** (<code>&quot;water_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«carrier» «or» «restraint» ссылка** (<code>&quot;carrier_or_restraint_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«documents» ссылка** (<code>&quot;documents_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«shelter» «constraints»** (<code>&quot;shelter_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«separation» «prohibition»** (<code>&quot;separation_prohibition&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Профиль статус** (<code>&quot;profile_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Животное не увеличивает human N; P01 существует во всех заявленных профилях, но handler не активен без принятия роли и проверки ресурсов&quot;</code>
> - **Группа профиль область** (<code>&quot;group_profile_scope&quot;</code>): <code>&quot;GP-N1|GP-N2|GP-N3|GP-N4|GP-N5|GP-N6|GP-N7&quot;</code>
> - **Основной «handler» приёмка состояние** (<code>&quot;primary_handler_acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Резервный «handler» приёмка состояние** (<code>&quot;backup_handler_acceptance_state&quot;</code>): <code>&quot;NOT_ASSIGNED&quot;</code>
> - **«handler» «activation» допуск состояние** (<code>&quot;handler_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
