---
id: "DATA-REGISTER-325394b0ed351099"
type: "generated-data-register-view"
title: "Объекты и площадки — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "site-register-template.csv"
source_sha256: "8aadd854d4e14355b4dc76c4904d2e05e00adc3ba144350edad3526e22239ec6"
source_bytes: 4193
source_row_count: 7
source_column_count: 46
source_cell_count: 322
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: site-register-template.csv -->

# Объекты и площадки — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 7
- **Полей в каждой записи:** 46
- **Ячеек данных, включая пустые:** 322
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `8aadd854d4e14355b4dc76c4904d2e05e00adc3ba144350edad3526e22239ec6`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Объект ID | <code>&quot;site_id&quot;</code> |
| 2 | Объект тип | <code>&quot;site_type&quot;</code> |
| 3 | Название публичный | <code>&quot;name_public&quot;</code> |
| 4 | Название «sensitive» | <code>&quot;name_sensitive&quot;</code> |
| 5 | «lat» «wgs84» | <code>&quot;lat_wgs84&quot;</code> |
| 6 | «lon» «wgs84» | <code>&quot;lon_wgs84&quot;</code> |
| 7 | «coord» «accuracy» «m» | <code>&quot;coord_accuracy_m&quot;</code> |
| 8 | «admin» «area» | <code>&quot;admin_area&quot;</code> |
| 9 | Сценарий «codes» | <code>&quot;scenario_codes&quot;</code> |
| 10 | Источник полномочие | <code>&quot;source_authority&quot;</code> |
| 11 | Источник ID | <code>&quot;source_id&quot;</code> |
| 12 | Адрес источника в сети | <code>&quot;source_url&quot;</code> |
| 13 | Источник «edition» | <code>&quot;source_edition&quot;</code> |
| 14 | Контакт | <code>&quot;contact&quot;</code> |
| 15 | Контакт подтверждённый время | <code>&quot;contact_verified_at&quot;</code> |
| 16 | «open» статус | <code>&quot;open_status&quot;</code> |
| 17 | «activation» требуемый | <code>&quot;activation_required&quot;</code> |
| 18 | Часы «or» «activation» «rule» | <code>&quot;hours_or_activation_rule&quot;</code> |
| 19 | «access» полномочие | <code>&quot;access_authority&quot;</code> |
| 20 | «accessibility» профиль | <code>&quot;accessibility_profile&quot;</code> |
| 21 | «pet» правило | <code>&quot;pet_policy&quot;</code> |
| 22 | Вода статус | <code>&quot;water_status&quot;</code> |
| 23 | Вода доказательство | <code>&quot;water_evidence&quot;</code> |
| 24 | Мощность «claim» | <code>&quot;capacity_claim&quot;</code> |
| 25 | Мощность доказательство | <code>&quot;capacity_evidence&quot;</code> |
| 26 | «power» доступный состояние | <code>&quot;power_available_state&quot;</code> |
| 27 | «communications» доступный состояние | <code>&quot;communications_available_state&quot;</code> |
| 28 | «field» подтверждённый время | <code>&quot;field_verified_at&quot;</code> |
| 29 | «field» «verifier» | <code>&quot;field_verifier&quot;</code> |
| 30 | «sensitivity» | <code>&quot;sensitivity&quot;</code> |
| 31 | Карта ID | <code>&quot;map_ids&quot;</code> |
| 32 | Маршрут ID | <code>&quot;route_ids&quot;</code> |
| 33 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 34 | Владелец | <code>&quot;owner&quot;</code> |
| 35 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 36 | «limitations» | <code>&quot;limitations&quot;</code> |
| 37 | Примечания | <code>&quot;notes&quot;</code> |
| 38 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 39 | «sensitive» «registry» ссылка | <code>&quot;sensitive_registry_ref&quot;</code> |
| 40 | «redacted» «copy» ID | <code>&quot;redacted_copy_id&quot;</code> |
| 41 | «encryption» требуемый | <code>&quot;encryption_required&quot;</code> |
| 42 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 43 | «access» «control» состояние | <code>&quot;access_control_state&quot;</code> |
| 44 | «printed» «copy» количество | <code>&quot;printed_copy_count&quot;</code> |
| 45 | Приватность проверенный время | <code>&quot;privacy_reviewed_at&quot;</code> |
| 46 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:46 -->
> [!abstract]- Запись 1 из 7 — HOME
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;PRIVATE_HOME&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;PRIVATE&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-BLD-HOME-001|MAP-LOC-HOME-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Точный адрес не включён до персонализации&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:2 cells:46 -->
> [!abstract]- Запись 2 из 7 — R1
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;MEETUP_NEAR_HOME&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|TEC-FIRE|TEC-CO|TEC-GAS&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;HOUSEHOLD_PLUS_MUNICIPAL&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;PUBLIC_OR_PERMISSION_REQUIRED&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-LOC-HOME-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Не проверено вне зон пожара фасада затопления и движения&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:3 cells:46 -->
> [!abstract]- Запись 3 из 7 — R2
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;MEETUP_OUTSIDE_NEIGHBORHOOD&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;HOUSEHOLD_PLUS_MUNICIPAL&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Нет муниципалитета и field check&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:4 cells:46 -->
> [!abstract]- Запись 4 из 7 — R3
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;MEETUP_OUTSIDE_MUNICIPALITY&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;REDACTED&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|ENV-RESOURCE|ENV-CLIMATE&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;HOUSEHOLD_PLUS_HOST_AUTHORITY&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-REG-EVAC-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Нет согласованного host и маршрута&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:5 cells:46 -->
> [!abstract]- Запись 5 из 7 — MED-CAND-001
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;MED-CAND-001&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;HEALTHCARE&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;ALL&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;SNS_OR_MUNICIPAL_AUTHORITY&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;CONTACT_NOT_RECENTLY_VERIFIED&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;PUBLIC&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;PUBLIC&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Координата не доказывает работающий emergency department&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:6 cells:46 -->
> [!abstract]- Запись 6 из 7 — WAT-CAND-001
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;WAT-CAND-001&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;WATER_CANDIDATE&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;INF-WATER-OFF|INF-WATER-CONTAM|BIO-WATER&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;WATER_OPERATOR_OR_MUNICIPALITY&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;CANDIDATE_NOT_POTABLE&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;NONE&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Никогда не маркировать питьевой без актуального доказательства&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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

