# Автономный комплект жизни и знаний

**Состояние live worktree:** `v0.5-draft` — изменяемая рабочая сборка, не выпуск  
**Последний замороженный выпуск:** `v0.4` — проверяется только по его исходному ZIP и sidecar-файлам  
**Дата основания:** 2026-08-29  
**Базовая локализация:** Португалия / Европейский союз  
**Основной язык:** русский; критические карточки впоследствии дублируются на португальском и английском

## Что это

Это проект единой системы готовности для 1–7 человек — от физической аптечки и карт до автономной офлайн-библиотеки, операционного управления и долгого восстановления. Система рассчитана не на один «конец света», а на широкий набор реальных нарушений нормальной жизни:

- внезапная болезнь или травма;
- пожар, угарный газ, утечка газа;
- землетрясение, цунами, наводнение, шторм, жара, холод, природный пожар и дым;
- отключение электричества, воды, связи, интернета или банковских сервисов;
- загрязнение воды и перебои с продуктами или лекарствами;
- эпидемия, эвакуация, потеря жилья или документов;
- химическая или радиологическая авария;
- длительный экономический, политический или инфраструктурный кризис;
- потеря цифровых данных, доступа к учётным записям и достоверной информации.

Проект не предполагает, что пятнадцать или сто лет можно прожить только на заранее купленных банках, батарейках и таблетках. На длинном горизонте запасы должны переходить в **способность получать безопасную воду, производить и сохранять пищу, поддерживать здоровье, ремонтировать и заменять системы, получать энергию, обмениваться, обучаться, передавать права и знания**. После 15 лет субъектом становится не только текущая группа, но и площадка с её активами и stewardship-институт, способный пережить смену первоначальных участников.

## Как открыть впервые

1. Открыть автономный вход [START_HERE.html](START_HERE.html) или текстовый fallback [START_HERE.txt](START_HERE.txt).
2. Прочитать [мастер-статус](24_MASTER_CATALOG_STATUS_RU.md), текущий [аудит полной изоляции](22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md) и [дерево технологических зависимостей](23_TECHNOLOGY_DEPENDENCY_TREE_RU.md). Они отделяют каталог функций от готовых процедур, вещей и навыков.
3. Открыть [главную страницу Obsidian Vault](Obsidian-Vault/00%20%E2%80%94%20%D0%9D%D0%90%D0%A7%D0%90%D0%A2%D0%AC.md) для выбора понятного маршрута по ситуации.
4. Проверить именно изменяемое дерево командой `python3 validate_worktree.py`. Успешная проверка доказывает структуру и целостность учтённых payload, но не готовность к автономной жизни.
5. Заполнить минимум из [02_PERSONALIZATION_RU.md](02_PERSONALIZATION_RU.md), не публикуя чувствительные координаты и диагнозы, и провести физическую инвентаризацию по [inventory-template.csv](inventory-template.csv).
6. После указания муниципалитета собрать map pack по [13_MAPS_GEODATA_NAVIGATION_RU.md](13_MAPS_GEODATA_NAVIGATION_RU.md), назначить структуру `1–7` по [14_GROUP_1_TO_7_OPERATIONS_RU.md](14_GROUP_1_TO_7_OPERATIONS_RU.md) и выбрать применимые сценарии из [15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md](15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md).
7. Для практической науки начать с [20_PRACTICAL_SCIENCE_PRESERVATION_RU.md](20_PRACTICAL_SCIENCE_PRESERVATION_RU.md) и вкладки `Safety Gates` в [practical-science-preservation-atlas.xlsx](practical-science-preservation-atlas.xlsx); не запускать проекты до source/rights/safety review.

## Как проверить live worktree v0.5-draft

Из текущего каталога выполнить:

```text
python3 validate_worktree.py
```

