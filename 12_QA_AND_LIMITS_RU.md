# QA, доказанность и открытые границы версии 0.4

**Срез:** 2026-08-29  
**Горизонт:** E0–E5, от события до 100 лет  
**Группа:** один человек или конкретная ячейка из 1–7 людей  
**Назначение:** не дать объёму документов создать ложное впечатление физической, медицинской, картографической, правовой, офлайн- или столетней готовности.

## 1. Что в этой версии действительно сделано

- создан связанный каркас от аптечки, воды, пищи, санитарии, жилья, энергии, ремонта, документов, карт и связи до образования, архива, управления, преемственности и институциональной памяти;
- введён канонический непрерывный словарь горизонтов: `E0 [0,12h]`, `E1 (12h,3d]`, `E2 (3d,14d]`, `E3 (14d,90d]`, `E4 (90d,15y)` и `E5 [15y,100y]`;
- E5 определён не как столетний склад, а как сохранение и восстановление функций через смену людей, поколений, оборудования, носителей, форматов, владельцев и условий среды;
- предмет E5 разделён на `CELL` — действующая ячейка N=1…7, `SITE` — земля/вода/жильё/активы/архив и `INSTITUTION` — право, stewardship, succession, safeguarding и аудит;
- введены контрольные окна `E5A 15–30`, `E5B 30–60`, `E5C 60–100`; они являются окнами планирования и переоценки, а не обещанием неизменности;
- допустимый положительный вывод ограничен `ALLOW_FOR_CURRENT_REVIEW_PERIOD`; статусы `100_YEAR_READY` и `PERMANENTLY_AUTONOMOUS` запрещены;
- создан отдельный безопасный бытовой контур аптечек и медицинский тематический индекс; M0–M4 остаются уровнями аудитории, а не лестницей полномочий;
- сохранены default-deny gates для роли, credential, currency, scope, protocol ID/version, jurisdiction, medical direction, facility, equipment и patient-specific order;
- карты оформлены как самостоятельная система: building/local/municipal/regional/national, scenario overlays, offline/print, route/site register, privacy и field-verification;
- создана операционная модель для одного человека и группы до семи: buddy, primary/backup roles, succession, accountability, PACE-связь, caregiver, fatigue, handoff и reunification;
- в all-hazards индекс добавлено 16 межпоколенческих сценариев `GEN-*`; прежние 117 сценариев не были автоматически расширены на E5;
- создан реестр из 32 столетних capability outcomes и 16 специализированных E5-шаблонов: институт, управление, преемственность, земля, вода, почва, семена, активы, компетенции, население, климат, хранение, архивные носители, миграция форматов, восстановление и передача знаний;
- создана архитектура максимального офлайн-корпуса: 79 package candidates, уровни L0–L4, права, acquisition, exact bytes, hash, malware scan, offline-open, индекс, retention, обновление, резервные копии и восстановление;
- добавлен отдельный контур практической науки: 239 capability domains, 259 package records (254 external URL candidates, 3 asset/person/authority placeholders и 2 local-authoring evidence packages), 239 предварительно типизированных `DESIGN_ONLY` проектов, 73 класса приборов, 17 no-go gates и 16 учебных траекторий;
- создан formula-driven XLSX-атлас и восемь plain CSV-представлений; science states намеренно остаются `FRAMEWORK_ONLY_NOT_TRAINED / CANDIDATE / NOT_DOWNLOADED или NOT_CREATED / NOT_REVIEWED / NOT_TESTED / DESIGN_ONLY_NOT_EXECUTED`;
- создан локальный stdlib-only инструмент [offline_library.py](offline_library.py) для инвентаризации SHA-256, проверки дерева, построения SQLite FTS5 и поиска;
- добавлен автономный [validate_release.py](validate_release.py), который fail-closed проверяет состав выпуска, 54 CSV, E0–E5, science states, ссылки, E5/rights состояния и hash визуализации;
- созданы два офлайн-входа: [START_HERE.txt](START_HERE.txt) и [START_HERE.html](START_HERE.html);
- интерактивная схема расширена до E5 и показывает переход `CELL → SITE → INSTITUTION`.

## 2. Размер и состав снимка

В каталоге 84 файла:

- 24 Markdown;
- 54 CSV;
- 2 самостоятельных HTML;
- 2 Python-инструмента;
- 1 XLSX-атлас;
- 1 текстовый стартовый файл.

