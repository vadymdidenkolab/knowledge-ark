---
id: "DATA-REGISTER-cbde7e0936c2c685"
type: "generated-data-register-view"
title: "Классы решений и полномочий"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "decision-class-register.csv"
source_sha256: "965f19ce850ed062821667c92b8eff90f37b22c9d27da305e3c1d5af0216c030"
source_bytes: 5550
source_row_count: 20
source_column_count: 5
source_cell_count: 100
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: decision-class-register.csv -->

# Классы решений и полномочий

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 20
- **Полей в каждой записи:** 5
- **Ячеек данных, включая пустые:** 100
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `965f19ce850ed062821667c92b8eff90f37b22c9d27da305e3c1d5af0216c030`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Решение класс ID | <code>&quot;decision_class_id&quot;</code> |
| 2 | «meaning» на русском | <code>&quot;meaning_ru&quot;</code> |
| 3 | «default» область | <code>&quot;default_scope&quot;</code> |
| 4 | Условие «or» граница | <code>&quot;condition_or_boundary&quot;</code> |
| 5 | Статус выпуска | <code>&quot;release_status&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:5 -->
> [!abstract]- Запись 1 из 20 — ASSESS_DEPENDENCIES
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Определить людей и критические функции уже теряющие безопасность&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не заменяет оценку опасной электрической сцены&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:2 cells:5 -->
> [!abstract]- Запись 2 из 20 — ASSESS_RED_FLAGS
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Определить безопасную развилку срочности без постановки диагноза&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Требует профессионально проверенных красных флагов&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:3 cells:5 -->
> [!abstract]- Запись 3 из 20 — CALL_112
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Вызвать экстренные службы при непосредственной угрозе&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PORTUGAL&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не задерживать физическую защиту когда звонок небезопасен&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:4 cells:5 -->
> [!abstract]- Запись 4 из 20 — CALL_112_OR_URGENT_MATERNITY
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;CALL_112_OR_URGENT_MATERNITY&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Экстренный или срочный maternity-route по проверенным признакам&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PORTUGAL&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Требует локальной акушерской карточки и персонального плана&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:5 cells:5 -->
> [!abstract]- Запись 5 из 20 — CALL_CIAV
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;CALL_CIAV&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Связаться с CIAV при возможном отравлении&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PORTUGAL&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;112 имеет приоритет при непосредственной угрозе жизни&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:6 cells:5 -->
> [!abstract]- Запись 6 из 20 — DISCREET_SAFETY
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Сохранить безопасность без раскрытия плана контролирующему лицу&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не использовать контролируемое устройство если это повышает риск&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:7 cells:5 -->
> [!abstract]- Запись 7 из 20 — DO_NOT_TOUCH_OR_ENTER
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;DO_NOT_TOUCH_OR_ENTER&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Не касаться и не входить в опасную энергетическую или замкнутую среду&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;SCENE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Изоляция только если безопасна и разрешена&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:8 cells:5 -->
> [!abstract]- Запись 8 из 20 — ESCAPE_OR_PROTECTIVE_SHELTER
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;ESCAPE_OR_PROTECTIVE_SHELTER&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Сначала уйти или физически защититься от непосредственного насилия&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;SCENE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Связь после достижения безопасной возможности&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:9 cells:5 -->
> [!abstract]- Запись 9 из 20 — EXIT_AND_DO_NOT_RETURN
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Покинуть опасный объект и не возвращаться&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;BUILDING_OR_VOLUME&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Возврат только после разрешения компетентной службы&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:10 cells:5 -->
> [!abstract]- Запись 10 из 20 — IMMEDIATE_SAFETY
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;IMMEDIATE_SAFETY&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Снизить непосредственный риск самоповреждения или вреда другим&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PERSON_OR_GROUP&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Требует кризисного маршрута и 112 при непосредственной опасности&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:11 cells:5 -->
> [!abstract]- Запись 11 из 20 — ISOLATE_AND_LOCKOUT
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Прекратить использование подозрительной системы или ресурса&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;SYSTEM_OR_RESOURCE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не выполнять опасные работы вне допуска&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:12 cells:5 -->
> [!abstract]- Запись 12 из 20 — MOVE_TO_HIGH_GROUND
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Немедленно уйти от быстрого потока или цунами на безопасную высоту&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;TERRAIN&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Маршрут зависит от местности и официального плана&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:13 cells:5 -->
> [!abstract]- Запись 13 из 20 — OFFICIAL_DIRECTION
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Следовать текущей команде компетентного органа&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;JURISDICTION_EVENT&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Источник зона и время должны быть подтверждены&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:14 cells:5 -->
> [!abstract]- Запись 14 из 20 — PRESERVE_EVIDENCE_AND_RECOVER
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Остановить дальнейший ущерб сохранить доказательства и восстановить доверенно&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;CYBER_ADMIN_FINANCE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не продолжать операции на недоверенном устройстве&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:15 cells:5 -->
> [!abstract]- Запись 15 из 20 — PROTECT_DURING_SHAKING
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;PROTECT_DURING_SHAKING&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Защититься во время землетрясения до решения о выходе&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;SCENE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Выход оценивается после толчков если нет другой непосредственной угрозы&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:16 cells:5 -->
> [!abstract]- Запись 16 из 20 — REMOVE_FROM_EXPOSURE_IF_SAFE
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;REMOVE_FROM_EXPOSURE_IF_SAFE&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Прекратить локальное воздействие без создания второй жертвы&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;LOCAL_EXPOSURE&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не входить в неизвестное облако и не импровизировать химическую защиту&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:17 cells:5 -->
> [!abstract]- Запись 17 из 20 — REUNIFY_AND_ACCOUNT
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Восстановить поимённый учёт и безопасное воссоединение&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не идти в опасную зону вопреки shelter или no-go&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:18 cells:5 -->
> [!abstract]- Запись 18 из 20 — SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Выбрать укрытие или эвакуацию по текущей зоне и команде&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;EXTERNAL_HAZARD&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Бытовая plume-модель не разрешает выбор&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:19 cells:5 -->
> [!abstract]- Запись 19 из 20 — SHELTER_PENDING_OFFICIAL
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Остаться в подходящем укрытии пока внешнее перемещение может увеличить воздействие&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;EXTERNAL_HAZARD&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не применяется к горящему или неустойчивому зданию&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

<!-- record:20 cells:5 -->
> [!abstract]- Запись 20 из 20 — URGENT_PROFESSIONAL_ASSESSMENT
> - **Решение класс ID** (<code>&quot;decision_class_id&quot;</code>): <code>&quot;URGENT_PROFESSIONAL_ASSESSMENT&quot;</code>
> - **«meaning» на русском** (<code>&quot;meaning_ru&quot;</code>): <code>&quot;Не откладывать оценку при риске необратимой потери функции&quot;</code>
> - **«default» область** (<code>&quot;default_scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Условие «or» граница** (<code>&quot;condition_or_boundary&quot;</code>): <code>&quot;Не заменяет 112 при непосредственной угрозе жизни&quot;</code>
> - **Статус выпуска** (<code>&quot;release_status&quot;</code>): <code>&quot;INDEX_ROUTER_ONLY&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
