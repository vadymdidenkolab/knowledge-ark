---
id: "DATA-REGISTER-107b9d765d300c59"
type: "generated-data-register-view"
title: "Связи прежних возможностей с каноническим деревом"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "capability-crosswalk.csv"
source_sha256: "2863dc4f1c16cfb5a6a0aa136e7dae2d8d8de8c224c97bbc60deb3f74e7c8d0f"
source_bytes: 7881
source_row_count: 33
source_column_count: 9
source_cell_count: 297
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: capability-crosswalk.csv -->

# Связи прежних возможностей с каноническим деревом

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 33
- **Полей в каждой записи:** 9
- **Ячеек данных, включая пустые:** 297
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `2863dc4f1c16cfb5a6a0aa136e7dae2d8d8de8c224c97bbc60deb3f74e7c8d0f`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «crosswalk» ID | <code>&quot;crosswalk_id&quot;</code> |
| 2 | Прежний возможность ID | <code>&quot;legacy_capability_id&quot;</code> |
| 3 | Канонический «technology» ID | <code>&quot;canonical_technology_ids&quot;</code> |
| 4 | «century» возможность ID | <code>&quot;century_capability_ids&quot;</code> |
| 5 | «moc» ID | <code>&quot;moc_ids&quot;</code> |
| 6 | «science» отрасль ID | <code>&quot;science_domain_ids&quot;</code> |
| 7 | «mapping» статус | <code>&quot;mapping_status&quot;</code> |
| 8 | Примечания | <code>&quot;notes&quot;</code> |
| 9 | Версия выпуска | <code>&quot;release_version&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:9 -->
> [!abstract]- Запись 1 из 33 — XW-AGR
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-AGR&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;AGR&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-FOOD|TD-FERTILIZERS&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-AGR-SOIL|CAP-AGR-SEED&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-FOOD-AGRI&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-AGRI-01|SCI-AGRI-05|SCI-AGRI-06&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:2 cells:9 -->
> [!abstract]- Запись 2 из 33 — XW-AIR
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-AIR&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;AIR&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-VENTILATION|TD-SHELTER-COMBUSTION-AIR&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-AIR&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SHELTER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-09&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:3 cells:9 -->
> [!abstract]- Запись 3 из 33 — XW-COM
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-COM&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;COM&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-MAPS-COMMS|TD-COMMS-PACE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-COMMS&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-MAPS-COMMS&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-OPS-04&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:4 cells:9 -->
> [!abstract]- Запись 4 из 33 — XW-COMM
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-COMM&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;COMM&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV-COMMUNITY&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-COMMUNITY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-GOVERNANCE&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-OPS-12&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:5 cells:9 -->
> [!abstract]- Запись 5 из 33 — XW-CYB
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-CYB&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;CYB&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-KNOWLEDGE-TOOLCHAINS|TD-KNOWLEDGE-HARDWARE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-SOFTWARE-READ&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-KNOWLEDGE-COMPUTING&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-COMP-12&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:6 cells:9 -->
> [!abstract]- Запись 6 из 33 — XW-DEAD
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-DEAD&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;DEAD&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-DEATH|TD-SAN-HUMAN-DEATH&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-DOC-IDENTITY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-16&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:7 cells:9 -->
> [!abstract]- Запись 7 из 33 — XW-DOC
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-DOC&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;DOC&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV-BIRTH-DEATH|TD-PEOPLE-CONSENT&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-DOC-IDENTITY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-GOVERNANCE&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-PORT-10&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:8 cells:9 -->
> [!abstract]- Запись 8 из 33 — XW-EDU
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-EDU&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;EDU&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-EDUCATION&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-EDUCATION|CAP-SKILL-SUCCESSION&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-KNOWLEDGE-COMPUTING&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-EDU-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:9 cells:9 -->
> [!abstract]- Запись 9 из 33 — XW-ENE
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-ENE&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;ENE&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-ENERGY&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-ENERGY-FUELS&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-ELEC-01|SCI-ELEC-10&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:10 cells:9 -->
> [!abstract]- Запись 10 из 33 — XW-FIN
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-FIN&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;FIN&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV-LEDGER|TD-GOV-TRADE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-FIN-LIFECYCLE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-GOVERNANCE&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-OPS-07&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:11 cells:9 -->
> [!abstract]- Запись 11 из 33 — XW-FIRE
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-FIRE&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;FIRE&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-FIRE-CO|TD-SHELTER-ALARMS|TD-SHELTER-EXTINGUISHER&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-FIRE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SHELTER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-12&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:12 cells:9 -->
> [!abstract]- Запись 12 из 33 — XW-FOOD
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-FOOD&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;FOOD&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-FOOD|TD-FOOD-P0-RESERVE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-FOOD-NUTRITION&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-FOOD-AGRI&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-AGRI-09|SCI-HEALTH-07&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:13 cells:9 -->
> [!abstract]- Запись 13 из 33 — XW-GOV
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-GOV&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;GOV&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-GOV-SUCCESSION|CAP-GOV-SAFEGUARD&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-GOVERNANCE&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-OPS-01|SCI-OPS-02&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:14 cells:9 -->
> [!abstract]- Запись 14 из 33 — XW-HOME
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-HOME&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;HOME&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-SHELTER|TD-CONSTRUCTION&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-SHELTER&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SHELTER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:15 cells:9 -->
> [!abstract]- Запись 15 из 33 — XW-INFO
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-INFO&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;INFO&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-KNOWLEDGE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-INFO-TRUST|CAP-ARCHIVE-RESTORE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-KNOWLEDGE-COMPUTING&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-ARCH-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:16 cells:9 -->
> [!abstract]- Запись 16 из 33 — XW-LEG
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-LEG&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;LEG&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV-LAW|TD-PORTUGAL-LAW&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-LAW-TENURE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-PORTUGAL&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-PORT-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:17 cells:9 -->
> [!abstract]- Запись 17 из 33 — XW-MED
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY|CAP-MED-PUBLIC-HEALTH&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:18 cells:9 -->
> [!abstract]- Запись 18 из 33 — XW-MED-BLS
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED-BLS&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED-BLS&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-BLS-AED|TD-HEALTH-AIRWAY&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-04&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:19 cells:9 -->
> [!abstract]- Запись 19 из 33 — XW-MED-ILL
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED-ILL&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED-ILL&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-PREVENTION|TD-HEALTH-DELAYED-CARE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-02|SCI-HEALTH-05&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:20 cells:9 -->
> [!abstract]- Запись 20 из 33 — XW-MED-MH
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED-MH&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED-MH&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-MENTAL-CRISIS&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-08&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:21 cells:9 -->
> [!abstract]- Запись 21 из 33 — XW-MED-NCD
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED-NCD&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED-NCD&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-MEDICATION-INVENTORY|TD-HEALTH-COLD-CHAIN&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-09&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:22 cells:9 -->
> [!abstract]- Запись 22 из 33 — XW-MED-TRAUMA
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-MED-TRAUMA&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;MED-TRAUMA&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-BLEED-SHOCK|TD-HEALTH-HEAD-SPINE|TD-HEALTH-FRACTURE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-HEALTH&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-04&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:23 cells:9 -->
> [!abstract]- Запись 23 из 33 — XW-NAV
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-NAV&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;NAV&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-NAVIGATION|TD-ROUTES&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-NAV&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-MAPS-COMMS&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-EARTH-11&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:24 cells:9 -->
> [!abstract]- Запись 24 из 33 — XW-PET
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-PET&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;PET&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-ANIMALS|TD-PEOPLE-ANIMALS&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-ANIMAL-CARE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-FOOD-AGRI&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-15|SCI-AGRI-13&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:25 cells:9 -->
> [!abstract]- Запись 25 из 33 — XW-PPE
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-PPE&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;PPE&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-HEALTH-SCENE-PPE|TD-WORKSHOP-PPE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-TOOLS&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SAFETY&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-HEALTH-05&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:26 cells:9 -->
> [!abstract]- Запись 26 из 33 — XW-PRES
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-PRES&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;PRES&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-FOOD-PRESERVATION|TD-HARVEST-STORAGE&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-FOOD-NUTRITION&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-FOOD-AGRI&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-AGRI-09&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:27 cells:9 -->
> [!abstract]- Запись 27 из 33 — XW-REC
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-REC&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;REC&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-GOV-RECOVERY|TD-GOV-RELOCATION&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-RECOVERY|CAP-RELOCATION&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-GOVERNANCE&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-OPS-10&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:28 cells:9 -->
> [!abstract]- Запись 28 из 33 — XW-SAFE
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-SAFE&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;SAFE&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-BASE-SAFETY|TD-SECURITY&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-GOV-SAFEGUARD&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SAFETY&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-METH-14&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:29 cells:9 -->
> [!abstract]- Запись 29 из 33 — XW-SAN
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-SAN&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;SAN&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-SANITATION&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-SANITATION&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-WATER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-07&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:30 cells:9 -->
> [!abstract]- Запись 30 из 33 — XW-SHEL
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-SHEL&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;SHEL&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-SHELTER&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-SHELTER&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-SHELTER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:31 cells:9 -->
> [!abstract]- Запись 31 из 33 — XW-TOOL
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-TOOL&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;TOOL&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-WORKSHOP|TD-BASE-METROLOGY&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-TOOLS|CAP-REPAIR&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-WORKSHOP&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-MECH-01&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:32 cells:9 -->
> [!abstract]- Запись 32 из 33 — XW-TRANS
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-TRANS&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;TRANS&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-TRANSPORT&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-TRANSPORT&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-MAPS-COMMS&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-MECH-12&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