Объём структуры — более 13 000 строк. Это объём схемы, реестров, исследования и шаблонов, а не объём уже загруженной внешней библиотеки.

## 3. Машинные таблицы

Во всех CSV проверяются единая ширина строк, уникальность заявленных primary keys, допустимые состояния и ссылки, где для них уже существует целевой реестр.

| Файл | Строк данных | Полей |
|---|---:|---:|
| `accountability-log-template.csv` | 4 | 20 |
| `action-card-register-template.csv` | 1 | 27 |
| `animal-profile-template.csv` | 1 | 25 |
| `archive-media-register-template.csv` | 1 | 27 |
| `asset-component-lifecycle-template.csv` | 1 | 38 |
| `buddy-assignment-template.csv` | 7 | 24 |
| `card-gate-snapshot-template.csv` | 1 | 30 |
| `cascade-register-template.csv` | 12 | 26 |
| `century-capability-register.csv` | 32 | 20 |
| `century-gate-snapshot-template.csv` | 1 | 34 |
| `climate-pathway-register-template.csv` | 1 | 29 |
| `competency-lineage-template.csv` | 1 | 24 |
| `decision-class-register.csv` | 20 | 5 |
| `dependent-care-authorization-template.csv` | 1 | 22 |
| `external-contact-template.csv` | 1 | 27 |
| `format-migration-register-template.csv` | 1 | 24 |
| `governance-policy-register-template.csv` | 1 | 24 |
| `group-composition-snapshot-template.csv` | 1 | 19 |
| `group-function-assignment-template.csv` | 49 | 26 |
| `group-operational-roster-template.csv` | 7 | 16 |
| `group-profile-template.csv` | 7 | 12 |
| `group-revision-register-template.csv` | 8 | 16 |
| `group-roster-template.csv` | 7 | 56 |
| `horizon-register.csv` | 6 | 15 |
| `incident-log-template.csv` | 4 | 59 |
| `institution-register-template.csv` | 1 | 22 |
| `inventory-template.csv` | 5 | 59 |
| `knowledge-succession-register-template.csv` | 1 | 21 |
| `land-parcel-register-template.csv` | 1 | 32 |
| `legacy-scenario-map.csv` | 25 | 5 |
| `map-register-template.csv` | 8 | 64 |
| `offline-corpus-manifest.csv` | 79 | 37 |
| `offline-restore-test-template.csv` | 1 | 28 |
| `offline-storage-plan-template.csv` | 1 | 23 |
| `population-capacity-snapshot-template.csv` | 1 | 26 |
| `practical-science-domain-register.csv` | 239 | 16 |
| `practical-science-instrument-register.csv` | 73 | 19 |
| `practical-science-learning-paths.csv` | 16 | 13 |
| `practical-science-package-register.csv` | 259 | 38 |
| `practical-science-project-register.csv` | 239 | 29 |
| `practical-science-protocol-template.csv` | 1 | 24 |
| `practical-science-raw-log-template.csv` | 12 | 17 |
| `practical-science-safety-gates.csv` | 17 | 6 |
| `resource-scaling-template.csv` | 10 | 43 |
| `resource-transaction-log-template.csv` | 2 | 17 |
| `role-gate-record-template.csv` | 1 | 26 |
| `route-register-template.csv` | 6 | 67 |
| `scenario-register.csv` | 133 | 31 |
| `seed-accession-template.csv` | 1 | 30 |
| `site-register-template.csv` | 7 | 46 |
| `soil-monitoring-template.csv` | 1 | 26 |
| `source-manifest.csv` | 39 | 20 |
| `succession-register-template.csv` | 1 | 26 |
| `water-source-capacity-template.csv` | 1 | 30 |

Независимый cross-parser и выпускной контроль:

- Python `csv.reader(strict=True)`: `PASS`, 54 файла, 1 357 строк данных;
- системный Ruby CSV: `PASS`, 54 файла, 1 357 строк данных;
- `validate_release.py`: `files=84`, `csv=54`, `scenarios=133`, `capabilities=32`, `offline_candidates=79`, `science_domains=239`, `science_packages=259`, `science_projects=239`, `science_instruments=73`, `issues=0`, `result=PASS`;
- оба Python-файла успешно компилируются встроенным `compile()`;
- относительные Markdown/HTML-ссылки и SHA-256 самостоятельной визуализации разрешаются валидатором;
- XLSX: 9 sheets отрендерены и просмотрены; проверены 268 формул — 9 dashboard KPI и 259 priority score; formula-error scan не нашёл `#REF!/#DIV0!/#VALUE!/#NAME?/#N/A`.

