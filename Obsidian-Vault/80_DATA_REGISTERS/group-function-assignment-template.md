---
id: "DATA-REGISTER-12bbe92b946b60bc"
type: "generated-data-register-view"
title: "Назначение функций в группе — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "group-function-assignment-template.csv"
source_sha256: "e532194740fd5126a7c166bb58447f547e7abfa558d3bc5574523f6d100a91d1"
source_bytes: 24279
source_row_count: 49
source_column_count: 26
source_cell_count: 1274
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: group-function-assignment-template.csv -->

# Назначение функций в группе — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 49
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 1274
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `e532194740fd5126a7c166bb58447f547e7abfa558d3bc5574523f6d100a91d1`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Назначение ID | <code>&quot;assignment_id&quot;</code> |
| 2 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 3 | Функция код | <code>&quot;function_code&quot;</code> |
| 4 | «activation» область | <code>&quot;activation_scope&quot;</code> |
| 5 | Основной человек ID | <code>&quot;primary_person_id&quot;</code> |
| 6 | Резервный человек ID | <code>&quot;backup_person_id&quot;</code> |
| 7 | «successor» человек ID | <code>&quot;successor_person_ids&quot;</code> |
| 8 | Внешний резервный контакт ID | <code>&quot;external_backup_contact_id&quot;</code> |
| 9 | Роль допуск запись ссылка | <code>&quot;role_gate_record_ref&quot;</code> |
| 10 | Роль допуск состояние | <code>&quot;role_gate_state&quot;</code> |
| 11 | «task» область | <code>&quot;task_scope&quot;</code> |
| 12 | Запрещённый область | <code>&quot;prohibited_scope&quot;</code> |
| 13 | «effective» из | <code>&quot;effective_from&quot;</code> |
| 14 | «effective» до | <code>&quot;effective_until&quot;</code> |
| 15 | «handover» состояние | <code>&quot;handover_state&quot;</code> |
| 16 | Назначение статус | <code>&quot;assignment_status&quot;</code> |
| 17 | Владелец | <code>&quot;owner&quot;</code> |
| 18 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 19 | Примечания | <code>&quot;notes&quot;</code> |
| 20 | Приёмка запись ссылки | <code>&quot;acceptance_record_refs&quot;</code> |
| 21 | Приёмка состояние | <code>&quot;acceptance_state&quot;</code> |
| 22 | Доступность «window» ссылка | <code>&quot;availability_window_ref&quot;</code> |
| 23 | Доступность состояние | <code>&quot;availability_state&quot;</code> |
| 24 | «concurrency» план ссылка | <code>&quot;concurrency_plan_ref&quot;</code> |
| 25 | «concurrency» мощность состояние | <code>&quot;concurrency_capacity_state&quot;</code> |
| 26 | Назначение «activation» допуск состояние | <code>&quot;assignment_activation_gate_state&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:2 cells:26 -->
> [!abstract]- Запись 2 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:3 cells:26 -->
> [!abstract]- Запись 3 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:4 cells:26 -->
> [!abstract]- Запись 4 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:5 cells:26 -->
> [!abstract]- Запись 5 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:6 cells:26 -->
> [!abstract]- Запись 6 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:7 cells:26 -->
> [!abstract]- Запись 7 из 49 — GP-N1
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Один человек выполняет функции последовательно; EXT-01 является эскалацией, а не доказанным исполнителем функции&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:8 cells:26 -->
> [!abstract]- Запись 8 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:9 cells:26 -->
> [!abstract]- Запись 9 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:10 cells:26 -->
> [!abstract]- Запись 10 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:11 cells:26 -->
> [!abstract]- Запись 11 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:12 cells:26 -->
> [!abstract]- Запись 12 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:13 cells:26 -->
> [!abstract]- Запись 13 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:14 cells:26 -->
> [!abstract]- Запись 14 из 49 — GP-N2
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N2-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N2&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:15 cells:26 -->
> [!abstract]- Запись 15 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:16 cells:26 -->
> [!abstract]- Запись 16 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:17 cells:26 -->
> [!abstract]- Запись 17 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:18 cells:26 -->
> [!abstract]- Запись 18 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:19 cells:26 -->
> [!abstract]- Запись 19 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:20 cells:26 -->
> [!abstract]- Запись 20 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:21 cells:26 -->
> [!abstract]- Запись 21 из 49 — GP-N3
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N3-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N3&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:22 cells:26 -->
> [!abstract]- Запись 22 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:23 cells:26 -->
> [!abstract]- Запись 23 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:24 cells:26 -->
> [!abstract]- Запись 24 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:25 cells:26 -->
> [!abstract]- Запись 25 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:26 cells:26 -->
> [!abstract]- Запись 26 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:27 cells:26 -->
> [!abstract]- Запись 27 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:28 cells:26 -->
> [!abstract]- Запись 28 из 49 — GP-N4
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N4-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N4&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:29 cells:26 -->
> [!abstract]- Запись 29 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:30 cells:26 -->
> [!abstract]- Запись 30 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:31 cells:26 -->
> [!abstract]- Запись 31 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:32 cells:26 -->
> [!abstract]- Запись 32 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:33 cells:26 -->
> [!abstract]- Запись 33 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:34 cells:26 -->
> [!abstract]- Запись 34 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:35 cells:26 -->
> [!abstract]- Запись 35 из 49 — GP-N5
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N5-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N5&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:36 cells:26 -->
> [!abstract]- Запись 36 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:37 cells:26 -->
> [!abstract]- Запись 37 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:38 cells:26 -->
> [!abstract]- Запись 38 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:39 cells:26 -->
> [!abstract]- Запись 39 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:40 cells:26 -->
> [!abstract]- Запись 40 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:41 cells:26 -->
> [!abstract]- Запись 41 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:42 cells:26 -->
> [!abstract]- Запись 42 из 49 — GP-N6
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N6-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N6&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:43 cells:26 -->
> [!abstract]- Запись 43 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P03&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Цель периода роли ресурсы связь&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Клинические и профессиональные решения вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:44 cells:26 -->
> [!abstract]- Запись 44 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-SAFETY&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SAFETY_AND_DEPUTY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Safety veto hazards fatigue succession&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Вход в опасную зону без допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:45 cells:26 -->
> [!abstract]- Запись 45 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-MED&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;MEDICAL_CONTINUITY&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P03&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Первая помощь в scope и continuity индивидуальных планов&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Диагностика назначения инвазивные действия вне полномочий&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:46 cells:26 -->
> [!abstract]- Запись 46 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-LOG&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;LOGISTICS_WASH_FOOD&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P04&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Вода санитария питание запасы&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Объявление непроверенной воды питьевой&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:47 cells:26 -->
> [!abstract]- Запись 47 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-COMMS&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;COMMS_INFO_NAV&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P05&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Официальная информация PACE карты журнал&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Незаконная передача или публикация чувствительных координат&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:48 cells:26 -->
> [!abstract]- Запись 48 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-SHEL&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;SHELTER_ENERGY_REPAIR&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P06&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P07&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P01&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Укрытие энергия безопасный ремонт&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Работы с сетью газом конструкцией вне допуска&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

