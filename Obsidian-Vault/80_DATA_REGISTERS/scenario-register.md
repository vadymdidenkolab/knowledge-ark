---
id: "DATA-REGISTER-692e792f6ec53a6c"
type: "generated-data-register-view"
title: "Сценарии нештатных ситуаций"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "scenario-register.csv"
source_sha256: "4c39ff46e5090c46ff23d7561512a07dd6ebd0f66ef445d9e5cfc48e5ca966f4"
source_bytes: 90813
source_row_count: 133
source_column_count: 31
source_cell_count: 4123
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: scenario-register.csv -->

# Сценарии нештатных ситуаций

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 133
- **Полей в каждой записи:** 31
- **Ячеек данных, включая пустые:** 4123
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `4c39ff46e5090c46ff23d7561512a07dd6ebd0f66ef445d9e5cfc48e5ca966f4`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Сценарий ID | <code>&quot;scenario_id&quot;</code> |
| 2 | «family» | <code>&quot;family&quot;</code> |
| 3 | Название на русском | <code>&quot;name_ru&quot;</code> |
| 4 | Область | <code>&quot;scope&quot;</code> |
| 5 | Триггер класс | <code>&quot;trigger_class&quot;</code> |
| 6 | «first» решение класс | <code>&quot;first_decision_class&quot;</code> |
| 7 | Решение «sequence» | <code>&quot;decision_sequence&quot;</code> |
| 8 | Решение условие примечания | <code>&quot;decision_condition_notes&quot;</code> |
| 9 | Решение «sequence» статус | <code>&quot;decision_sequence_status&quot;</code> |
| 10 | Возможность ID | <code>&quot;capability_ids&quot;</code> |
| 11 | «spatial» «need» «codes» | <code>&quot;spatial_need_codes&quot;</code> |
| 12 | Карта ID | <code>&quot;map_ids&quot;</code> |
| 13 | Маршрут ID | <code>&quot;route_ids&quot;</code> |
| 14 | Объект ID | <code>&quot;site_ids&quot;</code> |
| 15 | «modifier» «codes» | <code>&quot;modifier_codes&quot;</code> |
| 16 | Размер группы | <code>&quot;group_size_scope&quot;</code> |
| 17 | Горизонт область | <code>&quot;horizon_scope&quot;</code> |
| 18 | Источник полномочие класс | <code>&quot;source_authority_class&quot;</code> |
| 19 | «content» проверка состояние | <code>&quot;content_review_state&quot;</code> |
| 20 | «card» статус | <code>&quot;card_status&quot;</code> |
| 21 | Профессиональный проверка требуемый | <code>&quot;professional_review_required&quot;</code> |
| 22 | Профессиональный проверка состояние | <code>&quot;professional_review_state&quot;</code> |
| 23 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 24 | Примечания | <code>&quot;notes&quot;</code> |
| 25 | Идентификаторы источников | <code>&quot;source_ids&quot;</code> |
| 26 | Источник «section» ссылки | <code>&quot;source_section_refs&quot;</code> |
| 27 | Решение «provenance» состояние | <code>&quot;decision_provenance_state&quot;</code> |
| 28 | Горизонт «vocabulary» версия | <code>&quot;horizon_vocabulary_version&quot;</code> |
| 29 | Горизонт «semantics» | <code>&quot;horizon_semantics&quot;</code> |
| 30 | «e5» проверка состояние | <code>&quot;e5_review_state&quot;</code> |
| 31 | «e5» «basis» ссылки | <code>&quot;e5_basis_refs&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:31 -->
> [!abstract]- Запись 1 из 133 — MED-ARREST — Нет нормального дыхания или подозрение на остановку кровообращения
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-ARREST&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Нет нормального дыхания или подозрение на остановку кровообращения&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Действия только по диспетчеру или актуальному курсу&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-BLS|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ERC_PLUS_LOCAL_EMERGENCY_SYSTEM&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Действия только по диспетчеру или актуальному курсу&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:2 cells:31 -->
> [!abstract]- Запись 2 из 133 — MED-AIRWAY — Удушье или острая проблема дыхательных путей
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-AIRWAY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Удушье или острая проблема дыхательных путей&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не заменяет очное обучение&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-BLS|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ERC_PLUS_LOCAL_EMERGENCY_SYSTEM&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не заменяет очное обучение&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:3 cells:31 -->
> [!abstract]- Запись 3 из 133 — MED-BLEED — Массивное наружное кровотечение или признаки внутреннего
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-BLEED&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Массивное наружное кровотечение или признаки внутреннего&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Средства только в пределах навыка&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|PPE|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ANTICOAGULATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IFRC_ERC_PLUS_LOCAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Средства только в пределах навыка&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:4 cells:31 -->
> [!abstract]- Запись 4 из 133 — MED-TRAUMA — Тяжёлая травма падение или ДТП
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-TRAUMA&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Тяжёлая травма падение или ДТП&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не входить в опасную зону ради помощи&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|TRANS|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|ROAD|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IFRC_ERC_PLUS_LOCAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не входить в опасную зону ради помощи&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:5 cells:31 -->
> [!abstract]- Запись 5 из 133 — MED-HEAD-SPINE — Травма головы шеи или позвоночника
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-HEAD-SPINE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Травма головы шеи или позвоночника&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Перемещение только по необходимости безопасности и навыку&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ANTICOAGULATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IFRC_ERC_PLUS_LOCAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Перемещение только по необходимости безопасности и навыку&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:6 cells:31 -->
> [!abstract]- Запись 6 из 133 — MED-CRUSH — Сдавление или crush injury
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-CRUSH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Сдавление или crush injury&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не проводить опасное освобождение без координации&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;RESCUE_ACCESS|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PROFESSIONAL_RESCUE_MEDICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не проводить опасное освобождение без координации&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:7 cells:31 -->
> [!abstract]- Запись 7 из 133 — MED-BURN — Термический ожог: оценка красных флагов и срочности
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-BURN&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Термический ожог: оценка красных флагов и срочности&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Красные флаги или угроза жизни требуют 112; остальные маршруты определяет проверенная карточка, SNS 24 или клиницист&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|WAT|PPE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|SAFE_EXIT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IFRC_ERC_PLUS_LOCAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Красные флаги или угроза жизни требуют 112; остальные маршруты определяет проверенная карточка, SNS 24 или клиницист&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:8 cells:31 -->
> [!abstract]- Запись 8 из 133 — MED-ELECTRIC — Электротравма или молния
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-ELECTRIC&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Электротравма или молния&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Сначала исключить продолжающееся электрическое воздействие&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|ENE|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;UTILITY_SHUTOFF|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;EMERGENCY_MEDICAL_PLUS_UTILITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сначала исключить продолжающееся электрическое воздействие&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:9 cells:31 -->
> [!abstract]- Запись 9 из 133 — MED-DROWN — Утопление или инцидент в воде
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-DROWN&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Утопление или инцидент в воде&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не становиться второй жертвой&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-BLS|PPE|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_ACCESS|RESCUE_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;COLD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ERC_PLUS_PROFESSIONAL_RESCUE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не становиться второй жертвой&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:10 cells:31 -->
> [!abstract]- Запись 10 из 133 — MED-CHEST — Внезапная боль в груди или возможный сердечный приступ
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-CHEST&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Внезапная боль в груди или возможный сердечный приступ&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не ставить диагноз самостоятельно&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHRONIC_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_ERC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не ставить диагноз самостоятельно&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:11 cells:31 -->
> [!abstract]- Запись 11 из 133 — MED-STROKE — Внезапные признаки инсульта
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-STROKE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Внезапные признаки инсульта&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Фиксировать время появления признаков&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;LANGUAGE_BARRIER&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_ERC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Фиксировать время появления признаков&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:12 cells:31 -->
> [!abstract]- Запись 12 из 133 — MED-RESP — Острое нарушение дыхания астма или COPD
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-RESP&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Острое нарушение дыхания астма или COPD&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Назначенное личное средство только по персональному плану&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|AIR|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|AIR_QUALITY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;OXYGEN_OR_POWER_DEPENDENT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_ERC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Назначенное личное средство только по персональному плану&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:13 cells:31 -->
> [!abstract]- Запись 13 из 133 — MED-ANAPH — Тяжёлая аллергическая реакция или анафилаксия
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-ANAPH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Тяжёлая аллергическая реакция или анафилаксия&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Индивидуальное назначенное средство и срочная помощь&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_ERC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Индивидуальное назначенное средство и срочная помощь&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:14 cells:31 -->
> [!abstract]- Запись 14 из 133 — MED-SEIZURE — Судороги или изменённое сознание
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-SEIZURE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Судороги или изменённое сознание&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не давать внутрь при нарушенном сознании&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHRONIC_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_ERC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не давать внутрь при нарушенном сознании&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:15 cells:31 -->
> [!abstract]- Запись 15 из 133 — MED-DIAB — Острое осложнение диабета
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-DIAB&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Острое осложнение диабета&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM_OR_MEASUREMENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Следовать индивидуальному плану и не переоценивать прибор&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|MED-NCD|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|PHARMACY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHRONIC_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_CLINICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Следовать индивидуальному плану и не переоценивать прибор&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:16 cells:31 -->
> [!abstract]- Запись 16 из 133 — MED-POISON — Возможное отравление лекарством пищей или веществом
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-POISON&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Возможное отравление лекарством пищей или веществом&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;EXPOSURE_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_CIAV&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_CIAV&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;При угрозе жизни одновременно 112; не вызывать рвоту без указания&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM|PPE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;EXPOSURE_SITE|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;CIAV_PLUS_EMERGENCY_MEDICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;При угрозе жизни одновременно 112; не вызывать рвоту без указания&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:17 cells:31 -->
> [!abstract]- Запись 17 из 133 — MED-OVERDOSE — Передозировка или интоксикация веществом
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-OVERDOSE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Передозировка или интоксикация веществом&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;EXPOSURE_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Спасательное средство только по закону протоколу и обучению&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;EMERGENCY_MEDICAL_TOXICOLOGY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Спасательное средство только по закону протоколу и обучению&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:18 cells:31 -->
> [!abstract]- Запись 18 из 133 — MED-SEPSIS — Тяжёлая инфекция или возможный сепсис
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-SEPSIS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Тяжёлая инфекция или возможный сепсис&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не заменять антибиотиками из бытового запаса&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|COM|MED-NCD&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;IMMUNOCOMPROMISED&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_CLINICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не заменять антибиотиками из бытового запаса&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:19 cells:31 -->
> [!abstract]- Запись 19 из 133 — MED-DEHYD — Обезвоживание, диарея или рвота: оценка красных флагов
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-DEHYD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Обезвоживание, диарея или рвота: оценка красных флагов&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_CLUSTER&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;112 только при угрозе жизни; иначе срочность определяется по красным флагам, возрасту, беременности, сопутствующим состояниям и актуальной клинической маршрутизации&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|WAT|SAN|FOOD&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_SOURCE|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;WHO_NATIONAL_HEALTH&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;112 только при угрозе жизни; иначе срочность определяется по красным флагам, возрасту, беременности, сопутствующим состояниям и актуальной клинической маршрутизации&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:20 cells:31 -->
> [!abstract]- Запись 20 из 133 — MED-CONTINUITY — Потеря регулярных лекарств лечения холодовой цепи или медпитания
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-CONTINUITY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря регулярных лекарств лечения холодовой цепи или медпитания&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUPPLY_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не импровизировать замену препарата&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-NCD|ENE|DOC|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;PHARMACY|HEALTHCARE|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHRONIC_DISEASE|OXYGEN_OR_POWER_DEPENDENT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;CLINICIAN_PHARMACIST_NATIONAL_HEALTH&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не импровизировать замену препарата&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:21 cells:31 -->
> [!abstract]- Запись 21 из 133 — MED-OB — Неотложное состояние при беременности или родах
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-OB&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Неотложное состояние при беременности или родах&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;PREGNANCY_RED_FLAG_OR_LABOR_COMPLICATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112_OR_URGENT_MATERNITY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112_OR_URGENT_MATERNITY&gt;FOLLOW_DISPATCH_AND_PERSON_PLAN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Красные флаги, срок беременности и локальный maternity-route требуют профессиональной карточки; не импровизировать акушерские процедуры&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|MED-NCD|TRANS|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MATERNITY|MEDICAL_ACCESS|ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;PREGNANCY|ALONE|LANGUAGE_BARRIER&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SNS_DGS_OBSTETRIC_SERVICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:22 cells:31 -->
> [!abstract]- Запись 22 из 133 — MED-DENTAL — Острая стоматологическая проблема травма зуба или отёк
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-DENTAL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Острая стоматологическая проблема травма зуба или отёк&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DENTAL_TRAUMA_SEVERE_PAIN_BLEEDING_OR_SWELLING&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&gt;DENTAL_SERVICE_OR_112_BY_CONDITION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Нарушение дыхания, быстро растущий отёк, тяжёлая травма или кровотечение меняют маршрут на экстренный&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|MED-TRAUMA|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;DENTAL_SERVICE|MEDICAL_ACCESS|ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|ANTICOAGULATION|IMMUNOCOMPROMISED&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SNS_DGS_DENTAL_SERVICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:23 cells:31 -->
> [!abstract]- Запись 23 из 133 — MED-SENSORY — Внезапная потеря зрения или слуха либо серьёзная травма глаза
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-SENSORY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Внезапная потеря зрения или слуха либо серьёзная травма глаза&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUDDEN_VISION_HEARING_LOSS_OR_EYE_INJURY&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;URGENT_PROFESSIONAL_ASSESSMENT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;URGENT_PROFESSIONAL_ASSESSMENT&gt;PROTECT_FUNCTION_WITHOUT_DELAYING_HELP&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не пытаться извлекать внедрённый объект; безопасно прекратить только очевидное продолжающееся воздействие и не откладывать срочную оценку&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|MED-TRAUMA|PPE|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;EYE_EMERGENCY|ENT_SERVICE|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;VISION|HEARING|CHILD|LANGUAGE_BARRIER&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SNS_DGS_OPHTHALMOLOGY_ENT&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:24 cells:31 -->
> [!abstract]- Запись 24 из 133 — MED-MH-CRISIS — Острый психический кризис или непосредственный риск самоповреждения
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;MED-MH-CRISIS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;MED&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Острый психический кризис или непосредственный риск самоповреждения&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;IMMEDIATE_SELF_HARM_OTHER_HARM_OR_ACUTE_CRISIS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;IMMEDIATE_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;IMMEDIATE_SAFETY&gt;CALL_112_IF_IMMEDIATE_DANGER&gt;TRUSTED_CRISIS_ROUTE_AND_CONTINUITY&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не оставлять человека одного при непосредственном риске, не обещать секретность и не применять принуждение вне закона/профессиональной помощи&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-MH|SAFE|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_SPACE|MEDICAL_ACCESS|TRUSTED_CONTACT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MENTAL_HEALTH_CONTINUITY|ALONE|CHILD|ADOLESCENT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SNS_DGS_MENTAL_HEALTH_EMERGENCY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:25 cells:31 -->
> [!abstract]- Запись 25 из 133 — BIO-RESP — Респираторная вспышка эпидемия или пандемия
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-RESP&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Респираторная вспышка эпидемия или пандемия&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_CLUSTER&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Меры зависят от возбудителя и текущего guidance&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|MED-ILL|INFO|SAN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|AIR_QUALITY|OFFICIAL_ZONES&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;IMMUNOCOMPROMISED&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_ECDC_WHO&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Меры зависят от возбудителя и текущего guidance&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:26 cells:31 -->
> [!abstract]- Запись 26 из 133 — BIO-WATER — Вспышка заболевания связанная с водой
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-WATER&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Вспышка заболевания связанная с водой&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_MUNICIPAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_CLUSTER&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Природная вода не считается питьевой по карте&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|SAN|MED-ILL|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_SOURCE|DISTRIBUTION_ZONE|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;WATER_AUTHORITY_DGS_WHO&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Природная вода не считается питьевой по карте&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:27 cells:31 -->
> [!abstract]- Запись 27 из 133 — BIO-FOOD — Пищевое отравление или cluster
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-FOOD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Пищевое отравление или cluster&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_CLUSTER&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Сохранить идентификацию партии без повторного употребления&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FOOD|MED-ILL|SAN|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SUPPLY_SOURCE|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;FOOD_AUTHORITY_DGS_WHO&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сохранить идентификацию партии без повторного употребления&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:28 cells:31 -->
> [!abstract]- Запись 28 из 133 — BIO-ZOON — Зооноз укус или контакт с животным
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-ZOON&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Зооноз укус или контакт с животным&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;EXPOSURE_OR_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Человеческий и ветеринарный контуры разделены&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|PET|PPE|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;VET|HEALTHCARE|EXPOSURE_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;PET|LIVESTOCK&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_VETERINARY_WHO&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Человеческий и ветеринарный контуры разделены&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:29 cells:31 -->
> [!abstract]- Запись 29 из 133 — BIO-VECTOR — Болезни комаров клещей и других переносчиков
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-VECTOR&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Болезни комаров клещей и других переносчиков&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SEASONAL_ALERT_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Профилактика и симптомы по локальному виду&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PPE|SHEL|MED-ILL|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;VECTOR_RISK|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_ECDC_WHO&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Профилактика и симптомы по локальному виду&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:30 cells:31 -->
> [!abstract]- Запись 30 из 133 — BIO-WOUND — Признаки инфекции раны: оценка красных флагов
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-WOUND&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Признаки инфекции раны: оценка красных флагов&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;112 только при угрозе жизни; иначе требуется проверенная клиническая маршрутизация; домашняя хирургия запрещена&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|MED-ILL|SAN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;IMMUNOCOMPROMISED&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_HEALTH_IFRC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;112 только при угрозе жизни; иначе требуется проверенная клиническая маршрутизация; домашняя хирургия запрещена&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:31 cells:31 -->
> [!abstract]- Запись 31 из 133 — BIO-MOLD — Плесень и влажность после затопления
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-MOLD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Плесень и влажность после затопления&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_OR_SHELTER&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Вход и очистка зависят от безопасности здания и PPE&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|HOME|REC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;FLOOD_ZONE|BUILDING&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;RESPIRATORY_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_WHO_BUILDING_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Вход и очистка зависят от безопасности здания и PPE&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:32 cells:31 -->
> [!abstract]- Запись 32 из 133 — BIO-INFEST — Вредители паразиты педикулёз чесотка или infestation
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;BIO-INFEST&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;BIO&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Вредители паразиты педикулёз чесотка или infestation&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_OR_SHELTER&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не смешивать человеческие и ветеринарные средства&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAN|PPE|MED-ILL|PET&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SHELTER|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;TEMPORARY_SHELTER&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_WHO_VETERINARY_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не смешивать человеческие и ветеринарные средства&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:33 cells:31 -->
> [!abstract]- Запись 33 из 133 — NAT-EQ — Землетрясение и афтершоки
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-EQ&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Землетрясение и афтершоки&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PROTECT_DURING_SHAKING&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PROTECT_DURING_SHAKING&gt;ASSESS_SCENE_AND_PEOPLE&gt;EXIT_IF_UNSAFE_OR_OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Сначала защита во время толчков; выход после прекращения толчков, если здание небезопасно или так указано официально&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|FIRE|MED-TRAUMA|NAV|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SEISMIC|BUILDING|OPEN_AREA|ROAD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;BUILDING_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_IPMA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;После события мосты здания и газ требуют отдельной оценки&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:34 cells:31 -->
> [!abstract]- Запись 34 из 133 — NAT-TSU — Цунами
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-TSU&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Цунами&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;COASTAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;NATURAL_SIGN_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Локальный маршрут только по официальному плану и field check&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|COM|TRANS|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;TSUNAMI|ELEVATION|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;COAST|MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_IPMA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Локальный маршрут только по официальному плану и field check&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:35 cells:31 -->
> [!abstract]- Запись 35 из 133 — NAT-VOLC — Вулканическое событие пепел газ или лава
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-VOLC&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Вулканическое событие пепел газ или лава&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Применимо прежде всего к соответствующей территории&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|SHEL|NAV|WAT&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;VOLCANIC|EVAC_ROUTE|AIR_QUALITY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ISLAND&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;REGIONAL_CIVIL_PROTECTION_VOLCANO_OBSERVATORY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Применимо прежде всего к соответствующей территории&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:36 cells:31 -->
> [!abstract]- Запись 36 из 133 — NAT-FLD — Речное дождевое или прибрежное наводнение
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-FLD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Речное дождевое или прибрежное наводнение&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не входить и не въезжать в воду&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|TRANS|WAT|SAN|REC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;FLOOD_DEPTH|VELOCITY|ELEVATION|ROAD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не входить и не въезжать в воду&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:37 cells:31 -->
> [!abstract]- Запись 37 из 133 — NAT-FLASH — Внезапный паводок или быстрый поток
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-FLASH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Внезапный паводок или быстрый поток&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Время на решение может быть очень коротким&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|TRANS|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;DRAINAGE|ELEVATION|NO_GO&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_IPMA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Время на решение может быть очень коротким&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:38 cells:31 -->
> [!abstract]- Запись 38 из 133 — NAT-WIL — Природный пожар
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-WIL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Природный пожар&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не двигаться в дым и не считать structural risk live fire&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|TRANS|AIR|PPE|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;FIRE_HAZARD|ACTIVE_FIRE|ROAD|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;FOREST_EDGE|PET&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_ICNF_IPMA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не двигаться в дым и не считать structural risk live fire&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:39 cells:31 -->
> [!abstract]- Запись 39 из 133 — NAT-SMOKE — Дым и опасное качество воздуха
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-SMOKE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Дым и опасное качество воздуха&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_DATA_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Респиратор и фильтрация требуют правильного выбора&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|SHEL|MED-ILL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;AIR_QUALITY|FIRE|CLEAN_AIR_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;RESPIRATORY_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_APA_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Респиратор и фильтрация требуют правильного выбора&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:40 cells:31 -->
> [!abstract]- Запись 40 из 133 — NAT-STORM — Шторм сильный ветер или интенсивные осадки
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-STORM&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Шторм сильный ветер или интенсивные осадки&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_WARNING_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Учитывать каскадные отключения и повреждения&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|FIRE|ENE|NAV|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WEATHER|FLOOD|ROAD|TREE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_ANEPC_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Учитывать каскадные отключения и повреждения&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:41 cells:31 -->
> [!abstract]- Запись 41 из 133 — NAT-LIGHTNING — Молния и гроза
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-LIGHTNING&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Молния и гроза&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_WARNING_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не импровизировать убежище без актуальной карточки&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|MED-TRAUMA|ENE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WEATHER|SAFE_BUILDING&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;OUTDOOR&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не импровизировать убежище без актуальной карточки&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:42 cells:31 -->
> [!abstract]- Запись 42 из 133 — NAT-HEAT — Экстремальная жара
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-HEAT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Экстремальная жара&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_WARNING_OR_TEMPERATURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Лекарства и хронические болезни требуют персонального плана&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|WAT|SHEL|ENE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEAT|COOLING_SITE|WATER|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE|CHRONIC_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_DGS_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Лекарства и хронические болезни требуют персонального плана&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:43 cells:31 -->
> [!abstract]- Запись 43 из 133 — NAT-COLD — Экстремальный холод снег или лёд
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-COLD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Экстремальный холод снег или лёд&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_WARNING_OR_TEMPERATURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Горение внутри создаёт CO-риск&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|ENE|MED-ILL|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;COLD|ROAD|WARMING_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;AGE_PROFILE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_DGS_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Горение внутри создаёт CO-риск&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:44 cells:31 -->
> [!abstract]- Запись 44 из 133 — NAT-LANDSLIDE — Оползень обвал или просадка
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-LANDSLIDE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Оползень обвал или просадка&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не входить на неустойчивый склон или в повреждённое здание&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|SHEL|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SLOPE|GEOLOGY|NO_GO|ROAD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_MUNICIPAL_LNEG&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не входить на неустойчивый склон или в повреждённое здание&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:45 cells:31 -->
> [!abstract]- Запись 45 из 133 — NAT-AVALANCHE — Лавина или снежный склон
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-AVALANCHE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Лавина или снежный склон&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Только для применимой территории и с профильной подготовкой&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|PPE|COM|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;AVALANCHE|SLOPE|NO_GO&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MOUNTAIN&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;REGIONAL_MOUNTAIN_RESCUE_MET_SERVICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Только для применимой территории и с профильной подготовкой&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:46 cells:31 -->
> [!abstract]- Запись 46 из 133 — NAT-DROUGHT — Засуха и длительный дефицит воды
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-DROUGHT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Засуха и длительный дефицит воды&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;REGIONAL_TO_LONG_TERM&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_STATUS_OR_SUPPLY_DECLINE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Законность водозабора и качество проверяются отдельно&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|FOOD|AGR|FIN|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_RESOURCE|RESTRICTION|FIRE_HAZARD&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E3_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;APA_IPMA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Законность водозабора и качество проверяются отдельно&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:47 cells:31 -->
> [!abstract]- Запись 47 из 133 — NAT-COAST — Штормовой нагон высокие волны или береговая эрозия
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-COAST&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Штормовой нагон высокие волны или береговая эрозия&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;COASTAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_WARNING_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не приближаться к берегу ради наблюдения&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|SHEL|TRANS|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;COASTAL_HAZARD|ELEVATION|NO_GO&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;COAST&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_APA_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не приближаться к берегу ради наблюдения&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:48 cells:31 -->
> [!abstract]- Запись 48 из 133 — NAT-DUST — Пыль песок или зола в воздухе
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-DUST&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Пыль песок или зола в воздухе&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_DATA_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Фильтрация и уборка по типу загрязнения&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|MED-ILL|HOME&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;AIR_QUALITY|WEATHER&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;RESPIRATORY_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_DGS_APA&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Фильтрация и уборка по типу загрязнения&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:49 cells:31 -->
> [!abstract]- Запись 49 из 133 — NAT-ANIMAL — Контакт с опасным животным или растением, укусы и ужаления: оценка красных флагов
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-ANIMAL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Контакт с опасным животным или растением, укусы и ужаления: оценка красных флагов&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_EXPOSURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_RED_FLAGS&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;112 при угрозе жизни, тяжёлой реакции или иной экстренной развилке; в остальных случаях маршрут зависит от вида контакта и официальной медицинской рекомендации; универсального антидота нет&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-ILL|PET|PPE|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|VET|EXPOSURE_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|PET&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DGS_ICNF_VETERINARY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;112 при угрозе жизни, тяжёлой реакции или иной экстренной развилке; в остальных случаях маршрут зависит от вида контакта и официальной медицинской рекомендации; универсального антидота нет&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:50 cells:31 -->
> [!abstract]- Запись 50 из 133 — NAT-SPACE — Космическая погода влияющая на связь или энергетику
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;NAT-SPACE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;NAT&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Космическая погода влияющая на связь или энергетику&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;NATIONAL_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Рассматривать как инфраструктурный каскад&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;ENE|COM|NAV|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;INFRASTRUCTURE|GNSS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E3_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_MET_SPACE_WEATHER_AUTHORITIES&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Рассматривать как инфраструктурный каскад&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:51 cells:31 -->
> [!abstract]- Запись 51 из 133 — TEC-FIRE — Пожар в здании
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-FIRE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Пожар в здании&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ALARM_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не возвращаться за вещами&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIRE|COM|GOV|MED-TRAUMA&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING_EXIT|ASSEMBLY_POINT|FIRE_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;APARTMENT_HIGH_RISE|MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_FIRE_SERVICE_BUILDING_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не возвращаться за вещами&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:52 cells:31 -->
> [!abstract]- Запись 52 из 133 — TEC-CO — Угарный газ или продукты горения
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-CO&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Угарный газ или продукты горения&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_OR_VEHICLE&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ALARM_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не искать источник внутри при продолжающейся опасности&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIRE|AIR|MED-ILL|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING_EXIT|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;GENERATOR&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_DGS_FIRE_SERVICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не искать источник внутри при продолжающейся опасности&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:53 cells:31 -->
> [!abstract]- Запись 53 из 133 — TEC-GAS — Утечка горючего газа
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-GAS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Утечка горючего газа&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_OR_LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ODOR_ALARM_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не создавать искру&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIRE|COM|HOME&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING_EXIT|UTILITY_ZONE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;GAS_OPERATOR_ANEPC_FIRE_SERVICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не создавать искру&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:54 cells:31 -->
> [!abstract]- Запись 54 из 133 — TEC-EXPLOSION — Взрыв или blast incident
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-EXPLOSION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Взрыв или blast incident&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Учитывать вторичные устройства и неустойчивые конструкции&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-TRAUMA|FIRE|NAV|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;NO_GO|RESCUE_ACCESS|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_FIRE_POLICE_MEDICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Учитывать вторичные устройства и неустойчивые конструкции&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:55 cells:31 -->
> [!abstract]- Запись 55 из 133 — TEC-COLLAPSE — Обрушение или серьёзное повреждение здания
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-COLLAPSE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Обрушение или серьёзное повреждение здания&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_OR_LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не проводить самовольный structural search&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|MED-TRAUMA|COM|NAV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING|NO_GO|RESCUE_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_FIRE_ENGINEERING_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не проводить самовольный structural search&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:56 cells:31 -->
> [!abstract]- Запись 56 из 133 — TEC-BATTERY — Пожар или thermal runaway аккумулятора
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-BATTERY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Пожар или thermal runaway аккумулятора&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_OR_VEHICLE&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_ALARM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Тип батареи и действия требуют карточки производителя/служб&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIRE|ENE|PPE|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING_EXIT|HAZMAT_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;FIRE_SERVICE_MANUFACTURER&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Тип батареи и действия требуют карточки производителя/служб&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:57 cells:31 -->
> [!abstract]- Запись 57 из 133 — TEC-CHEM-LOCAL — Локальный химический разлив или непосредственная экспозиция
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-CHEM-LOCAL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Локальный химический разлив или непосредственная экспозиция&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_SCENE&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_EXPOSURE_OR_LOCAL_RELEASE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REMOVE_FROM_EXPOSURE_IF_SAFE&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REMOVE_FROM_EXPOSURE_IF_SAFE&gt;CALL_112_OR_CIAV&gt;DECONTAMINATION_ONLY_PER_SAFE_GUIDANCE&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не входить в облако и не ждать точной идентификации перед прекращением безопасно устранимой экспозиции&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PPE|AIR|COM|MED-ILL|NAV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SEVESO|WIND|NO_GO|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;INDUSTRIAL_NEARBY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_DGS_CIAV&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Уйти или укрыться зависит от вещества и официальной команды&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:58 cells:31 -->
> [!abstract]- Запись 58 из 133 — TEC-CHEM-PLUME — Внешнее химическое облако или промышленный выброс
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-CHEM-PLUME&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Внешнее химическое облако или промышленный выброс&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_OBSERVED_EXTERNAL_RELEASE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION&gt;CONTROL_AIR_PATHS_IF_SHELTERED&gt;REASSESS_FROM_OFFICIAL_SOURCE&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Направление ухода или укрытие зависят от вещества, ветра, здания и официальной команды; не строить бытовую plume-модель&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PPE|AIR|COM|MED-ILL|NAV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SEVESO|WIND|OFFICIAL_ZONE|NO_GO|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;INDUSTRIAL_NEARBY|RESPIRATORY_DISEASE|MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_DGS_CIAV&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:59 cells:31 -->
> [!abstract]- Запись 59 из 133 — TEC-HAZMAT-TRANSPORT — ДТП с опасным грузом или неизвестным веществом
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-HAZMAT-TRANSPORT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;ДТП с опасным грузом или неизвестным веществом&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не приближаться для чтения маркировки&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|PPE|AIR|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HAZMAT_ROUTE|NO_GO|WIND&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ROAD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_FIRE_POLICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не приближаться для чтения маркировки&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:60 cells:31 -->
> [!abstract]- Запись 60 из 133 — TEC-SEVESO — Крупная промышленная авария
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-SEVESO&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Крупная промышленная авария&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не строить самодельный безопасный радиус&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AIR|PPE|NAV|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SEVESO|OFFICIAL_ZONE|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;INDUSTRIAL_NEARBY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не строить самодельный безопасный радиус&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:61 cells:31 -->
> [!abstract]- Запись 61 из 133 — TEC-DAM — Авария плотины или быстрый downstream flood
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-DAM&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Авария плотины или быстрый downstream flood&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;MOVE_TO_HIGH_GROUND&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Только по официальной зоне и маршруту&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|TRANS|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;DAM_PLAN|DOWNSTREAM_ZONE|ELEVATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;DAM_DOWNSTREAM&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_MUNICIPAL_OPERATOR&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Только по официальной зоне и маршруту&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:62 cells:31 -->
> [!abstract]- Запись 62 из 133 — TEC-RAD-SOURCE — Подозрительный локальный радиационный источник
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-RAD-SOURCE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Подозрительный локальный радиационный источник&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не трогать и увеличить дистанцию&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PPE|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;NO_GO|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_RADNET_POLICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не трогать и увеличить дистанцию&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:63 cells:31 -->
> [!abstract]- Запись 63 из 133 — TEC-RAD-FALLOUT — Наружное радиологическое загрязнение или fallout
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-RAD-FALLOUT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Наружное радиологическое загрязнение или fallout&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_MAJOR_EVENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_PENDING_OFFICIAL&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Йод только по официальному указанию&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|AIR|PPE|WAT|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFICIAL_ZONE|RADNET|SAFE_BUILDING&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_APA_DGS&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Йод только по официальному указанию&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:64 cells:31 -->
> [!abstract]- Запись 64 из 133 — TEC-UNKNOWN-ITEM — Неизвестный порошок контейнер или подозрительный предмет
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-UNKNOWN-ITEM&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Неизвестный порошок контейнер или подозрительный предмет&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не трогать не нюхать не перемещать&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PPE|COM|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;NO_GO|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_FIRE_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не трогать не нюхать не перемещать&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:65 cells:31 -->
> [!abstract]- Запись 65 из 133 — TEC-UXO — Мина боеприпас или неразорвавшийся предмет
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-UXO&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Мина боеприпас или неразорвавшийся предмет&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_CONFLICT&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не приближаться и не маркировать рядом физически&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|NAV|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;NO_GO|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CONFLICT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_MILITARY_CIVIL_PROTECTION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не приближаться и не маркировать рядом физически&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:66 cells:31 -->
> [!abstract]- Запись 66 из 133 — TEC-ELECTRIC-SCENE — Оголённый провод затопленная электрика или иная действующая электрическая опасность
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-ELECTRIC-SCENE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Оголённый провод затопленная электрика или иная действующая электрическая опасность&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_ALARM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DO_NOT_TOUCH_OR_ENTER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DO_NOT_TOUCH_OR_ENTER&gt;ISOLATE_POWER_ONLY_IF_SAFE_AND_AUTHORIZED&gt;CALL_112_OR_UTILITY&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Пострадавшего или воду не касаться, пока источник не изолирован компетентно; отключение допустимо только без входа в опасную зону&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIRE|HOME|MED-BLS|COM|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;UTILITY_SHUTOFF|NO_GO|RESCUE_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|MOBILITY_LIMITATION|FLOODPLAIN&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_UTILITY_112&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:67 cells:31 -->
> [!abstract]- Запись 67 из 133 — TEC-CONFINED — Застревание в лифте тоннеле колодце или замкнутом пространстве
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;TEC-CONFINED&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;TEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Застревание в лифте тоннеле колодце или замкнутом пространстве&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_LOST_CONTACT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&gt;DO_NOT_ENTER_OR_IMPROVISE_RESCUE&gt;MAINTAIN_SAFE_CONTACT_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Неподготовленный вход может создать нескольких пострадавших из-за газа, энергии, воды, конструкции или ограниченного выхода&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|COM|NAV|MED-BLS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;EXACT_LOCATION|RESCUE_ACCESS|UTILITY_ZONE|NO_GO&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;UNDERGROUND|TUNNEL|MOBILITY_LIMITATION|CHILD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;112_FIRE_RESCUE_UTILITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:68 cells:31 -->
> [!abstract]- Запись 68 из 133 — INF-POWER — Отключение электричества
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-POWER&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Отключение электричества&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&gt;CHECK_OFFICIAL_STATUS&gt;ISOLATE_SPECIFIC_FAILED_EQUIPMENT_IF_NEEDED&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Обычный outage не равен опасному электрическому объекту; сначала люди, медзависимости, пожар/CO и официальная информация&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;ENE|FIRE|COM|MED-NCD|FOOD&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;UTILITY_ZONE|CHARGING|HEALTHCARE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;OXYGEN_OR_POWER_DEPENDENT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;GRID_OPERATOR_ANEPC_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;CO и холодовая цепь являются отдельными рисками&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:69 cells:31 -->
> [!abstract]- Запись 69 из 133 — INF-WATER-OFF — Прекращение или низкое давление воды
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-WATER-OFF&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Прекращение или низкое давление воды&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_MUNICIPAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Планировать хранение и refill до события&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|SAN|FOOD|MED-NCD&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_DISTRIBUTION|SUPPLY_POINTS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;WATER_OPERATOR_MUNICIPAL_DGS&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Планировать хранение и refill до события&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:70 cells:31 -->
> [!abstract]- Запись 70 из 133 — INF-WATER-CONTAM — Официальное или подозреваемое загрязнение водопровода
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-WATER-CONTAM&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Официальное или подозреваемое загрязнение водопровода&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_MUNICIPAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_NOTICE_OR_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Кипячение не исправляет любой тип загрязнения&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|SAN|INFO|MED-ILL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_DISTRIBUTION|OFFICIAL_ZONE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;WATER_OPERATOR_DGS_APA&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Кипячение не исправляет любой тип загрязнения&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:71 cells:31 -->
> [!abstract]- Запись 71 из 133 — INF-SEWER — Отказ канализации дренажа или туалета
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-SEWER&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Отказ канализации дренажа или туалета&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING_TO_MUNICIPAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE_OR_BACKFLOW&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Разделять чистую и загрязнённую зоны&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAN|WAT|PPE|HOME&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SEWER|FLOOD|WASTE_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ACCESSIBILITY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;MUNICIPAL_WATER_OPERATOR_DGS&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Разделять чистую и загрязнённую зоны&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:72 cells:31 -->
> [!abstract]- Запись 72 из 133 — INF-GAS-FUEL — Прекращение газа топлива или безопасной готовки
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-GAS-FUEL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Прекращение газа топлива или безопасной готовки&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUPPLY_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не переносить горение в жилой объём&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FOOD|ENE|FIRE|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;FUEL|SUPPLY|COOKING_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;UTILITY_OPERATOR_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не переносить горение в жилой объём&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:73 cells:31 -->
> [!abstract]- Запись 73 из 133 — INF-TEL — Отсутствие мобильной или телефонной связи
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-TEL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Отсутствие мобильной или телефонной связи&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Два приложения на одном телефоне не независимы&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;COM|INFO|GOV|NAV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;COVERAGE|MEETUP|MESSAGE_POINT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANACOM_OPERATORS_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Два приложения на одном телефоне не независимы&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:74 cells:31 -->
> [!abstract]- Запись 74 из 133 — INF-INTERNET — Отсутствие интернета или облачных сервисов
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-INTERNET&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Отсутствие интернета или облачных сервисов&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_GLOBAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Критические инструкции должны работать офлайн&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|CYB|DOC|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFLINE_RESOURCES|SERVICE_POINTS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PROVIDER_ANACOM&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Критические инструкции должны работать офлайн&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:75 cells:31 -->
> [!abstract]- Запись 75 из 133 — INF-GNSS — Недоступная или неверная спутниковая навигация
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-GNSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Недоступная или неверная спутниковая навигация&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DEVICE_ANOMALY_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Бумажная карта и навык обязательны&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|INFO|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;PAPER_MAP|LANDMARKS|ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;OFFICIAL_NAV_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Бумажная карта и навык обязательны&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:76 cells:31 -->
> [!abstract]- Запись 76 из 133 — INF-ROAD — Закрытие дороги мостов тоннелей или общественного транспорта
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-ROAD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Закрытие дороги мостов тоннелей или общественного транспорта&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_NOTICE_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Резерв не должен иметь тот же chokepoint&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;NAV|TRANS|COM|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ROAD|CLOSURE|CHOKEPOINT|ALT_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ROAD_OPERATOR_POLICE_ANEPC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Резерв не должен иметь тот же chokepoint&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:77 cells:31 -->
> [!abstract]- Запись 77 из 133 — INF-PAY — Платёжный банковский или ATM-сбой
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-PAY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Платёжный банковский или ATM-сбой&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Небольшой законный резерв и записи обязательств&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIN|DOC|CYB|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BANK|ADMIN|SUPPLY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;BANK_REGULATOR_PROVIDER_POLICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Небольшой законный резерв и записи обязательств&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:78 cells:31 -->
> [!abstract]- Запись 78 из 133 — INF-SUPPLY — Дефицит пищи лекарств топлива или расходников
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-SUPPLY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Дефицит пищи лекарств топлива или расходников&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUPPLY_DECLINE_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Ротация и раннее законное пополнение&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FOOD|MED-NCD|WAT|FIN|TRANS&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SUPPLY|PHARMACY|FUEL|ALT_REGION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E2_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SECTOR_AUTHORITIES_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Ротация и раннее законное пополнение&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:79 cells:31 -->
> [!abstract]- Запись 79 из 133 — INF-HEALTH — Перегрузка или недоступность здравоохранения и аптек
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-HEALTH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Перегрузка или недоступность здравоохранения и аптек&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SERVICE_FAILURE_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Continuity plan до кризиса&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-NCD|MED-ILL|TRANS|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|PHARMACY|ALT_REGION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHRONIC_DISEASE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SNS_DGS_MUNICIPAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Continuity plan до кризиса&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:80 cells:31 -->
> [!abstract]- Запись 80 из 133 — INF-HOUSING — Непригодность жилья или массовое временное размещение
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;INF-HOUSING&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;INF&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Непригодность жилья или массовое временное размещение&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Объект не считается открытым без подтверждения&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|DOC|FIN|SAN|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SHELTER|HOUSING|REUNIFICATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;PET|ACCESSIBILITY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;MUNICIPAL_ANEPC_SOCIAL_SERVICES&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Объект не считается открытым без подтверждения&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:81 cells:31 -->
> [!abstract]- Запись 81 из 133 — CYB-DEVICE — Потеря кража или поломка устройства
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-DEVICE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря кража или поломка устройства&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Удалённая блокировка и recovery по заранее сохранённому плану&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|DOC|COM|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;TRUSTED_SERVICE|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PLATFORM_VENDOR_POLICE_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Удалённая блокировка и recovery по заранее сохранённому плану&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:82 cells:31 -->
> [!abstract]- Запись 82 из 133 — CYB-ACCOUNT — Блокировка аккаунта или утрата MFA
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-ACCOUNT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Блокировка аккаунта или утрата MFA&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ACCESS_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Recovery-коды офлайн и наследуемая процедура&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|DOC|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;TRUSTED_SERVICE|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SERVICE_PROVIDER&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Recovery-коды офлайн и наследуемая процедура&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:83 cells:31 -->
> [!abstract]- Запись 83 из 133 — CYB-PHISH — Phishing social engineering или impersonation
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-PHISH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Phishing social engineering или impersonation&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUSPICIOUS_MESSAGE_OR_TRANSACTION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Проверять через независимый канал&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|FIN|SAFE|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;POLICE|BANK|SERVICE_PROVIDER&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;LANGUAGE_BARRIER&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_BANK_PROVIDER_CYBER_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Проверять через независимый канал&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:84 cells:31 -->
> [!abstract]- Запись 84 из 133 — CYB-MALWARE — Malware или ransomware
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-MALWARE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Malware или ransomware&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;DEVICE_TO_ORGANIZATION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SECURITY_ALERT_OR_ANOMALY&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Восстановление только из проверенного бэкапа&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|INFO|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;TRUSTED_DEVICE|RECOVERY_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;NATIONAL_CYBER_AUTHORITY_VENDOR&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Восстановление только из проверенного бэкапа&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:85 cells:31 -->
> [!abstract]- Запись 85 из 133 — CYB-DATA — Удаление порча или потеря данных
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-DATA&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Удаление порча или потеря данных&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;RESTORE_FAILURE_OR_MISSING_DATA&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Backup не доказан без restore-test&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|INFO|DOC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFSITE_BACKUP|TRUSTED_DEVICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;CISA_NATIONAL_CYBER_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Backup не доказан без restore-test&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:86 cells:31 -->
> [!abstract]- Запись 86 из 133 — CYB-LEAK — Утечка персональных медицинских или адресных данных
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-LEAK&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Утечка персональных медицинских или адресных данных&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;BREACH_NOTICE_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Оценить физические точки и доступы которые раскрыты&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;CYB|SAFE|DOC|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;POLICE|REGULATOR|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;DATA_PROTECTION_AUTHORITY_POLICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Оценить физические точки и доступы которые раскрыты&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:87 cells:31 -->
> [!abstract]- Запись 87 из 133 — CYB-DISINFO — Дезинформация подмена официального сообщения или deepfake
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-DISINFO&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Дезинформация подмена официального сообщения или deepfake&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_GLOBAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;CONFLICTING_MESSAGE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Сверять источник время и применимую территорию&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|COM|GOV|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFICIAL_SOURCE|CURRENT_ZONE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ANEPC_DGS_GOVERNMENT_PRIMARY_SOURCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сверять источник время и применимую территорию&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:88 cells:31 -->
> [!abstract]- Запись 88 из 133 — CYB-SMART-HOME — Отказ умного замка автоматики или удалённого управления
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;CYB-SMART-HOME&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Отказ умного замка автоматики или удалённого управления&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;BUILDING&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ACCESS_OR_CONTROL_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Нужен безопасный ручной fallback&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;HOME|FIRE|CYB|ENE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BUILDING_EXIT|MANUAL_CONTROL&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ACCESSIBILITY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;MANUFACTURER_BUILDING_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Нужен безопасный ручной fallback&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:89 cells:31 -->
> [!abstract]- Запись 89 из 133 — SEC-CRIME — Кража грабёж или преступление в моменте
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-CRIME&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Кража грабёж или преступление в моменте&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_BUILDING&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;CALL_112&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Приоритет уход дистанция и помощь&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|COM|DOC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_EXIT|POLICE|EXACT_LOCATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_112&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Приоритет уход дистанция и помощь&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:90 cells:31 -->
> [!abstract]- Запись 90 из 133 — SEC-DOMESTIC — Домашнее или гендерное насилие coercive control
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-DOMESTIC&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Домашнее или гендерное насилие coercive control&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DISCLOSURE_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DISCREET_SAFETY&gt;TRUSTED_CHANNEL_IF_SAFE&gt;CALL_112_IF_IMMEDIATE_DANGER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не провоцировать раскрытие плана или использование контролируемого устройства; 112 при непосредственной опасности&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|DOC|COM|SHEL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_SERVICE|SHELTER|POLICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_SOCIAL_HEALTH_SPECIALIST_SERVICES&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;План не должен быть доступен агрессору&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:91 cells:31 -->
> [!abstract]- Запись 91 из 133 — SEC-MISSING — Пропавший человек ребёнок или животное
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-MISSING&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Пропавший человек ребёнок или животное&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;MISSED_ACCOUNTABILITY&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не создавать новых пострадавших самовольным поиском&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|COM|NAV|SAFE|PET&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;LAST_KNOWN|ROUTE|POLICE|MEETUP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|PET&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_112_ANIMAL_AUTHORITY_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не создавать новых пострадавших самовольным поиском&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:92 cells:31 -->
> [!abstract]- Запись 92 из 133 — SEC-CROWD — Толпа паника давка или беспорядки
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-CROWD&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Толпа паника давка или беспорядки&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;EXIT_AND_DO_NOT_RETURN&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Ранний уход и reunification&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|NAV|COM|MED-TRAUMA&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;CROWD|SAFE_EXIT|MEETUP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|MOBILITY_LIMITATION&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_ANEPC_MEDICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Ранний уход и reunification&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:93 cells:31 -->
> [!abstract]- Запись 93 из 133 — SEC-MASS-VIOLENCE — Массовое насилие или террористический инцидент
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-MASS-VIOLENCE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Массовое насилие или террористический инцидент&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ESCAPE_OR_PROTECTIVE_SHELTER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ESCAPE_OR_PROTECTIVE_SHELTER&gt;CALL_112_WHEN_SAFE&gt;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Немедленная физическая защита предшествует звонку, если звонок задерживает уход или раскрывает позицию&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|COM|MED-TRAUMA|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;NO_GO|POLICE|MEDICAL_ACCESS&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_ANEPC_MEDICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Без наступательных или оружейных инструкций&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:94 cells:31 -->
> [!abstract]- Запись 94 из 133 — SEC-CONFLICT — Вооружённый конфликт обстрел или вынужденное перемещение
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-CONFLICT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Вооружённый конфликт обстрел или вынужденное перемещение&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;REGIONAL_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_ALERT_OR_DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Мины и UXO отдельный default-deny контур&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|SHEL|NAV|DOC|MED-NCD&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFICIAL_ZONE|SHELTER|BORDER|EVAC_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;DISPLACED&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;CIVIL_PROTECTION_GOVERNMENT_HUMANITARIAN&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Мины и UXO отдельный default-deny контур&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:95 cells:31 -->
> [!abstract]- Запись 95 из 133 — SEC-EXPLOIT — Эксплуатация trafficking или мошенническая помощь
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-EXPLOIT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Эксплуатация trafficking или мошенническая помощь&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUSPICIOUS_OFFER_OR_DISCLOSURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DISCREET_SAFETY&gt;PRESERVE_EVIDENCE_IF_SAFE&gt;TRUSTED_AUTHORITY_OR_112_IF_IMMEDIATE_DANGER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не сообщать подозреваемому о плане и не ставить пострадавшего под дополнительный риск&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|DOC|COM|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;POLICE|SOCIAL_SERVICE|SAFE_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|MIGRANT&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_SOCIAL_SPECIALIST_SERVICES&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Проверять личность и организацию независимо&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:96 cells:31 -->
> [!abstract]- Запись 96 из 133 — SEC-INTERNAL — Конфликт внутри группы или unsafe behavior
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SEC-INTERNAL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SEC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Конфликт внутри группы или unsafe behavior&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Safety veto и внешняя помощь при угрозе&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|SAFE|MED-MH|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_SPACE|EXTERNAL_HELP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HEALTH_SOCIAL_POLICE_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Safety veto и внешняя помощь при угрозе&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:97 cells:31 -->
> [!abstract]- Запись 97 из 133 — SOC-HOME-LOSS — Потеря жилья пожар наводнение выселение или непригодность
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-HOME-LOSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря жилья пожар наводнение выселение или непригодность&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION_OR_OFFICIAL_NOTICE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Сохранить доказательства без входа в опасное здание&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|DOC|FIN|REC|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SHELTER|ADMIN|INSURER&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;PET|ACCESSIBILITY&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;MUNICIPAL_SOCIAL_INSURER_LEGAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Сохранить доказательства без входа в опасное здание&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:98 cells:31 -->
> [!abstract]- Запись 98 из 133 — SOC-INCOME — Потеря работы дохода или длительный кассовый разрыв
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-INCOME&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря работы дохода или длительный кассовый разрыв&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;FINANCIAL_EVENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Приоритет непрерывность жилья здоровья и питания&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;FIN|DOC|FOOD|SHEL|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SOCIAL_SERVICE|BANK|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E3_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;GOV_BANK_SOCIAL_LEGAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Приоритет непрерывность жилья здоровья и питания&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:99 cells:31 -->
> [!abstract]- Запись 99 из 133 — SOC-DOC — Потеря паспорта ВНЖ рецепта страховки или ключевого документа
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-DOC&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря паспорта ВНЖ рецепта страховки или ключевого документа&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Офлайн копия не заменяет оригинал но ускоряет восстановление&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;DOC|LEG|CYB|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ADMIN|CONSULATE|POLICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ABROAD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;GOV_CONSULATE_POLICE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Офлайн копия не заменяет оригинал но ускоряет восстановление&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:100 cells:31 -->
> [!abstract]- Запись 100 из 133 — SOC-MIGRATION — Срочная миграция граница или эвакуация за рубеж
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-MIGRATION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Срочная миграция граница или эвакуация за рубеж&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION_OR_LOSS_OF_SAFETY&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Правила пересечения и статус проверяются непосредственно перед действием&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;DOC|LEG|NAV|MED-NCD|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;BORDER|CONSULATE|EVAC_ROUTE|SHELTER&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ABROAD|PET&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;GOV_CONSULATE_BORDER_HUMANITARIAN&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Правила пересечения и статус проверяются непосредственно перед действием&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:101 cells:31 -->
> [!abstract]- Запись 101 из 133 — SOC-CAREGIVER — Госпитализация смерть или недоступность caregiver
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-CAREGIVER&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Госпитализация смерть или недоступность caregiver&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Резервный caregiver и доступ к индивидуальному плану&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|MED-NCD|SAFE|PET|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|AUTHORIZED_CAREGIVER|MEETUP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD|DEPENDENT_CARE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HEALTH_SOCIAL_LEGAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Резервный caregiver и доступ к индивидуальному плану&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:102 cells:31 -->
> [!abstract]- Запись 102 из 133 — SOC-DEATH — Смерть утрата и последующие процедуры
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-DEATH&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Смерть утрата и последующие процедуры&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_MULTI&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;PROFESSIONAL_CONFIRMATION_OR_EVENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не импровизировать юридические или медицинские процедуры&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;DEAD|DOC|LEG|MED-MH|REC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|POLICE|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HEALTH_POLICE_MUNICIPAL_LEGAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не импровизировать юридические или медицинские процедуры&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:103 cells:31 -->
> [!abstract]- Запись 103 из 133 — SOC-INSURANCE — Страховой ущерб и восстановление имущества
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-INSURANCE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Страховой ущерб и восстановление имущества&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;LOSS_EVENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Безопасность выше фото ущерба&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;REC|DOC|FIN|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;INSURER|ADMIN|SAFE_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;INSURER_GOV_LEGAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Безопасность выше фото ущерба&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:104 cells:31 -->
> [!abstract]- Запись 104 из 133 — SOC-ISOLATION — Длительная изоляция горе или разрушение распорядка
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;SOC-ISOLATION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;SOC&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Длительная изоляция горе или разрушение распорядка&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DURATION_OR_SYMPTOM&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Суицидальный риск имеет отдельный срочный маршрут&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED-MH|COMM|EDU|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTHCARE|COMMUNITY|SAFE_SPACE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;ALONE&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HEALTH_SOCIAL_COMMUNITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Суицидальный риск имеет отдельный срочный маршрут&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:105 cells:31 -->
> [!abstract]- Запись 105 из 133 — ENV-SOIL-WATER — Длительное загрязнение почвы грунтовой воды или урожая
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-SOIL-WATER&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Длительное загрязнение почвы грунтовой воды или урожая&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OFFICIAL_FINDING_OR_TEST&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Бытовой тест не заменяет профильную лабораторию&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|AGR|FOOD|LEG|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;CONTAMINATION|WATER_RESOURCE|LAND_USE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;APA_DGS_AGRICULTURE_LAB&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Бытовой тест не заменяет профильную лабораторию&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:106 cells:31 -->
> [!abstract]- Запись 106 из 133 — ENV-CROP — Неурожай вредители или болезнь растений
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-CROP&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Неурожай вредители или болезнь растений&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OBSERVATION_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не использовать запрещённые средства&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AGR|FOOD|PRES|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;LAND_USE|WATER|SUPPLY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;AGRICULTURE_AUTHORITY_EXTENSION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не использовать запрещённые средства&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:107 cells:31 -->
> [!abstract]- Запись 107 из 133 — ENV-ANIMAL — Болезнь или гибель животных
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-ANIMAL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Болезнь или гибель животных&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SYMPTOM_OR_OFFICIAL_ALERT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Ветеринарный и человеческий контуры разделены&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;PET|FOOD|PPE|SAN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;VET|QUARANTINE|SUPPLY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;PET|LIVESTOCK&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;VETERINARY_AGRICULTURE_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Ветеринарный и человеческий контуры разделены&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:108 cells:31 -->
> [!abstract]- Запись 108 из 133 — ENV-RESOURCE — Истощение топлива материалов запчастей или расходников
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-RESOURCE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Истощение топлива материалов запчастей или расходников&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_SYSTEMIC&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;INVENTORY_TREND&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Переход к ремонту стандартизации и обмену&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;TOOL|ENE|FIN|COMM|AGR&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SUPPLY|REPAIR|ALTERNATE_REGION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E3_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;SECTOR_AUTHORITIES_MANUFACTURERS&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Переход к ремонту стандартизации и обмену&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:109 cells:31 -->
> [!abstract]- Запись 109 из 133 — ENV-KNOWLEDGE — Потеря навыка инструкции формата или совместимости архива
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-KNOWLEDGE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря навыка инструкции формата или совместимости архива&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_TO_GENERATIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;REVIEW_OR_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Миграция форматов и обучение следующего&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|EDU|CYB|TOOL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ARCHIVE|TRAINING|SERVICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_PUBLISHER_STANDARDS_BODY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Миграция форматов и обучение следующего&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;CAPABILITY_CONTINUITY&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:110 cells:31 -->
> [!abstract]- Запись 110 из 133 — ENV-CLIMATE — Долгосрочное изменение климата и локальной пригодности жилья
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;ENV-CLIMATE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;ENV&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Долгосрочное изменение климата и локальной пригодности жилья&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;LOCAL_TO_LONG_TERM&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;TREND_AND_OFFICIAL_ASSESSMENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Адаптация по измеренным локальным рискам&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|WAT|AGR|FIN|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;CLIMATE|WATER|FIRE|COAST|HEAT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;IPMA_APA_MUNICIPAL_EU&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Адаптация по измеренным локальным рискам&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:111 cells:31 -->
> [!abstract]- Запись 111 из 133 — OPS-ALONE — Одиночный участник не выходит на связь
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-ALONE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Одиночный участник не выходит на связь&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;MISSED_CHECKIN&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Заранее заданная лестница эскалации&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;COM|GOV|SAFE|MED-ILL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;LAST_KNOWN|ROUTE|EXTERNAL_CONTACT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HOUSEHOLD_POLICE_MEDICAL_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Заранее заданная лестница эскалации&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:112 cells:31 -->
> [!abstract]- Запись 112 из 133 — OPS-KEY-PERSON — Координатор водитель caregiver или навигатор недоступен
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-KEY-PERSON&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Координатор водитель caregiver или навигатор недоступен&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ROLE_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Succession или minimal safe mode&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|TRANS|MED-NCD|NAV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEETUP|EVAC_ROUTE|EXTERNAL_HELP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N2_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;ROLE_SPECIFIC_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Succession или minimal safe mode&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:113 cells:31 -->
> [!abstract]- Запись 113 из 133 — OPS-SEPARATION — Группа разделилась или потеряла участника
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-SEPARATION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Группа разделилась или потеряла участника&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;ACCOUNTABILITY_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не искать в опасной зоне без служб&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|COM|NAV|SAFE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;MEETUP|LAST_KNOWN|ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;CHILD&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N2_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;POLICE_112_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не искать в опасной зоне без служб&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:114 cells:31 -->
> [!abstract]- Запись 114 из 133 — OPS-KIT-LOSS — Потерян украден или недоступен критический комплект
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-KIT-LOSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потерян украден или недоступен критический комплект&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_OR_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DIRECT_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Критические функции распределяются по разным failure domains&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|TRANS|DOC|MED-NCD|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;CACHE|SUPPLY|ADMIN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HOUSEHOLD_PROVIDER_POLICE_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Критические функции распределяются по разным failure domains&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:115 cells:31 -->
> [!abstract]- Запись 115 из 133 — OPS-DEVICE-FAIL — Не работает фильтр энергия связь транспорт или иное критическое устройство
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-DEVICE-FAIL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Не работает фильтр энергия связь транспорт или иное критическое устройство&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_OR_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;TEST_OR_RUNTIME_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ISOLATE_AND_LOCKOUT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Использовать независимый fallback а не опасный ремонт&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|ENE|COM|TRANS|TOOL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;REPAIR|SUPPLY|ALTERNATE_ROUTE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;MANUFACTURER_SERVICE_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Использовать независимый fallback а не опасный ремонт&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:116 cells:31 -->
> [!abstract]- Запись 116 из 133 — OPS-STALE-INFO — Инструкция карта источник или контакт устарели или противоречат
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-STALE-INFO&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Инструкция карта источник или контакт устарели или противоречат&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;HOUSEHOLD_OR_GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;REVIEW_OR_CONFLICT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Fail closed для опасных действий&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|GOV|NAV|COM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFICIAL_SOURCE|CURRENT_ZONE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_CURRENT_AUTHORITY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Fail closed для опасных действий&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:117 cells:31 -->
> [!abstract]- Запись 117 из 133 — OPS-FATIGUE — Усталость паника или конфликт нарушают способность группы
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;OPS-FATIGUE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;OPS&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Усталость паника или конфликт нарушают способность группы&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;GROUP&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;OBSERVED_PERFORMANCE_DECLINE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;REUNIFY_AND_ACCOUNT&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Передать роль и включить минимально безопасный режим&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|MED-MH|SAFE|SHEL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;REST_SITE|EXTERNAL_HELP&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E0_E4&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;HEALTH_SOCIAL_AS_APPLICABLE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Передать роль и включить минимально безопасный режим&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;RECURRENT_OVER_LIFECYCLE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:118 cells:31 -->
> [!abstract]- Запись 118 из 133 — GEN-SUCCESSION-FAIL — Срыв передачи критической роли полномочия или доступа
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-SUCCESSION-FAIL&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Срыв передачи критической роли полномочия или доступа&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUCCESSION_TRIGGER_OR_OWNER_LOSS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Переход не активен без согласия права и handoff-test&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|INFO|DOC|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ARCHIVE|REGISTRY|EXTERNAL_OVERSIGHT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Переход не активен без согласия права и handoff-test&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:119 cells:31 -->
> [!abstract]- Запись 119 из 133 — GEN-GOV-CAPTURE — Захват управления или постоянное чрезвычайное полномочие
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-GOV-CAPTURE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Захват управления или постоянное чрезвычайное полномочие&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;AUTHORITY_ABUSE_OR_EXPIRY_BYPASS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Безопасность и закон выше внутреннего приказа&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|SAFE|LEG|COMM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;EXTERNAL_OVERSIGHT|SAFE_CONTACT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Безопасность и закон выше внутреннего приказа&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:120 cells:31 -->
> [!abstract]- Запись 120 из 133 — GEN-GOV-INCAPACITY — Недееспособность или отсутствие органа управления
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-GOV-INCAPACITY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Недееспособность или отсутствие органа управления&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;QUORUM_OR_AUTHORITY_LOSS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Временная власть имеет scope и expiry&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|DOC|LEG|COMM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;REGISTRY|EXTERNAL_OVERSIGHT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Временная власть имеет scope и expiry&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:121 cells:31 -->
> [!abstract]- Запись 121 из 133 — GEN-INTERNAL-CONFLICT — Разрушительный внутренний конфликт и потеря сотрудничества
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-INTERNAL-CONFLICT&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Разрушительный внутренний конфликт и потеря сотрудничества&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;CELL_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;CONFLICT_ESCALATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Никаких offensive или coercive процедур&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|GOV|COMM|MED-MH&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_CONTACT|MEDIATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Никаких offensive или coercive процедур&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:122 cells:31 -->
> [!abstract]- Запись 122 из 133 — GEN-SAFEGUARDING-ABUSE — Насилие эксплуатация или нарушение safeguarding внутри системы
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-SAFEGUARDING-ABUSE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Насилие эксплуатация или нарушение safeguarding внутри системы&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;PERSON_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DISCLOSURE_OR_OBSERVATION&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;DISCREET_SAFETY&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Защита пострадавшего и внешняя помощь приоритетны&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SAFE|GOV|LEG|MED&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;SAFE_CONTACT|AUTHORITY|EXIT&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Защита пострадавшего и внешняя помощь приоритетны&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:123 cells:31 -->
> [!abstract]- Запись 123 из 133 — GEN-TENURE-DISPUTE — Спор о праве собственности пользования или границе
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-TENURE-DISPUTE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Спор о праве собственности пользования или границе&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;SITE_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;LEGAL_NOTICE_OR_CONFLICT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не применять силу и не считать внутреннюю запись титулом&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;LEG|DOC|GOV|SHEL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;REGISTRY|CADASTRE|LEGAL_SERVICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не применять силу и не считать внутреннюю запись титулом&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:124 cells:31 -->
> [!abstract]- Запись 124 из 133 — GEN-INHERITANCE-FRAGMENTATION — Фрагментация актива или прав при наследовании
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-INHERITANCE-FRAGMENTATION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Фрагментация актива или прав при наследовании&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SUCCESSION_EVENT&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Нужен jurisdiction-specific legal review&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;LEG|DOC|GOV|FIN&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;REGISTRY|LEGAL_SERVICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Нужен jurisdiction-specific legal review&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:125 cells:31 -->
> [!abstract]- Запись 125 из 133 — GEN-WATER-RIGHT-LOSS — Утрата или ограничение законного доступа к воде
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-WATER-RIGHT-LOSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Утрата или ограничение законного доступа к воде&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;SITE_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;PERMIT_NOTICE_OR_ACCESS_LOSS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Ownership of land не создаёт water right&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;WAT|LEG|AGR|FOOD|REC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;WATER_AUTHORITY|ALTERNATE_SOURCE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Ownership of land не создаёт water right&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:126 cells:31 -->
> [!abstract]- Запись 126 из 133 — GEN-SEED-LINE-LOSS — Потеря жизнеспособности происхождения или права на семенную линию
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-SEED-LINE-LOSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря жизнеспособности происхождения или права на семенную линию&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;SITE_TO_NETWORK&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;GERMINATION_FAILURE_OR_PROVENANCE_LOSS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не распространять болезнь или материал с неясными правами&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;AGR|FOOD|INFO|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;GENEBANK|SUPPLIER|SAFETY_DUPLICATE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не распространять болезнь или материал с неясными правами&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:127 cells:31 -->
> [!abstract]- Запись 127 из 133 — GEN-SKILL-LINE-BREAK — Потеря критической компетенции и линии обучения
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-SKILL-LINE-BREAK&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря критической компетенции и линии обучения&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;CELL_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;HOLDER_LOSS_OR_ASSESSMENT_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Снизить scope до minimal-safe-mode&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;EDU|TOOL|INFO|COMM&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;TRAINING|EXTERNAL_SPECIALIST&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Снизить scope до minimal-safe-mode&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:128 cells:31 -->
> [!abstract]- Запись 128 из 133 — GEN-CARE-CAPACITY-COLLAPSE — Спрос на уход превышает доказанную capacity
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-CARE-CAPACITY-COLLAPSE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Спрос на уход превышает доказанную capacity&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;CELL_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;CARE_GAP&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Нельзя скрывать дефицит за принуждением caregiver&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;MED|MED-MH|GOV|COMM|SHEL&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;HEALTH_SERVICE|SOCIAL_SERVICE|ACCESSIBLE_SITE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Нельзя скрывать дефицит за принуждением caregiver&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:129 cells:31 -->
> [!abstract]- Запись 129 из 133 — GEN-INSTITUTION-DISSOLUTION — Прекращение или распад stewardship-института
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-INSTITUTION-DISSOLUTION&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Прекращение или распад stewardship-института&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;DISSOLUTION_TRIGGER&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Активы и records передаются по lawful rule&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;GOV|LEG|DOC|FIN|INFO&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;LEGAL_SERVICE|SUCCESSOR_INSTITUTION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Активы и records передаются по lawful rule&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:130 cells:31 -->
> [!abstract]- Запись 130 из 133 — GEN-ARCHIVE-CUSTODIAN-LOSS — Потеря хранителя ключей прав или каталога
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-ARCHIVE-CUSTODIAN-LOSS&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Потеря хранителя ключей прав или каталога&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;CUSTODIAN_LOSS&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не раскрывать secrets без законного succession&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|CYB|DOC|GOV&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;OFFSITE_COPY|EXTERNAL_CUSTODIAN&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не раскрывать secrets без законного succession&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:131 cells:31 -->
> [!abstract]- Запись 131 из 133 — GEN-TECHNOLOGY-UNREADABLE — Формат носитель или среда выполнения стали нечитаемыми
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-TECHNOLOGY-UNREADABLE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Формат носитель или среда выполнения стали нечитаемыми&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;READ_OR_FORMAT_FAILURE&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;PRESERVE_EVIDENCE_AND_RECOVER&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Original сохраняется; migration проверяется&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;INFO|CYB|TOOL|ENE&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;READER|MIGRATION|EMULATION&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Original сохраняется; migration проверяется&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:132 cells:31 -->
> [!abstract]- Запись 132 из 133 — GEN-SITE-UNINHABITABLE — Площадка стала длительно непригодной
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-SITE-UNINHABITABLE&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Площадка стала длительно непригодной&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;SITE_TO_REGIONAL&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;SAFETY_OR_LEGAL_THRESHOLD&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;SHELTER_OR_EVACUATE_PER_OFFICIAL_DIRECTION&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Жизнь и закон выше sunk cost&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;SHEL|REC|NAV|TRANS|LEG&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ALTERNATE_SITE|ROUTE|AUTHORITY&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Жизнь и закон выше sunk cost&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

