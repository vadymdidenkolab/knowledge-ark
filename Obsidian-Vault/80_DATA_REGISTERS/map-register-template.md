---
id: "DATA-REGISTER-68fc6c579249b0a7"
type: "generated-data-register-view"
title: "Реестр карт — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "map-register-template.csv"
source_sha256: "5d7efa2bc00ca05fa599b502b159cc7b547148cd95b220cb9303e2654daff957"
source_bytes: 8671
source_row_count: 8
source_column_count: 64
source_cell_count: 512
ignored_blank_row_count: 0
semantic_group: "MAPS_ENVIRONMENT"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: map-register-template.csv -->

# Реестр карт — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Карты, маршруты и климат
- **Записей:** 8
- **Полей в каждой записи:** 64
- **Ячеек данных, включая пустые:** 512
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `5d7efa2bc00ca05fa599b502b159cc7b547148cd95b220cb9303e2654daff957`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Карта ID | <code>&quot;map_id&quot;</code> |
| 2 | Название | <code>&quot;title&quot;</code> |
| 3 | «pack» ID | <code>&quot;pack_id&quot;</code> |
| 4 | «area» класс | <code>&quot;area_class&quot;</code> |
| 5 | «area» название | <code>&quot;area_name&quot;</code> |
| 6 | «bbox» «wgs84» | <code>&quot;bbox_wgs84&quot;</code> |
| 7 | «scale» «denominator» | <code>&quot;scale_denominator&quot;</code> |
| 8 | «layer» класс | <code>&quot;layer_class&quot;</code> |
| 9 | Сценарий «codes» | <code>&quot;scenario_codes&quot;</code> |
| 10 | Целевая аудитория | <code>&quot;audience&quot;</code> |
| 11 | «sensitivity» | <code>&quot;sensitivity&quot;</code> |
| 12 | Источник полномочие | <code>&quot;source_authority&quot;</code> |
| 13 | Источник ID | <code>&quot;source_id&quot;</code> |
| 14 | Канонический адрес в сети | <code>&quot;canonical_url&quot;</code> |
| 15 | Источник «dataset» название | <code>&quot;source_dataset_title&quot;</code> |
| 16 | Источник «edition» дата | <code>&quot;source_edition_date&quot;</code> |
| 17 | Источник «retrieved» время | <code>&quot;source_retrieved_at&quot;</code> |
| 18 | Источник «crs» | <code>&quot;source_crs&quot;</code> |
| 19 | «working» «crs» | <code>&quot;working_crs&quot;</code> |
| 20 | Лицензия | <code>&quot;license&quot;</code> |
| 21 | «attribution» | <code>&quot;attribution&quot;</code> |
| 22 | Источник статус | <code>&quot;source_status&quot;</code> |
| 23 | «raw» формат | <code>&quot;raw_format&quot;</code> |
| 24 | «raw» «filename» | <code>&quot;raw_filename&quot;</code> |
| 25 | «raw» SHA-256 | <code>&quot;raw_sha256&quot;</code> |
| 26 | «derived» формат | <code>&quot;derived_format&quot;</code> |
| 27 | «derived» «filename» | <code>&quot;derived_filename&quot;</code> |
| 28 | «derived» SHA-256 | <code>&quot;derived_sha256&quot;</code> |
| 29 | Офлайн основной испытанный время | <code>&quot;offline_primary_tested_at&quot;</code> |
| 30 | Офлайн резервный испытанный время | <code>&quot;offline_backup_tested_at&quot;</code> |
| 31 | «print» «filename» | <code>&quot;print_filename&quot;</code> |
| 32 | «print» «size» | <code>&quot;print_size&quot;</code> |
| 33 | «print» «scale» подтверждённый | <code>&quot;print_scale_verified&quot;</code> |
| 34 | «north» «arrow» | <code>&quot;north_arrow&quot;</code> |
| 35 | «legend» | <code>&quot;legend&quot;</code> |
| 36 | «grid» | <code>&quot;grid&quot;</code> |
| 37 | Маршрут ID | <code>&quot;route_ids&quot;</code> |
| 38 | «field» подтверждённый время | <code>&quot;field_verified_at&quot;</code> |
| 39 | «verifier» | <code>&quot;verifier&quot;</code> |
| 40 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 41 | «limitations» | <code>&quot;limitations&quot;</code> |
| 42 | Владелец | <code>&quot;owner&quot;</code> |
| 43 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 44 | «supersedes» | <code>&quot;supersedes&quot;</code> |
| 45 | Примечания | <code>&quot;notes&quot;</code> |
| 46 | «temporal» класс | <code>&quot;temporal_class&quot;</code> |
| 47 | «event» ID | <code>&quot;event_id&quot;</code> |
| 48 | «captured» время «utc» | <code>&quot;captured_at_utc&quot;</code> |
| 49 | «valid» из «utc» | <code>&quot;valid_from_utc&quot;</code> |
| 50 | «valid» до «utc» | <code>&quot;valid_until_utc&quot;</code> |
| 51 | Полномочие «checked» время | <code>&quot;authority_checked_at&quot;</code> |
| 52 | «freshness» состояние | <code>&quot;freshness_state&quot;</code> |
| 53 | «freshness» допуск решение | <code>&quot;freshness_gate_decision&quot;</code> |
| 54 | «exchange» «crs» | <code>&quot;exchange_crs&quot;</code> |
| 55 | «coverage» «extent» | <code>&quot;coverage_extent&quot;</code> |
| 56 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 57 | «sensitive» «registry» ссылка | <code>&quot;sensitive_registry_ref&quot;</code> |
| 58 | «redacted» «copy» ID | <code>&quot;redacted_copy_id&quot;</code> |
| 59 | «encryption» требуемый | <code>&quot;encryption_required&quot;</code> |
| 60 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 61 | «access» «control» состояние | <code>&quot;access_control_state&quot;</code> |
| 62 | «printed» «copy» количество | <code>&quot;printed_copy_count&quot;</code> |
| 63 | Приватность проверенный время | <code>&quot;privacy_reviewed_at&quot;</code> |
| 64 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:64 -->
> [!abstract]- Запись 1 из 8 — MAP-BLD-HOME-001 — План дома и выходов
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-BLD-HOME-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;План дома и выходов&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;BUILDING&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;BUILDING_PLAN&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;TEC-FIRE|TEC-CO|TEC-GAS|NAT-EQ|INF-POWER&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Пользовательский план здания&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;LOCAL_PLAN&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;LOCAL_PLAN&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;PRIVATE&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;Не распространять&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A4&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;OPTIONAL&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Требует фактического обследования здания и проверки выходов&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не содержит адреса до персонализации&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;STRUCTURAL&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;TBD_IF_GEOREFERENCED&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;SITE_TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:2 cells:64 -->
> [!abstract]- Запись 2 из 8 — SRC-SNIG-RNDG — Локальная базовая карта вокруг дома
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Локальная базовая карта вокруг дома&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;E1|HOME&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;10000&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;BASEMAP&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;DGT/SNIG plus licensed routable basemap&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-SNIG-RNDG&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Базовая география и топография&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;Указать на листе&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A3&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Нет адреса и не подтверждена проходимость&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Резервный basemap не заменяет hazard layers&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;STATIC_BASELINE&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;AREA_TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:3 cells:64 -->
> [!abstract]- Запись 3 из 8 — SRC-ANEPC-SIPE — Муниципальные риски и помощь
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Муниципальные риски и помощь&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;HOME|E1&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;MUNICIPAL&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;50000&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;MULTI_HAZARD&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;ANEPC plus municipality&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-ANEPC-SIPE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://prociv.gov.pt/pt/prevencao-e-preparacao/programas-e-projetos/sipe-planeamento-de-emergencia/&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Действующий муниципальный emergency plan и публичные карты&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;ANEPC/муниципалитет&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A3&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Муниципалитет ещё не указан; действующая редакция не выбрана&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;После выбора территории найти конкретный план&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;PLAN_VERSIONED&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;MUNICIPALITY_TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:4 cells:64 -->
> [!abstract]- Запись 4 из 8 — SRC-APA-PGRI-2022-27 — Затопление и маршруты вверх
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-OV-FLD-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Затопление и маршруты вверх&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;HOME|E1|CAR&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;SCENARIO&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;HAZARD_OVERLAY&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-FLD|NAT-FLASH&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;APA&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-APA-PGRI-2022-27&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://apambiente.pt/agua/2o-ciclo-de-planeamento-2022-2027&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;PGRI 2022-2027 / ARPSI&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;2026-07-29&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;Agência Portuguesa do Ambiente&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A3&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Покрытие ARPSI не доказывает отсутствие риска вне слоя&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Нужны высоты и независимые маршруты&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;PLAN_VERSIONED&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;SOURCE_COVERAGE_REQUIRES_AREA_INTERSECTION&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:5 cells:64 -->
> [!abstract]- Запись 5 из 8 — SRC-ICNF-RISK-GEO — Природный пожар и выходы
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-OV-WIL-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Природный пожар и выходы&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;HOME|E1|CAR&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;SCENARIO&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;HAZARD_OVERLAY&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-WIL&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;ICNF&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-ICNF-RISK-GEO&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://geocatalogo.icnf.pt/catalogo_tema5.html&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Риски и угрозы / пожарные слои&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;EPSG:3763 or source-dependent&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;ICNF/DGT&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A3&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Структурная опасность не является текущим пожаром или открытой дорогой&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Во время события нужны текущие указания Proteção Civil&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;STRUCTURAL_HAZARD&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;SOURCE_COVERAGE_REQUIRES_AREA_INTERSECTION&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:6 cells:64 -->
> [!abstract]- Запись 6 из 8 — SRC-IPMA-TSUNAMI — Цунами и немедленный путь на высоту
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-OV-TSU-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Цунами и немедленный путь на высоту&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;HOME|E1&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;SCENARIO&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;HAZARD_OVERLAY&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-TSU&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;IPMA plus municipality/ANEPC&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-IPMA-TSUNAMI&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.ipma.pt/pt/media/noticias/documentos/2021/Folheto_Tsunami.pdf&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Официальная информация о цунами плюс локальный план&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;2021&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;IPMA/муниципалитет&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A4&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;NOT_APPLICABLE_PENDING_LOCATION&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Применимость неизвестна без адреса и официальной локальной зоны&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не выпускать generic маршрут вдоль побережья&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;PLAN_VERSIONED&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;COASTAL_AREA_TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:7 cells:64 -->
> [!abstract]- Запись 7 из 8 — SRC-SNIG-RNDG — Региональная эвакуация и объезды
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-REG-EVAC-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Региональная эвакуация и объезды&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;CAR|HOME&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;REGIONAL&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;200000&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;TRANSPORT&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|NAT-WIL|NAT-FLD|NAT-FLASH|NAT-EQ&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;DGT/SNIG plus transport authorities&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-SNIG-RNDG&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Региональная топография и транспорт&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;Указать по каждому слою&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;GEOPACKAGE|PDF|MBTILES&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A3&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Нет точек назначения и проверки мостов/тоннелей/доступа&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Нужны независимые направления и пешая альтернатива&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;STATIC_BASELINE&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;REGION_TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

