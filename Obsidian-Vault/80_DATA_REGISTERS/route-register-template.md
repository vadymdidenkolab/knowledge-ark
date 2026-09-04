---
id: "DATA-REGISTER-e4d6fd6148140215"
type: "generated-data-register-view"
title: "Реестр маршрутов — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "route-register-template.csv"
source_sha256: "ca030e39b15bc7134f6e6d1553497c06a4603cdb9b47778ae2d78e38f7dcfd5f"
source_bytes: 4990
source_row_count: 6
source_column_count: 67
source_cell_count: 402
ignored_blank_row_count: 0
semantic_group: "MAPS_ENVIRONMENT"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: route-register-template.csv -->

# Реестр маршрутов — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Карты, маршруты и климат
- **Записей:** 6
- **Полей в каждой записи:** 67
- **Ячеек данных, включая пустые:** 402
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `ca030e39b15bc7134f6e6d1553497c06a4603cdb9b47778ae2d78e38f7dcfd5f`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Маршрут ID | <code>&quot;route_id&quot;</code> |
| 2 | Маршрут название | <code>&quot;route_name&quot;</code> |
| 3 | Маршрут класс | <code>&quot;route_class&quot;</code> |
| 4 | Сценарий «codes» | <code>&quot;scenario_codes&quot;</code> |
| 5 | «origin» ID | <code>&quot;origin_id&quot;</code> |
| 6 | «destination» ID | <code>&quot;destination_id&quot;</code> |
| 7 | «waypoint» ID | <code>&quot;waypoint_ids&quot;</code> |
| 8 | «mode» | <code>&quot;mode&quot;</code> |
| 9 | «distance» «km» | <code>&quot;distance_km&quot;</code> |
| 10 | «ascent» «m» | <code>&quot;ascent_m&quot;</code> |
| 11 | «descent» «m» | <code>&quot;descent_m&quot;</code> |
| 12 | Время «range» «min» | <code>&quot;time_range_min&quot;</code> |
| 13 | Группа «size» испытанный | <code>&quot;group_size_tested&quot;</code> |
| 14 | «slowest» «member» профиль | <code>&quot;slowest_member_profile&quot;</code> |
| 15 | «mobility» «support» | <code>&quot;mobility_support&quot;</code> |
| 16 | «child» «constraints» | <code>&quot;child_constraints&quot;</code> |
| 17 | «pet» «constraints» | <code>&quot;pet_constraints&quot;</code> |
| 18 | «cargo» «kg» испытанный | <code>&quot;cargo_kg_tested&quot;</code> |
| 19 | «surface» | <code>&quot;surface&quot;</code> |
| 20 | «max» «grade» | <code>&quot;max_grade&quot;</code> |
| 21 | «stairs» | <code>&quot;stairs&quot;</code> |
| 22 | «bridges» | <code>&quot;bridges&quot;</code> |
| 23 | «tunnels» | <code>&quot;tunnels&quot;</code> |
| 24 | «ferries» | <code>&quot;ferries&quot;</code> |
| 25 | «flood» «exposure» | <code>&quot;flood_exposure&quot;</code> |
| 26 | «wildfire» «exposure» | <code>&quot;wildfire_exposure&quot;</code> |
| 27 | «coastal» «exposure» | <code>&quot;coastal_exposure&quot;</code> |
| 28 | «landslide» «exposure» | <code>&quot;landslide_exposure&quot;</code> |
| 29 | Приватный «access» | <code>&quot;private_access&quot;</code> |
| 30 | «access» часы | <code>&quot;access_hours&quot;</code> |
| 31 | «night» статус | <code>&quot;night_status&quot;</code> |
| 32 | «season» статус | <code>&quot;season_status&quot;</code> |
| 33 | «weather» «limits» | <code>&quot;weather_limits&quot;</code> |
| 34 | «communications» «gaps» | <code>&quot;communications_gaps&quot;</code> |
| 35 | Вода «points» подтверждённый | <code>&quot;water_points_verified&quot;</code> |
| 36 | «toilet» «points» подтверждённый | <code>&quot;toilet_points_verified&quot;</code> |
| 37 | Медицинский «points» подтверждённый | <code>&quot;medical_points_verified&quot;</code> |
| 38 | Решение «points» | <code>&quot;decision_points&quot;</code> |
| 39 | «turnaround» «triggers» | <code>&quot;turnaround_triggers&quot;</code> |
| 40 | «no» «go» «triggers» | <code>&quot;no_go_triggers&quot;</code> |
| 41 | «alternate» маршрут ID | <code>&quot;alternate_route_id&quot;</code> |
| 42 | «geometry» «filename» | <code>&quot;geometry_filename&quot;</code> |
| 43 | «geometry» SHA-256 | <code>&quot;geometry_sha256&quot;</code> |
| 44 | Карта ID | <code>&quot;map_ids&quot;</code> |
| 45 | Источник дата | <code>&quot;source_date&quot;</code> |
| 46 | «desk» «checked» время | <code>&quot;desk_checked_at&quot;</code> |
| 47 | «field» «checked» время | <code>&quot;field_checked_at&quot;</code> |
| 48 | «field» «checker» | <code>&quot;field_checker&quot;</code> |
| 49 | «last» «safe» «walk» время | <code>&quot;last_safe_walk_at&quot;</code> |
| 50 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 51 | Владелец | <code>&quot;owner&quot;</code> |
| 52 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 53 | Примечания | <code>&quot;notes&quot;</code> |
| 54 | «event» ID | <code>&quot;event_id&quot;</code> |
| 55 | «event» снимок карта ID | <code>&quot;event_snapshot_map_ids&quot;</code> |
| 56 | «event» снимок «valid» до «utc» | <code>&quot;event_snapshot_valid_until_utc&quot;</code> |
| 57 | «event» «activation» «checked» время | <code>&quot;event_activation_checked_at&quot;</code> |
| 58 | «freshness» допуск решение | <code>&quot;freshness_gate_decision&quot;</code> |
| 59 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 60 | «sensitive» «registry» ссылка | <code>&quot;sensitive_registry_ref&quot;</code> |
| 61 | «redacted» «copy» ID | <code>&quot;redacted_copy_id&quot;</code> |
| 62 | «encryption» требуемый | <code>&quot;encryption_required&quot;</code> |
| 63 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 64 | «access» «control» состояние | <code>&quot;access_control_state&quot;</code> |
| 65 | «printed» «copy» количество | <code>&quot;printed_copy_count&quot;</code> |
| 66 | Приватность проверенный время | <code>&quot;privacy_reviewed_at&quot;</code> |
| 67 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:67 -->
> [!abstract]- Запись 1 из 6 — R-A-HOME-R1 — Дом к ближайшей точке встречи
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-A-HOME-R1&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Дом к ближайшей точке встречи&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;A&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|TEC-FIRE|TEC-CO|TEC-GAS&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;WALK&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;R-B-HOME-R1&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Точки и маршрут не заданы&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

