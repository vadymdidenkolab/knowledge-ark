# Каталог медицинских первичных источников

**Срез:** 2026-08-29.  
**Назначение:** определить, какие официальные материалы должны находиться в автономной библиотеке, для кого они предназначены и как быстро устаревают.  
**Статус:** каталог ссылок; наличие записи ещё не доказывает, что файл скачан, проверен в авиарежиме, переведён или распечатан.

## 1. Разделение по аудитории

| Каталог | Аудитория | Что допустимо |
|---|---|---|
| `00_QUICK_ACTION_LAY` | любой человек | распознавание, безопасность, вызов помощи, простые действия и запреты |
| `10_TRAINED_FIRST_AID` | прошедший очное обучение | BLS/AED, удушье, кровотечение и первая помощь в пределах курса |
| `20_CLINICIAN` | лицензированный медработник | клиническая оценка, рецептурное лечение и процедуры в пределах профессии |
| `30_SPECIALIST_ONLY` | профильный специалист/служба | хирургия, анестезия, акушерские осложнения, токсикология, CBRN, общественное здравоохранение |
| `90_LEGACY_DO_NOT_USE_WITHOUT_PATCH` | редактор/эксперт | старые, но исторически или методически полезные руководства с обязательными актуальными дополнениями |

Один и тот же документ может содержать разделы разных уровней. Для него обязателен section-level map: страницы/главы, аудитория, конкретная роль и gates. Пока такой карты нет, смешанный документ целиком имеет статус `REFERENCE_ONLY` и не появляется в оперативном поиске. Для бытовой красной карточки берутся только отдельно проверенные действия уровня населения; профессиональные дозы и процедуры не переносятся автоматически.

## 2. Первая помощь и реанимация

### MED-SRC-IFRC-FA-2025

- **Источник:** IFRC International First Aid, Resuscitation and Education Guidelines 2025.
- **Аудитория:** редакторы программ и инструкторы; адаптированный результат — LAY/TRAINED.
- **Страница:** <https://www.ifrc.org/document/ifrc-international-first-aid-resuscitation-and-education-guidelines-2025>
- **PDF:** <https://www.ifrc.org/sites/default/files/2026-03/IFRC%20International%20First%20Aid%2C%20Resuscitation%20and%20Education%20Guidelines%202025.pdf>
- **Проверено:** опубликовано IFRC 2026-03-18 как редакция 2025.
- **Пересмотр:** ежегодно и после обновления IFRC.

### MED-SRC-ERC-2025

- **Источник:** European Resuscitation Council Guidelines 2025.
- **Аудитория:** LAY/TRAINED/CLINICIAN в зависимости от главы.
- **Центр:** <https://www.erc.edu/science-research/guidelines/guidelines-2025/>
- **Материал для населения:** <https://www.erc.edu/for-everyone/learn-cpr/guidelines-for-everyone/>
- **Первая помощь PDF:** <https://www.erc.edu/media/i2vllpae/gl2025-12-faid-e.pdf>
- **Пересмотр:** ежегодно; немедленно после interim update.

### MED-SRC-WHO-BEC

- **Источник:** WHO–ICRC Basic Emergency Care.
- **Аудитория:** клиницисты первого контакта; не бытовой курс.
- **Страница и обновляемые материалы:** <https://www.who.int/publications/i/item/basic-emergency-care-approach-to-the-acutely-ill-and-injured>
- **Состав:** ABCDE, SAMPLE, травма, дыхание, шок, нарушение сознания, передача; базовый manual 2018, слайды обновлены в 2025.
- **Правило архива:** сохранять страницу-комплект и quick cards, а не только старый PDF.
- **Пересмотр:** ежегодно.

### MED-SRC-WHO-ECT

- **Источник:** WHO Emergency Care Toolkit.
- **Аудитория:** CLINICIAN/организация учреждения.
- **Ссылка:** <https://www.who.int/teams/integrated-health-services/clinical-services-and-systems/emergency-and-critical-care/emergency-care-toolkit>
- **Назначение:** триаж, регистрация, маршрутизация, чек-листы и обучение.
- **Пересмотр:** ежегодно.

