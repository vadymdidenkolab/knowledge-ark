# QA атласа практической науки v0.4

## Артефакт

- файл: `practical-science-preservation-atlas.xlsx`;
- формат: XLSX;
- sheets: `Overview`, `Domains`, `Packages`, `Projects`, `Instruments`, `Safety Gates`, `Learning Paths`, `Protocol`, `Raw Log`;
- пользовательские CSV-derivatives созданы из тех же канонических строк.

## Состав

| Объект | Строк | Полей |
|---|---:|---:|
| domains | 239 | 16 |
| package candidates | 259 | 38 |
| practical projects | 239 | 29 |
| instruments | 73 | 19 |
| safety gates | 17 | 6 |
| learning paths | 16 | 13 |
| protocol example | 1 | 24 |
| raw-log blank rows | 12 | 17 |

## Проверка формул

- KPI на `Overview` вычисляются формулами из реестров;
- `S3/S4 domains = 15` сверено с 11 `S3` + 4 `S4` строками;
- `Pending acquire/create = 259` сверено как 257 `NOT_DOWNLOADED` + 2 `NOT_CREATED`;
- `High priority ≥70 = 24` вычисляется из формульного score;
- score каждого пакета использует видимые веса `Overview!B18:B28`, входы 0–5 и ограничение 0–100;
- в XLSX находятся 268 формул: 9 KPI на `Overview` и 259 построчных priority score на `Packages`;
- выборочно проверено протягивание формулы `Packages!AK4:AK14` с правильным изменением номера строки;
- поиск `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A` совпадений не нашёл.

Формульный score — triage, а не release gate. Изменение весов требует журнала решения; score не меняет rights/content/safety states.

## Визуальная проверка

Отрендерен и просмотрен каждый из девяти sheets:

- title/subtitle видимы;
- header rows контрастны;
- перенос текста включён;
- критические KPI и no-go выделены;
- строки и столбцы не выходят за используемый диапазон;
- нет пустого default sheet;
- wide registers читаются с горизонтальной прокруткой и замороженной header row;
- `Safety Gates` выделяет запреты красным фоном;
- `Raw Log` содержит пустые observation slots и отдельные unit columns;
- `Protocol` явно помечен `NOT_RUN`.

## CSV QA

- все восемь CSV разбираются стандартным CSV parser;
- UTF-8, LF и RFC4180-style quoting;
- ширина каждой data row равна header;
- primary IDs заполнены и уникальны;
- package: 259/259 `CANDIDATE`, `NOT_REVIEWED`, `NOT_TESTED`; 257/259 `NOT_DOWNLOADED`, 2/259 local-authoring `NOT_CREATED`;
- domains: 239/239 `FRAMEWORK_ONLY_NOT_TRAINED`;
- projects: 239/239 `DESIGN_ONLY_NOT_EXECUTED`, provisional topic bindings и blocked execution gate;
- instruments: 73/73 `CANDIDATE_NOT_INVENTORIED`;
- внешние hash/local path/retrieved date сознательно пусты.

## Проверенные отрицательные утверждения

- external payload downloaded: 0;
- projects executed: 0;
- people trained: 0;
- instruments inventoried/calibrated: 0 подтверждённых;
- rights-cleared packages: 0 заявленных;
- offline-opened external packages: 0;
- professional authorizations: 0 заявленных.

## Открытые границы

1. URL transport/content повторно проверяется перед acquisition; веб-страница может измениться.
2. Rights precheck не является юридическим заключением.
3. Дополнительные research rows нормализованы в единую S0–S4 модель, но exact item review ещё не проведён.
4. Нет Portuguese municipality/site/person/asset personalization.
5. Нет реальной instrument calibration chain.
6. Нет clean-device restore внешнего научного payload.
7. XLSX — удобный интерфейс; канонические CSV и Markdown нужны как более простые долговременные представления.
