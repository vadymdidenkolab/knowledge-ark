---
id: "DATA-REGISTER-3159c3ced5acad9a"
type: "generated-data-register-view"
title: "Журнал происшествий — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "incident-log-template.csv"
source_sha256: "28e0c9047eb6bc878e15135b196708728127dda9a7e6622740e235bfb4bc7590"
source_bytes: 2826
source_row_count: 4
source_column_count: 59
source_cell_count: 236
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: incident-log-template.csv -->

# Журнал происшествий — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 4
- **Полей в каждой записи:** 59
- **Ячеек данных, включая пустые:** 236
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `28e0c9047eb6bc878e15135b196708728127dda9a7e6622740e235bfb4bc7590`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «event» ID | <code>&quot;event_id&quot;</code> |
| 2 | Запись ID | <code>&quot;entry_id&quot;</code> |
| 3 | «timestamp» локальный «iso8601» «with» «offset» | <code>&quot;timestamp_local_iso8601_with_offset&quot;</code> |
| 4 | «timestamp» «utc» | <code>&quot;timestamp_utc&quot;</code> |
| 5 | Запись тип | <code>&quot;entry_type&quot;</code> |
| 6 | Источник класс | <code>&quot;source_class&quot;</code> |
| 7 | Источник название | <code>&quot;source_name&quot;</code> |
| 8 | Источник ссылка | <code>&quot;source_reference&quot;</code> |
| 9 | «valid» до | <code>&quot;valid_until&quot;</code> |
| 10 | Место ID | <code>&quot;location_id&quot;</code> |
| 11 | Люди «present» ID | <code>&quot;people_present_ids&quot;</code> |
| 12 | Люди «missing» ID | <code>&quot;people_missing_ids&quot;</code> |
| 13 | «observed» «facts» | <code>&quot;observed_facts&quot;</code> |
| 14 | «unverified» «reports» | <code>&quot;unverified_reports&quot;</code> |
| 15 | «hazards» | <code>&quot;hazards&quot;</code> |
| 16 | «objective» | <code>&quot;objective&quot;</code> |
| 17 | Решение | <code>&quot;decision&quot;</code> |
| 18 | Решение владелец ID | <code>&quot;decision_owner_id&quot;</code> |
| 19 | Безопасность проверка ID | <code>&quot;safety_review_id&quot;</code> |
| 20 | «task» ID | <code>&quot;task_id&quot;</code> |
| 21 | «task» «assigned» в ID | <code>&quot;task_assigned_to_ids&quot;</code> |
| 22 | «task» срок время | <code>&quot;task_due_at&quot;</code> |
| 23 | «task» «checkback» состояние | <code>&quot;task_checkback_state&quot;</code> |
| 24 | Условия остановки | <code>&quot;stop_conditions&quot;</code> |
| 25 | Результат | <code>&quot;result&quot;</code> |
| 26 | Ресурс «changes» | <code>&quot;resource_changes&quot;</code> |
| 27 | Медицинский запись ссылки | <code>&quot;medical_record_refs&quot;</code> |
| 28 | Маршрут ID | <code>&quot;route_id&quot;</code> |
| 29 | Карта ID | <code>&quot;map_id&quot;</code> |
| 30 | Следующий проверка время | <code>&quot;next_review_at&quot;</code> |
| 31 | «handoff» в ID | <code>&quot;handoff_to_id&quot;</code> |
| 32 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 33 | Статус | <code>&quot;status&quot;</code> |
| 34 | «created» кем | <code>&quot;created_by&quot;</code> |
| 35 | Примечания | <code>&quot;notes&quot;</code> |
| 36 | Сценарий ID | <code>&quot;scenario_id&quot;</code> |
| 37 | «cascade» отношение ID | <code>&quot;cascade_relation_id&quot;</code> |
| 38 | «proposed» «card» ссылка | <code>&quot;proposed_card_reference&quot;</code> |
| 39 | «released» «card» ID | <code>&quot;released_card_id&quot;</code> |
| 40 | «released» «card» версия | <code>&quot;released_card_version&quot;</code> |
| 41 | «card» допуск снимок ID | <code>&quot;card_gate_snapshot_id&quot;</code> |
| 42 | «card» выпуск состояние | <code>&quot;card_release_state&quot;</code> |
| 43 | Решение «sequence» снимок | <code>&quot;decision_sequence_snapshot&quot;</code> |
| 44 | Функция назначение ID | <code>&quot;function_assignment_ids&quot;</code> |
| 45 | «buddy» назначение ID | <code>&quot;buddy_assignment_ids&quot;</code> |
| 46 | «accountability» запись ID | <code>&quot;accountability_entry_ids&quot;</code> |
| 47 | Уход разрешение ID | <code>&quot;care_authorization_id&quot;</code> |
| 48 | «handoff» полномочие доказательство ссылка | <code>&quot;handoff_authority_evidence_ref&quot;</code> |
| 49 | «handoff» приёмка состояние | <code>&quot;handoff_acceptance_state&quot;</code> |
| 50 | Ресурс операция ID | <code>&quot;resource_transaction_ids&quot;</code> |
| 51 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 52 | «composition» снимок ID | <code>&quot;composition_snapshot_id&quot;</code> |
| 53 | «composition» допуск состояние | <code>&quot;composition_gate_state&quot;</code> |
| 54 | Локальный «timezone» «iana» | <code>&quot;local_timezone_iana&quot;</code> |
| 55 | «task» «instruction» «recipient» ID | <code>&quot;task_instruction_recipient_ids&quot;</code> |
| 56 | «task» «instruction» «sent» время «utc» | <code>&quot;task_instruction_sent_at_utc&quot;</code> |
| 57 | «task» «checkback» «received» время «utc» | <code>&quot;task_checkback_received_at_utc&quot;</code> |
| 58 | «task» «checkback» «readback» «content» | <code>&quot;task_checkback_readback_content&quot;</code> |
| 59 | «task» «checkback» подтверждённый кем человек ID | <code>&quot;task_checkback_verified_by_person_id&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:59 -->
> [!abstract]- Запись 1 из 4 — TBD
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Запись ID** (<code>&quot;entry_id&quot;</code>): <code>&quot;LOG-0001&quot;</code>
> - **«timestamp» локальный «iso8601» «with» «offset»** (<code>&quot;timestamp_local_iso8601_with_offset&quot;</code>): <code>&quot;&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Запись тип** (<code>&quot;entry_type&quot;</code>): <code>&quot;INITIAL_ACCOUNT&quot;</code>
> - **Источник класс** (<code>&quot;source_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **Источник название** (<code>&quot;source_name&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ссылка** (<code>&quot;source_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до** (<code>&quot;valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **Место ID** (<code>&quot;location_id&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «present» ID** (<code>&quot;people_present_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «missing» ID** (<code>&quot;people_missing_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«observed» «facts»** (<code>&quot;observed_facts&quot;</code>): <code>&quot;&quot;</code>
> - **«unverified» «reports»** (<code>&quot;unverified_reports&quot;</code>): <code>&quot;&quot;</code>
> - **«hazards»** (<code>&quot;hazards&quot;</code>): <code>&quot;&quot;</code>
> - **«objective»** (<code>&quot;objective&quot;</code>): <code>&quot;&quot;</code>
> - **Решение** (<code>&quot;decision&quot;</code>): <code>&quot;&quot;</code>
> - **Решение владелец ID** (<code>&quot;decision_owner_id&quot;</code>): <code>&quot;&quot;</code>
> - **Безопасность проверка ID** (<code>&quot;safety_review_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» ID** (<code>&quot;task_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «assigned» в ID** (<code>&quot;task_assigned_to_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» срок время** (<code>&quot;task_due_at&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» состояние** (<code>&quot;task_checkback_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;&quot;</code>
> - **Результат** (<code>&quot;result&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс «changes»** (<code>&quot;resource_changes&quot;</code>): <code>&quot;&quot;</code>
> - **Медицинский запись ссылки** (<code>&quot;medical_record_refs&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка время** (<code>&quot;next_review_at&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» в ID** (<code>&quot;handoff_to_id&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Шаблон; реальные медицинские детали хранятся отдельно&quot;</code>
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«cascade» отношение ID** (<code>&quot;cascade_relation_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«proposed» «card» ссылка** (<code>&quot;proposed_card_reference&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«released» «card» ID** (<code>&quot;released_card_id&quot;</code>): <code>&quot;&quot;</code>
> - **«released» «card» версия** (<code>&quot;released_card_version&quot;</code>): <code>&quot;&quot;</code>
> - **«card» допуск снимок ID** (<code>&quot;card_gate_snapshot_id&quot;</code>): <code>&quot;&quot;</code>
> - **«card» выпуск состояние** (<code>&quot;card_release_state&quot;</code>): <code>&quot;NOT_AVAILABLE&quot;</code>
> - **Решение «sequence» снимок** (<code>&quot;decision_sequence_snapshot&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Функция назначение ID** (<code>&quot;function_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход разрешение ID** (<code>&quot;care_authorization_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» полномочие доказательство ссылка** (<code>&quot;handoff_authority_evidence_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» приёмка состояние** (<code>&quot;handoff_acceptance_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Ресурс операция ID** (<code>&quot;resource_transaction_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Локальный «timezone» «iana»** (<code>&quot;local_timezone_iana&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «recipient» ID** (<code>&quot;task_instruction_recipient_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «sent» время «utc»** (<code>&quot;task_instruction_sent_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «received» время «utc»** (<code>&quot;task_checkback_received_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «readback» «content»** (<code>&quot;task_checkback_readback_content&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» подтверждённый кем человек ID** (<code>&quot;task_checkback_verified_by_person_id&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:2 cells:59 -->
> [!abstract]- Запись 2 из 4 — TBD
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Запись ID** (<code>&quot;entry_id&quot;</code>): <code>&quot;LOG-0002&quot;</code>
> - **«timestamp» локальный «iso8601» «with» «offset»** (<code>&quot;timestamp_local_iso8601_with_offset&quot;</code>): <code>&quot;&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Запись тип** (<code>&quot;entry_type&quot;</code>): <code>&quot;OFFICIAL_UPDATE&quot;</code>
> - **Источник класс** (<code>&quot;source_class&quot;</code>): <code>&quot;OFFICIAL&quot;</code>
> - **Источник название** (<code>&quot;source_name&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ссылка** (<code>&quot;source_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до** (<code>&quot;valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **Место ID** (<code>&quot;location_id&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «present» ID** (<code>&quot;people_present_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «missing» ID** (<code>&quot;people_missing_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«observed» «facts»** (<code>&quot;observed_facts&quot;</code>): <code>&quot;&quot;</code>
> - **«unverified» «reports»** (<code>&quot;unverified_reports&quot;</code>): <code>&quot;&quot;</code>
> - **«hazards»** (<code>&quot;hazards&quot;</code>): <code>&quot;&quot;</code>
> - **«objective»** (<code>&quot;objective&quot;</code>): <code>&quot;&quot;</code>
> - **Решение** (<code>&quot;decision&quot;</code>): <code>&quot;&quot;</code>
> - **Решение владелец ID** (<code>&quot;decision_owner_id&quot;</code>): <code>&quot;&quot;</code>
> - **Безопасность проверка ID** (<code>&quot;safety_review_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» ID** (<code>&quot;task_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «assigned» в ID** (<code>&quot;task_assigned_to_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» срок время** (<code>&quot;task_due_at&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» состояние** (<code>&quot;task_checkback_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;&quot;</code>
> - **Результат** (<code>&quot;result&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс «changes»** (<code>&quot;resource_changes&quot;</code>): <code>&quot;&quot;</code>
> - **Медицинский запись ссылки** (<code>&quot;medical_record_refs&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка время** (<code>&quot;next_review_at&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» в ID** (<code>&quot;handoff_to_id&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Записать точное время и применимую зону&quot;</code>
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«cascade» отношение ID** (<code>&quot;cascade_relation_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«proposed» «card» ссылка** (<code>&quot;proposed_card_reference&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«released» «card» ID** (<code>&quot;released_card_id&quot;</code>): <code>&quot;&quot;</code>
> - **«released» «card» версия** (<code>&quot;released_card_version&quot;</code>): <code>&quot;&quot;</code>
> - **«card» допуск снимок ID** (<code>&quot;card_gate_snapshot_id&quot;</code>): <code>&quot;&quot;</code>
> - **«card» выпуск состояние** (<code>&quot;card_release_state&quot;</code>): <code>&quot;NOT_AVAILABLE&quot;</code>
> - **Решение «sequence» снимок** (<code>&quot;decision_sequence_snapshot&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Функция назначение ID** (<code>&quot;function_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход разрешение ID** (<code>&quot;care_authorization_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» полномочие доказательство ссылка** (<code>&quot;handoff_authority_evidence_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» приёмка состояние** (<code>&quot;handoff_acceptance_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Ресурс операция ID** (<code>&quot;resource_transaction_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Локальный «timezone» «iana»** (<code>&quot;local_timezone_iana&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «recipient» ID** (<code>&quot;task_instruction_recipient_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «sent» время «utc»** (<code>&quot;task_instruction_sent_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «received» время «utc»** (<code>&quot;task_checkback_received_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «readback» «content»** (<code>&quot;task_checkback_readback_content&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» подтверждённый кем человек ID** (<code>&quot;task_checkback_verified_by_person_id&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:3 cells:59 -->
> [!abstract]- Запись 3 из 4 — TBD
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Запись ID** (<code>&quot;entry_id&quot;</code>): <code>&quot;LOG-0003&quot;</code>
> - **«timestamp» локальный «iso8601» «with» «offset»** (<code>&quot;timestamp_local_iso8601_with_offset&quot;</code>): <code>&quot;&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Запись тип** (<code>&quot;entry_type&quot;</code>): <code>&quot;DECISION&quot;</code>
> - **Источник класс** (<code>&quot;source_class&quot;</code>): <code>&quot;&quot;</code>
> - **Источник название** (<code>&quot;source_name&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ссылка** (<code>&quot;source_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до** (<code>&quot;valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **Место ID** (<code>&quot;location_id&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «present» ID** (<code>&quot;people_present_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «missing» ID** (<code>&quot;people_missing_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«observed» «facts»** (<code>&quot;observed_facts&quot;</code>): <code>&quot;&quot;</code>
> - **«unverified» «reports»** (<code>&quot;unverified_reports&quot;</code>): <code>&quot;&quot;</code>
> - **«hazards»** (<code>&quot;hazards&quot;</code>): <code>&quot;&quot;</code>
> - **«objective»** (<code>&quot;objective&quot;</code>): <code>&quot;&quot;</code>
> - **Решение** (<code>&quot;decision&quot;</code>): <code>&quot;&quot;</code>
> - **Решение владелец ID** (<code>&quot;decision_owner_id&quot;</code>): <code>&quot;&quot;</code>
> - **Безопасность проверка ID** (<code>&quot;safety_review_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» ID** (<code>&quot;task_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «assigned» в ID** (<code>&quot;task_assigned_to_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» срок время** (<code>&quot;task_due_at&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» состояние** (<code>&quot;task_checkback_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;&quot;</code>
> - **Результат** (<code>&quot;result&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс «changes»** (<code>&quot;resource_changes&quot;</code>): <code>&quot;&quot;</code>
> - **Медицинский запись ссылки** (<code>&quot;medical_record_refs&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка время** (<code>&quot;next_review_at&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» в ID** (<code>&quot;handoff_to_id&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Факт неизвестное решение ответственный критерий отмены&quot;</code>
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«cascade» отношение ID** (<code>&quot;cascade_relation_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«proposed» «card» ссылка** (<code>&quot;proposed_card_reference&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«released» «card» ID** (<code>&quot;released_card_id&quot;</code>): <code>&quot;&quot;</code>
> - **«released» «card» версия** (<code>&quot;released_card_version&quot;</code>): <code>&quot;&quot;</code>
> - **«card» допуск снимок ID** (<code>&quot;card_gate_snapshot_id&quot;</code>): <code>&quot;&quot;</code>
> - **«card» выпуск состояние** (<code>&quot;card_release_state&quot;</code>): <code>&quot;NOT_AVAILABLE&quot;</code>
> - **Решение «sequence» снимок** (<code>&quot;decision_sequence_snapshot&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Функция назначение ID** (<code>&quot;function_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход разрешение ID** (<code>&quot;care_authorization_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» полномочие доказательство ссылка** (<code>&quot;handoff_authority_evidence_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» приёмка состояние** (<code>&quot;handoff_acceptance_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Ресурс операция ID** (<code>&quot;resource_transaction_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Локальный «timezone» «iana»** (<code>&quot;local_timezone_iana&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «recipient» ID** (<code>&quot;task_instruction_recipient_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «sent» время «utc»** (<code>&quot;task_instruction_sent_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «received» время «utc»** (<code>&quot;task_checkback_received_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «readback» «content»** (<code>&quot;task_checkback_readback_content&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» подтверждённый кем человек ID** (<code>&quot;task_checkback_verified_by_person_id&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:4 cells:59 -->
> [!abstract]- Запись 4 из 4 — TBD
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Запись ID** (<code>&quot;entry_id&quot;</code>): <code>&quot;LOG-0004&quot;</code>
> - **«timestamp» локальный «iso8601» «with» «offset»** (<code>&quot;timestamp_local_iso8601_with_offset&quot;</code>): <code>&quot;&quot;</code>
> - **«timestamp» «utc»** (<code>&quot;timestamp_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Запись тип** (<code>&quot;entry_type&quot;</code>): <code>&quot;HANDOFF&quot;</code>
> - **Источник класс** (<code>&quot;source_class&quot;</code>): <code>&quot;&quot;</code>
> - **Источник название** (<code>&quot;source_name&quot;</code>): <code>&quot;&quot;</code>
> - **Источник ссылка** (<code>&quot;source_reference&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до** (<code>&quot;valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **Место ID** (<code>&quot;location_id&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «present» ID** (<code>&quot;people_present_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Люди «missing» ID** (<code>&quot;people_missing_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«observed» «facts»** (<code>&quot;observed_facts&quot;</code>): <code>&quot;&quot;</code>
> - **«unverified» «reports»** (<code>&quot;unverified_reports&quot;</code>): <code>&quot;&quot;</code>
> - **«hazards»** (<code>&quot;hazards&quot;</code>): <code>&quot;&quot;</code>
> - **«objective»** (<code>&quot;objective&quot;</code>): <code>&quot;&quot;</code>
> - **Решение** (<code>&quot;decision&quot;</code>): <code>&quot;&quot;</code>
> - **Решение владелец ID** (<code>&quot;decision_owner_id&quot;</code>): <code>&quot;&quot;</code>
> - **Безопасность проверка ID** (<code>&quot;safety_review_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» ID** (<code>&quot;task_id&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «assigned» в ID** (<code>&quot;task_assigned_to_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» срок время** (<code>&quot;task_due_at&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» состояние** (<code>&quot;task_checkback_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;&quot;</code>
> - **Результат** (<code>&quot;result&quot;</code>): <code>&quot;&quot;</code>
> - **Ресурс «changes»** (<code>&quot;resource_changes&quot;</code>): <code>&quot;&quot;</code>
> - **Медицинский запись ссылки** (<code>&quot;medical_record_refs&quot;</code>): <code>&quot;&quot;</code>
> - **Маршрут ID** (<code>&quot;route_id&quot;</code>): <code>&quot;&quot;</code>
> - **Карта ID** (<code>&quot;map_id&quot;</code>): <code>&quot;&quot;</code>
> - **Следующий проверка время** (<code>&quot;next_review_at&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» в ID** (<code>&quot;handoff_to_id&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Статус** (<code>&quot;status&quot;</code>): <code>&quot;OPEN&quot;</code>
> - **«created» кем** (<code>&quot;created_by&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Незавершённые задачи и следующая проверка&quot;</code>
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«cascade» отношение ID** (<code>&quot;cascade_relation_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«proposed» «card» ссылка** (<code>&quot;proposed_card_reference&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«released» «card» ID** (<code>&quot;released_card_id&quot;</code>): <code>&quot;&quot;</code>
> - **«released» «card» версия** (<code>&quot;released_card_version&quot;</code>): <code>&quot;&quot;</code>
> - **«card» допуск снимок ID** (<code>&quot;card_gate_snapshot_id&quot;</code>): <code>&quot;&quot;</code>
> - **«card» выпуск состояние** (<code>&quot;card_release_state&quot;</code>): <code>&quot;NOT_AVAILABLE&quot;</code>
> - **Решение «sequence» снимок** (<code>&quot;decision_sequence_snapshot&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Функция назначение ID** (<code>&quot;function_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«accountability» запись ID** (<code>&quot;accountability_entry_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Уход разрешение ID** (<code>&quot;care_authorization_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» полномочие доказательство ссылка** (<code>&quot;handoff_authority_evidence_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» приёмка состояние** (<code>&quot;handoff_acceptance_state&quot;</code>): <code>&quot;NOT_APPLICABLE&quot;</code>
> - **Ресурс операция ID** (<code>&quot;resource_transaction_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» снимок ID** (<code>&quot;composition_snapshot_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«composition» допуск состояние** (<code>&quot;composition_gate_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Локальный «timezone» «iana»** (<code>&quot;local_timezone_iana&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «recipient» ID** (<code>&quot;task_instruction_recipient_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «instruction» «sent» время «utc»** (<code>&quot;task_instruction_sent_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «received» время «utc»** (<code>&quot;task_checkback_received_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» «readback» «content»** (<code>&quot;task_checkback_readback_content&quot;</code>): <code>&quot;&quot;</code>
> - **«task» «checkback» подтверждённый кем человек ID** (<code>&quot;task_checkback_verified_by_person_id&quot;</code>): <code>&quot;&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
