---
id: MOC-PORTUGAL
type: moc
title: "PORTUGAL — локализация для Португалии"
aliases: [Португалия, Portugal MOC]
status: ARCHITECTURE
maturity: CATALOG_SKELETON
risk_class: S3
domain: PORTUGAL
jurisdiction: PT
release_gate: DENY
global_generated_catalog_notes: 2075
manual_released_notes: 0
version: "0.1.0"
created: "2026-09-04"
updated: "2026-09-04"
tags: [moc, portugal, localization, legal]
---

# PORTUGAL — локализация для Португалии

Домой: [[00 — НАЧАТЬ]]. Карты: [[MOCs/MOC_MAPS_COMMS|MAPS_COMMS]]. Управление: [[MOCs/MOC_GOVERNANCE|GOVERNANCE]]. Безопасность: [[MOCs/MOC_SAFETY|SAFETY]].

## Цель карты

Отделить общие знания от данных, которые зависят от законодательства, климата, муниципалитета, конкретного участка, служб и языка Португалии. Эта MOC не содержит домашний адрес или иные личные данные. Любая правовая, медицинская, пожарная, радио- или разрешительная информация должна иметь официальный источник и дату проверки.

## Каталог локализации

| Ключ | Объект | Типы заметок | Риск | Требуемый официальный слой |
|---|---|---|---|---|
| PT-EMERGENCY | экстренные службы, предупреждения и муниципальная защита | source, process, evidence | S2–S3 | национальный и муниципальный authority, offline card |
| PT-HEALTH | SNS, аптеки, токсикология, непрерывность рецептов | source, capability | S3 | действующие официальные контакты и eligibility |
| PT-FIRE | rural fire danger, burning restrictions, evacuation | source, hazard, evidence | S3–S4 | ICNF/ANEPC/municipality, дата и сезон |
| PT-WATER | поставщик, колодец/скважина, drought, качество и разрешения | source, capability, hazard | S2–S4 | APA, municipality, water utility, lab network |
| PT-CLIMATE | жара, засуха, шторм, берег, наводнение и микроклимат | source, evidence, hazard | S2–S3 | IPMA и официальные hazard maps |
| PT-AGRI | календарь, почвы, разрешённые семена/средства, болезни | source, capability, material | S2–S4 | DGAV, INIAV, municipality и официальный label |
| PT-LAND | кадастр, право прохода, zoning, protected areas | source, evidence, hazard | S3–S4 | DGT, municipality, land registry, ICNF |
| PT-BUILD | строительство, ремонт, вода, sanitation, fire code | source, process, hazard | S3–S4 | municipality и действующие национальные нормы |
| PT-ENERGY | сеть, генерация, топливо, хранение и лицензии | source, hazard, capability | S3–S4 | DGEG, ERSE, municipality, supplier manuals |
| PT-RADIO | spectrum, licensing, callsigns и emergency rules | source, process, hazard | S3–S4 | ANACOM с датой проверки |
| PT-FOOD | пищевая безопасность, slaughter, preservation, trade | source, process, hazard | S3–S4 | ASAE/DGAV и применимые нормы |
| PT-WASTE | бытовые, опасные, медицинские и строительные отходы | source, process, hazard | S2–S4 | municipality/APA и authorised operator |
| PT-TRANSPORT | дороги, техосмотр, топливо, велосипеды, эвакуация | source, tool, evidence | S2–S3 | IMT, municipality, road authority |
| PT-COMMS | public broadcast, cell, internet, postal and local contacts | source, tool, evidence | S1–S3 | authority/provider, coverage test, update date |
| PT-LANGUAGE | португальские термины, формы и bilingual cards | capability, source, evidence | S1 | checked translation and field drill |

## Географические уровни

Каждая PT-заметка должна указывать уровень: EU → Portugal → distrito/região → município → freguesia → конкретный объект. Норму более высокого уровня нельзя считать единственной, если местное правило строже. Адрес, координаты запасов, health data и контакты людей хранятся в отдельном защищённом контуре, а не в общем vault.

## Временная нестабильность

Обязательные поля: checked_on, valid_from, valid_until_if_known, issuing_authority, official_url, local_payload, next_review, supersedes, jurisdiction_level. Источник без даты проверки остаётся SOURCE_IDENTIFIED максимум; он не разрешает действие.

## Общая и локальная заметка

Общий принцип хранится в тематической MOC. PT-заметка содержит только местные параметры, authority, карты, правовые ограничения, контакты и доказательства участка, с обратной ссылкой на общую карточку. Это предотвращает смешение универсального знания с изменчивым местным правилом.

## Связанные карты

[[MOCs/MOC_WATER|WATER]] · [[MOCs/MOC_FOOD_AGRI|FOOD_AGRI]] · [[MOCs/MOC_HEALTH|HEALTH]] · [[MOCs/MOC_ENERGY_FUELS|ENERGY_FUELS]] · [[MOCs/MOC_SHELTER|SHELTER]]