## 4. Проверенные структурные инварианты

### Горизонты

- `horizon-register.csv` содержит ровно шесть строк E0–E5 и непрерывные границы без зазора между E4 и E5;
- голое значение `ALL` запрещено в полях горизонта, потому что оно могло бы молча распространить старые строки на новый E5;
- 107 старых scenario rows имеют явный `E0_E4`, 1 — `E2_E4`, 4 — `E3_E4`, 5 — `E4`; 16 новых `GEN-*` имеют `E5`;
- все 117 унаследованных сценариев имеют `e5_review_state=NOT_REVIEWED`;
- все 16 `GEN-*` имеют `e5_review_state=ARCHITECTURE_ONLY`;
- все десять строк `resource-scaling-template.csv` явно ограничены E0–E4 и не объявлены ресурсами E5.

### Сценарии и карточки

- в `scenario-register.csv` 133 уникальных ID;
- распределение: `MED 24`, `NAT 18`, `TEC 17`, `GEN 16`, `INF 13`, по `BIO/CYB/SEC/SOC 8`, `OPS 7`, `ENV 6`;
- все 133 сценария остаются `INDEX_ONLY`, `NOT_REVIEWED`, `NOT_LINKED`; это маршрутизаторы покрытия, а не готовые инструкции;
- все first-decision IDs разрешаются в `decision-class-register.csv`, а первый шаг decision sequence совпадает с declared class;
- 16 `GEN-*` не содержат утверждённых action cards и требуют профессиональной проверки;
- пример action-card остаётся `NOT_CREATED/NOT_RELEASED`, а snapshot — `BLOCKED/DENY` без hash-match и role gate;
- SHA-256 точного content-файла, версия и gate snapshot должны совпасть прежде, чем карточка может быть выпущена.

### E5 capability continuity

- все 32 capability rows имеют `evidence_state=MISSING`, `lifecycle_state=PLANNED`, `gate_decision=DENY`;
- ни один E5-пример не объявляет функцию доказанной, работающей или столетне готовой;
- institution, governance, succession, land, water, soil, seed, asset, competency, population и climate examples остаются draft/fail-closed;
- century gate не может дать `ALLOW_FOR_CURRENT_REVIEW_PERIOD`, пока обязательные evidence records, review, successor и recovery conditions не подтверждены;
- человеческая ячейка N=1…7 не смешивается с SITE/INSTITUTION: это разные субъекты, владельцы доказательств и failure modes.

### Группа 1–7

- каждый `GP-N1…GP-N7` содержит точное число активных person IDs и семь function-assignment rows;
- primary/backup/successor не выходят за active person set профиля;
- назначения остаются `PLANNED/BLOCKED` до принятия роли, доступности, capability и concurrency evidence;
- buddy-набор покрывает каждого активного человека ровно один раз в каждом N-профиле;
- животные не входят в human N; handler activation остаётся `BLOCKED`;
- composition snapshot остаётся `DRAFT_NOT_EFFECTIVE`, пока digest roster/profile revision не подтверждён;
- incident/accountability rows не могут считаться проверенными без разрешённых group profile и composition snapshot.

### Карты, маршруты и площадки

- map/route/site references проверяются на разрешение либо явно остаются `TBD`;
- route register является authoritative для route→map и origin/destination;
- freshness/privacy gates примеров остаются `DENY`;
- нет строк, объявляющих route `FIELD_CHECKED/OPERATIONAL` без фактической проверки;
- наличие геометрии, координаты или hazard layer не доказывает доступность дороги, воды, убежища или медицинской функции во время события.

### Офлайн-корпус