<!-- record:2 cells:67 -->
> [!abstract]- Запись 2 из 6 — R-B-HOME-R1 — Независимый резерв к ближайшей точке встречи
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-B-HOME-R1&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Независимый резерв к ближайшей точке встречи&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;B&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|TEC-FIRE|TEC-CO|TEC-GAS&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;WALK&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;R-A-HOME-R1&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Независимость от основного маршрута не доказана&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

<!-- record:3 cells:67 -->
> [!abstract]- Запись 3 из 6 — R-C-WORK-HOME — Работа к дому пешком
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-C-WORK-HOME&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Работа к дому пешком&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;C&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;INF-TEL|INF-INTERNET|INF-POWER|SOC-HOME-LOSS|SOC-MIGRATION&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;WALK&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Работа и дом не заданы&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

<!-- record:4 cells:67 -->
> [!abstract]- Запись 4 из 6 — R-D-ACCESS-R2 — Доступный маршрут к внешней точке встречи
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-D-ACCESS-R2&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Доступный маршрут к внешней точке встречи&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;D&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;ACCESSIBLE_MODE&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;REQUIRED&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Конкретная мобильность и сопровождающий не заданы&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

<!-- record:5 cells:67 -->
> [!abstract]- Запись 5 из 6 — R-E-TSU-HIGH — Немедленный путь на высоту
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-E-TSU-HIGH&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Немедленный путь на высоту&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;E&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-TSU&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;WALK&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;REQUIRED_CHECK&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-TSU-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;NOT_APPLICABLE_PENDING_LOCATION&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Выпускать только для применимой прибрежной зоны по официальному плану&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-OV-TSU-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

