# Исследование источников практической науки

## 1. Статус исследования

Дата среза: **2026-08-29**. Реестр содержит 259 package records: 254 кандидата с внешним HTTP(S)-маршрутом, 3 asset/person/authority placeholders с ещё не выбранным маршрутом и 2 локально создаваемых evidence packages. Это каталог преимущественно официальных/первичных кандидатов, но не внешний payload и не утверждение, что каждый объект уже прошёл item-level проверку. `canonical_url` и `rights_url` — маршруты к будущей проверке, а не доказательство неизменности страницы, права на локальную копию или пригодности содержания.

Рабочее правило:

```text
официальный домен ≠ открытая лицензия
свободное чтение ≠ разрешение зеркалировать
download button ≠ право перераспределять
open access ≠ единая лицензия всех объектов
книга ≠ безопасный протокол
технический стандарт ≠ право выполнять регулируемую работу
старый официальный PDF ≠ текущая норма
```

## 2. Приоритетные первичные экосистемы

### 2.1. Метрология, математика и научный метод

| Экосистема | Практическая ценность | Offline/right boundary |
|---|---|---|
| BIPM SI Brochure — https://www.bipm.org/en/publications/si-brochure | определения SI и единицы | сохранить точную edition/license; документы JCGM имеют отдельные ограничения |
| NIST SP 330/SP 811 — https://www.nist.gov/pml/owm/si-units | SI notation и применение | NIST/third-party portions проверяются на уровне публикации |
| NIST/SEMATECH Handbook — https://www.itl.nist.gov/div898/handbook/ | design of experiments, measurement, process, reliability | официальный CD/download route описывает копирование; текущие компоненты и ссылки перепроверяются |
| NIST Chemistry WebBook — https://webbook.nist.gov/chemistry/ | свойства веществ и спектры | NIST SRD/database terms; это reference data, не процедура |
| NIST Statistical Reference Datasets — https://www.itl.nist.gov/div898/strd/ | проверка статистического software | сохранить certified values и tests |
| JCGM GUM/VIM — https://www.bipm.org/en/committees/jc/jcgm/publications | uncertainty и vocabulary | бесплатный доступ не приравнивать к свободной переработке/распространению |

### 2.2. Базовые учебники и курсы

| Экосистема | Offline mechanism | Rights gate |
|---|---|---|
| OpenStax — https://openstax.org/ | официальный PDF каждого title; web view | текущая общая политика CC BY-NC-SA 4.0; точный notice каждого title/edition и third-party material сохраняются отдельно |
| MIT OpenCourseWare — https://ocw.mit.edu/ | официальный per-course download | CC BY-NC-SA и third-party exclusions; MIT Learn и OCW не смешиваются в один bulk route |
| PhET — https://phet.colorado.edu/en/offline-access | individual regular HTML sim или официальный offline app | regular HTML sims сейчас CC BY-NC 4.0; PhET-iO/Studio/legacy assets проверяются отдельно |
| Kolibri — https://learningequality.org/kolibri/about-kolibri/ | экспорт/import каналов на USB | software и каждый channel/resource имеют отдельные права |
| Kiwix/OpenZIM — https://library.kiwix.org/ | ZIM + reader | ZIM наследует права исходного проекта/материалов; variant/date/hash обязательны |
| Wikimedia dumps — https://dumps.wikimedia.org/backup-index.html | XML dumps/checksums | атрибуция, история и project/page licenses; нужен собственный renderer/index |

### 2.3. Физика, химия и инженерия

Кандидаты включают:

- NASA Systems Engineering Handbook;
- NIST fire/material/measurement publications;
- IUPAC Gold Book и PubChem bulk interfaces с source-level provenance;
- UNECE GHS и official SDS/hazard literacy;
- NIOSH/OSHA/HSE safety references;
- OpenStax Physics/Chemistry и MIT OCW;
- KiCad, FreeCAD, OpenSCAD, Arduino и Raspberry Pi documentation/source;
- EnergyPlus, SAM, PVGIS и NREL research/tooling;
- USDA Wood Handbook, FEMA/HUD building-science references;
- LNEC repository и Portugal-specific engineering publications.

Граница: chemistry books сохраняются как теория и hazard literacy; reactive synthesis, toxic gas, energetic materials и неизвестные смеси остаются S4. Engineering books не открывают mains, structural, gas, pressure, refrigeration или official commissioning scope.

### 2.4. Земля, вода, биология, сельское хозяйство и пища