<!-- record:133 cells:31 -->
> [!abstract]- Запись 133 из 133 — GEN-RELOCATION-DELAY — Опасная задержка заранее обоснованного переезда
> - **Сценарий ID** (<code>&quot;scenario_id&quot;</code>): <code>&quot;GEN-RELOCATION-DELAY&quot;</code>
> - **«family»** (<code>&quot;family&quot;</code>): <code>&quot;GEN&quot;</code>
> - **Название на русском** (<code>&quot;name_ru&quot;</code>): <code>&quot;Опасная задержка заранее обоснованного переезда&quot;</code>
> - **Область** (<code>&quot;scope&quot;</code>): <code>&quot;CELL_TO_INSTITUTION&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;RETREAT_TRIGGER_MET_BUT_NOT_EXECUTED&quot;</code>
> - **«first» решение класс** (<code>&quot;first_decision_class&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение «sequence»** (<code>&quot;decision_sequence&quot;</code>): <code>&quot;ASSESS_DEPENDENCIES&quot;</code>
> - **Решение условие примечания** (<code>&quot;decision_condition_notes&quot;</code>): <code>&quot;Не ждать необратимого отказа при выполненном trigger&quot;</code>
> - **Решение «sequence» статус** (<code>&quot;decision_sequence_status&quot;</code>): <code>&quot;INDEX_ONLY_NOT_REVIEWED&quot;</code>
> - **Возможность ID** (<code>&quot;capability_ids&quot;</code>): <code>&quot;REC|GOV|NAV|TRANS|DOC&quot;</code>
> - **«spatial» «need» «codes»** (<code>&quot;spatial_need_codes&quot;</code>): <code>&quot;ALTERNATE_SITE|LEGAL_SERVICE&quot;</code>
> - **Карта ID** (<code>&quot;map_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Маршрут ID** (<code>&quot;route_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Объект ID** (<code>&quot;site_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«modifier» «codes»** (<code>&quot;modifier_codes&quot;</code>): <code>&quot;&quot;</code>
> - **Размер группы** (<code>&quot;group_size_scope&quot;</code>): <code>&quot;N1_TO_N7&quot;</code>
> - **Горизонт область** (<code>&quot;horizon_scope&quot;</code>): <code>&quot;E5&quot;</code>
> - **Источник полномочие класс** (<code>&quot;source_authority_class&quot;</code>): <code>&quot;PRIMARY_LAW_AUTHORITY_STANDARDS_PROFESSIONAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«card» статус** (<code>&quot;card_status&quot;</code>): <code>&quot;INDEX_ONLY&quot;</code>
> - **Профессиональный проверка требуемый** (<code>&quot;professional_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **Профессиональный проверка состояние** (<code>&quot;professional_review_state&quot;</code>): <code>&quot;NOT_STARTED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не ждать необратимого отказа при выполненном trigger&quot;</code>
> - **Идентификаторы источников** (<code>&quot;source_ids&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Источник «section» ссылки** (<code>&quot;source_section_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Решение «provenance» состояние** (<code>&quot;decision_provenance_state&quot;</code>): <code>&quot;NOT_LINKED&quot;</code>
> - **Горизонт «vocabulary» версия** (<code>&quot;horizon_vocabulary_version&quot;</code>): <code>&quot;0.3&quot;</code>
> - **Горизонт «semantics»** (<code>&quot;horizon_semantics&quot;</code>): <code>&quot;TREND_OR_STATE&quot;</code>
> - **«e5» проверка состояние** (<code>&quot;e5_review_state&quot;</code>): <code>&quot;ARCHITECTURE_ONLY&quot;</code>
> - **«e5» «basis» ссылки** (<code>&quot;e5_basis_refs&quot;</code>): <code>&quot;16_CENTURY_CONTINUITY_RU.md|18_E5_REGISTERS_AND_GATES_RU.md&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
