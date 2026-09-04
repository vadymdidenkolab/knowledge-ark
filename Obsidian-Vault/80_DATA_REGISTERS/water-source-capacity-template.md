---
id: "DATA-REGISTER-742c06d3c1571ba7"
type: "generated-data-register-view"
title: "Мощность источников воды — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "water-source-capacity-template.csv"
source_sha256: "943420edadc9cb9dc9c15d54969e3261beea17487950b5de937c5f35e3c8e591"
source_bytes: 954
source_row_count: 1
source_column_count: 30
source_cell_count: 30
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: water-source-capacity-template.csv -->

# Мощность источников воды — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 1
- **Полей в каждой записи:** 30
- **Ячеек данных, включая пустые:** 30
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `943420edadc9cb9dc9c15d54969e3261beea17487950b5de937c5f35e3c8e591`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Вода источник ID | <code>&quot;water_source_id&quot;</code> |
| 2 | Объект ID | <code>&quot;site_id&quot;</code> |
| 3 | Источник тип | <code>&quot;source_type&quot;</code> |
| 4 | «geometry» ссылка | <code>&quot;geometry_ref&quot;</code> |
| 5 | «ownership» «or» «access» «basis» | <code>&quot;ownership_or_access_basis&quot;</code> |
| 6 | «permit» «or» «entitlement» ссылка | <code>&quot;permit_or_entitlement_ref&quot;</code> |
| 7 | «permitted» «withdrawal» «limit» | <code>&quot;permitted_withdrawal_limit&quot;</code> |
| 8 | «measurement» единица | <code>&quot;measurement_unit&quot;</code> |
| 9 | «seasonal» «yield» «series» ссылка | <code>&quot;seasonal_yield_series_ref&quot;</code> |
| 10 | «historic» «drought» «series» ссылка | <code>&quot;historic_drought_series_ref&quot;</code> |
| 11 | «professionally» «assessed» «safe» «yield» | <code>&quot;professionally_assessed_safe_yield&quot;</code> |
| 12 | «safe» «yield» «assessment» ссылка | <code>&quot;safe_yield_assessment_ref&quot;</code> |
| 13 | «ecological» «flow» «constraint» | <code>&quot;ecological_flow_constraint&quot;</code> |
| 14 | Вода «quality» план ссылка | <code>&quot;water_quality_plan_ref&quot;</code> |
| 15 | «sample» «point» ID | <code>&quot;sample_point_ids&quot;</code> |
| 16 | «laboratory» ссылка | <code>&quot;laboratory_ref&quot;</code> |
| 17 | «latest» «quality» результат ссылка | <code>&quot;latest_quality_result_ref&quot;</code> |
| 18 | «treatment» «train» ID | <code>&quot;treatment_train_id&quot;</code> |
| 19 | «power» зависимость ID | <code>&quot;power_dependency_ids&quot;</code> |
| 20 | «spare» компонент ID | <code>&quot;spare_component_ids&quot;</code> |
| 21 | «alternate» источник ID | <code>&quot;alternate_source_ids&quot;</code> |
| 22 | «shared» отказ отрасль ID | <code>&quot;shared_failure_domain_ids&quot;</code> |
| 23 | «drought» триггер | <code>&quot;drought_trigger&quot;</code> |
| 24 | «contamination» «lockout» триггер | <code>&quot;contamination_lockout_trigger&quot;</code> |
| 25 | «last» «failover» испытание время | <code>&quot;last_failover_test_at&quot;</code> |
| 26 | Правовой допуск состояние | <code>&quot;legal_gate_state&quot;</code> |
| 27 | «quality» допуск состояние | <code>&quot;quality_gate_state&quot;</code> |
| 28 | Мощность допуск состояние | <code>&quot;capacity_gate_state&quot;</code> |
| 29 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 30 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:30 -->
> [!abstract]- Запись 1 из 1 — SITE-TBD
> - **Вода источник ID** (<code>&quot;water_source_id&quot;</code>): <code>&quot;WATSRC-EXAMPLE-001&quot;</code>
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;SITE-TBD&quot;</code>
> - **Источник тип** (<code>&quot;source_type&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«geometry» ссылка** (<code>&quot;geometry_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ownership» «or» «access» «basis»** (<code>&quot;ownership_or_access_basis&quot;</code>): <code>&quot;&quot;</code>
> - **«permit» «or» «entitlement» ссылка** (<code>&quot;permit_or_entitlement_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«permitted» «withdrawal» «limit»** (<code>&quot;permitted_withdrawal_limit&quot;</code>): <code>&quot;&quot;</code>
> - **«measurement» единица** (<code>&quot;measurement_unit&quot;</code>): <code>&quot;&quot;</code>
> - **«seasonal» «yield» «series» ссылка** (<code>&quot;seasonal_yield_series_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«historic» «drought» «series» ссылка** (<code>&quot;historic_drought_series_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«professionally» «assessed» «safe» «yield»** (<code>&quot;professionally_assessed_safe_yield&quot;</code>): <code>&quot;&quot;</code>
> - **«safe» «yield» «assessment» ссылка** (<code>&quot;safe_yield_assessment_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ecological» «flow» «constraint»** (<code>&quot;ecological_flow_constraint&quot;</code>): <code>&quot;&quot;</code>
> - **Вода «quality» план ссылка** (<code>&quot;water_quality_plan_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«sample» «point» ID** (<code>&quot;sample_point_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«laboratory» ссылка** (<code>&quot;laboratory_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«latest» «quality» результат ссылка** (<code>&quot;latest_quality_result_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«treatment» «train» ID** (<code>&quot;treatment_train_id&quot;</code>): <code>&quot;&quot;</code>
> - **«power» зависимость ID** (<code>&quot;power_dependency_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«spare» компонент ID** (<code>&quot;spare_component_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» источник ID** (<code>&quot;alternate_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«shared» отказ отрасль ID** (<code>&quot;shared_failure_domain_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«drought» триггер** (<code>&quot;drought_trigger&quot;</code>): <code>&quot;&quot;</code>
> - **«contamination» «lockout» триггер** (<code>&quot;contamination_lockout_trigger&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «failover» испытание время** (<code>&quot;last_failover_test_at&quot;</code>): <code>&quot;&quot;</code>
> - **Правовой допуск состояние** (<code>&quot;legal_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«quality» допуск состояние** (<code>&quot;quality_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Мощность допуск состояние** (<code>&quot;capacity_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Источник не питьевой и не законный до отдельных доказательств&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