### MED-SRC-ANZCOR-CRUSH-2025

- **Источник:** ANZCOR Guideline 9.1.7 First Aid Management of Crush Injury, approved 2025-06.
- **Ссылка:** <https://www.anzcor.org/home/first-aid/guideline-9-1-7-first-aid-management-of-crush-injury>
- **Аудитория:** LAY/TRAINED; австралийско-новозеландский сравнительный источник.
- **Статус для Португалии:** `REFERENCE_ONLY` до сверки с португальским курсом/протоколом; используется, чтобы не сохранять устаревший категорический запрет на освобождение.
- **Ключевая граница:** 112 и безопасность зоны; безопасное физически возможное прекращение сдавления не следует намеренно задерживать; турникет только по показанию кровотечения и курсу.

## 3. Инфекции, эпидемии и общественное здоровье

### MED-SRC-WHO-EWAR-2023

- **Источник:** WHO Early Warning, Alert and Response in Emergencies, 2023.
- **Ссылка:** <https://www.who.int/publications/b/61173>
- **Аудитория:** общественное здравоохранение/организаторы.
- **Назначение:** раннее обнаружение вспышек, сигналы, расследование и ответ.
- **Пересмотр:** ежегодно.

### MED-SRC-ECDC-PHSM-2024

- **Источник:** ECDC Public Health and Social Measures for Health Emergencies and Pandemics, 2024.
- **Ссылка:** <https://www.ecdc.europa.eu/en/publications-data/public-health-and-social-measures-health-emergencies-and-pandemics>
- **Аудитория:** органы и организаторы; бытовые карточки адаптируются под текущую угрозу.
- **Пересмотр:** при каждой эпидемии и минимум ежегодно.

### MED-SRC-CDC-IPC

- **Источник:** CDC Core Infection Prevention and Control Practices.
- **Ссылка:** <https://www.cdc.gov/infection-control/hcp/core-practices/>
- **Аудитория:** уход и медицина, включая домашний контекст после адаптации.
- **Пересмотр:** ежегодно и при новой инфекции.

### MED-SRC-WHO-CD-LEGACY

- **Источник:** Communicable Disease Control in Emergencies: A Field Manual, 2005.
- **Ссылка:** <https://www.who.int/publications/i/item/9241546166>
- **Каталог:** `90_LEGACY_DO_NOT_USE_WITHOUT_PATCH`.
- **Назначение:** организация эпидконтроля; лекарства, вакцины и disease-specific схемы считать устаревшими без современных патчей.

## 4. Вода, санитария и инфекционный контроль

### MED-SRC-WHO-WASH-NOTES

- **Источник:** WHO/WEDC Technical Notes on WASH in Emergencies.
- **Ссылка:** <https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/environmental-health-in-emergencies/technical-notes-on-wash-in-emergencies>
- **Аудитория:** полевые техники/организаторы; часть памяток адаптируема для дома.
- **Ограничение:** серия в основном 2011–2013; конкретные дозы реагентов сверять с продуктом и текущими указаниями.
- **Пересмотр:** ежегодно.

### MED-SRC-WHO-GDWQ-2026

- **Источник:** WHO Guidelines for Drinking-water Quality, 4th edition incorporating the first, second and third addenda, 2026.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240121225>
- **Аудитория:** специалисты воды/общественного здоровья.
- **Назначение:** технический эталон микробиологических, химических и радиологических рисков.
- **Проверено:** опубликовано 2026-06-17; заменяет редакцию 2022 с первым и вторым addenda.
- **Правило:** хранить corrigenda/следующие addenda вместе с книгой, прежнюю редакцию перевести в `SUPERSEDED`.

### MED-SRC-WHO-WSP-2023

- **Источник:** WHO Water Safety Plan Manual, 2nd edition, 2023.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240067691>
- **Аудитория:** проектирование и эксплуатация водоснабжения.
- **Пересмотр:** раз в год.

### MED-SRC-WHO-HOUSEHOLD-INSPECTION-2026

