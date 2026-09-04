---
id: MOC-KNOWLEDGE-COMPUTING
type: moc
title: "KNOWLEDGE_COMPUTING — офлайн-знания и вычислительная среда"
aliases: [Знания и вычисления, Knowledge Computing MOC]
status: ARCHITECTURE
maturity: CATALOG_SKELETON
risk_class: S2
domain: KNOWLEDGE_COMPUTING
jurisdiction: GLOBAL
release_gate: DENY
global_generated_catalog_notes: 2075
manual_released_notes: 0
version: "0.1.0"
created: "2026-09-04"
updated: "2026-09-04"
tags: [moc, knowledge, offline, computing, archive]
---

# KNOWLEDGE_COMPUTING — офлайн-знания и вычислительная среда

Домой: [[00 — НАЧАТЬ]]. Карты и связь: [[MOCs/MOC_MAPS_COMMS|MAPS_COMMS]]. Энергия: [[MOCs/MOC_ENERGY_FUELS|ENERGY_FUELS]]. Управление: [[MOCs/MOC_GOVERNANCE|GOVERNANCE]].

## Цель карты

Каталогизировать получение, правовую проверку, локальное хранение, поиск, чтение, проверку целостности, резервирование, печать, обучение и восстановление знаний. URL, метаданные или название источника не являются офлайн-корпусом.

## Каталог capability

| Ключ | Объект | Типы заметок | Риск | Evidence |
|---|---|---|---|---|
| KNOW-SCOPE | перечень доменов, языков и критических вопросов | capability, evidence | S0–S1 | gap review с владельцем и датой |
| KNOW-SOURCE | авторитетность, версия, права и ограничения | source, evidence | S0–S2 | item-level review, а не доменное предположение |
| KNOW-ACQUIRE | законное получение и карантин файла | process, source, hazard | S1–S2 | provenance, malware scan, checksum |
| KNOW-CATALOG | id, metadata, связи, статус и supersession | process, evidence | S1 | валидатор схемы и отчёт конфликтов |
| KNOW-FORMAT | PDF/EPUB/ZIM/HTML/CSV/CAD/GIS/media и миграция | material, tool, source | S1–S2 | тест открытия, спецификация формата, export fallback |
| KNOW-READER | приложения, portable runtime и инструкции запуска | tool, process, evidence | S1–S2 | запуск без сети на двух устройствах |
| KNOW-SEARCH | индекс, MOC, теги и полнотекстовый поиск | capability, tool, evidence | S1 | контрольные запросы и ручной индекс |
| KNOW-INTEGRITY | SHA-256, manifest, подписи и аудит изменений | process, tool, evidence | S1–S2 | повторный hash и независимая копия manifest |
| KNOW-BACKUP | 3-2-1, офсайт, write-protect и ротация | capability, material, process | S1–S2 | восстановление, а не только успешное копирование |
| KNOW-COMPUTE | ноутбуки, одноплатные ПК, storage, периферия | tool, material, evidence | S1–S3 | фактический инвентарь, power budget, cold boot |
| KNOW-PRINT | бумажный critical subset, расходники и переплёт | capability, tool, material | S1–S2 | читаемая печать, индекс, влагозащита |
| KNOW-RECOVER | восстановление ОС, приложения, ключей и данных | process, tool, evidence | S2–S3 | bare-device drill и известная чистая копия |
| KNOW-CYBER | вредоносные файлы, доступ, секреты и приватность | hazard, process, evidence | S2–S3 | threat model, offline backup, журнал доступа |
| KNOW-TEACH | учебные маршруты, teach-back и преемственность | capability, process, evidence | S1–S2 | второй человек выполняет контрольную задачу |

## Уровни сохранения

| Уровень | Минимум |
|---|---|
| SOURCE_IDENTIFIED | официальный URL, издатель, версия и scope review |
| LOCAL_PAYLOAD | файл, права, SHA-256, размер, локальный путь |
| OFFLINE_OPENED | открытие при отключённой сети на указанном reader |
| SEARCHABLE | индекс и контрольные запросы |
| RECOVERABLE | успешное восстановление из отдельной копии |
| TEACHABLE | второй человек находит и применяет безопасный материал |

Эти уровни не заменяют статусы EXECUTABLE, TESTED и RELEASED для физического процесса.

## Долговечность

Ни один носитель не считать «на 100 лет». Нужны миграция форматов, регулярный scrubbing, несколько технологий хранения, печатное ядро, запас readers/кабелей/питания, открытые форматы и план восстановления ключей. Дата следующей проверки обязательна.

## Связанные карты

[[MOCs/MOC_WORKSHOP|WORKSHOP]] · [[MOCs/MOC_PORTUGAL|PORTUGAL]] · [[MOCs/MOC_SAFETY|SAFETY]]