Это рабочая проверка изменяемого дерева. Она не превращает каталожную запись в инструкцию, не подтверждает наличие физического имущества, адресных карт, практического навыка или клинического допуска. Текущие количественные итоги графа следует брать из вывода валидатора и самих CSV-реестров, а не из числа, переписанного в обзорный текст.

## Как проверить замороженный официальный архив v0.4

Эти команды относятся только к неизменённому архиву `v0.4`, а не к live worktree `v0.5-draft`. После распаковки рядом должны находиться каталог `autonomous-life-kit` и файл `autonomous-life-kit-v0.4.seed-lock.csv`. Сначала из каталога, где лежат ZIP и sidecar, проверить сам ZIP командой `shasum -a 256 -c autonomous-life-kit-v0.4.sha256`. Затем перейти в распакованный каталог `autonomous-life-kit` и выполнить:

```text
python3 offline_library.py verify . ../autonomous-life-kit-v0.4.seed-lock.csv
python3 validate_release.py
```

Первый шаг сверяет точные байты 84 файлов с опубликованным снимком, второй — структурные и семантические инварианты. Для изменяемой собственной библиотеки следует создать отдельный lock с другим именем; нельзя заново создать release lock и выдать самосогласованный новый снимок за проверку официального выпуска.

## Модель системы

Каждая тема строится как один законченный модуль:

1. **Риск:** что может произойти и как это распознать.
2. **Физический комплект:** что иметь, где хранить и сколько нужно.
3. **Карточка первых действий:** что делать в первые секунды и минуты.
4. **Полевое руководство:** что делать в течение часов и дней.
5. **Глубокий справочник:** теория, варианты, ограничения и восстановление.
6. **Навык:** что требуется отработать заранее с инструктором или самостоятельно.
7. **Карта и маршрут:** какой слой нужен, какие точки/пути допустимы и что ещё не проверено в поле.
8. **Группа:** кто отвечает, кто замещает, как ведётся учёт и как функция масштабируется от 1 до 7.
9. **Контроль:** срок годности, test evidence, ротация, журнал и дата пересмотра источников.

Для каждого предмета фиксируются: назначение, количество или формула расчёта, комплект размещения, условия хранения, срок проверки, необходимые навыки, запреты, допустимые замены, юридические ограничения и источник требования.

## Шесть эшелонов

| Эшелон | Горизонт | Назначение | Типичный носитель |
|---|---:|---|---|
| E0 | минуты–12 часов | То, что всегда при человеке | карманы / EDC |
| E1 | свыше 12–72 часов | Быстрый выход или ожидание первичной помощи | эвакуационный рюкзак |
| E2 | свыше 72 часов–14 дней | Автономность дома при нарушении снабжения | домашние модули |
| E3 | свыше 14–90 дней | Продолжительный сбой и ограниченное пополнение | ротационный резерв и оборудование |
| E4 | свыше 90 дней–менее 15 лет | Воспроизводство, ремонт, обучение и кооперация | мастерская, участок, библиотека, сеть людей |
| E5 | 15–100 лет | Межпоколенческая и институциональная непрерывность | люди, площадки, право, архив, succession и внешняя сеть |

Машинные границы, включительность и запрет ложных утверждений заданы в [horizon-register.csv](horizon-register.csv). `E5` не означает срок годности предмета, лекарства, карты, лицензии или человека. Для аудита он делится на `E5A 15–30`, `E5B 30–60` и `E5C 60–100 лет`, но scenario-card использует единый код `E5`.

Минимум 72 часа соответствует направлению стратегии готовности ЕС. Это guidance об автономности домохозяйства/населения в целом, а не обязательная единая норма ЕС и не готовая спецификация массы или состава переносимого E1-рюкзака. Для воды рабочий стартовый ориентир — около 3,8 л на человека в сутки для питья, приготовления пищи, чистки зубов и части гигиены; CDC рекомендует минимум на 3 дня и, если возможно, запас на 2 недели. Это только исходная величина: жаркий климат, болезнь, беременность, физическая нагрузка и животные увеличивают потребность.