- **Источник:** WHO Sanitary Inspection Package: Household Practices, 2026.
- **Ссылка:** <https://www.who.int/publications/m/item/sanitary-inspection-package-%28drinking-water%29--household-practices>
- **Аудитория:** домохозяйство/санитарный контроль.
- **Назначение:** актуальный чек-лист домашних практик питьевой воды.

## 5. Радиационные и химические события

### MED-SRC-CDC-RAD-LAY

- **Источник:** CDC, What to Do in Radiation Emergencies / Preparing for a Radiation Emergency.
- **Ссылка:** <https://www.cdc.gov/radiation-emergencies/response/index.html>
- **Исключения к укрытию:** <https://www.cdc.gov/radiation-emergencies/prevention/index.html>
- **Аудитория:** LAY; американский источник адаптируется к указаниям ANEPC/112.
- **Назначение:** наружный выброс/fallout — get inside, stay inside, stay tuned; не оставаться в горящем/неустойчивом здании или при иной непосредственной угрозе.

### MED-SRC-IAEA-FOUND-SOURCE

- **Источник:** IAEA, public guidance when a potentially dangerous radioactive source/device/package is found.
- **Ссылка:** <https://gnssn.iaea.org/CSN/Scrap/SitePages/Prevention%20and%20Response.aspx>
- **Аудитория:** LAY/industrial awareness.
- **Назначение:** не трогать локальный источник, покинуть непосредственную зону, не допускать других и уведомить экстренные службы; не применять к нему ветку fallout shelter-in-place.

### MED-SRC-CDC-CHEM-CLEAN-2026

- **Источник:** CDC, About Getting Clean, обновлено 2026-06-10.
- **Ссылка:** <https://www.cdc.gov/chemical-emergencies/response/get-clean.html>
- **Аудитория:** LAY; американские номера заменяются на 112/CIAV.
- **Назначение:** после выхода из зоны не ждать определения неизвестного химиката; быстро снять загрязнённую одежду, удалить вещество, вымыться без растирания и получить помощь.
- **Пересмотр:** ежегодно и после обновления CDC/португальских указаний.

### MED-SRC-IAEA-EPR-2024

- **Источник:** IAEA EPR-Medical 2024.
- **PDF:** <https://www-pub.iaea.org/MTCD/Publications/PDF/EPR-Medical%20%282024%29_web.pdf>
- **Аудитория:** SPECIALIST/CLINICIAN.
- **Назначение:** медицинский ответ при ядерной/радиологической аварии; заменяет редакцию 2005.
- **Пересмотр:** ежегодно.

### MED-SRC-REMM

- **Источник:** HHS Radiation Emergency Medical Management.
- **Загрузка:** <https://remm.hhs.gov/download.htm>
- **Мобильная версия:** <https://www.remm.hhs.gov/downloadmremm.htm>
- **Проверено:** Mobile REMM 6.0 (2025); контент сайта обновлялся в 2026.
- **Аудитория:** CLINICIAN/SPECIALIST.
- **Офлайн:** доступны пакеты HTML/PDF/изображений; внешний поиск/ссылки в авиарежиме не работают.
- **Пересмотр:** ежеквартально и после сообщения REMM.

### MED-SRC-CHEMM-2026

- **Источник:** HHS Chemical Hazards Emergency Medical Management.
- **Загрузка:** <https://chemm.hhs.gov/download.htm>
- **Проверено:** версия 2.6, март 2026.
- **Аудитория:** CLINICIAN/SPECIALIST.
- **Офлайн:** Windows/macOS/ZIP; проверить запуск на реальном резервном устройстве.
- **Пересмотр:** ежеквартально.

### MED-SRC-OPCW-CHEM-2019

- **Источник:** OPCW Practical Guide for Medical Management of Chemical Warfare Casualties.
- **Страница:** <https://www.opcw.org/resources/assistance-and-protection/practical-guide-medical-management-chemical-warfare-casualties>
- **Аудитория:** SPECIALIST.
- **Ограничение:** антидоты и инвазивные вмешательства не переносятся в бытовые инструкции.

### MED-SRC-WHO-KI-2017

