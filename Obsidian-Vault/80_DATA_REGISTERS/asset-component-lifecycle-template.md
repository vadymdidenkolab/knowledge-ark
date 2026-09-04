---
id: "DATA-REGISTER-b59d71618051fae1"
type: "generated-data-register-view"
title: "Жизненный цикл имущества и компонентов — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "asset-component-lifecycle-template.csv"
source_sha256: "071bcddf5abc20b6ed44233482a20dd695ff0da572a652313d5a8bc04ab42295"
source_bytes: 1064
source_row_count: 1
source_column_count: 38
source_cell_count: 38
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: asset-component-lifecycle-template.csv -->

# Жизненный цикл имущества и компонентов — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 1
- **Полей в каждой записи:** 38
- **Ячеек данных, включая пустые:** 38
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `071bcddf5abc20b6ed44233482a20dd695ff0da572a652313d5a8bc04ab42295`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Компонент ID | <code>&quot;component_id&quot;</code> |
| 2 | «system» ID | <code>&quot;system_id&quot;</code> |
| 3 | Возможность ID | <code>&quot;capability_ids&quot;</code> |
| 4 | «manufacturer» | <code>&quot;manufacturer&quot;</code> |
| 5 | «model» | <code>&quot;model&quot;</code> |
| 6 | «serial» «or» «batch» | <code>&quot;serial_or_batch&quot;</code> |
| 7 | «specification» | <code>&quot;specification&quot;</code> |
| 8 | «material» «composition» ссылка | <code>&quot;material_composition_ref&quot;</code> |
| 9 | «criticality» класс | <code>&quot;criticality_class&quot;</code> |
| 10 | «installation» время | <code>&quot;installation_at&quot;</code> |
| 11 | «observed» сервис часы | <code>&quot;observed_service_hours&quot;</code> |
| 12 | «manufacturer» сервис «life» «range» | <code>&quot;manufacturer_service_life_range&quot;</code> |
| 13 | Условие состояние | <code>&quot;condition_state&quot;</code> |
| 14 | «inspection» метод | <code>&quot;inspection_method&quot;</code> |
| 15 | «last» «inspected» время | <code>&quot;last_inspected_at&quot;</code> |
| 16 | Отказ «modes» | <code>&quot;failure_modes&quot;</code> |
| 17 | Опасность «classes» | <code>&quot;hazard_classes&quot;</code> |
| 18 | «isolation» «procedure» ссылка | <code>&quot;isolation_procedure_ref&quot;</code> |
| 19 | «repairability» класс | <code>&quot;repairability_class&quot;</code> |
| 20 | «disassembly» «instruction» ссылка | <code>&quot;disassembly_instruction_ref&quot;</code> |
| 21 | «bill» «of» материалы ссылка | <code>&quot;bill_of_materials_ref&quot;</code> |
| 22 | «drawing» «or» «schematic» ссылка | <code>&quot;drawing_or_schematic_ref&quot;</code> |
| 23 | «firmware» «or» «software» ссылка | <code>&quot;firmware_or_software_ref&quot;</code> |
| 24 | Требуемый инструмент ID | <code>&quot;required_tool_ids&quot;</code> |
| 25 | Требуемый навык ID | <code>&quot;required_skill_ids&quot;</code> |
| 26 | «spare» «part» ID | <code>&quot;spare_part_ids&quot;</code> |
| 27 | «consumable» ID | <code>&quot;consumable_ids&quot;</code> |
| 28 | «compatible» «substitute» ID | <code>&quot;compatible_substitute_ids&quot;</code> |
| 29 | Замена источник ID | <code>&quot;replacement_source_ids&quot;</code> |
| 30 | Локальный «fabrication» область | <code>&quot;local_fabrication_scope&quot;</code> |
| 31 | Запрещённый локальный «fabrication» область | <code>&quot;prohibited_local_fabrication_scope&quot;</code> |
| 32 | «salvage» «or» «recycling» маршрут | <code>&quot;salvage_or_recycling_route&quot;</code> |
| 33 | Замена «funding» ссылка | <code>&quot;replacement_funding_ref&quot;</code> |
| 34 | Следующий сервис срок | <code>&quot;next_service_due&quot;</code> |
| 35 | «successor» «custodian» роль ID | <code>&quot;successor_custodian_role_id&quot;</code> |
| 36 | Жизненный цикл состояние | <code>&quot;lifecycle_state&quot;</code> |
| 37 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 38 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:38 -->
> [!abstract]- Запись 1 из 1 — COMP-EXAMPLE-001
> - **Компонент ID** (<code>&quot;component_id&quot;</code>): <code>&quot;COMP-EXAMPLE-001&quot;</code>
> - **«system» ID** (<code>&quot;system_id&quot;</code>): <code>&quot;SYSTEM-TBD&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«manufacturer»** (<code>&quot;manufacturer&quot;</code>): <code>&quot;&quot;</code>
> - **«model»** (<code>&quot;model&quot;</code>): <code>&quot;&quot;</code>
> - **«serial» «or» «batch»** (<code>&quot;serial_or_batch&quot;</code>): <code>&quot;&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;&quot;</code>
> - **«material» «composition» ссылка** (<code>&quot;material_composition_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«criticality» класс** (<code>&quot;criticality_class&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«installation» время** (<code>&quot;installation_at&quot;</code>): <code>&quot;&quot;</code>
> - **«observed» сервис часы** (<code>&quot;observed_service_hours&quot;</code>): <code>&quot;&quot;</code>
> - **«manufacturer» сервис «life» «range»** (<code>&quot;manufacturer_service_life_range&quot;</code>): <code>&quot;&quot;</code>
> - **Условие состояние** (<code>&quot;condition_state&quot;</code>): <code>&quot;NOT_INSPECTED&quot;</code>
> - **«inspection» метод** (<code>&quot;inspection_method&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «inspected» время** (<code>&quot;last_inspected_at&quot;</code>): <code>&quot;&quot;</code>
> - **Отказ «modes»** (<code>&quot;failure_modes&quot;</code>): <code>&quot;&quot;</code>
> - **Опасность «classes»** (<code>&quot;hazard_classes&quot;</code>): <code>&quot;&quot;</code>
> - **«isolation» «procedure» ссылка** (<code>&quot;isolation_procedure_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«repairability» класс** (<code>&quot;repairability_class&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **«disassembly» «instruction» ссылка** (<code>&quot;disassembly_instruction_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«bill» «of» материалы ссылка** (<code>&quot;bill_of_materials_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«drawing» «or» «schematic» ссылка** (<code>&quot;drawing_or_schematic_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«firmware» «or» «software» ссылка** (<code>&quot;firmware_or_software_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Требуемый инструмент ID** (<code>&quot;required_tool_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Требуемый навык ID** (<code>&quot;required_skill_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«spare» «part» ID** (<code>&quot;spare_part_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«consumable» ID** (<code>&quot;consumable_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«compatible» «substitute» ID** (<code>&quot;compatible_substitute_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Замена источник ID** (<code>&quot;replacement_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный «fabrication» область** (<code>&quot;local_fabrication_scope&quot;</code>): <code>&quot;&quot;</code>
> - **Запрещённый локальный «fabrication» область** (<code>&quot;prohibited_local_fabrication_scope&quot;</code>): <code>&quot;&quot;</code>
> - **«salvage» «or» «recycling» маршрут** (<code>&quot;salvage_or_recycling_route&quot;</code>): <code>&quot;&quot;</code>
> - **Замена «funding» ссылка** (<code>&quot;replacement_funding_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий сервис срок** (<code>&quot;next_service_due&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» «custodian» роль ID** (<code>&quot;successor_custodian_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;E5 не доказывает срок службы экземпляра&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
