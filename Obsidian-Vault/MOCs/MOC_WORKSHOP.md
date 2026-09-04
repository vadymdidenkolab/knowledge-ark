---
id: MOC-WORKSHOP
type: moc
title: "WORKSHOP — мастерская, измерения и ремонт"
aliases: [Мастерская, Workshop MOC]
status: ARCHITECTURE
maturity: CATALOG_SKELETON
risk_class: S3
domain: WORKSHOP
jurisdiction: GLOBAL
release_gate: DENY
global_generated_catalog_notes: 2075
manual_released_notes: 0
version: "0.1.0"
created: "2026-09-04"
updated: "2026-09-04"
tags: [moc, workshop, tools, repair, metrology]
---

# WORKSHOP — мастерская, измерения и ремонт

Домой: [[00 — НАЧАТЬ]]. Материалы: [[MOCs/MOC_MATERIALS_CHEMISTRY|MATERIALS_CHEMISTRY]]. Энергия: [[MOCs/MOC_ENERGY_FUELS|ENERGY_FUELS]]. Безопасность: [[MOCs/MOC_SAFETY|SAFETY]].

## Цель карты

Каталогизировать способность измерять, размечать, удерживать, резать, сверлить, соединять, обслуживать, диагностировать и проверять ремонт. Инструмент в списке не означает, что он физически имеется, исправен, подходит к задаче или безопасен.

## Каталог capability

| Ключ | Объект | Типы заметок | Риск | Минимальное evidence |
|---|---|---|---|---|
| WORK-SPACE | верстак, освещение, вентиляция, хранение и эвакуация | capability, hazard, evidence | S1–S3 | фото, план, инспекция, свободный выход |
| WORK-MEASURE | длина, угол, масса, объём, время, температура | instrument, process, evidence | S1–S2 | диапазон, resolution, reference, журнал проверки |
| WORK-MARK | разметка, шаблоны, кондукторы и контроль баз | tool, process | S1–S2 | проверка геометрии и пробная деталь |
| WORK-HOLD | тиски, струбцины, опоры и фиксация | tool, hazard | S1–S3 | допустимая нагрузка, осмотр и устойчивость |
| WORK-CUT | ручная и механическая резка | tool, process, hazard | S1–S4 | материал/оснастка, guard/PPE, stop-условия |
| WORK-DRILL | ручное и механизированное сверление | tool, process, hazard | S2–S4 | фиксация, оснастка, обороты из manual, контроль результата |
| WORK-SHAPE | опиливание, строгание, абразивная обработка | tool, material, hazard | S1–S3 | совместимость, пыль/осколки, измерение |
| WORK-JOIN | крепёж, резьбы, швы, клеевые и иные соединения | material, tool, process | S1–S4 | спецификация соединения и разрушающий/нагрузочный тест |
| WORK-WOOD | низкорисковая деревообработка и ремонт | material, tool, process | S1–S3 | влажность, направление волокон, пробный узел |
| WORK-METAL | холодная обработка и профессиональные горячие работы | material, tool, hazard | S2–S4 | material ID; горячие работы только gated |
| WORK-TEXTILE | шитьё, ремонт одежды, сетей и мягкого снаряжения | material, tool, process | S1–S2 | пробный шов и нагрузочный критерий |
| WORK-MECHANICAL | подшипники, приводы, насосы, клапаны и велосипеды | tool, process, source | S2–S4 | manual модели, изоляция энергии, послеремонтный тест |
| WORK-ELECTRICAL | низковольтная диагностика и закрытые сетевые ветви | instrument, tool, hazard | S2–S4 | схема, current limit, CAT rating; 230 V только специалист |
| WORK-SPARES | детали, расходники, совместимость и каннибализация | material, tool, evidence | S1–S3 | точный интерфейс, партия, условия, тест замены |
| WORK-DRAWING | размерные схемы, BOM, допуски и ревизии | source, capability, evidence | S1–S3 | редактируемый исходник, печатный вид, independent check |
| WORK-REPAIR | диагностика → изоляция → разборка → замена → приёмка | process, hazard, evidence | S2–S4 | asset-specific manual и доказательство теста |

## Самодельные низкорисковые приспособления

Будущие карточки могут каталогизировать отвес, водяной уровень, угольник с reversal check, мерную ёмкость, сетку масштаба для фото, дождемер, сортировочные лотки, шаблоны разметки и другие S1/S2-объекты. Для каждого нужны чертёж, BOM, материал, размеры, допустимая замена, измерительная проверка, uncertainty, нагрузочный тест, ремонт и stop-условия. Название идеи не равно производственному пакету.

## S3/S4 без fabrication data

Сварка, пайка опасных систем, горячие работы, сосуды под давлением, подъём грузов, станки, сеть 230 V, газ, холодильный контур, литиевые батареи, несущие конструкции и неизвестные материалы каталогизируются только как assets/sources/hazards до появления квалификации, площадки, разрешения и task-specific package.

## Связанные карты

[[MOCs/MOC_SHELTER|SHELTER]] · [[MOCs/MOC_WATER|WATER]] · [[MOCs/MOC_KNOWLEDGE_COMPUTING|KNOWLEDGE_COMPUTING]] · [[MOCs/MOC_GOVERNANCE|GOVERNANCE]]