<!-- record:6 cells:67 -->
> [!abstract]- Запись 6 из 6 — R-REG-ALT-001 — Региональный резервный маршрут
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;R-REG-ALT-001&quot;</code>
> - **Маршрут название** (<code>&quot;route_name&quot;</code>): <code>&quot;Региональный резервный маршрут&quot;</code>
> - **Маршрут класс** (<code>&quot;route_class&quot;</code>): <code>&quot;B&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;NAT-WIL|NAT-FLD|NAT-FLASH|NAT-EQ|SOC-HOME-LOSS|SOC-MIGRATION&quot;</code>
> - **«origin» ID** (<code>&quot;origin_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **«destination» ID** (<code>&quot;destination_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«waypoint» ID** (<code>&quot;waypoint_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«mode»** (<code>&quot;mode&quot;</code>): <code>&quot;CAR_AND_WALK_FALLBACK&quot;</code>
> - **«distance» «km»** (<code>&quot;distance_km&quot;</code>): <code>&quot;&quot;</code>
> - **«ascent» «m»** (<code>&quot;ascent_m&quot;</code>): <code>&quot;&quot;</code>
> - **«descent» «m»** (<code>&quot;descent_m&quot;</code>): <code>&quot;&quot;</code>
> - **Время «range» «min»** (<code>&quot;time_range_min&quot;</code>): <code>&quot;&quot;</code>
> - **Группа «size» испытанный** (<code>&quot;group_size_tested&quot;</code>): <code>&quot;0&quot;</code>
> - **«slowest» «member» профиль** (<code>&quot;slowest_member_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» «support»** (<code>&quot;mobility_support&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«child» «constraints»** (<code>&quot;child_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» «constraints»** (<code>&quot;pet_constraints&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«cargo» «kg» испытанный** (<code>&quot;cargo_kg_tested&quot;</code>): <code>&quot;&quot;</code>
> - **«surface»** (<code>&quot;surface&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«max» «grade»** (<code>&quot;max_grade&quot;</code>): <code>&quot;&quot;</code>
> - **«stairs»** (<code>&quot;stairs&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«bridges»** (<code>&quot;bridges&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«tunnels»** (<code>&quot;tunnels&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«ferries»** (<code>&quot;ferries&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«flood» «exposure»** (<code>&quot;flood_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«wildfire» «exposure»** (<code>&quot;wildfire_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«coastal» «exposure»** (<code>&quot;coastal_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«landslide» «exposure»** (<code>&quot;landslide_exposure&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватный «access»** (<code>&quot;private_access&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«access» часы** (<code>&quot;access_hours&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«night» статус** (<code>&quot;night_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«season» статус** (<code>&quot;season_status&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«weather» «limits»** (<code>&quot;weather_limits&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» «gaps»** (<code>&quot;communications_gaps&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода «points» подтверждённый** (<code>&quot;water_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **«toilet» «points» подтверждённый** (<code>&quot;toilet_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Медицинский «points» подтверждённый** (<code>&quot;medical_points_verified&quot;</code>): <code>&quot;NO&quot;</code>
> - **Решение «points»** (<code>&quot;decision_points&quot;</code>): <code>&quot;&quot;</code>
> - **«turnaround» «triggers»** (<code>&quot;turnaround_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«no» «go» «triggers»** (<code>&quot;no_go_triggers&quot;</code>): <code>&quot;&quot;</code>
> - **«alternate» маршрут ID** (<code>&quot;alternate_route_id&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» «filename»** (<code>&quot;geometry_filename&quot;</code>): <code>&quot;&quot;</code>
> - **«geometry» SHA-256** (<code>&quot;geometry_sha256&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-REG-EVAC-001&quot;</code>
> - **Источник дата** (<code>&quot;source_date&quot;</code>): <code>&quot;&quot;</code>
> - **«desk» «checked» время** (<code>&quot;desk_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checked» время** (<code>&quot;field_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «checker»** (<code>&quot;field_checker&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «safe» «walk» время** (<code>&quot;last_safe_walk_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Назначение и транспорт не заданы&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;&quot;</code>
> - **«event» снимок карта ID** (<code>&quot;event_snapshot_map_ids&quot;</code>): <code>&quot;MAP-REG-EVAC-001&quot;</code>
> - **«event» снимок «valid» до «utc»** (<code>&quot;event_snapshot_valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«event» «activation» «checked» время** (<code>&quot;event_activation_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **«freshness» допуск решение** (<code>&quot;freshness_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
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

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
