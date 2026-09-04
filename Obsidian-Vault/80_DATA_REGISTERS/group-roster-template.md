---
id: "DATA-REGISTER-cd0c40392c20a535"
type: "generated-data-register-view"
title: "Состав участников группы — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-roster-template.csv"
source_sha256: "5830fd20777eb06e03b71436abb16b52a9995e0dec8d995a1e89f65e9bac81e6"
source_bytes: 5242
source_row_count: 7
source_column_count: 56
source_cell_count: 392
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-roster-template.csv -->

# Состав участников группы — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 7
- **Полей в каждой записи:** 56
- **Ячеек данных, включая пустые:** 392
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `5830fd20777eb06e03b71436abb16b52a9995e0dec8d995a1e89f65e9bac81e6`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Человек ID | <code>&quot;person_id&quot;</code> |
| 2 | «display» название «or» «alias» | <code>&quot;display_name_or_alias&quot;</code> |
| 3 | «sensitivity» | <code>&quot;sensitivity&quot;</code> |
| 4 | «age» «band» | <code>&quot;age_band&quot;</code> |
| 5 | «languages» | <code>&quot;languages&quot;</code> |
| 6 | Аварийный «phrase» «languages» | <code>&quot;emergency_phrase_languages&quot;</code> |
| 7 | «communication» профиль | <code>&quot;communication_profile&quot;</code> |
| 8 | «mobility» профиль | <code>&quot;mobility_profile&quot;</code> |
| 9 | «sensory» профиль | <code>&quot;sensory_profile&quot;</code> |
| 10 | «cognitive» «support» | <code>&quot;cognitive_support&quot;</code> |
| 11 | «caregiver» требуемый | <code>&quot;caregiver_required&quot;</code> |
| 12 | «caregiver» основной ID | <code>&quot;caregiver_primary_id&quot;</code> |
| 13 | «caregiver» резервный ID | <code>&quot;caregiver_backup_id&quot;</code> |
| 14 | «buddy» основной ID | <code>&quot;buddy_primary_id&quot;</code> |
| 15 | «buddy» резервный ID | <code>&quot;buddy_backup_id&quot;</code> |
| 16 | «default» роль | <code>&quot;default_role&quot;</code> |
| 17 | Резервный «roles» | <code>&quot;backup_roles&quot;</code> |
| 18 | Преемственность «order» | <code>&quot;succession_order&quot;</code> |
| 19 | Внешний контакт ID | <code>&quot;external_contact_id&quot;</code> |
| 20 | «meetup» «r1» ID | <code>&quot;meetup_r1_id&quot;</code> |
| 21 | «meetup» «r2» ID | <code>&quot;meetup_r2_id&quot;</code> |
| 22 | «meetup» «r3» ID | <code>&quot;meetup_r3_id&quot;</code> |
| 23 | «personal» «e1» ID | <code>&quot;personal_e1_id&quot;</code> |
| 24 | Медицинский профиль ссылка | <code>&quot;medical_profile_ref&quot;</code> |
| 25 | «critical» «medication» ссылка | <code>&quot;critical_medication_ref&quot;</code> |
| 26 | «critical» «device» ссылка | <code>&quot;critical_device_ref&quot;</code> |
| 27 | «dietary» «constraints» ссылка | <code>&quot;dietary_constraints_ref&quot;</code> |
| 28 | «ppe» «size» ссылка | <code>&quot;ppe_size_ref&quot;</code> |
| 29 | «pet» «responsibility» ID | <code>&quot;pet_responsibility_ids&quot;</code> |
| 30 | «transport» «constraints» | <code>&quot;transport_constraints&quot;</code> |
| 31 | «can» «self» «evacuate» состояние | <code>&quot;can_self_evacuate_state&quot;</code> |
| 32 | «can» «carry» «personal» «e1» состояние | <code>&quot;can_carry_personal_e1_state&quot;</code> |
| 33 | «navigation» обучение ссылка | <code>&quot;navigation_training_ref&quot;</code> |
| 34 | «first» «aid» обучение ссылка | <code>&quot;first_aid_training_ref&quot;</code> |
| 35 | Роль допуск запись ссылка | <code>&quot;role_gate_record_ref&quot;</code> |
| 36 | Согласие в «share» «with» аварийный «services» | <code>&quot;consent_to_share_with_emergency_services&quot;</code> |
| 37 | «last» «confirmed» время | <code>&quot;last_confirmed_at&quot;</code> |
| 38 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 39 | Владелец | <code>&quot;owner&quot;</code> |
| 40 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 41 | Примечания | <code>&quot;notes&quot;</code> |
| 42 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 43 | «sensitive» «registry» ссылка | <code>&quot;sensitive_registry_ref&quot;</code> |
| 44 | Операционный «view» ID | <code>&quot;operational_view_id&quot;</code> |
| 45 | «redacted» «copy» ID | <code>&quot;redacted_copy_id&quot;</code> |
| 46 | «encryption» требуемый | <code>&quot;encryption_required&quot;</code> |
| 47 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 48 | «access» «control» состояние | <code>&quot;access_control_state&quot;</code> |
| 49 | «retention» «rule» | <code>&quot;retention_rule&quot;</code> |
| 50 | Приватность проверенный время | <code>&quot;privacy_reviewed_at&quot;</code> |
| 51 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |
| 52 | Назначение полномочие | <code>&quot;assignment_authority&quot;</code> |
| 53 | Прежний роль «fields» состояние | <code>&quot;legacy_role_fields_state&quot;</code> |
| 54 | «buddy» «fields» состояние | <code>&quot;buddy_fields_state&quot;</code> |
| 55 | «caregiver» «fields» состояние | <code>&quot;caregiver_fields_state&quot;</code> |
| 56 | «roster» ревизия ID | <code>&quot;roster_revision_id&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:56 -->
> [!abstract]- Запись 1 из 7 — P01
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-01&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;ADULT&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;1&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример без реального человека&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P01&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:2 cells:56 -->
> [!abstract]- Запись 2 из 7 — P02
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-02&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;ADULT&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;NO&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;2&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример без реального человека&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P02&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:3 cells:56 -->
> [!abstract]- Запись 3 из 7 — P03
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-03&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;3&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Роль не означает медицинскую квалификацию&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P03&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:4 cells:56 -->
> [!abstract]- Запись 4 из 7 — P04
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-04&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;4&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример без реального человека&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P04&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:5 cells:56 -->
> [!abstract]- Запись 5 из 7 — P05
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-05&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;5&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Радиопередача только при законном допуске&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P05&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:6 cells:56 -->
> [!abstract]- Запись 6 из 7 — P06
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-06&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;6&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Опасные работы только в пределах квалификации&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P06&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

