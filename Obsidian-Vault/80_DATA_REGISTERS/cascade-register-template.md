---
id: "DATA-REGISTER-58d721314503eec0"
type: "generated-data-register-view"
title: "Реестр каскадов отказов — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "cascade-register-template.csv"
source_sha256: "9d17ed55a0970f6f5e8edd6c421fa219b7a2e5217a288694c1e3d5e094e40334"
source_bytes: 8804
source_row_count: 12
source_column_count: 26
source_cell_count: 312
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: cascade-register-template.csv -->

# Реестр каскадов отказов — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 12
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 312
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `9d17ed55a0970f6f5e8edd6c421fa219b7a2e5217a288694c1e3d5e094e40334`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Отношение ID | <code>&quot;relation_id&quot;</code> |
| 2 | Из сценарий ID | <code>&quot;from_scenario_id&quot;</code> |
| 3 | В сценарий ID | <code>&quot;to_scenario_id&quot;</code> |
| 4 | Отношение тип | <code>&quot;relation_type&quot;</code> |
| 5 | «transition» условие | <code>&quot;transition_condition&quot;</code> |
| 6 | Триггер источник класс | <code>&quot;trigger_source_class&quot;</code> |
| 7 | Решение владелец функция | <code>&quot;decision_owner_function&quot;</code> |
| 8 | «proposed» «card» ID | <code>&quot;proposed_card_id&quot;</code> |
| 9 | «proposed» «card» статус | <code>&quot;proposed_card_status&quot;</code> |
| 10 | Возможность «impact» ID | <code>&quot;capability_impact_ids&quot;</code> |
| 11 | Карта «layer» «codes» | <code>&quot;map_layer_codes&quot;</code> |
| 12 | Карта ID | <code>&quot;map_ids&quot;</code> |
| 13 | Группа «implications» | <code>&quot;group_implications&quot;</code> |
| 14 | «preventive» «control» | <code>&quot;preventive_control&quot;</code> |
| 15 | «detection» метод | <code>&quot;detection_method&quot;</code> |
| 16 | «first» «safe» «direction» | <code>&quot;first_safe_direction&quot;</code> |
| 17 | «abort» триггер | <code>&quot;abort_trigger&quot;</code> |
| 18 | Запрещённый действие | <code>&quot;prohibited_action&quot;</code> |
| 19 | Отношение источник ID | <code>&quot;relation_source_ids&quot;</code> |
| 20 | Действие источник ID | <code>&quot;action_source_ids&quot;</code> |
| 21 | Источник область примечания | <code>&quot;source_scope_notes&quot;</code> |
| 22 | Отношение «content» статус | <code>&quot;relation_content_status&quot;</code> |
| 23 | «drill» статус | <code>&quot;drill_status&quot;</code> |
| 24 | Владелец | <code>&quot;owner&quot;</code> |
| 25 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 12 — CAS-001
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-001&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-EQ&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;TEC-COLLAPSE&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;CAUSES_OR_INCREASES&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Повреждение здания или признаки неустойчивости&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION|OFFICIAL&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-TEC-COLLAPSE&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;SHEL|FIRE|MED-TRAUMA&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;BUILDING|NO_GO|RESCUE_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-BLD-HOME-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|EXIT|NO_REENTRY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Building plan and secured contents&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Observation and competent authority&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не входить для поиска или вещей&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-ANEPC-INFORISCOS&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_SOURCE_ONLY; ACTION_SOURCE_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример связи не утверждённая action-card&quot;</code>
>

<!-- record:2 cells:26 -->
> [!abstract]- Запись 2 из 12 — CAS-002
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-002&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-EQ&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;TEC-GAS&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;CAUSES_OR_INCREASES&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Запах газа alarm или повреждение сети после толчков&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION|ALARM&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-TEC-GAS&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;FIRE|HOME|COM&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;BUILDING_EXIT|UTILITY_ZONE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-BLD-HOME-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|EXIT|CALL&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Known safe exit and utility contacts&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Smell alarm official notice&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не создавать искру и не возвращаться&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-ANEPC-INFORISCOS&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_SOURCE_ONLY; ACTION_SOURCE_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:3 cells:26 -->
> [!abstract]- Запись 3 из 12 — CAS-003
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-003&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-EQ&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;NAT-TSU&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;CONTEXT_DEPENDENT&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Прибрежная зона и естественные признаки или официальный сигнал&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;NATURAL_SIGN|OFFICIAL&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-NAT-TSU&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;NAV|TRANS|COM&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;TSUNAMI|ELEVATION|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-TSU-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|MOVE_AS_GROUP|MOBILITY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Preverified high-ground route&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Natural sign and official alert&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не ждать телефона при естественном признаке&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-IPMA-TSUNAMI|SRC-ANEPC-SIPE&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_SOURCE_ONLY; ACTION_SOURCE_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Только для применимой территории&quot;</code>
>