<!-- record:49 cells:26 -->
> [!abstract]- Запись 49 из 49 — GP-N7
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N7-CARE&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;CARE_ACCESSIBILITY_PETS&quot;</code>
> - **«activation» область** (<code>&quot;activation_scope&quot;</code>): <code>&quot;GP-N7&quot;</code>
> - **Основной человек ID** (<code>&quot;primary_person_id&quot;</code>): <code>&quot;P07&quot;</code>
> - **Резервный человек ID** (<code>&quot;backup_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **«successor» человек ID** (<code>&quot;successor_person_ids&quot;</code>): <code>&quot;P02&quot;</code>
> - **Внешний резервный контакт ID** (<code>&quot;external_backup_contact_id&quot;</code>): <code>&quot;&quot;</code>
> - **Роль допуск запись ссылка** (<code>&quot;role_gate_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«task» область** (<code>&quot;task_scope&quot;</code>): <code>&quot;Доступность dependent care дети животные&quot;</code>
> - **Запрещённый область** (<code>&quot;prohibited_scope&quot;</code>): <code>&quot;Передача зависимого лица без подтверждённого права и identity&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **«handover» состояние** (<code>&quot;handover_state&quot;</code>): <code>&quot;NOT_EFFECTIVE&quot;</code>
> - **Назначение статус** (<code>&quot;assignment_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профильный пример; пригодность и согласие не подтверждены&quot;</code>
> - **Приёмка запись ссылки** (<code>&quot;acceptance_record_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Доступность «window» ссылка** (<code>&quot;availability_window_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«concurrency» план ссылка** (<code>&quot;concurrency_plan_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«concurrency» мощность состояние** (<code>&quot;concurrency_capacity_state&quot;</code>): <code>&quot;NOT_ASSESSED&quot;</code>
> - **Назначение «activation» допуск состояние** (<code>&quot;assignment_activation_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