- **Источник:** WHO Iodine Thyroid Blocking, 2017.
- **Ссылка:** <https://www.who.int/publications/i/item/9789241550185>
- **Аудитория:** органы здравоохранения/клиницисты; населению — только официальная команда.
- **Ключевая граница:** KI защищает только щитовидную железу от радиоактивного йода, не от внешнего излучения и других радионуклидов.

## 6. Материнство, новорождённые и дети

### MED-SRC-WHO-MATERNAL-2025

- **Источник:** WHO Recommendations on Maternal Health, 2nd edition, 2025.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240080591>
- **Аудитория:** CLINICIAN/SPECIALIST.
- **Ограничение:** нормативный клинический слой, не инструкция для самостоятельных родов.

### MED-SRC-WHO-PPH-2025

- **Источник:** WHO/FIGO/ICM Consolidated Guidelines for Postpartum Haemorrhage, 2025.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240115637>
- **Implementation Guide 2026:** <https://www.who.int/publications/i/item/9789240116115>
- **Аудитория:** CLINICIAN/SPECIALIST.
- **Пересмотр:** раз в полгода.

### MED-SRC-WHO-NEWBORN-2022

- **Источник:** WHO Early Essential Newborn Care Pocket Guide, 2nd edition, 2022.
- **Ссылка:** <https://www.who.int/publications/i/item/9789290619659>
- **Аудитория:** обученные специалисты.

### MED-SRC-WHO-CHILD-PATCHES

- **Пневмония и диарея у детей до 10 лет, 2024:** <https://www.who.int/publications/i/item/9789240103412>
- **Тяжёлые бактериальные инфекции 0–59 дней, 2024:** <https://www.who.int/publications/i/item/9789240102903/>
- **Менингит, 2025:** <https://www.who.int/publications/i/item/9789240108042>
- **Правило:** эти источники должны патчить старые педиатрические справочники.

## 7. Психическое здоровье

### MED-SRC-WHO-PFA-RU

- **Источник:** WHO Psychological First Aid: Guide for Field Workers.
- **Русская страница:** <https://www.who.int/europe/ru/publications/i/item/9789241548205>
- **Аудитория:** LAY/TRAINED.
- **Назначение:** гуманная, практическая поддержка; не психотерапия и не принудительный эмоциональный дебрифинг.

### MED-SRC-WHO-DWM-2020

- **Источник:** WHO Doing What Matters in Times of Stress, 2020.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240003927>
- **Аудитория:** LAY; доступны официальные переводы и аудио.

### MED-SRC-WHO-MHGAP-2023

- **Источник:** WHO mhGAP Guideline, 3rd edition, 2023.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240084278>
- **Аудитория:** неспециализированные медработники/организаторы.
- **Ограничение:** не книга самостоятельной диагностики или назначения лекарств.

## 8. Лекарства и лекарственная безопасность

### MED-SRC-WHO-EML-2025

- **Источник:** WHO Model List of Essential Medicines, 24th list, 2025.
- **Ссылка:** <https://www.who.int/publications/i/item/B09474>
- **Детский список, 10th list:** <https://www.who.int/publications/i/item/B09475>
- **Аудитория:** системы здравоохранения/формулярные комиссии.
- **Ключевая граница:** список определяет приоритетные препараты для систем, но не разрешает самоназначение или домашний склад.
- **Цикл:** WHO обычно обновляет список каждые два года.

### MED-SRC-WHO-IEHK-2024

- **Источник:** WHO Interagency Emergency Health Kit 2024.
- **Ссылка:** <https://www.who.int/emergencies/emergency-health-kits/interagency-emergency-health-kit>
- **Аудитория:** гуманитарные организации/системы снабжения.
- **Ограничение:** расчёт на крупное население, не домашняя аптечка; не закрывает все специализированные функции.

### MED-SRC-WHO-AWARE-2022

- **Источник:** WHO AWaRe Antibiotic Book, 2022.
- **Ссылка:** <https://www.who.int/publications/i/item/9789240062382>
- **Аудитория:** CLINICIAN/фармацевтическое управление.
- **Риск устаревания:** WHO обновляет связанные рекомендации; хранить со списком актуальных поправок.
- **Ключевая граница:** самостоятельное применение антибиотиков недопустимо.

### Обязательная карточка любого хранимого лекарства

