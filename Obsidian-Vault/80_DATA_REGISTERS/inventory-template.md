---
id: "DATA-REGISTER-4797442933ec1584"
type: "generated-data-register-view"
title: "Физический инвентарь — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "inventory-template.csv"
source_sha256: "07ba6b9fe2fad10bb8beaf987a030d52587c944d71a8c0282982e26cf805995b"
source_bytes: 5338
source_row_count: 5
source_column_count: 59
source_cell_count: 295
ignored_blank_row_count: 0
semantic_group: "PHYSICAL_RESOURCES"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: inventory-template.csv -->

# Физический инвентарь — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Имущество, участок, вода, почва, семена и животные
- **Записей:** 5
- **Полей в каждой записи:** 59
- **Ячеек данных, включая пустые:** 295
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `07ba6b9fe2fad10bb8beaf987a030d52587c944d71a8c0282982e26cf805995b`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Предмет ID | <code>&quot;item_id&quot;</code> |
| 2 | «category» | <code>&quot;category&quot;</code> |
| 3 | «kit» | <code>&quot;kit&quot;</code> |
| 4 | Предмет название на русском | <code>&quot;item_name_ru&quot;</code> |
| 5 | «specification» | <code>&quot;specification&quot;</code> |
| 6 | «purpose» | <code>&quot;purpose&quot;</code> |
| 7 | Количество «formula» | <code>&quot;quantity_formula&quot;</code> |
| 8 | Целевой количество | <code>&quot;target_quantity&quot;</code> |
| 9 | Фактический количество | <code>&quot;actual_quantity&quot;</code> |
| 10 | Единица | <code>&quot;unit&quot;</code> |
| 11 | Место | <code>&quot;location&quot;</code> |
| 12 | Владелец | <code>&quot;owner&quot;</code> |
| 13 | «audience» «layer» | <code>&quot;audience_layer&quot;</code> |
| 14 | Обучение требуемый | <code>&quot;training_required&quot;</code> |
| 15 | «authorized» роль | <code>&quot;authorized_role&quot;</code> |
| 16 | «authorized» роль состояние | <code>&quot;authorized_role_state&quot;</code> |
| 17 | «credential» ID | <code>&quot;credential_id&quot;</code> |
| 18 | «credential» «issuer» | <code>&quot;credential_issuer&quot;</code> |
| 19 | «credential» «expires» время | <code>&quot;credential_expires_at&quot;</code> |
| 20 | «credential» состояние | <code>&quot;credential_state&quot;</code> |
| 21 | «currency» доказательство | <code>&quot;currency_evidence&quot;</code> |
| 22 | «currency» «valid» до | <code>&quot;currency_valid_until&quot;</code> |
| 23 | «currency» состояние | <code>&quot;currency_state&quot;</code> |
| 24 | Область «of» «practice» | <code>&quot;scope_of_practice&quot;</code> |
| 25 | Область состояние | <code>&quot;scope_state&quot;</code> |
| 26 | Протокол ID | <code>&quot;protocol_id&quot;</code> |
| 27 | Протокол версия | <code>&quot;protocol_version&quot;</code> |
| 28 | Протокол состояние | <code>&quot;protocol_state&quot;</code> |
| 29 | Юрисдикция | <code>&quot;jurisdiction&quot;</code> |
| 30 | Юрисдикция состояние | <code>&quot;jurisdiction_state&quot;</code> |
| 31 | Медицинский «direction» | <code>&quot;medical_direction&quot;</code> |
| 32 | Медицинский «direction» состояние | <code>&quot;medical_direction_state&quot;</code> |
| 33 | «facility» | <code>&quot;facility&quot;</code> |
| 34 | «facility» состояние | <code>&quot;facility_state&quot;</code> |
| 35 | Оборудование | <code>&quot;equipment&quot;</code> |
| 36 | Оборудование состояние | <code>&quot;equipment_state&quot;</code> |
| 37 | «patient» «specific» «order» | <code>&quot;patient_specific_order&quot;</code> |
| 38 | «patient» «specific» «order» состояние | <code>&quot;patient_specific_order_state&quot;</code> |
| 39 | Допуск «checked» время | <code>&quot;gate_checked_at&quot;</code> |
| 40 | Допуск «checked» кем | <code>&quot;gate_checked_by&quot;</code> |
| 41 | Допуск проверка срок | <code>&quot;gate_review_due&quot;</code> |
| 42 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 43 | Правовой «constraint» | <code>&quot;legal_constraint&quot;</code> |
| 44 | Хранение «conditions» | <code>&quot;storage_conditions&quot;</code> |
| 45 | «lot» «serial» | <code>&quot;lot_serial&quot;</code> |
| 46 | «acquired» дата | <code>&quot;acquired_date&quot;</code> |
| 47 | «opened» дата | <code>&quot;opened_date&quot;</code> |
| 48 | «expiry» сервис дата | <code>&quot;expiry_service_date&quot;</code> |
| 49 | «last» «checked» | <code>&quot;last_checked&quot;</code> |
| 50 | Проверка метод | <code>&quot;check_method&quot;</code> |
| 51 | Проверка результат | <code>&quot;check_result&quot;</code> |
| 52 | Доказательство тип | <code>&quot;evidence_type&quot;</code> |
| 53 | Доказательство «limitations» | <code>&quot;evidence_limitations&quot;</code> |
| 54 | Предмет статус | <code>&quot;item_status&quot;</code> |
| 55 | «substitute» | <code>&quot;substitute&quot;</code> |
| 56 | Условия остановки | <code>&quot;stop_conditions&quot;</code> |
| 57 | Источник ID | <code>&quot;source_id&quot;</code> |
| 58 | Источник «checked» время | <code>&quot;source_checked_at&quot;</code> |
| 59 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:59 -->
> [!abstract]- Запись 1 из 5 — SRC-CDC-WATER-2025 — Питьевая вода
> - **Предмет ID** (<code>&quot;item_id&quot;</code>): <code>&quot;WATER-STORE-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **«kit»** (<code>&quot;kit&quot;</code>): <code>&quot;HOME&quot;</code>
> - **Предмет название на русском** (<code>&quot;item_name_ru&quot;</code>): <code>&quot;Питьевая вода&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;Заводская герметичная тара&quot;</code>
> - **«purpose»** (<code>&quot;purpose&quot;</code>): <code>&quot;Питьё и приготовление пищи&quot;</code>
> - **Количество «formula»** (<code>&quot;quantity_formula&quot;</code>): <code>&quot;baseline + people + days + heat/illness/pregnancy/pets + reserve&quot;</code>
> - **Целевой количество** (<code>&quot;target_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;л&quot;</code>
> - **Место** (<code>&quot;location&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;M0&quot;</code>
> - **Обучение требуемый** (<code>&quot;training_required&quot;</code>): <code>&quot;Инструктаж по ротации&quot;</code>
> - **«authorized» роль** (<code>&quot;authorized_role&quot;</code>): <code>&quot;LAY&quot;</code>
> - **«authorized» роль состояние** (<code>&quot;authorized_role_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **«credential» ID** (<code>&quot;credential_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «issuer»** (<code>&quot;credential_issuer&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «expires» время** (<code>&quot;credential_expires_at&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«currency» доказательство** (<code>&quot;currency_evidence&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«currency» «valid» до** (<code>&quot;currency_valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Область «of» «practice»** (<code>&quot;scope_of_practice&quot;</code>): <code>&quot;Household water storage&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Протокол ID** (<code>&quot;protocol_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол версия** (<code>&quot;protocol_version&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол состояние** (<code>&quot;protocol_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;Portugal&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Медицинский «direction»** (<code>&quot;medical_direction&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Медицинский «direction» состояние** (<code>&quot;medical_direction_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«facility»** (<code>&quot;facility&quot;</code>): <code>&quot;Personalized household location&quot;</code>
> - **«facility» состояние** (<code>&quot;facility_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Оборудование** (<code>&quot;equipment&quot;</code>): <code>&quot;Exact sealed containers&quot;</code>
> - **Оборудование состояние** (<code>&quot;equipment_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order»** (<code>&quot;patient_specific_order&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«patient» «specific» «order» состояние** (<code>&quot;patient_specific_order_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Допуск «checked» время** (<code>&quot;gate_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск «checked» кем** (<code>&quot;gate_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск проверка срок** (<code>&quot;gate_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Правовой «constraint»** (<code>&quot;legal_constraint&quot;</code>): <code>&quot;&quot;</code>
> - **Хранение «conditions»** (<code>&quot;storage_conditions&quot;</code>): <code>&quot;По этикетке производителя&quot;</code>
> - **«lot» «serial»** (<code>&quot;lot_serial&quot;</code>): <code>&quot;&quot;</code>
> - **«acquired» дата** (<code>&quot;acquired_date&quot;</code>): <code>&quot;&quot;</code>
> - **«opened» дата** (<code>&quot;opened_date&quot;</code>): <code>&quot;&quot;</code>
> - **«expiry» сервис дата** (<code>&quot;expiry_service_date&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «checked»** (<code>&quot;last_checked&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка метод** (<code>&quot;check_method&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка результат** (<code>&quot;check_result&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доказательство тип** (<code>&quot;evidence_type&quot;</code>): <code>&quot;UNSELECTED&quot;</code>
> - **Доказательство «limitations»** (<code>&quot;evidence_limitations&quot;</code>): <code>&quot;Item not acquired&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;planned&quot;</code>
> - **«substitute»** (<code>&quot;substitute&quot;</code>): <code>&quot;&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;Не рассчитывать target_quantity до заполнения всех модификаторов; не использовать повреждённую или загрязнённую тару&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-CDC-WATER-2025&quot;</code>
> - **Источник «checked» время** (<code>&quot;source_checked_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:2 cells:59 -->
> [!abstract]- Запись 2 из 5 — MED-CARD-001 — Индивидуальная медицинская карточка
> - **Предмет ID** (<code>&quot;item_id&quot;</code>): <code>&quot;MED-CARD-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MED&quot;</code>
> - **«kit»** (<code>&quot;kit&quot;</code>): <code>&quot;E0&quot;</code>
> - **Предмет название на русском** (<code>&quot;item_name_ru&quot;</code>): <code>&quot;Индивидуальная медицинская карточка&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;Влагостойкая печать&quot;</code>
> - **«purpose»** (<code>&quot;purpose&quot;</code>): <code>&quot;Передать критические данные спасателям&quot;</code>
> - **Количество «formula»** (<code>&quot;quantity_formula&quot;</code>): <code>&quot;1 * persons&quot;</code>
> - **Целевой количество** (<code>&quot;target_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;шт&quot;</code>
> - **Место** (<code>&quot;location&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;M0&quot;</code>
> - **Обучение требуемый** (<code>&quot;training_required&quot;</code>): <code>&quot;Обновление данных&quot;</code>
> - **«authorized» роль** (<code>&quot;authorized_role&quot;</code>): <code>&quot;LAY&quot;</code>
> - **«authorized» роль состояние** (<code>&quot;authorized_role_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **«credential» ID** (<code>&quot;credential_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «issuer»** (<code>&quot;credential_issuer&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «expires» время** (<code>&quot;credential_expires_at&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«currency» доказательство** (<code>&quot;currency_evidence&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«currency» «valid» до** (<code>&quot;currency_valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Область «of» «practice»** (<code>&quot;scope_of_practice&quot;</code>): <code>&quot;Carry and hand over verified personal data&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Протокол ID** (<code>&quot;protocol_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол версия** (<code>&quot;protocol_version&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол состояние** (<code>&quot;protocol_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;Portugal&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Медицинский «direction»** (<code>&quot;medical_direction&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Медицинский «direction» состояние** (<code>&quot;medical_direction_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«facility»** (<code>&quot;facility&quot;</code>): <code>&quot;On person&quot;</code>
> - **«facility» состояние** (<code>&quot;facility_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Оборудование** (<code>&quot;equipment&quot;</code>): <code>&quot;Water-resistant card&quot;</code>
> - **Оборудование состояние** (<code>&quot;equipment_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order»** (<code>&quot;patient_specific_order&quot;</code>): <code>&quot;Verified personal medical data&quot;</code>
> - **«patient» «specific» «order» состояние** (<code>&quot;patient_specific_order_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Допуск «checked» время** (<code>&quot;gate_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск «checked» кем** (<code>&quot;gate_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск проверка срок** (<code>&quot;gate_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Правовой «constraint»** (<code>&quot;legal_constraint&quot;</code>): <code>&quot;Защита персональных данных&quot;</code>
> - **Хранение «conditions»** (<code>&quot;storage_conditions&quot;</code>): <code>&quot;Защищать от потери и несанкционированного доступа&quot;</code>
> - **«lot» «serial»** (<code>&quot;lot_serial&quot;</code>): <code>&quot;&quot;</code>
> - **«acquired» дата** (<code>&quot;acquired_date&quot;</code>): <code>&quot;&quot;</code>
> - **«opened» дата** (<code>&quot;opened_date&quot;</code>): <code>&quot;&quot;</code>
> - **«expiry» сервис дата** (<code>&quot;expiry_service_date&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «checked»** (<code>&quot;last_checked&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка метод** (<code>&quot;check_method&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка результат** (<code>&quot;check_result&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доказательство тип** (<code>&quot;evidence_type&quot;</code>): <code>&quot;UNSELECTED&quot;</code>
> - **Доказательство «limitations»** (<code>&quot;evidence_limitations&quot;</code>): <code>&quot;Item not created&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;planned&quot;</code>
> - **«substitute»** (<code>&quot;substitute&quot;</code>): <code>&quot;Временная рукописная карточка&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;Не включать недостоверную группу крови&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «checked» время** (<code>&quot;source_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Dedicated Portugal-compatible medical-card provenance pending&quot;</code>
>

<!-- record:3 cells:59 -->
> [!abstract]- Запись 3 из 5 — SRC-ANEPC-KIT — Батарейный радиоприёмник
> - **Предмет ID** (<code>&quot;item_id&quot;</code>): <code>&quot;COMMS-RADIO-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;COMMS&quot;</code>
> - **«kit»** (<code>&quot;kit&quot;</code>): <code>&quot;HOME&quot;</code>
> - **Предмет название на русском** (<code>&quot;item_name_ru&quot;</code>): <code>&quot;Батарейный радиоприёмник&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;Приём официального вещания без сети&quot;</code>
> - **«purpose»** (<code>&quot;purpose&quot;</code>): <code>&quot;Получать официальные сообщения&quot;</code>
> - **Количество «formula»** (<code>&quot;quantity_formula&quot;</code>): <code>&quot;1 household&quot;</code>
> - **Целевой количество** (<code>&quot;target_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;шт&quot;</code>
> - **Место** (<code>&quot;location&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;M0&quot;</code>
> - **Обучение требуемый** (<code>&quot;training_required&quot;</code>): <code>&quot;Ежеквартальный тест&quot;</code>
> - **«authorized» роль** (<code>&quot;authorized_role&quot;</code>): <code>&quot;LAY&quot;</code>
> - **«authorized» роль состояние** (<code>&quot;authorized_role_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **«credential» ID** (<code>&quot;credential_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «issuer»** (<code>&quot;credential_issuer&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «expires» время** (<code>&quot;credential_expires_at&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«currency» доказательство** (<code>&quot;currency_evidence&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«currency» «valid» до** (<code>&quot;currency_valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Область «of» «practice»** (<code>&quot;scope_of_practice&quot;</code>): <code>&quot;Receive-only official broadcasts&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Протокол ID** (<code>&quot;protocol_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол версия** (<code>&quot;protocol_version&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол состояние** (<code>&quot;protocol_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;Portugal&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Медицинский «direction»** (<code>&quot;medical_direction&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Медицинский «direction» состояние** (<code>&quot;medical_direction_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«facility»** (<code>&quot;facility&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«facility» состояние** (<code>&quot;facility_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Оборудование** (<code>&quot;equipment&quot;</code>): <code>&quot;Receiver plus batteries&quot;</code>
> - **Оборудование состояние** (<code>&quot;equipment_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order»** (<code>&quot;patient_specific_order&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«patient» «specific» «order» состояние** (<code>&quot;patient_specific_order_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Допуск «checked» время** (<code>&quot;gate_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск «checked» кем** (<code>&quot;gate_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск проверка срок** (<code>&quot;gate_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Правовой «constraint»** (<code>&quot;legal_constraint&quot;</code>): <code>&quot;&quot;</code>
> - **Хранение «conditions»** (<code>&quot;storage_conditions&quot;</code>): <code>&quot;Сухо; батареи по инструкции&quot;</code>
> - **«lot» «serial»** (<code>&quot;lot_serial&quot;</code>): <code>&quot;&quot;</code>
> - **«acquired» дата** (<code>&quot;acquired_date&quot;</code>): <code>&quot;&quot;</code>
> - **«opened» дата** (<code>&quot;opened_date&quot;</code>): <code>&quot;&quot;</code>
> - **«expiry» сервис дата** (<code>&quot;expiry_service_date&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «checked»** (<code>&quot;last_checked&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка метод** (<code>&quot;check_method&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка результат** (<code>&quot;check_result&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доказательство тип** (<code>&quot;evidence_type&quot;</code>): <code>&quot;UNSELECTED&quot;</code>
> - **Доказательство «limitations»** (<code>&quot;evidence_limitations&quot;</code>): <code>&quot;Item not acquired&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;planned&quot;</code>
> - **«substitute»** (<code>&quot;substitute&quot;</code>): <code>&quot;Автомобильный радиоприёмник&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;Не считать двусторонней связью&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-ANEPC-KIT&quot;</code>
> - **Источник «checked» время** (<code>&quot;source_checked_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:4 cells:59 -->
> [!abstract]- Запись 4 из 5 — FIRE-CO-001 — Извещатель угарного газа
> - **Предмет ID** (<code>&quot;item_id&quot;</code>): <code>&quot;FIRE-CO-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;FIRE&quot;</code>
> - **«kit»** (<code>&quot;kit&quot;</code>): <code>&quot;HOME&quot;</code>
> - **Предмет название на русском** (<code>&quot;item_name_ru&quot;</code>): <code>&quot;Извещатель угарного газа&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;Сертифицированная модель по месту установки&quot;</code>
> - **«purpose»** (<code>&quot;purpose&quot;</code>): <code>&quot;Раннее предупреждение CO&quot;</code>
> - **Количество «formula»** (<code>&quot;quantity_formula&quot;</code>): <code>&quot;per manufacturer siting&quot;</code>
> - **Целевой количество** (<code>&quot;target_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;шт&quot;</code>
> - **Место** (<code>&quot;location&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;M0&quot;</code>
> - **Обучение требуемый** (<code>&quot;training_required&quot;</code>): <code>&quot;Семейное упражнение&quot;</code>
> - **«authorized» роль** (<code>&quot;authorized_role&quot;</code>): <code>&quot;LAY&quot;</code>
> - **«authorized» роль состояние** (<code>&quot;authorized_role_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **«credential» ID** (<code>&quot;credential_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «issuer»** (<code>&quot;credential_issuer&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «expires» время** (<code>&quot;credential_expires_at&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«currency» доказательство** (<code>&quot;currency_evidence&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«currency» «valid» до** (<code>&quot;currency_valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Область «of» «practice»** (<code>&quot;scope_of_practice&quot;</code>): <code>&quot;Recognize alarm and leave safely&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Протокол ID** (<code>&quot;protocol_id&quot;</code>): <code>&quot;PENDING-MANUFACTURER-MANUAL&quot;</code>
> - **Протокол версия** (<code>&quot;protocol_version&quot;</code>): <code>&quot;&quot;</code>
> - **Протокол состояние** (<code>&quot;protocol_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;Portugal&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Медицинский «direction»** (<code>&quot;medical_direction&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Медицинский «direction» состояние** (<code>&quot;medical_direction_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«facility»** (<code>&quot;facility&quot;</code>): <code>&quot;Personalized installation point&quot;</code>
> - **«facility» состояние** (<code>&quot;facility_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Оборудование** (<code>&quot;equipment&quot;</code>): <code>&quot;Certified detector&quot;</code>
> - **Оборудование состояние** (<code>&quot;equipment_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order»** (<code>&quot;patient_specific_order&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«patient» «specific» «order» состояние** (<code>&quot;patient_specific_order_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Допуск «checked» время** (<code>&quot;gate_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск «checked» кем** (<code>&quot;gate_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск проверка срок** (<code>&quot;gate_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Правовой «constraint»** (<code>&quot;legal_constraint&quot;</code>): <code>&quot;Монтаж по применимым нормам&quot;</code>
> - **Хранение «conditions»** (<code>&quot;storage_conditions&quot;</code>): <code>&quot;По инструкции конкретной модели&quot;</code>
> - **«lot» «serial»** (<code>&quot;lot_serial&quot;</code>): <code>&quot;&quot;</code>
> - **«acquired» дата** (<code>&quot;acquired_date&quot;</code>): <code>&quot;&quot;</code>
> - **«opened» дата** (<code>&quot;opened_date&quot;</code>): <code>&quot;&quot;</code>
> - **«expiry» сервис дата** (<code>&quot;expiry_service_date&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «checked»** (<code>&quot;last_checked&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка метод** (<code>&quot;check_method&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка результат** (<code>&quot;check_result&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доказательство тип** (<code>&quot;evidence_type&quot;</code>): <code>&quot;UNSELECTED&quot;</code>
> - **Доказательство «limitations»** (<code>&quot;evidence_limitations&quot;</code>): <code>&quot;Exact model local source and siting not selected&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;planned&quot;</code>
> - **«substitute»** (<code>&quot;substitute&quot;</code>): <code>&quot;&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;Не игнорировать тревогу и не искать источник в опасной зоне&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;&quot;</code>
> - **Источник «checked» время** (<code>&quot;source_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;CO source and exact manufacturer manual pending; do not mark gate satisfied&quot;</code>
>

<!-- record:5 cells:59 -->
> [!abstract]- Запись 5 из 5 — SRC-CISA-321 — Зашифрованная копия критических документов
> - **Предмет ID** (<code>&quot;item_id&quot;</code>): <code>&quot;DOCS-PACK-001&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;DOCS&quot;</code>
> - **«kit»** (<code>&quot;kit&quot;</code>): <code>&quot;OFFSITE&quot;</code>
> - **Предмет название на русском** (<code>&quot;item_name_ru&quot;</code>): <code>&quot;Зашифрованная копия критических документов&quot;</code>
> - **«specification»** (<code>&quot;specification&quot;</code>): <code>&quot;Открытый индекс плюс защищённый архив&quot;</code>
> - **«purpose»** (<code>&quot;purpose&quot;</code>): <code>&quot;Восстановление личности и доступа&quot;</code>
> - **Количество «formula»** (<code>&quot;quantity_formula&quot;</code>): <code>&quot;2 independent copies&quot;</code>
> - **Целевой количество** (<code>&quot;target_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Фактический количество** (<code>&quot;actual_quantity&quot;</code>): <code>&quot;&quot;</code>
> - **Единица** (<code>&quot;unit&quot;</code>): <code>&quot;комплект&quot;</code>
> - **Место** (<code>&quot;location&quot;</code>): <code>&quot;&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **«audience» «layer»** (<code>&quot;audience_layer&quot;</code>): <code>&quot;M0&quot;</code>
> - **Обучение требуемый** (<code>&quot;training_required&quot;</code>): <code>&quot;Ежегодное пробное восстановление&quot;</code>
> - **«authorized» роль** (<code>&quot;authorized_role&quot;</code>): <code>&quot;LAY&quot;</code>
> - **«authorized» роль состояние** (<code>&quot;authorized_role_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **«credential» ID** (<code>&quot;credential_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «issuer»** (<code>&quot;credential_issuer&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«credential» «expires» время** (<code>&quot;credential_expires_at&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«currency» доказательство** (<code>&quot;currency_evidence&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«currency» «valid» до** (<code>&quot;currency_valid_until&quot;</code>): <code>&quot;&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Область «of» «practice»** (<code>&quot;scope_of_practice&quot;</code>): <code>&quot;Personal data recovery&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Протокол ID** (<code>&quot;protocol_id&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол версия** (<code>&quot;protocol_version&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Протокол состояние** (<code>&quot;protocol_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;Portugal&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;REQUIRED_SATISFIED&quot;</code>
> - **Медицинский «direction»** (<code>&quot;medical_direction&quot;</code>): <code>&quot;N/A&quot;</code>
> - **Медицинский «direction» состояние** (<code>&quot;medical_direction_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **«facility»** (<code>&quot;facility&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«facility» состояние** (<code>&quot;facility_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Оборудование** (<code>&quot;equipment&quot;</code>): <code>&quot;Encrypted archive and independent reader&quot;</code>
> - **Оборудование состояние** (<code>&quot;equipment_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order»** (<code>&quot;patient_specific_order&quot;</code>): <code>&quot;N/A&quot;</code>
> - **«patient» «specific» «order» состояние** (<code>&quot;patient_specific_order_state&quot;</code>): <code>&quot;NOT_REQUIRED&quot;</code>
> - **Допуск «checked» время** (<code>&quot;gate_checked_at&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск «checked» кем** (<code>&quot;gate_checked_by&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск проверка срок** (<code>&quot;gate_review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Правовой «constraint»** (<code>&quot;legal_constraint&quot;</code>): <code>&quot;Защита персональных данных&quot;</code>
> - **Хранение «conditions»** (<code>&quot;storage_conditions&quot;</code>): <code>&quot;Одна копия отключена и вне дома&quot;</code>
> - **«lot» «serial»** (<code>&quot;lot_serial&quot;</code>): <code>&quot;&quot;</code>
> - **«acquired» дата** (<code>&quot;acquired_date&quot;</code>): <code>&quot;&quot;</code>
> - **«opened» дата** (<code>&quot;opened_date&quot;</code>): <code>&quot;&quot;</code>
> - **«expiry» сервис дата** (<code>&quot;expiry_service_date&quot;</code>): <code>&quot;&quot;</code>
> - **«last» «checked»** (<code>&quot;last_checked&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка метод** (<code>&quot;check_method&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка результат** (<code>&quot;check_result&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доказательство тип** (<code>&quot;evidence_type&quot;</code>): <code>&quot;UNSELECTED&quot;</code>
> - **Доказательство «limitations»** (<code>&quot;evidence_limitations&quot;</code>): <code>&quot;Archive and restore path not built&quot;</code>
> - **Предмет статус** (<code>&quot;item_status&quot;</code>): <code>&quot;planned&quot;</code>
> - **«substitute»** (<code>&quot;substitute&quot;</code>): <code>&quot;Бумажные копии по назначению&quot;</code>
> - **Условия остановки** (<code>&quot;stop_conditions&quot;</code>): <code>&quot;Не хранить ключ вместе с единственной копией&quot;</code>
> - **Источник ID** (<code>&quot;source_id&quot;</code>): <code>&quot;SRC-CISA-321&quot;</code>
> - **Источник «checked» время** (<code>&quot;source_checked_at&quot;</code>): <code>&quot;2026-08-29&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