<!-- record:33 cells:9 -->
> [!abstract]- Запись 33 из 33 — XW-WAT
> - **«crosswalk» ID** (<code>&quot;crosswalk_id&quot;</code>): <code>&quot;XW-WAT&quot;</code>
> - **Прежний возможность ID** (<code>&quot;legacy_capability_id&quot;</code>): <code>&quot;WAT&quot;</code>
> - **Канонический «technology» ID** (<code>&quot;canonical_technology_ids&quot;</code>): <code>&quot;TD-WATER&quot;</code>
> - **«century» возможность ID** (<code>&quot;century_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE&quot;</code>
> - **«moc» ID** (<code>&quot;moc_ids&quot;</code>): <code>&quot;MOC-WATER&quot;</code>
> - **«science» отрасль ID** (<code>&quot;science_domain_ids&quot;</code>): <code>&quot;SCI-CIVIL-07|SCI-AGRI-03&quot;</code>
> - **«mapping» статус** (<code>&quot;mapping_status&quot;</code>): <code>&quot;PROVISIONAL_HUMAN_REVIEW_REQUIRED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Links scenario vocabulary to canonical capability layers; does not prove execution&quot;</code>
> - **Версия выпуска** (<code>&quot;release_version&quot;</code>): <code>&quot;0.5-draft&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