Кандидаты включают:

- FAO Knowledge Repository, AGRIS, AGROVOC, FAOSTAT, AQUASTAT и selected seed/genebank materials;
- Catalogue of Life, ITIS, NCBI Taxonomy и GBIF;
- EEA Waterbase, Copernicus Land/Climate/Emergency, ESA и NASA Earthdata;
- USGS National Map, Water Science School и Publications Warehouse;
- SoilGrids, WoSIS, USDA Soil Survey Manual/Field Book и LUCAS/ESDAC rights-controlled datasets;
- WHO drinking-water guidance, water-safety planning and sanitary-inspection materials;
- USDA/NCHFP validated home-canning references и FoodData Central;
- WOAH veterinary reference with redistribution/currentness gate;
- Portugal ICNF, APA/SNIRH, LNEG, DGAV и PortFIR candidates.

Field pH, EC, turbidity, moisture, imagery and visual sanitary inspection остаются скринингом. Они не доказывают potability, contaminant absence, disease, fertilizer requirement или legal compliance. Нельзя определять съедобность гриба, растения или животного по картинке/базе.

### 2.5. Вычисления, инструменты и сохранение software

| Экосистема | Что сохранять |
|---|---|
| Debian — https://www.debian.org/distrib/ | installer media, checksums/signatures, selected package pool, source и licenses |
| Python — https://docs.python.org/3/download.html | docs, exact interpreter source/binary, tests, wheels/source dependencies |
| GNU — https://www.gnu.org/manual/manual.html | manuals, source, build instructions, licenses |
| PostgreSQL/SQLite | docs, source, dump/restore fixtures и version matrix |
| Git/Pro Git | executable/source, documentation, offline bundles и integrity tests |
| R/Julia/GNU Octave | source, packages/depot snapshot, manuals, reference results |
| QGIS/FreeCAD/KiCad | LTR/stable binaries, source, plugins/libraries, docs, project fixtures |
| Software Heritage | persistent identifiers и external redundancy, но не вместо локально собираемой копии |
| OpenZIM/libzim | specification, reader/tool source, build dependencies и sample ZIM |

Каждый software package должен иметь source, binary, toolchain, build instructions, lock/manifest, licenses, test fixture, expected output, fonts/codecs и запасной open-format export. Успешный запуск старого бинарника сегодня не доказывает возможность его запуска через 25 лет.

### 2.6. Цифровое сохранение

- Library of Congress Recommended Formats Statement: https://www.loc.gov/preservation/resources/rfs/
- Library of Congress Sustainability of Digital Formats: https://www.loc.gov/preservation/digital/formats/
- NDSA Levels of Digital Preservation: https://ndsa.org/publications/levels-of-digital-preservation/
- RFC 8493 BagIt: https://www.rfc-editor.org/rfc/rfc8493.html
- PRONOM: https://www.nationalarchives.gov.uk/PRONOM/

Эти источники помогают проектировать хранение, но не гарантируют век. Гарантийный объект — регулярный restore/migration/succession process.

## 3. Portugal/EU: что локализуется отдельно

### 3.1. Приоритетные authority paths

- SNIG/DGT/CAOP — geodata, CRS, official administrative layers;
- IPMA — weather, climate, seismic and ocean data;
- APA/SNIRH — water, flood and environmental information;
- LNEG — geology/hydrogeology;
- ICNF — conservation, forest and fire-related layers;
- DGAV — plant health, food, animal welfare and regulated agriculture;
- LNEC — civil-engineering research and technical practice;
- DGEG/ERSE — energy and regulatory context;
- DGS — health norms and guidance;
- INFARMED/Infomed — exact medicine information;
- EUR-Lex — EU law;
- Diário da República — Portugal primary law;
- dados.gov.pt — dataset discovery, with license per dataset.

### 3.2. Fail-closed права

- DGS: локальная копия не выпускается, пока не документировано право; ссылка и metadata допустимы.
- INFARMED/Infomed: условия ограничивают воспроизведение/распространение; bulk mirror запрещён без разрешения.
- Diário da República: primary-law metadata и ссылки сохраняются; общий mirror не предполагается без доказанного правового режима.
- DGAV, APA, IPMA, LNEC, LNEG, DGEG и datasets catalog: право проверяется per item/per dataset.
- IPQ/CEN/CENELEC/IEC/ISO/ASTM и другие standards: paid/viewable standard не копируется в общий корпус без соответствующей лицензии; хранится citation, edition, lawful access path и, если разрешено, персональная restricted copy.