- `offline-corpus-manifest.csv` содержит 79 уникальных package candidates;
- 76 строк имеют `NOT_DOWNLOADED`, а DGS, INFARMED и Diário da República — `DO_NOT_INGEST` до сохранённого разрешения или конкретного правового основания для локального воспроизведения;
- у всех 79 строк `content_review_state=NOT_REVIEWED`, `section_review_state=NOT_REVIEWED`, `offline_open_state=NOT_TESTED`, `search_index_state=NOT_INDEXED`;
- нет заполненных `local_path`, `byte_size`, `sha256` или upstream checksum, потому что внешний payload ещё не загружен;
- `source-manifest.csv` остаётся 39-строчным link catalog; `offline-corpus-manifest.csv` — package/object queue. Ни один из них сам по себе не доказывает офлайн-наличие;
- HTTP-исследование отчёта проверило 126 URL как transport-level evidence; это не означает, что каждая из 79 manifest rows прошла content, rights, edition и local-applicability review;
- free-to-read не приравнивается к праву копирования или перераспределения; права фиксируются для каждого точного item/version.

### Практическая наука

- `practical-science-domain-register.csv`: 239 уникальных domains; 116 S0, 75 S1, 33 S2, 11 S3 и 4 S4; все `FRAMEWORK_ONLY_NOT_TRAINED`; prerequisite graph не содержит self-link, duplicate edge или cycle;
- `practical-science-package-register.csv`: 259 уникальных records; все `CANDIDATE`, `NOT_REVIEWED`, `NOT_TESTED`; 257 имеют `NOT_DOWNLOADED`, два local-authoring records — `NOT_CREATED`; hash/local path/retrieved date пусты;
- rights states: 233 `REQUIRES_ITEM_REVIEW`, 17 `REFERENCE_ONLY_NO_COPY`, 3 `DO_NOT_INGEST_UNTIL_RIGHTS_CLEARED` и отдельные personalization/localization/asset/local-authoring gates;
- `practical-science-project-register.csv`: 239 уникальных designs; все `DESIGN_ONLY_NOT_EXECUTED`, все 239 source bindings явно `PROVISIONAL_TOPIC_CANDIDATES_NOT_METHOD_REVIEWED`, а execution gates — `BLOCKED_UNTIL_EXACT_METHOD_SOURCE_SAFETY_AND_LOCAL_REVIEW`; S3 превращён в dataset/simulation/pro observation, S4 — в reference-only/no execution;
- `practical-science-instrument-register.csv`: 73 уникальных instrument classes; все `CANDIDATE_NOT_INVENTORIED`; range/resolution/reference остаются `TBD_PER_EXACT_*`, поэтому владение, пригодность, calibration и traceability не заявлены;
- `practical-science-safety-gates.csv`: 17 уникальных no-go; кроме исходных медицинских, биологических, химических, электрических, structural, pressure/gas, radiation и confined-space границ добавлены lithium/high-current/capacitor, machinery/stored-energy, hazardous-building-material, laser/optical и uncontrolled-heat gates;
- workbook `Overview`: 239 domains, 259 packages, 239 projects, 73 instruments, 15 S3/S4 domains, формульная очередь priority, 259 pending acquisition/creation, 17 safety gates, 0 external payload, 0 executed projects, 0 trained people;
- formula priority использует видимые веса, построчно протянута и не содержит обнаруженных spreadsheet errors;
- визуально просмотрены все 9 sheets; wide registers требуют горизонтальной прокрутки, но заголовки заморожены и ключевые поля не обрезаны;
- XLSX не считается долговременным единственным master: рядом находятся CSV и Markdown.

### Локальный инструмент

На временном двухфайловом корпусе проверены:

- `inventory`: 2 файла, 57 878 bytes, SHA-256 lock создан;
- `verify`: исходное дерево — `PASS`, 2/2 файла;
- `index`: 2 full-text документа проиндексированы в SQLite FTS5;
- `search`: запрос `столетний` вернул оба релевантных документа;
- negative test: после замены одного файла проверка завершилась ненулевым кодом и `FAIL` из-за size mismatch.

Это доказывает работу инструмента на тестовом текстовом наборе в текущей среде. Это не доказывает восстановимость большого корпуса, поддержку каждого бинарного формата или долговечность физического носителя.

### Визуализация

- самостоятельный [framework-visualization.html](framework-visualization.html) прошёл 24 комбинации: 360/736/1 024 px × light/dark × N=1/N=7 × E4/E5;
- выполнен smoke test всех горизонтов E0–E5;
- во всех случаях отображаются ровно шесть horizon options и шесть dots, крайние dots совпадают с концами track;
- зафиксированы 0 JavaScript errors и отсутствие горизонтального переполнения;
- E5 показывает stewardship-строку, E4 её скрывает;
- три representative screenshots просмотрены визуально; наложений и обрезки ключевого E5-содержания не обнаружено;
- клавиатурное управление в headless-среде не заявляется проверенным.