<!-- record:7 cells:56 -->
> [!abstract]- Запись 7 из 7 — P07
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P07&quot;</code>
> - **«display» название «or» «alias»** (<code>&quot;display_name_or_alias&quot;</code>): <code>&quot;ALIAS-07&quot;</code>
> - **«sensitivity»** (<code>&quot;sensitivity&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«age» «band»** (<code>&quot;age_band&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный «phrase» «languages»** (<code>&quot;emergency_phrase_languages&quot;</code>): <code>&quot;&quot;</code>
> - **«communication» профиль** (<code>&quot;communication_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«mobility» профиль** (<code>&quot;mobility_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«sensory» профиль** (<code>&quot;sensory_profile&quot;</code>): <code>&quot;&quot;</code>
> - **«cognitive» «support»** (<code>&quot;cognitive_support&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» требуемый** (<code>&quot;caregiver_required&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«caregiver» основной ID** (<code>&quot;caregiver_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«caregiver» резервный ID** (<code>&quot;caregiver_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» основной ID** (<code>&quot;buddy_primary_id&quot;</code>): <code>&quot;&quot;</code>
> - **«buddy» резервный ID** (<code>&quot;buddy_backup_id&quot;</code>): <code>&quot;&quot;</code>
> - **«default» роль** (<code>&quot;default_role&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **Резервный «roles»** (<code>&quot;backup_roles&quot;</code>): <code>&quot;&quot;</code>
> - **Преемственность «order»** (<code>&quot;succession_order&quot;</code>): <code>&quot;7&quot;</code>
> - **Внешний контакт ID** (<code>&quot;external_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«meetup» «r1» ID** (<code>&quot;meetup_r1_id&quot;</code>): <code>&quot;R1&quot;</code>
> - **«meetup» «r2» ID** (<code>&quot;meetup_r2_id&quot;</code>): <code>&quot;R2&quot;</code>
> - **«meetup» «r3» ID** (<code>&quot;meetup_r3_id&quot;</code>): <code>&quot;R3&quot;</code>
> - **«personal» «e1» ID** (<code>&quot;personal_e1_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Медицинский профиль ссылка** (<code>&quot;medical_profile_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«critical» «medication» ссылка** (<code>&quot;critical_medication_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«critical» «device» ссылка** (<code>&quot;critical_device_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«dietary» «constraints» ссылка** (<code>&quot;dietary_constraints_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«ppe» «size» ссылка** (<code>&quot;ppe_size_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«pet» «responsibility» ID** (<code>&quot;pet_responsibility_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«transport» «constraints»** (<code>&quot;transport_constraints&quot;</code>): <code>&quot;&quot;</code>
> - **«can» «self» «evacuate» состояние** (<code>&quot;can_self_evacuate_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«can» «carry» «personal» «e1» состояние** (<code>&quot;can_carry_personal_e1_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«navigation» обучение ссылка** (<code>&quot;navigation_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«first» «aid» обучение ссылка** (<code>&quot;first_aid_training_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Согласие в «share» «with» аварийный «services»** (<code>&quot;consent_to_share_with_emergency_services&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **«last» «confirmed» время** (<code>&quot;last_confirmed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример без реального человека&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **«sensitive» «registry» ссылка** (<code>&quot;sensitive_registry_ref&quot;</code>): <code>&quot;SELF_RESTRICTED_MASTER&quot;</code>
> - **Операционный «view» ID** (<code>&quot;operational_view_id&quot;</code>): <code>&quot;OPR-P07&quot;</code>
> - **«redacted» «copy» ID** (<code>&quot;redacted_copy_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность проверенный время** (<code>&quot;privacy_reviewed_at&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Назначение полномочие** (<code>&quot;assignment_authority&quot;</code>): <code>&quot;group-function-assignment-template.csv&quot;</code>
> - **Прежний роль «fields» состояние** (<code>&quot;legacy_role_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_HINTS&quot;</code>
> - **«buddy» «fields» состояние** (<code>&quot;buddy_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_SEE_BUDDY_REGISTER&quot;</code>
> - **«caregiver» «fields» состояние** (<code>&quot;caregiver_fields_state&quot;</code>): <code>&quot;NON_AUTHORITATIVE_UNTIL_CARE_AUTHORIZATION&quot;</code>
> - **«roster» ревизия ID** (<code>&quot;roster_revision_id&quot;</code>): <code>&quot;ROSTER-EXAMPLE-R0&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
