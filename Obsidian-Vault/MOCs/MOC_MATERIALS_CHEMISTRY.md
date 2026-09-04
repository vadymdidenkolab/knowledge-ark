---
id: MOC-MATERIALS-CHEMISTRY
type: moc
title: "MATERIALS_CHEMISTRY — материалы, совместимость и химические границы"
aliases: [Материалы и химия, Materials Chemistry MOC]
status: ARCHITECTURE
maturity: CATALOG_SKELETON
risk_class: S4
domain: MATERIALS_CHEMISTRY
jurisdiction: GLOBAL
release_gate: DENY
global_generated_catalog_notes: 2075
manual_released_notes: 0
version: "0.1.0"
created: "2026-09-04"
updated: "2026-09-04"
tags: [moc, materials, chemistry, compatibility]
---

# MATERIALS_CHEMISTRY — материалы, совместимость и химические границы

Домой: [[00 — НАЧАТЬ]]. Мастерская: [[MOCs/MOC_WORKSHOP|WORKSHOP]]. Безопасность: [[MOCs/MOC_SAFETY|SAFETY]].

## Цель карты

Каталогизировать идентичность материала, свойства, совместимость, старение, допустимые замены, хранение и отходы. Химические вещества учитываются по точному продукту, концентрации/марке, партии и SDS. Эта MOC не содержит синтезов, реакционных рецептур или инструкций получения опасных веществ.

## Каталог материалов

| Ключ | Семейство | Типы заметок | Риск | Обязательные поля |
|---|---|---|---|---|
| MAT-WOOD | древесина, фанера, плиты, защита | material, source, hazard | S1–S3 | вид/grade, влажность, клей, нагрузка, огонь/биология |
| MAT-METAL | стали, нержавеющие, алюминий, медь и сплавы | material, source, evidence | S2–S4 | grade, состояние, коррозия, соединение, контактные пары |
| MAT-POLYMER | трубы, листы, уплотнения, ёмкости | material, source, hazard | S1–S3 | polymer code, температура, UV, пищевой/водный контакт |
| MAT-GLASS-CERAMIC | стекло, керамика, огнеупоры | material, hazard, process | S1–S4 | термошок, сколы, нагрузка, температурный rating |
| MAT-TEXTILE | волокна, ткани, нити, мембраны | material, source, evidence | S1–S3 | состав, UV/влага, прочность, горючесть |
| MAT-MASONRY | камень, кирпич, растворы и бетон | material, source, hazard | S2–S4 | состав, cure/age, конструктивная роль, пыль |
| MAT-FOOD-CONTACT | тара, прокладки и покрытия для пищи/воды | material, source, evidence | S2–S3 | явная пригодность, температура, миграция, очистка |
| MAT-ADHESIVE-SEALANT | клеи, герметики, ленты | material, source, hazard | S2–S4 | точный продукт, substrate, cure, вентиляция, срок |
| MAT-COATING | краски, масла и защитные покрытия | material, source, hazard | S2–S4 | состав, surface prep из manual, VOC/fire, контактные ограничения |
| MAT-CLEANER | мыло, detergent, дезсредства и растворители | material, source, hazard | S2–S4 | точный label/SDS, совместимость, запрет смешивания, отходы |
| MAT-LUBRICANT | масла, смазки, гидравлические жидкости | material, source, hazard | S2–S3 | specification, оборудование, пищевой контакт, загрязнение |
| MAT-UNKNOWN | найденные, вторичные и неидентифицированные материалы | hazard, evidence | S4 | карантин, происхождение, анализ; использование DENY |

## Совместимость как отдельный граф

Для каждой пары material ↔ environment и material ↔ material фиксировать: температура, время, нагрузка, вода/пища, UV, кислород, солёность, pH, растворители, гальваническая пара, биологический рост, пожар, данные источника и обязательный тест. Совместимость в одном режиме не переносится на другой.

## Классификация химических ветвей

| Ветвь | Класс | Что разрешено в каркасе | Что не включать |
|---|---|---|---|
| готовое бытовое средство с оригинальной этикеткой | S2–S3 | identity, SDS, storage, compatibility, PPE, disposal | изменение состава и смешивание |
| концентраты, сильные кислоты/щёлочи, окислители, токсичные растворители | S4 | source/hazard inventory, segregation, emergency reference | разведение, reaction quantities, synthesis или substitute recipes |
| топливная химия, газообразование и пиролиз | S4 | только связь с [[MOCs/MOC_ENERGY_FUELS|ENERGY_FUELS]] и hazards | условия реакции, аппарат, выходы и рабочие параметры |
| агрохимия и удобрения | S3–S4 | связь с [[MOCs/MOC_FOOD_AGRI|FOOD_AGRI]], продукт/label/SDS | домашнее получение, неизвестные смеси и универсальные дозы |
| медицинская/фармацевтическая химия | S4 | официальный продукт, условия, правовой статус | синтез, экстракция или изменение лекарства |
| неизвестный образец | S4 | quarantine, non-contact identification plan | нагрев, запах, вкус, реакционный тест без метода |

## Правила замен

Похожий внешний вид не является эквивалентностью. Замена требует известного состава/grade, критических свойств, совместимости, размерного интерфейса, допустимого режима, источника и приёмочного теста. Если исходная деталь выполняет несущую, пожарную, питьевую, газовую, электрическую, медицинскую или pressure-функцию, замена остаётся S3/S4 и DENY до профессионального допуска.

## Связанные карты

[[MOCs/MOC_WATER|WATER]] · [[MOCs/MOC_SHELTER|SHELTER]] · [[MOCs/MOC_HEALTH|HEALTH]] · [[MOCs/MOC_PORTUGAL|PORTUGAL]]