<!-- record:4 cells:26 -->
> [!abstract]- Запись 4 из 12 — CAS-004
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-004&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-FLD&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;INF-WATER-CONTAM&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;CAUSES_OR_INCREASES&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Вода затронула источник или официальное сообщение&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION|OFFICIAL&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-INF-WATER-CONTAM&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;WAT|SAN|MED-ILL&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;FLOOD|WATER_DISTRIBUTION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-FLD-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;SEPARATE_CLEAN_DIRTY|PROTECT_VULNERABLE&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Closed stored water and protected containers&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Official notice and source inspection&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не считать кипячение универсальным решением&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-CDC-FLOOD-HOME&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;SRC-CDC-FLOOD-HOME&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;LINKS_CLASSIFIED_BY_SCOPE; CONTENT_NOT_ARCHIVED_OR_SECTION_REVIEWED; CARD_NOT_CREATED&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:5 cells:26 -->
> [!abstract]- Запись 5 из 12 — CAS-005
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-005&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-FLD&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;BIO-MOLD&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;DELAYED_IMPACT&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Здание оставалось влажным после безопасного возврата&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION|PROFESSIONAL_ASSESSMENT&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-BIO-MOLD&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;AIR|PPE|HOME|REC&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;FLOOD_ZONE|BUILDING&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-FLD-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;LIMIT_EXPOSURE|PROTECT_RESPIRATORY_PROFILE&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Drying plan and professional contacts&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Visible moisture odor professional assessment&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не входить если structure sewage electricity or chemicals unsafe&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-CDC-FLOOD-HOME&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;SRC-CDC-FLOOD-HOME&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;LINKS_CLASSIFIED_BY_SCOPE; CONTENT_NOT_ARCHIVED_OR_SECTION_REVIEWED; CARD_NOT_CREATED&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:6 cells:26 -->
> [!abstract]- Запись 6 из 12 — CAS-006
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-006&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-WIL&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;INF-ROAD&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;CAUSES_OR_INCREASES&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Пожар дым или официальное закрытие затронули маршрут&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;OFFICIAL|DIRECT_OBSERVATION&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-INF-ROAD&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;NAV|TRANS|COM&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;ACTIVE_FIRE|ROAD|ALT_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-WIL-001|MAP-REG-EVAC-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|ROUTE_SWITCH|NO_BLIND_ENTRY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Independent alternate routes&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;ANEPC municipality road authority&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не ехать в дым и не объезжать барьер&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-ICNF-RISK-GEO|SRC-ANEPC-ALERTS&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_SOURCE_ONLY; ACTION_SOURCE_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:7 cells:26 -->
> [!abstract]- Запись 7 из 12 — CAS-007
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-007&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;INF-POWER&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;TEC-CO&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;UNSAFE_WORKAROUND&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Внутри или рядом с закрытым объёмом используется combustion device&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION|ALARM|SYMPTOM&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-TEC-CO&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;FIRE|AIR|MED-ILL&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;BUILDING_EXIT|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-BLD-HOME-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|EXIT|CALL&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;No indoor generator or unapproved combustion&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;CO alarm symptoms observation&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не искать источник внутри&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-CDC-POWER-CO&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;SRC-CDC-POWER-CO&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;LINKS_CLASSIFIED_BY_SCOPE; CONTENT_NOT_ARCHIVED_OR_SECTION_REVIEWED; CARD_NOT_CREATED&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:8 cells:26 -->
> [!abstract]- Запись 8 из 12 — CAS-008
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-008&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;INF-POWER&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;MED-CONTINUITY&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;DEPENDENCY_FAILURE&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Недостаточно энергии или температуры для критического устройства/лекарства&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;MEASUREMENT|DEVICE_ALERT|INVENTORY&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-MED-CONTINUITY&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;MED-NCD|ENE|TRANS&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;HEALTHCARE|PHARMACY|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;PROTECT_PERSON|EARLY_ESCALATION|TRANSPORT&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Measured energy budget and clinician-approved plan&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Runtime temperature device alarm&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не менять препарат или режим самостоятельно&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_AND_ACTION_SOURCES_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:9 cells:26 -->
> [!abstract]- Запись 9 из 12 — CAS-009
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-009&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;CYB-MALWARE&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;INF-PAY&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;SERVICE_IMPACT&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Компрометация блокирует платёж или доверенный доступ&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;SERVICE_NOTICE|DIRECT_OBSERVATION&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-INF-PAY&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;FIN|DOC|CYB&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;BANK|ADMIN|SUPPLY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;VERIFY|PRESERVE_RECORDS|PRIVACY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Diversified lawful payment and offline records&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Bank/provider confirmation&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не вводить данные на недоверенном устройстве&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-ENISA-MOBILE-BANKING&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;SRC-CISA-RANSOMWARE|SRC-BPORTUGAL-FRAUD|SRC-CNCS-REPORT&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;LINKS_CLASSIFIED_BY_SCOPE; CONTENT_NOT_ARCHIVED_OR_SECTION_REVIEWED; CARD_NOT_CREATED&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:10 cells:26 -->
> [!abstract]- Запись 10 из 12 — CAS-010
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-010&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;SOC-CAREGIVER&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;MED-CONTINUITY&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;DEPENDENCY_FAILURE&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Основной caregiver недоступен&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-MED-CONTINUITY&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;MED-NCD|SAFE|LEG|TRANS&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;HEALTHCARE|AUTHORIZED_CAREGIVER|MEETUP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-MUN-RISK-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ASSIGN_BACKUP|ACCOUNT|PRIVACY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Authorized backup and accessible continuity plan&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Missed role confirmation&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не передавать зависимого неподтверждённому лицу&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_AND_ACTION_SOURCES_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:11 cells:26 -->
> [!abstract]- Запись 11 из 12 — CAS-011
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-011&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;NAT-DROUGHT&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;NAT-WIL&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;RISK_AMPLIFIER&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Официально повышенная пожарная опасность при засухе&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;OFFICIAL&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-NAT-WIL&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;WAT|NAV|TRANS|AIR&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;FIRE_HAZARD|WATER|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-OV-WIL-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;EARLY_TRIGGER|PETS|MOBILITY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Preseason route and water planning&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;ICNF IPMA ANEPC notices&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не путать structural danger с live fire&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;SRC-ICNF-RISK-GEO|SRC-IPMA-WARNINGS&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_SOURCE_ONLY; ACTION_SOURCE_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:12 cells:26 -->
> [!abstract]- Запись 12 из 12 — CAS-012
> - **Отношение ID** (<code>&quot;relation_id&quot;</code>): <code>&quot;CAS-012&quot;</code>
> - **Из сценарий ID** (<code>&quot;from_scenario_id&quot;</code>): <code>&quot;SEC-CONFLICT&quot;</code>
> - **В сценарий ID** (<code>&quot;to_scenario_id&quot;</code>): <code>&quot;SOC-MIGRATION&quot;</code>
> - **Отношение тип** (<code>&quot;relation_type&quot;</code>): <code>&quot;FORCES_CONTINUITY_EVENT&quot;</code>
> - **«transition» условие** (<code>&quot;transition_condition&quot;</code>): <code>&quot;Официальная эвакуация или утрата безопасности места&quot;</code>
> - **Триггер источник класс** (<code>&quot;trigger_source_class&quot;</code>): <code>&quot;OFFICIAL|DIRECT_OBSERVATION&quot;</code>
> - **Решение владелец функция** (<code>&quot;decision_owner_function&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«proposed» «card» ID** (<code>&quot;proposed_card_id&quot;</code>): <code>&quot;CARD-SOC-MIGRATION&quot;</code>
> - **«proposed» «card» статус** (<code>&quot;proposed_card_status&quot;</code>): <code>&quot;NOT_CREATED&quot;</code>
> - **Возможность «impact» ID** (<code>&quot;capability_impact_ids&quot;</code>): <code>&quot;DOC|LEG|NAV|MED-NCD|FIN&quot;</code>
> - **Карта «layer» «codes»** (<code>&quot;map_layer_codes&quot;</code>): <code>&quot;BORDER|CONSULATE|EVAC_ROUTE|SHELTER&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;MAP-REG-EVAC-001&quot;</code>
> - **Группа «implications»** (<code>&quot;group_implications&quot;</code>): <code>&quot;ACCOUNT|DEPENDENTS|PETS|PRIVACY&quot;</code>
> - **«preventive» «control»** (<code>&quot;preventive_control&quot;</code>): <code>&quot;Documents external contact early triggers&quot;</code>
> - **«detection» метод** (<code>&quot;detection_method&quot;</code>): <code>&quot;Government civil protection consular sources&quot;</code>
> - **«first» «safe» «direction»** (<code>&quot;first_safe_direction&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **«abort» триггер** (<code>&quot;abort_trigger&quot;</code>): <code>&quot;TBD_PENDING_CARD_REVIEW&quot;</code>
> - **Запрещённый действие** (<code>&quot;prohibited_action&quot;</code>): <code>&quot;Не использовать неподтверждённый опасный маршрут&quot;</code>
> - **Отношение источник ID** (<code>&quot;relation_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Действие источник ID** (<code>&quot;action_source_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Источник область примечания** (<code>&quot;source_scope_notes&quot;</code>): <code>&quot;RELATION_AND_ACTION_SOURCES_REQUIRED_BEFORE_CARD_RELEASE&quot;</code>
> - **Отношение «content» статус** (<code>&quot;relation_content_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **«drill» статус** (<code>&quot;drill_status&quot;</code>): <code>&quot;NOT_DRILLED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