<!-- record:8 cells:64 -->
> [!abstract]- Запись 8 из 8 — SRC-SNIG-RNDG — Португалия и Иберия
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;MAP-NAT-PT-001&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Португалия и Иберия&quot;</code>
> - **«pack» ID** (<code>&quot;pack_id&quot;</code>): <code>&quot;CAR|ARCHIVE&quot;</code>
> - **«area» класс** (<code>&quot;area_class&quot;</code>): <code>&quot;NATIONAL&quot;</code>
> - **«area» название** (<code>&quot;area_name&quot;</code>): <code>&quot;Portugal and Iberia&quot;</code>
> - **«bbox» «wgs84»** (<code>&quot;bbox_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«scale» «denominator»** (<code>&quot;scale_denominator&quot;</code>): <code>&quot;500000&quot;</code>
> - **«layer» класс** (<code>&quot;layer_class&quot;</code>): <code>&quot;STRATEGIC_BASEMAP&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|ENV-RESOURCE|ENV-CLIMATE&quot;</code>
> - **Целевая аудитория** (<code>&quot;audience&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;PUBLIC&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;DGT/SNIG plus licensed regional basemap&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-SNIG-RNDG&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/&quot;</code>
> - **Источник «dataset» название** (<code>&quot;source_dataset_title&quot;</code>): <code>&quot;Национальная и трансграничная база&quot;</code>
> - **Источник «edition» дата** (<code>&quot;source_edition_date&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «retrieved» время** (<code>&quot;source_retrieved_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Источник «crs»** (<code>&quot;source_crs&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«working» «crs»** (<code>&quot;working_crs&quot;</code>): <code>&quot;TBD_PROJECTED_BY_TERRITORY_AND_SCALE&quot;</code>
> - **Лицензия** (<code>&quot;license&quot;</code>): <code>&quot;SOURCE_DEPENDENT&quot;</code>
> - **«attribution»** (<code>&quot;attribution&quot;</code>): <code>&quot;Указать по каждому слою&quot;</code>
> - **Источник статус** (<code>&quot;source_status&quot;</code>): <code>&quot;LINK_ONLY&quot;</code>
> - **«raw» формат** (<code>&quot;raw_format&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» «filename»** (<code>&quot;raw_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«raw» SHA-256** (<code>&quot;raw_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» формат** (<code>&quot;derived_format&quot;</code>): <code>&quot;PDF|MBTILES&quot;</code>
> - **«derived» «filename»** (<code>&quot;derived_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«derived» SHA-256** (<code>&quot;derived_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн основной испытанный время** (<code>&quot;offline_primary_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **Офлайн резервный испытанный время** (<code>&quot;offline_backup_tested_at&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «filename»** (<code>&quot;print_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«print» «size»** (<code>&quot;print_size&quot;</code>): <code>&quot;A2&quot;</code>
> - **«print» «scale» подтверждённый** (<code>&quot;print_scale_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«north» «arrow»** (<code>&quot;north_arrow&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«legend»** (<code>&quot;legend&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«grid»** (<code>&quot;grid&quot;</code>): <code>&quot;OPTIONAL&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«verifier»** (<code>&quot;verifier&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Стратегический масштаб непригоден для локальной навигации&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«supersedes»** (<code>&quot;supersedes&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пограничные правила проверяются отдельно&quot;</code>
> - **«temporal» класс** (<code>&quot;temporal_class&quot;</code>): <code>&quot;STATIC_BASELINE&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«captured» время «utc»** (<code>&quot;captured_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» из «utc»** (<code>&quot;valid_from_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Полномочие «checked» время** (<code>&quot;authority_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» состояние** (<code>&quot;freshness_state&quot;</code>): <code>&quot;NOT_EVALUATED&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«exchange» «crs»** (<code>&quot;exchange_crs&quot;</code>): <code>&quot;EPSG:4326&quot;</code>
> - **«coverage» «extent»** (<code>&quot;coverage_extent&quot;</code>): <code>&quot;PORTUGAL_AND_IBERIA_SOURCE_DEPENDENT&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **«printed» «copy» количество** (<code>&quot;printed_copy_count&quot;</code>): <code>&quot;0&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