## 5. Что не доказано и не выполнено

### Физическое состояние

- ни один предмет не куплен, не пересчитан и не подтверждён физически;
- не проверены конкретные модели, сертификация, инструкции производителя, совместимость, подделки или безопасное размещение;
- количества воды, пищи, лекарств, энергии и расходников не рассчитаны без персональных профилей;
- фактическая вместимость автомобиля, масса переносимого комплекта и способность людей нести груз не измерены;
- ни один генератор, аккумулятор, фильтр, насос, инструмент или spare part не прошёл реальный функциональный тест.

### Медицина

- комплект не является медицинским назначением и не заменяет 112, SNS 24, CIAV, врача, фармацевта или очное обучение;
- личные лекарства, дозировки, противопоказания, cold chain и запас непрерывности не заполнены;
- ни одна высокорисковая карточка не прошла двуязычную клиническую проверку;
- отсутствие профессионала не расширяет полномочия пользователя;
- M2–M4 и CBRN остаются gated/reference-only там, где требуются qualification, facility, medical direction или authority.

### Карты и маршруты

- не указаны муниципалитет, район, дом, работа, школа и реальные R1/R2/R3;
- не выбран конкретный действующий municipal emergency plan;
- геоданные не скачаны, не нормализованы по CRS, не экспортированы и не хешированы;
- ни один маршрут не прошёл desktop, field, load или drill verification;
- ни одна вода не подтверждена как питьевая, ни одно убежище — как открытое, ни одна больница — как выполняющая нужную функцию в момент события.

### Группа и организация

- семь roster rows — псевдонимный пример, а не реальные люди;
- role acceptance, capability, buddy, caregiver, external contact, succession и safeguarding authority фактически не согласованы;
- PACE failure domains не выбраны и не испытаны;
- handoff, separation/reunification, minimal-safe-mode и successor recovery не отрабатывались;
- правоспособность институции, владение/аренда, наследование, water rights, insurance и архивные полномочия не проверены.

### Офлайн-библиотека

- ни один внешний ZIM, PBF, PDF, EPUB, WARC, dataset или software package не скачан в рамках этого выпуска;
- ни один внешний object не имеет локального SHA-256, malware scan, offline-open, section review или clean-room restore evidence;
- не собраны физические уровни L0–L4, резервный reader, бумажный красный комплект и географически отдельная копия;
- не измерены фактические объёмы, скорость обновления, энергопотребление, срок восстановления и стоимость носителей;
- права каждого item, перевода, изображения, карты, шрифта и dataset не проверены;
- поисковый индекс реального корпуса не построен;
- результаты HTTP-проверки могут устареть.

### Столетний горизонт

- E5 — архитектура continuity, а не доказательство выживания 100 лет;
- не доказаны урожайность, климатическая пригодность, carrying capacity, право на землю/воду, демография, здоровье поколений, отсутствие конфликтов или непрерывность цепочек поставок;
- не доказано, что нынешний формат, носитель, шифр, оборудование, организация или юрисдикция проживут 100 лет;
- ни одна capability не имеет реальных evidence series за E5A/E5B/E5C;
- единственно допустимый будущий положительный статус — ограниченное по сроку `ALLOW_FOR_CURRENT_REVIEW_PERIOD` после проверки текущего цикла.

## 6. Что доказывает конкретная проверка

| Проверка | Доказывает | Не доказывает |
|---|---|---|
| HTTP/link check | URL отвечал в момент проверки | права, актуальность, локальную применимость, офлайн-доступ |
| item/license capture | зафиксированы terms точного item/version | что юридическая интерпретация полна или навсегда неизменна |
| SHA-256 | bytes совпадают с зафиксированным digest | корректность, безопасность, право использования или понятность |
| malware scan | конкретный scanner не нашёл известный pattern | абсолютную безопасность файла |
| offline-open | файл открылся на конкретном устройстве без сети | что нужный раздел будет найден и понят под стрессом |
| index search | query вернул documents/sections | клиническую, техническую или юридическую пригодность результата |
| restore test | выбранная копия восстановила проверяемый набор | что все другие копии и будущие устройства сработают |
| package/expiry check | состояние упаковки/срок на дату проверки | правильное применение или эффективность для человека |
| device self-test | заявленную инструкцией часть self-test | полную работоспособность во всех режимах и навык оператора |
| field walk | маршрут был проходим в тех условиях | безопасность во время пожара, наводнения или закрытия |
| drill | группа выполнила заданный безопасный сценарий | гарантию результата в реальном событии |
| successor demonstration | successor восстановил заданную функцию | вечную преемственность институции |
| current-cycle E5 gate | обязательные evidence прошли текущий review | `100_YEAR_READY` или постоянную автономность |