## Критические границы безопасности

- В Португалии **112** — единый национальный номер экстренных служб. Во всех странах ЕС 112 доступен бесплатно, но в некоторых странах работает наряду с национальными экстренными номерами.
- Медицинский раздел разделяет самопомощь, сертифицированную первую помощь, профессиональные роли и системные площадки. Код M0–M4 — только слой аудитории; право на responder/клиническое действие определяется отдельно по роли, действующей квалификации, scope, протоколу, юрисдикции, супервизии и оснащению. Наличие инструмента, лекарства или общей профессиональной лицензии не даёт отсутствующей компетенции.
- Запасы рецептурных препаратов, индивидуальные дозировки и возможные замены согласуются с врачом и фармацевтом. Самодельная анестезия, хирургия, внутривенное лечение и опасные схемы не входят в базовый уровень.
- Кипячение, фильтрация и бытовое обеззараживание не делают воду безопасной при любом химическом, топливном или радиологическом загрязнении.
- Респиратор, противогаз, турникет, генератор, радиооборудование и огнетушитель помогают только при правильном выборе, законном применении, обслуживании и тренировке.
- Генераторы и любые устройства с горением нельзя использовать в жилом помещении, гараже или другом плохо проветриваемом объёме из-за риска угарного газа.
- При официальном приказе об эвакуации или укрытии приоритет имеют указания властей и фактическая обстановка, а не универсальная памятка.
- Раздел личной безопасности ориентирован на предотвращение, уход от опасности, связь, деэскалацию и законную защиту; он не является пособием по причинению вреда.
- Научный/инженерный текст не расширяет квалификацию. Неизвестная биология, инвазивная медицина/ветеринария, синтез лекарств, взрывчатые/оружейные/токсичные системы, сеть и высокое напряжение, давление/газ, несущие конструкции, хладагент/hot work, реактивная химия, источники излучения, confined spaces, lithium/high-current/capacitors, machinery/stored energy, опасные строительные материалы, лазеры/интенсивное оптическое излучение и неконтролируемый нагрев/пар не входят в household execution layer. Точная матрица из 17 fail-closed gates находится в [practical-science-safety-gates.csv](practical-science-safety-gates.csv).

## Что находится в этой версии