<!-- record:7 cells:46 -->
> [!abstract]- Запись 7 из 7 — SRC-ANEPC-SIPE
> - **Объект ID** (<code>&quot;site_id&quot;</code>): <code>&quot;SHELTER-CAND-001&quot;</code>
> - **Объект тип** (<code>&quot;site_type&quot;</code>): <code>&quot;OFFICIAL_SHELTER_CANDIDATE&quot;</code>
> - **Название публичный** (<code>&quot;name_public&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Название «sensitive»** (<code>&quot;name_sensitive&quot;</code>): <code>&quot;&quot;</code>
> - **«lat» «wgs84»** (<code>&quot;lat_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«lon» «wgs84»** (<code>&quot;lon_wgs84&quot;</code>): <code>&quot;&quot;</code>
> - **«coord» «accuracy» «m»** (<code>&quot;coord_accuracy_m&quot;</code>): <code>&quot;&quot;</code>
> - **«admin» «area»** (<code>&quot;admin_area&quot;</code>): <code>&quot;&quot;</code>
> - **Сценарий «codes»** (<code>&quot;scenario_codes&quot;</code>): <code>&quot;SOC-HOME-LOSS|SOC-MIGRATION|INF-HOUSING&quot;</code>
> - **Источник полномочие** (<code>&quot;source_authority&quot;</code>): <code>&quot;MUNICIPAL_PROTECAO_CIVIL&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-ANEPC-SIPE&quot;</code>
> - **Адрес источника в сети** (<code>&quot;source_url&quot;</code>): <code>&quot;https://planos.prociv.pt/&quot;</code>
> - **Источник «edition»** (<code>&quot;source_edition&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт** (<code>&quot;contact&quot;</code>): <code>&quot;&quot;</code>
> - **Контакт подтверждённый время** (<code>&quot;contact_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«open» статус** (<code>&quot;open_status&quot;</code>): <code>&quot;NOT_CONFIRMED_ACTIVE&quot;</code>
> - **«activation» требуемый** (<code>&quot;activation_required&quot;</code>): <code>&quot;YES_OR_UNKNOWN&quot;</code>
> - **Часы «or» «activation» «rule»** (<code>&quot;hours_or_activation_rule&quot;</code>): <code>&quot;Только после официальной активации&quot;</code>
> - **«access» полномочие** (<code>&quot;access_authority&quot;</code>): <code>&quot;MUNICIPAL_AUTHORITY&quot;</code>
> - **«accessibility» профиль** (<code>&quot;accessibility_profile&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«pet» правило** (<code>&quot;pet_policy&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Вода статус** (<code>&quot;water_status&quot;</code>): <code>&quot;NOT_CONFIRMED&quot;</code>
> - **Вода доказательство** (<code>&quot;water_evidence&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность «claim»** (<code>&quot;capacity_claim&quot;</code>): <code>&quot;&quot;</code>
> - **Мощность доказательство** (<code>&quot;capacity_evidence&quot;</code>): <code>&quot;NONE&quot;</code>
> - **«power» доступный состояние** (<code>&quot;power_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«communications» доступный состояние** (<code>&quot;communications_available_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«field» подтверждённый время** (<code>&quot;field_verified_at&quot;</code>): <code>&quot;&quot;</code>
> - **«field» «verifier»** (<code>&quot;field_verifier&quot;</code>): <code>&quot;&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;PUBLIC&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;Объект не считается открытым или имеющим место без подтверждения&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
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