Proof states не сворачиваются в один процент готовности.

## 7. Жёсткие safety boundaries

- **Медицина:** отсутствие врача не расширяет бытовые полномочия; личные рецептурные препараты не становятся общим запасом.
- **CBRN:** никаких hot-zone entry, sampling, sniffing, самостоятельной идентификации, нейтрализации, переноски источника, KI/антидота без официального указания.
- **Огонь/CO/газ:** выход, 112 и no-reentry; никакого поиска в дыму или возвращения за вещами.
- **Электричество:** никаких live work, backfeed, повреждённого щита, high-voltage/EV battery intervention.
- **Обрушение/confined space:** никакого самостоятельного structural search, shoring, перемещения плит, входа в шахту или замкнутый объём.
- **Вода:** не входить и не въезжать в поток; бытовая обработка не исправляет любую chemical/radiological contamination.
- **Насилие:** avoidance, escape, distance, de-escalation, 112 и safeguarding; без наступательных и оружейных инструкций.
- **Карты:** официальный приказ, фактическое закрытие и наблюдаемая опасность выше персонального маршрута.
- **Семена/пища/вода:** энциклопедическое совпадение не доказывает съедобность, агрономическую пригодность или питьевую безопасность.
- **Право:** офлайн-копия закона — historical snapshot; перед необратимым действием при доступной связи нужна актуальная проверка.

## 8. Release gates персонального рабочего комплекта

Версия не получает статус персонального рабочего комплекта, пока не выполнены все применимые пункты:

1. заполнены реальные люди, животные, здоровье, языки, mobility, жильё, муниципалитет, транспорт, навыки и бюджет;
2. проведена физическая инвентаризация без покупок по памяти;
3. рассчитаны E0–E4 quantities, capacity, throughput, concurrency, storage и rotation;
4. выбран действующий Portugal/municipal risk overlay с edition/license/CRS;
5. выпущены privacy-разделённые building/local/municipal/regional maps;
6. маршруты имеют chokepoints, access check, field/load/drill evidence и `review_due`;
7. site records проверены fail-closed: вода, медицина, shelter activation, accessibility и pets;
8. сформированы реальный roster, buddy, primary/backup, caregiver, lawful handoff и succession;
9. PACE-связь использует независимые failure domains; проведены missed-check-in и reunification drills;
10. каждая критическая покупка имеет specification, официальный источник, storage и evidence plan;
11. разрешённые официальные файлы загружены, названы стабильно, хешированы, проверены и открыты без сети на двух readers;
12. опасные переводы и карточки проверены профильным двуязычным специалистом;
13. action-linked карточки имеют точный content hash, version, gates и review due;
14. красные карточки прошли безопасную симуляцию;
15. каскадные tabletop exercises проверили materially applicable downstream branches;
16. введены rotation, recall, maintenance, training, restore, migration, cartographic и source-review schedules;
17. для E5 назначены steward и successor, задокументированы authority/safeguarding/recusal и проверено восстановление после утраты custodian;
18. land/water/soil/seed/asset/competency/population/climate registers заполнены реальными данными, где применимо;
19. ни один E5 gate не использует запрещённые статусы `100_YEAR_READY` или `PERMANENTLY_AUTONOMOUS`;
20. решение ограничено текущим review period и автоматически истекает при просрочке evidence.

## 9. Практический следующий шаг

Сначала заполнить профиль N=1…7, муниципалитет/тип жилья, медицинские зависимости, транспорт, бюджет и фактический инвентарь. Параллельно собрать минимальный L0/L1: бумажный START HERE, критические контакты/карты/личные медицинские планы и rights-cleared офлайн-ядро на основном и резервном reader. Только затем расширять L2–L4 и E5 registers. Иначе «максимум информации» станет большим неуправляемым складом файлов без доказанной доступности, прав, актуальности и восстановления.