- [START_HERE.html](START_HERE.html) и [START_HERE.txt](START_HERE.txt) — автономный стартовый маршрут без внешних зависимостей.
- [22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md](22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md) — датированный аудит разрыва между архитектурой и фактической готовностью; исходный baseline сохранён, последующие изменения отмечаются отдельно.
- [23_TECHNOLOGY_DEPENDENCY_TREE_RU.md](23_TECHNOLOGY_DEPENDENCY_TREE_RU.md) — правила дерева зависимостей, уровни готовности, типы рёбер, предпосылки и запрет выдавать опасный reference-контур за бытовую процедуру.
- [24_MASTER_CATALOG_STATUS_RU.md](24_MASTER_CATALOG_STATUS_RU.md) — единый мастер-статус: что уже есть, чего нет, домены, приоритеты, service levels и следующая очередь.
- [known-gap-register.csv](known-gap-register.csv) — 32 формальных открытых разрыва с блокируемыми уровнями, доказательствами и `DENY`-gates.
- [Obsidian-Vault/00 — НАЧАТЬ.md](Obsidian-Vault/00%20%E2%80%94%20%D0%9D%D0%90%D0%A7%D0%90%D0%A2%D0%AC.md) — единственный пользовательский вход в Obsidian; сгенерированные заметки остаются каталогом и не становятся автоматически проверенными карточками действий.
- [technology-dependency-register.csv](technology-dependency-register.csv), [technology-dependency-edges.csv](technology-dependency-edges.csv) и [technology-node-planning-register.csv](technology-node-planning-register.csv) — узлы, типизированные связи и план материализации; актуальные количества выводит валидатор.
- [technology-service-level-register.csv](technology-service-level-register.csv) — требуемые функции по уровням сервиса, приоритетам и масштабу группы.
- [capability-crosswalk.csv](capability-crosswalk.csv) — связи legacy-сценариев с технологическими узлами, MOC и научными контурами.
- [payload-source-crosswalk.csv](payload-source-crosswalk.csv) — явная связь реально сохранённых payload с источниками и пакетами; umbrella-связь не равна section-level review.
- [offline-library/README.md](offline-library/README.md) и [offline-library/offline-payload-register.csv](offline-library/offline-payload-register.csv) — фактический локальный стартовый корпус: 45 офлайн-файлов с локальными путями и контрольными данными. Это **не 45 готовых инструкций**: содержание, аудитория, применимость, перевод и условия допуска к действию проверяются отдельно.
- [01_MASTER_BLUEPRINT_RU.md](01_MASTER_BLUEPRINT_RU.md) — полный каркас системы, сценарии, материальные и информационные модули.
- [02_PERSONALIZATION_RU.md](02_PERSONALIZATION_RU.md) — данные, без которых нельзя честно рассчитать количества и маршруты.
- [03_INVENTORY_SCHEMA_RU.md](03_INVENTORY_SCHEMA_RU.md) — правила единого реестра предметов и запасов.
- [inventory-template.csv](inventory-template.csv) — машиночитаемый шаблон инвентаризации.
- [source-manifest.csv](source-manifest.csv) — стартовый машиночитаемый каталог ссылок (`link_status`), территориального охвата и provenance/transport-state, но не operational content manifest. Пустые `local_filename/offline_tested_at/sha256` означают, что источник ещё не скачан и не проверен в авиарежиме; строки нельзя использовать для action-retrieval до присвоения отдельного content status и section-level gates.
- [04_SOURCE_REGISTER_RU.md](04_SOURCE_REGISTER_RU.md) — первичный реестр официальных источников и сроков проверки.
- [05_BUILD_ROADMAP_RU.md](05_BUILD_ROADMAP_RU.md) — порядок превращения каркаса в проверенный комплект.
- [06_COVERAGE_MATRIX_RU.md](06_COVERAGE_MATRIX_RU.md) — матрица полноты от аптечки и воды до права, данных и восстановления.
- [07_MATERIAL_TECHNICAL_CONTOUR_RU.md](07_MATERIAL_TECHNICAL_CONTOUR_RU.md) — расчёты воды, пищи, энергии, запасов, ремонта, CBRN и ротации.
- [08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md](08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md) — полный медицинский тематический контур и границы M0–M4.
- [09_MEDICAL_SOURCE_CATALOG_RU.md](09_MEDICAL_SOURCE_CATALOG_RU.md) — медицинские руководства с уровнем аудитории и циклом обновления.
- [10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md](10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md) — офлайн-библиотека, карты, связь, резервирование, поиск и восстановление.
- [11_FIRST_AID_KIT_BASELINE_RU.md](11_FIRST_AID_KIT_BASELINE_RU.md) — физическая аптечка по модулям, условиям приёмки и ограничениям.
- [12_QA_AND_LIMITS_RU.md](12_QA_AND_LIMITS_RU.md) — что проверено, что не доказано и какие release gates обязательны до реального применения.
- [framework-visualization.html](framework-visualization.html) — самостоятельная интерактивная схема архитектуры, масштаба `N=1…7` и горизонтов `E0…E5`.
- [VISUALIZATION_QA.md](VISUALIZATION_QA.md) — воспроизводимый срез viewport/interaction/JavaScript-проверки схемы и её SHA-256.
- [13_MAPS_GEODATA_NAVIGATION_RU.md](13_MAPS_GEODATA_NAVIGATION_RU.md) — самостоятельная система карт, геоданных, бумажной/офлайн-навигации и независимых маршрутов.
- [map-register-template.csv](map-register-template.csv) — происхождение, версия, coverage, projected/exchange CRS, временной срок действия, privacy и offline/print/field status каждого продукта.
- [route-register-template.csv](route-register-template.csv) — отдельный реестр маршрутов, chokepoints, доступности, event-snapshot, privacy и stop/no-go условий.
- [site-register-template.csv](site-register-template.csv) — точки помощи, встреч, воды и укрытия с fail-closed статусами доступности и privacy-gate.
- [14_GROUP_1_TO_7_OPERATIONS_RU.md](14_GROUP_1_TO_7_OPERATIONS_RU.md) — роли, succession, buddy, связь, отдых, ресурсы и reunification от одного человека до семи.
- [group-roster-template.csv](group-roster-template.csv) — restricted master-профиль с default-deny privacy gate и внешним revision ID; не operational view.
- [group-operational-roster-template.csv](group-operational-roster-template.csv) — минимальный обезличенный operational view.
- [group-profile-template.csv](group-profile-template.csv) — отдельные составы людей `GP-N1…GP-N7` с revision ID; животные учитываются вне `N`.
- [group-revision-register-template.csv](group-revision-register-template.csv) — внешний реестр неизменяемых roster/profile-ревизий и content SHA-256 без самоссылочного хеша.
- [animal-profile-template.csv](animal-profile-template.csv) — отдельный профиль животных, применимые составы группы, handler/backup, acceptance-gates, ресурсы и ограничения shelter/transport.
- [group-function-assignment-template.csv](group-function-assignment-template.csv) — per-profile primary/backup/succession, role-gate FK, принятие назначения, доступность и проверка совмещения семи функций.
- [role-gate-record-template.csv](role-gate-record-template.csv) — каноническое доказательство пригодности конкретного человека для конкретного assignment; текущий пример `BLOCKED/DENY`.
- [group-composition-snapshot-template.csv](group-composition-snapshot-template.csv) — неизменяемый снимок активного состава конкретного события, к которому привязаны incident/accountability-записи.
- [buddy-assignment-template.csv](buddy-assignment-template.csv) — пары/триады/remote-buddy, точные `group_profile_ids`, effective scope и PACE.
- [external-contact-template.csv](external-contact-template.csv) — внешний check-in, identity, consent и privacy.
- [dependent-care-authorization-template.csv](dependent-care-authorization-template.csv) — полномочие и доказательство передачи ребёнка/зависимого человека.
- [resource-scaling-template.csv](resource-scaling-template.csv) — персональные, общие, резервные, расходные и capacity-ресурсы для `N=1…7`.
- [incident-log-template.csv](incident-log-template.csv) — журнал событий, ISO-время с offset/IANA zone, task/read-back checkback, composition snapshot, graph refs, released-card gate snapshot и handoff.
- [accountability-log-template.csv](accountability-log-template.csv) — поимённый учёт, subgroup, buddy, выход/возврат.
- [resource-transaction-log-template.csv](resource-transaction-log-template.csv) — выдача, перенос, измеренный остаток и состояние ресурса.
- [15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md](15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md) — нормализованная онтология угроз, модификаторов, каскадов и release states.
- [scenario-register.csv](scenario-register.csv) — машиночитаемый индекс 133 decision-distinct сценариев, включая 16 межпоколенческих `GEN-*`; section-level provenance пока `NOT_LINKED`, а `INDEX_ONLY` не является готовой карточкой действий.
- [decision-class-register.csv](decision-class-register.csv) — контролируемый словарь первых маршрутизаторов; каждый остаётся `INDEX_ROUTER_ONLY` до выпуска карточки.
- [action-card-register-template.csv](action-card-register-template.csv) — канонический реестр версий, источников, content SHA-256, review и release-state будущих карточек.
- [card-gate-snapshot-template.csv](card-gate-snapshot-template.csv) — fail-closed снимок обязательных допусков и hash-binding к точным байтам карточки; только вычисленное `ALLOW` с подтверждённым совпадением может сопровождать выпуск.
- [legacy-scenario-map.csv](legacy-scenario-map.csv) — явная миграция старых v0.1-кодов; все они `DO_NOT_USE_FOR_NEW_CARD`.
- [cascade-register-template.csv](cascade-register-template.csv) — переходы от исходного события к downstream-отказам; `proposed_card_status=NOT_CREATED` не выдаёт предложенный ID за существующую карточку, а relation/action sources ведутся раздельно.
- [16_CENTURY_CONTINUITY_RU.md](16_CENTURY_CONTINUITY_RU.md) — контракт E5: capability continuity, люди, площадка, stewardship, succession и столетний ритм проверок.
- [17_OFFLINE_LIBRARY_100Y_RU.md](17_OFFLINE_LIBRARY_100Y_RU.md) — многоуровневый офлайн-корпус, rights/fixity/release workflow, поиск, readers, носители, restore и миграция.
- [18_E5_REGISTERS_AND_GATES_RU.md](18_E5_REGISTERS_AND_GATES_RU.md) — машинная модель `CELL / SITE / INSTITUTION`, доменные gates и связи новых реестров.
- [19_OFFLINE_CORPUS_RESEARCH_RU.md](19_OFFLINE_CORPUS_RESEARCH_RU.md) — расширенный источниковедческий аудит: 30 категорий, open/offline ecosystems, лицензии, storage tiers, OCR, air-gap и tests.
- [20_PRACTICAL_SCIENCE_PRESERVATION_RU.md](20_PRACTICAL_SCIENCE_PRESERVATION_RU.md) — контракт сохранения воспроизводимой практической науки: источник, протокол, прибор, калибровка, raw data, uncertainty, evidence, safety и teach-back.
- [21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md](21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md) — официальный/первичный источниковый контур науки, права, Portugal/EU localization и acquisition waves.
- [practical-science-preservation-atlas.xlsx](practical-science-preservation-atlas.xlsx) — 9-sheet рабочий атлас с formula-driven priority: 239 domains, 259 package records, 239 projects, 73 instruments, 17 safety gates и 16 learning paths.
- [practical-science-domain-register.csv](practical-science-domain-register.csv), [practical-science-package-register.csv](practical-science-package-register.csv), [practical-science-project-register.csv](practical-science-project-register.csv), [practical-science-instrument-register.csv](practical-science-instrument-register.csv), [practical-science-safety-gates.csv](practical-science-safety-gates.csv), [practical-science-learning-paths.csv](practical-science-learning-paths.csv), [practical-science-protocol-template.csv](practical-science-protocol-template.csv) и [practical-science-raw-log-template.csv](practical-science-raw-log-template.csv) — долговременные plain-table представления; 257 внешне приобретаемых/TBD science packages остаются `CANDIDATE/NOT_DOWNLOADED`, два локально создаваемых evidence packages — `CANDIDATE/NOT_CREATED`.
- [PRACTICAL_SCIENCE_WORKBOOK_QA.md](PRACTICAL_SCIENCE_WORKBOOK_QA.md) — формульная, визуальная и CSV-проверка атласа.
- [horizon-register.csv](horizon-register.csv), [century-capability-register.csv](century-capability-register.csv) и [century-gate-snapshot-template.csv](century-gate-snapshot-template.csv) — словарь E0–E5, 32 capability и fail-closed E5 snapshot.
- [offline-corpus-manifest.csv](offline-corpus-manifest.csv) — исторический реестр 79 кандидатов на получение. Его статусы не описывают отдельный фактически сохранённый стартовый корпус из 45 офлайн-файлов в `offline-library/`; обе учётные плоскости нельзя складывать или подменять друг другом.
- [offline_library.py](offline_library.py) — автономный SHA-256 inventory/verify и SQLite FTS5 index/search без сетевых функций.
- [validate_worktree.py](validate_worktree.py) — текущая структурная проверка изменяемого `v0.5-draft` и целостности учтённых локальных payload.
- [validate_release.py](validate_release.py) — историческая fail-closed проверка состава замороженного `v0.4`; она не является валидатором live worktree.
- [offline-storage-plan-template.csv](offline-storage-plan-template.csv), [archive-media-register-template.csv](archive-media-register-template.csv), [format-migration-register-template.csv](format-migration-register-template.csv), [offline-restore-test-template.csv](offline-restore-test-template.csv) и [knowledge-succession-register-template.csv](knowledge-succession-register-template.csv) — копии, носители, миграция, blank-device restore и передача следующему хранителю.
- [institution-register-template.csv](institution-register-template.csv), [governance-policy-register-template.csv](governance-policy-register-template.csv) и [succession-register-template.csv](succession-register-template.csv) — stewardship, полномочия, safeguarding и передача прав.
- [land-parcel-register-template.csv](land-parcel-register-template.csv), [water-source-capacity-template.csv](water-source-capacity-template.csv), [soil-monitoring-template.csv](soil-monitoring-template.csv), [seed-accession-template.csv](seed-accession-template.csv), [asset-component-lifecycle-template.csv](asset-component-lifecycle-template.csv), [competency-lineage-template.csv](competency-lineage-template.csv), [population-capacity-snapshot-template.csv](population-capacity-snapshot-template.csv) и [climate-pathway-register-template.csv](climate-pathway-register-template.csv) — E5-модель территории, воды, почвы, семян, техники, навыков, care-capacity и климатических развилок.

