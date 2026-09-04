---
id: MOC-SAFETY
type: moc
title: "SAFETY — риски, допуски и остановка работ"
aliases: [Безопасность, Safety MOC]
status: ARCHITECTURE
maturity: CATALOG_SKELETON
risk_class: S4
domain: SAFETY
jurisdiction: GLOBAL
release_gate: DENY
global_generated_catalog_notes: 2075
manual_released_notes: 0
version: "0.1.0"
created: "2026-09-04"
updated: "2026-09-04"
tags: [moc, safety, hazard, stop-work]
---

# SAFETY — риски, допуски и остановка работ

Домой: [[00 — НАЧАТЬ]]. Управление: [[MOCs/MOC_GOVERNANCE|GOVERNANCE]]. Здоровье: [[MOCs/MOC_HEALTH|HEALTH]].

## Цель карты

Создать единый слой hazard → prevention → detection → stop-work → safe state → escalation → evidence. Безопасность — не предупреждение в конце инструкции, а условие её существования. Любой человек может остановить работу при неизвестном риске или отклонении; снять блокировку может только явно назначенная и компетентная роль.

## Классы риска

| Класс | Характер работы | Допустимый статус без физического evidence |
|---|---|---|
| S0 | справка, каталог, навигация | ARCHITECTURE/CANDIDATE |
| S1 | низкорисковая обратимая задача | максимум EXECUTABLE после полного письменного gate; применение всё равно требует осмотра |
| S2 | бытовая задача с измерениями, PPE и остаточным риском | DENY до task-specific hazards, обучения и приёмки |
| S3 | профессиональная, промышленная, лицензируемая или значимая для жизни система | только каталог/источник до подтверждённой роли, площадки и разрешения |
| S4 | риск тяжёлой травмы, токсичности, пожара/взрыва, высокого напряжения/давления, биологического распространения или серьёзного правового вреда | только source/hazard catalog; NO_FABRICATION_DATA и DENY |

## Каталог control-системы

| Ключ | Объект | Типы заметок | Gate evidence |
|---|---|---|---|
| SAFE-HAZARD-REGISTER | полный перечень hazards и владельцев | hazard, evidence | review по каждому домену и дата |
| SAFE-RISK-ASSESS | контекст, тяжесть, вероятность, обнаружимость | process, hazard, source | метод, assessor, неопределённость |
| SAFE-STOP-WORK | триггер, команда, безопасное состояние, restart | process, evidence | tabletop и реальное учение без опасного воздействия |
| SAFE-COMPETENCE | роли, обучение, ограничения и срок допуска | capability, evidence | наблюдаемая демонстрация и expiry |
| SAFE-PPE | выбор, совместимость, fit, хранение и замена | material, tool, source | exact hazard и производитель; PPE не единственный control |
| SAFE-ENERGY-ISOLATION | механическая, электрическая, pressure, thermal isolation | process, hazard, evidence | asset-specific LOTO и qualified review |
| SAFE-FIRE | prevention, detection, escape и response | capability, tool, evidence | подходящий detector/extinguisher, inspection, drill |
| SAFE-CHEMICAL | label, SDS, segregation, spill и отходы | material, hazard, source | точный продукт, совместимость и местный маршрут отходов |
| SAFE-BIOLOGICAL | неизвестные образцы, плесень, отходы и санитарные barriers | hazard, process, source | no-culture rule, containment, health escalation |
| SAFE-MACHINE | guards, entanglement, projectiles, stored energy | tool, hazard, evidence | manual, guard inspection, emergency stop test |
| SAFE-STRUCTURE | падение, обрушение, высота и excavation | hazard, source, process | professional plan и permits |
| SAFE-MEDICAL | красные флаги, первая помощь, handoff | capability, process, source | current protocol и trained responder |
| SAFE-FOOD-WATER | contamination, process controls и recall | hazard, instrument, evidence | traceability, measurements, isolation rule |
| SAFE-INCIDENT | помощь, сохранение evidence, review и corrective action | process, evidence | журнал, root cause without blame, verified closure |
| SAFE-DRILL | сценарий, наблюдатель, stop rule и lessons | process, evidence | safe simulation, no intentional exposure |

## Абсолютные блокировки текущего каркаса

Без отдельного профессионального пакета и допуска не создавать или выполнять инструкции для: сети 230 V и выше; газа и дымоходов; сосудов под давлением; взрывчатых/пиротехнических веществ; токсичных газов; сильных реактивов и опасных синтезов; производства топлива; литиевых battery packs; несущих конструкций; горячих работ; неизвестных биологических культур; медицинской хирургии/анестезии; обхода защит и охранных систем.

## Универсальный stop-work

Работа останавливается, если неизвестны материал/вещество; отсутствует требуемая роль; источник или ревизия не совпадает; сломана защита; прибор вне допуска; условия вышли за разрешённый диапазон; появился неожиданный запах, нагрев, дым, газ, давление, биологический рост, течь, деформация или симптом; нет безопасного пути отхода; отсутствует связь/наблюдатель, когда он обязателен; результат измерения неоднозначен.

## Возврат к работе

Не автоматически. Нужны изоляция, запись события, установление причины, восстановленный control, послеремонтная проверка, independent reviewer и явное решение ответственной роли. Отсутствие происшествия в прошлый раз не является доказательством безопасности.

## Связанные карты

[[MOCs/MOC_MATERIALS_CHEMISTRY|MATERIALS_CHEMISTRY]] · [[MOCs/MOC_ENERGY_FUELS|ENERGY_FUELS]] · [[MOCs/MOC_WORKSHOP|WORKSHOP]] · [[MOCs/MOC_PORTUGAL|PORTUGAL]]