### 3.3. Открытые локальные пробелы

До operational release нужны:

1. municipality и конкретная площадка;
2. Portugal mainland/Madeira/Azores coverage distinction;
3. текущие нормы воды и список аккредитованных лабораторий;
4. legal/technical corpus по building, fire, electricity, gas, water, waste и environment;
5. местные agronomic calendars, varieties, soils, water availability и plant-health rules;
6. официальные PT-PT identifiers для опасных/охраняемых/инвазивных видов;
7. DGS/DGAV/ERSAR/PortFIR exact rights и stable bulk routes;
8. двуязычный PT/RU review опасных терминов, единиц, отрицаний и stop-conditions;
9. asset-specific OEM manuals;
10. calibration providers, traceable references и сертификаты.

## 4. Права: классы решения

| Rights state | Допустимое действие |
|---|---|
| `REQUIRES_ITEM_REVIEW` | выбрать точный item, сохранить notice, проверить third-party parts, решить personal/group/redistribution scope |
| `REFERENCE_ONLY_NO_COPY` | хранить citation/metadata и lawful access path; payload только в разрешённом private vault |
| `DO_NOT_INGEST_UNTIL_RIGHTS_CLEARED` | не скачивать/не включать в release; ссылка и причина блокировки |
| `LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED` | локальный authority важен, но копия не выпускается до legal evidence |
| `REQUIRES_ASSET_INVENTORY` | источник нельзя определить без maker/model/serial/revision |
| `REQUIRES_PERSONALIZATION` | индивидуальный care/medical record создаётся специалистом и хранится restricted |
| `REQUIRES_LOCALIZATION` | нужен Portugal/municipality/installation-specific review |
| `LOCAL_AUTHORING_REQUIRED` | corpus появляется только после собственных tests, logs, translations и consent |

## 5. Приоритет будущего скачивания

### Волна A — маленькое ядро

1. SI/units, NIST statistics/measurement и BagIt;
2. exact reader stack и Debian/Python documentation;
3. выбранные OpenStax math/physics/biology/computing titles;
4. один language set RU/UK/PT/EN;
5. exact OEM manuals фактических приборов/активов;
6. локальные official maps/authority contacts после localization;
7. protocol/raw-log/restore forms и printed core.

### Волна B — воспроизводимое обучение

1. selected MIT OCW/PhET/Kolibri items;
2. QGIS/FreeCAD/KiCad and test projects;
3. FAO/USGS/WHO/EEA materials с очищенными правами;
4. soil/water/food/agriculture field references;
5. software source, build closure and test fixtures.

### Волна C — глубокий корпус

- большие ZIM/dumps;
- Earth/climate datasets;
- Europe PMC/PMC OA subset per-article rights;
- course video;
- source mirrors and emulation images;
- scientific datasets with stable DOI and data dictionaries.

### Волна D — community/rights-controlled

- paid standards under correct group license;
- professional texts with role-gated access;
- institutional datasets and translations;
- multi-site community replicas.

## 6. Что намеренно исключено из household action layer

- оружие, взрывчатые, зажигательные, токсичные и offensive cyber procedures;
- культивирование неизвестных организмов, pathogens, toxin extraction или virulence work;
- pharmaceutical synthesis, anaesthesia, surgery, injections и invasive dentistry/veterinary work;
- mains/live electrical work, high voltage, backfeed и unsafe battery rebuilding;
- structural modification, gas, pressure vessels, refrigerant service и hot work без допуска;
- ionizing-radiation sources;
- confined spaces, flooded systems, diving and unprotected height;
- pesticide selection/mixing/application вне label, law и trained scope;
- объявление воды/пищи/почвы безопасной по одному полевому датчику;
- определение съедобности по изображению;
- раскрытие sensitive species coordinates, health records или private infrastructure data.

## 7. Итог

Наиболее дефицитны не ещё тысячи ссылок, а:

- item-level rights decisions;
- точные editions и immutable bytes;
- Portuguese localization;
- asset/person-specific manuals;
- калиброванные references;
- безопасно выполненные проекты;
- independent review;
- clean-device restore;
- teach-back и successor handoff.

Поэтому 259 кандидатов остаются честной очередью. Следующий выпуск корпуса должен увеличивать не число строк, а число пакетов, которые прошли весь путь `rights → bytes → hash → offline-open → content review → safety gate → restore → teach-back`.