## Статус доказанности

Live worktree `v0.5-draft` — это **расширенный архитектурный all-hazards framework E0–E5, типизированное дерево зависимостей, Obsidian-каталог, измеримый контур практической науки и небольшой фактически сохранённый стартовый офлайн-корпус**, а не завершённая медицинская энциклопедия, не готовые адресные карты, не выпущенные action packages, не выполненные 239 проектов и не подтверждение физического наличия снаряжения/73 приборов. `v0.4` остаётся отдельным замороженным историческим выпуском. Для каждого будущего модуля отдельно отмечаются состояния:

`спроектировано → источник проверен → приобретено → собрано → category-specific evidence получено → action-gates удовлетворены → обслуживается`

Нельзя заменять одно состояние другим. Например, запись в списке не доказывает, что предмет куплен; целая упаковка не доказывает соблюдение холодовой цепи; самопроверка AED не доказывает навык оператора; учебная симуляция не доказывает стерильность или пригодность конкретной партии; покупка турникета не доказывает умение им пользоваться; скачанный PDF не доказывает, что он читается без интернета и понятен в стрессе.

## Немедленные официальные контакты для Португалии

- **112** — угроза жизни, пожар, преступление в моменте, срочная медицинская помощь; бесплатно, круглосуточно.
- **SNS 24: 808 24 24 24** — круглосуточный клинический контакт для триажа, консультации и направления; не замена 112 при угрозе жизни. Административные услуги имеют отдельный режим работы.
- **CIAV: 800 250 250** — Центр информации по отравлениям; актуальный номер по gov.pt на 2026-06-26.
- **144** — бесплатная круглосуточная национальная линия социальной чрезвычайной помощи при ситуации, требующей немедленного вмешательства социальной защиты.
- При серьёзном риске ANEPC может направить бесплатное геотаргетированное SMS устройствам в затронутой зоне; отправитель — **AvisoPROCIV**, подписка не нужна. Это исключительный, не гарантированный единственный канал: необходимо следить и за сайтом ANEPC, официальными СМИ и муниципальной Proteção Civil.

Контакты и локальные планы должны быть распечатаны и проверяться не реже двух раз в год, поскольку номера, службы и процедуры могут измениться.
