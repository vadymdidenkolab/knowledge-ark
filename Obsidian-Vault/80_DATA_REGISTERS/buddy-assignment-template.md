---
id: "DATA-REGISTER-f3876851e0fb0981"
type: "generated-data-register-view"
title: "Назначения напарников — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "buddy-assignment-template.csv"
source_sha256: "57b637bbfd63bd1b91925bc42e7c1ecc24967ae9723bdae3bc9220888d2ba15b"
source_bytes: 2489
source_row_count: 7
source_column_count: 24
source_cell_count: 168
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: buddy-assignment-template.csv -->

# Назначения напарников — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 7
- **Полей в каждой записи:** 24
- **Ячеек данных, включая пустые:** 168
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `57b637bbfd63bd1b91925bc42e7c1ecc24967ae9723bdae3bc9220888d2ba15b`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «buddy» назначение ID | <code>&quot;buddy_assignment_id&quot;</code> |
| 2 | Назначение тип | <code>&quot;assignment_type&quot;</code> |
| 3 | «member» человек ID | <code>&quot;member_person_ids&quot;</code> |
| 4 | Внешний контакт ID | <code>&quot;external_contact_id&quot;</code> |
| 5 | «activation» область | <code>&quot;activation_scope&quot;</code> |
| 6 | «subgroup» ID | <code>&quot;subgroup_id&quot;</code> |
| 7 | «effective» из | <code>&quot;effective_from&quot;</code> |
| 8 | «effective» до | <code>&quot;effective_until&quot;</code> |
| 9 | Основной «checkin» метод | <code>&quot;primary_checkin_method&quot;</code> |
| 10 | «alternate» «checkin» метод | <code>&quot;alternate_checkin_method&quot;</code> |
| 11 | «contingency» «checkin» метод | <code>&quot;contingency_checkin_method&quot;</code> |
| 12 | Аварийный «checkin» метод | <code>&quot;emergency_checkin_method&quot;</code> |
| 13 | «channel» отказ отрасль доказательство | <code>&quot;channel_failure_domain_evidence&quot;</code> |
| 14 | «pace» испытание состояние | <code>&quot;pace_test_state&quot;</code> |
| 15 | «missed» «checkin» триггер | <code>&quot;missed_checkin_trigger&quot;</code> |
| 16 | «escalation» «sequence» | <code>&quot;escalation_sequence&quot;</code> |
| 17 | «child» «or» «dependent» «constraints» | <code>&quot;child_or_dependent_constraints&quot;</code> |
| 18 | Согласие состояние | <code>&quot;consent_state&quot;</code> |
| 19 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 20 | Назначение статус | <code>&quot;assignment_status&quot;</code> |
| 21 | Владелец | <code>&quot;owner&quot;</code> |
| 22 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 23 | Примечания | <code>&quot;notes&quot;</code> |
| 24 | Группа профиль ID | <code>&quot;group_profile_ids&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:24 -->
> [!abstract]- Запись 1 из 7 — BUD-01
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-01&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;PAIR&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P01|P02&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N2|N4|N5|N6|N7&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример пары; взаимность и способность не подтверждены&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N2|GP-N4|GP-N5|GP-N6|GP-N7&quot;</code>
>

<!-- record:2 cells:24 -->
> [!abstract]- Запись 2 из 7 — BUD-02
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-02&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;PAIR&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P03|P04&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N4|N6|N7&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример пары; взаимность и способность не подтверждены&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N4|GP-N6|GP-N7&quot;</code>
>

<!-- record:3 cells:24 -->
> [!abstract]- Запись 3 из 7 — BUD-03
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-03&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;TRIAD&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P05|P06|P07&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N7&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;Не назначать ребёнка единственным ответственным&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример триады для нечётного состава&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N7&quot;</code>
>

<!-- record:4 cells:24 -->
> [!abstract]- Запись 4 из 7 — BUD-N1-EXT
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-N1-EXT&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;REMOTE_BUDDY&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N1&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;REMOTE&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;Не заменяет физическую помощь&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Внешний check-in требует реального контакта и согласованной эскалации&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N1&quot;</code>
>

<!-- record:5 cells:24 -->
> [!abstract]- Запись 5 из 7 — BUD-N3-TRIAD
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-N3-TRIAD&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;TRIAD&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P01|P02|P03&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N3&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Триада для состава N3; только пример&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N3&quot;</code>
>

<!-- record:6 cells:24 -->
> [!abstract]- Запись 6 из 7 — BUD-N5-TRIAD
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-N5-TRIAD&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;TRIAD&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P03|P04|P05&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N5&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Вместе с BUD-01 покрывает N5; только пример&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N5&quot;</code>
>

<!-- record:7 cells:24 -->
> [!abstract]- Запись 7 из 7 — BUD-N6-PAIR
> - **«buddy» назначение ID** (<code>&quot;buddy_assignment_id&quot;</code>): <code>&quot;BUD-N6-PAIR&quot;</code>
> - **Назначение тип** (<code>&quot;assignment_type&quot;</code>): <code>&quot;PAIR&quot;</code>
> - **«member» человек ID** (<code>&quot;member_person_ids&quot;</code>): <code>&quot;P05|P06&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;N6&quot;</code>
> - **«subgroup» ID** (<code>&quot;subgroup_id&quot;</code>): <code>&quot;MAIN&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Основной «checkin» метод** (<code>&quot;primary_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «checkin» метод** (<code>&quot;alternate_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «checkin» метод** (<code>&quot;contingency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «checkin» метод** (<code>&quot;emergency_checkin_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«missed» «checkin» триггер** (<code>&quot;missed_checkin_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» «sequence»** (<code>&quot;escalation_sequence&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«child» «or» «dependent» «constraints»** (<code>&quot;child_or_dependent_constraints&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Вместе с BUD-01/BUD-02 покрывает N6; только пример&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_ids&quot;</code>): <code>&quot;GP-N6&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
