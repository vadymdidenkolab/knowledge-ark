---
id: "DATA-REGISTER-58c905c64d31eb57"
type: "generated-data-register-view"
title: "Допуски безопасности практической науки"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "practical-science-safety-gates.csv"
source_sha256: "f5d2961f76308209181aae5e003a76b7a059646309b3b6c92cbc5437d57fdbf7"
source_bytes: 6769
source_row_count: 17
source_column_count: 6
source_cell_count: 102
ignored_blank_row_count: 0
semantic_group: "PRACTICAL_SCIENCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: practical-science-safety-gates.csv -->

# Допуски безопасности практической науки

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Практическая наука, приборы и безопасность
- **Записей:** 17
- **Полей в каждой записи:** 6
- **Ячеек данных, включая пустые:** 102
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `f5d2961f76308209181aae5e003a76b7a059646309b3b6c92cbc5437d57fdbf7`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Допуск ID | <code>&quot;gate_id&quot;</code> |
| 2 | Опасность класс | <code>&quot;hazard_class&quot;</code> |
| 3 | «no» «go» «rule» на русском | <code>&quot;no_go_rule_ru&quot;</code> |
| 4 | Класс безопасности | <code>&quot;safety_class&quot;</code> |
| 5 | «safe» «fallback» на русском | <code>&quot;safe_fallback_ru&quot;</code> |
| 6 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:6 -->
> [!abstract]- Запись 1 из 17 — SG-01
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-01&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;UNKNOWN_BIOLOGY&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не культивировать неизвестные бактерии, грибы, ткани или природные образцы&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;изолировать, не открывать, профильная лаборатория/служба&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:2 cells:6 -->
> [!abstract]- Запись 2 из 17 — SG-02
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-02&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;INVASIVE_HEALTH&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не выполнять инъекции, разрезы, хирургические, стоматологические или ветеринарные процедуры&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;112/врач/ветеринар/лицензированная служба&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:3 cells:6 -->
> [!abstract]- Запись 3 из 17 — SG-03
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-03&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;MEDICINE_SYNTHESIS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не синтезировать лекарства, анестетики или терапевтические вещества&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;аптека, врач, регуляторный supply chain&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:4 cells:6 -->
> [!abstract]- Запись 4 из 17 — SG-04
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-04&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;EXPLOSIVES_WEAPONS_TOXINS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не разрабатывать взрывчатые, зажигательные, оружейные, токсичные или вредоносные системы&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;безопасность, полиция/112 при находке&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:5 cells:6 -->
> [!abstract]- Запись 5 из 17 — SG-05
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-05&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;MAINS_HIGH_VOLTAGE&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не работать под напряжением, не вскрывать щиты и не создавать backfeed&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;отключение по инструкции; лицензированный электрик&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:6 cells:6 -->
> [!abstract]- Запись 6 из 17 — SG-06
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-06&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;PRESSURE_VESSELS_GAS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не нагревать герметичные сосуды, не ремонтировать газ/pressure vessel и не обходить relief devices&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;отойти, проветрить если официально безопасно, аварийная/профильная служба&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:7 cells:6 -->
> [!abstract]- Запись 7 из 17 — SG-07
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-07&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;STRUCTURAL_MODIFICATION&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не менять несущие элементы, фундамент, склон или подпорную систему&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;закрыть доступ и вызвать инженера&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:8 cells:6 -->
> [!abstract]- Запись 8 из 17 — SG-08
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-08&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;REFRIGERANT_HOT_WORK&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не выпускать хладагент и не выполнять сварку/горячие работы без допуска и площадки&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;квалифицированный техник/разрешение&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:9 cells:6 -->
> [!abstract]- Запись 9 из 17 — SG-09
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-09&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;REACTIVE_CHEMISTRY&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не смешивать реактивные, неизвестные, токсичные, едкие, окисляющие или выделяющие газ вещества в household science layer; наличие SDS само по себе не создаёт разрешения, лаборатории или квалификации&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;разделить, не трогать; CIAV/112/профильная служба по ситуации&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:10 cells:6 -->
> [!abstract]- Запись 10 из 17 — SG-10
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-10&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;IONIZING_RADIATION&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не приобретать, вскрывать и не экспериментировать с источниками ионизирующего излучения&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;не трогать, удалиться, 112/компетентный орган&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:11 cells:6 -->
> [!abstract]- Запись 11 из 17 — SG-11
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-11&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;CONFINED_SPACE_WATER_HEIGHT&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не входить в колодцы, резервуары, стоки, шахты; не работать у воды/на высоте без системы&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;службы/профессиональная команда&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:12 cells:6 -->
> [!abstract]- Запись 12 из 17 — SG-12
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-12&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;PESTICIDES_AND_PROTECTED_SPECIES&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не применять пестициды вне этикетки/закона и не вмешиваться в охраняемые виды&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;DGAV/ICNF/лицензированный специалист&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:13 cells:6 -->
> [!abstract]- Запись 13 из 17 — SG-13
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-13&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;LITHIUM_HIGH_CURRENT_CAPACITORS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не вскрывать, собирать, восстанавливать, заряжать неизвестным способом или коротить lithium/lead-acid/vehicle/traction packs; не работать с повреждёнными батареями, неизвестными power capacitors или высокотоковыми DC-источниками&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;обесточить только штатно, не трогать горячее/вздутие/дым, удалить людей, 112/пожарная/квалифицированный сервис&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:14 cells:6 -->
> [!abstract]- Запись 14 из 17 — SG-14
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-14&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;MACHINERY_STORED_ENERGY&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не снимать ограждения, не обходить interlock и не работать с вращением, пружиной, гидравликой, поднятым грузом или иной запасённой энергией без квалифицированной isolation/LOTO&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S3_LICENSED_PROFESSIONAL&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;остановить, оградить и вызвать компетентного техника&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:15 cells:6 -->
> [!abstract]- Запись 15 из 17 — SG-15
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-15&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;HAZARDOUS_BUILDING_MATERIALS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не нарушать неизвестные материалы здания, асбест, свинцовую краску, загрязнённую пыль или плесень большой площади&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;закрыть доступ; профессиональная идентификация и remediation&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:16 cells:6 -->
> [!abstract]- Запись 16 из 17 — SG-16
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-16&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;LASER_INTENSE_OPTICAL&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не направлять лазер/сфокусированный свет в глаза, транспорт или небо; не разбирать laser devices и не наблюдать Солнце через оптику&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;обесточить/закрыть источник штатно; использовать только безопасную готовую оптику по инструкции&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

<!-- record:17 cells:6 -->
> [!abstract]- Запись 17 из 17 — SG-17
> - **Допуск ID** (<code>&quot;gate_id&quot;</code>): <code>&quot;SG-17&quot;</code>
> - **Опасность класс** (<code>&quot;hazard_class&quot;</code>): <code>&quot;UNCONTROLLED_HEAT_STEAM_BURNS&quot;</code>
> - **«no» «go» «rule» на русском** (<code>&quot;no_go_rule_ru&quot;</code>): <code>&quot;Не использовать научный опыт с кипящей жидкостью, паром, горячим маслом, открытым пламенем или нагреваемой герметичной ёмкостью; бытовое приготовление пищи не превращать в эксперимент и выполнять только штатным прибором/валидированным процессом&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD&quot;</code>
> - **«safe» «fallback» на русском** (<code>&quot;safe_fallback_ru&quot;</code>): <code>&quot;остановить нагрев штатно, не открывать давление; при ожоге/пожаре действовать по выпущенной карточке и 112&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.4&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