- национальная инструкция/SmPC;
- действующее вещество, форма и концентрация;
- назначенный пациент и режим;
- партия, срок, дата открытия;
- температура и свет;
- противопоказания и аллергии;
- беременность/лактация;
- взаимодействия;
- статус отзыва;
- законность хранения и отпуска;
- маршрут замены/пополнения.

## 9. Стоматология

### MED-SRC-IADT-2020

- **Источник:** International Association of Dental Traumatology Guidelines 2020.
- **Ссылка:** <https://iadt-dentaltrauma.org/bkk/for-professionals.html>
- **Аудитория:** стоматологи/обученные специалисты; бытовая часть — сохранение зуба и срочный маршрут после адаптации.
- **Пересмотр:** ежегодно.

### MED-SRC-ADA-PAIN-2024

- **Источник:** ADA Evidence-based Guideline for Acute Dental Pain, 2024.
- **Ссылка:** <https://www.ada.org/resources/research/science/evidence-based-dental-research/pain-management-guideline>
- **Ограничение:** обезболивание не заменяет дренирование, лечение инфекции или хирургическую помощь.

### MED-SRC-HESPERIAN-DENT

- **Источник:** Where There Is No Dentist, издательский архив Hesperian; это не официальный актуальный clinical guideline.
- **Ссылка:** <https://languages.hesperian.org/pages/en/pdf.html>
- **Статус:** `REFERENCE_ONLY`, `operational_visibility=false`.
- **Владелец review:** `M3-DENTAL/editor`; до section-level specialist review не индексировать как action source.
- **Ограничение:** инъекции, разрезы и удаления не становятся бытовыми действиями; доступ к книге не создаёт role/scope/gate.

## 10. Метаданные каждого файла

```text
issuer
title
edition_or_date
audience
audience_segments
section_id
page_range
audience_layer
authorized_role
authorized_role_state
credential_id
credential_issuer
credential_expires_at
credential_state
currency_evidence
currency_valid_until
currency_state
scope_of_practice
scope_state
protocol_id
protocol_version
protocol_state
jurisdiction
jurisdiction_state
medical_direction
medical_direction_state
facility
facility_state
equipment
equipment_state
patient_specific_order
patient_specific_order_state
gate_checked_at
gate_checked_by
gate_review_due
gate_decision
canonical_url
download_url
language
retrieved_at
sha256
supersedes
errata_url
review_due
status: CURRENT | CURRENT_WITH_ERRATA | SUPERSEDED | LEGACY_PATCHED | QUARANTINED | REFERENCE_ONLY
operational_visibility: true | false
local_filename
offline_tested_at
printed_revision
```

Это section/action manifest; file-level source manifest может храниться отдельно. Типы, state vocabulary и алгоритм default-deny канонически определены в `03_INVENTORY_SCHEMA_RU.md`; пустое обязательное поле или дата означает `DENY`.

## 11. График актуализации

- **Ежеквартально:** CHEMM/REMM, антибиотические и инфекционные обновления, отзывы лекарств, номера токсикологических центров.
- **Раз в полгода:** акушерство, педиатрия, WASH, стоматология, mental-health corrigenda.
- **Ежегодно:** IFRC/ERC, WHO BEC, официальные переводы, EML/формуляры, локальные португальские протоколы.
- **Немедленно:** новая официальная редакция, локальная вспышка, CBRN-событие, отзыв препарата или распоряжение властей.

Старые файлы не перезаписываются молча: они переводятся в `SUPERSEDED`, получают ссылку на замену и убираются из оперативного каталога. Оригинал на английском хранится вместе с официальными русской, украинской и португальской версиями, если они существуют. Клинические дозы и алгоритмы нельзя считать безопасно переведёнными машинно.

В оперативный поиск по умолчанию попадает только `CURRENT`, а `CURRENT_WITH_ERRATA` — только если проверенный errata-файл поставляется и открывается вместе с документом. `SUPERSEDED`, `LEGACY_PATCHED`, `QUARANTINED` и `REFERENCE_ONLY` имеют `operational_visibility=false`; их можно увидеть лишь в явно включённом редакторском/историческом режиме.
