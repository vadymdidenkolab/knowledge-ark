---
id: "DATA-REGISTER-ee4aee2592dadc5e"
type: "generated-data-register-view"
title: "Манифест офлайн-корпуса"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "offline-corpus-manifest.csv"
source_sha256: "50bf481837c37ad62b439412a538d761b2aba39e39ab8c557b819756f0bc470c"
source_bytes: 52456
source_row_count: 79
source_column_count: 37
source_cell_count: 2923
ignored_blank_row_count: 0
semantic_group: "OFFLINE_KNOWLEDGE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: offline-corpus-manifest.csv -->

# Манифест офлайн-корпуса

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Источники, архив и офлайн-библиотека
- **Записей:** 79
- **Полей в каждой записи:** 37
- **Ячеек данных, включая пустые:** 2923
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `50bf481837c37ad62b439412a538d761b2aba39e39ab8c557b819756f0bc470c`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | «package» ID | <code>&quot;package_id&quot;</code> |
| 2 | Приоритет | <code>&quot;priority_tier&quot;</code> |
| 3 | «category» | <code>&quot;category&quot;</code> |
| 4 | «subcategory» | <code>&quot;subcategory&quot;</code> |
| 5 | Название | <code>&quot;title&quot;</code> |
| 6 | Издатель | <code>&quot;publisher&quot;</code> |
| 7 | «languages» | <code>&quot;languages&quot;</code> |
| 8 | Юрисдикция | <code>&quot;jurisdiction&quot;</code> |
| 9 | Канонический адрес в сети | <code>&quot;canonical_url&quot;</code> |
| 10 | Адрес получения | <code>&quot;acquisition_url&quot;</code> |
| 11 | «distribution» формат | <code>&quot;distribution_format&quot;</code> |
| 12 | «reader» «or» «runtime» | <code>&quot;reader_or_runtime&quot;</code> |
| 13 | «size» класс | <code>&quot;size_class&quot;</code> |
| 14 | Лицензия «expression» | <code>&quot;license_expression&quot;</code> |
| 15 | Лицензия адрес в сети | <code>&quot;license_url&quot;</code> |
| 16 | Лицензия проверка состояние | <code>&quot;license_review_state&quot;</code> |
| 17 | «redistribution» состояние | <code>&quot;redistribution_state&quot;</code> |
| 18 | «attribution» требуемый | <code>&quot;attribution_required&quot;</code> |
| 19 | Полномочие класс | <code>&quot;authority_class&quot;</code> |
| 20 | Класс безопасности | <code>&quot;safety_class&quot;</code> |
| 21 | «content» проверка состояние | <code>&quot;content_review_state&quot;</code> |
| 22 | «section» проверка состояние | <code>&quot;section_review_state&quot;</code> |
| 23 | «download» состояние | <code>&quot;download_state&quot;</code> |
| 24 | «downloaded» версия | <code>&quot;downloaded_version&quot;</code> |
| 25 | «retrieved» время | <code>&quot;retrieved_at&quot;</code> |
| 26 | Локальный путь | <code>&quot;local_path&quot;</code> |
| 27 | Размер в байтах | <code>&quot;byte_size&quot;</code> |
| 28 | Хеш SHA-256 | <code>&quot;sha256&quot;</code> |
| 29 | «upstream» «checksum» состояние | <code>&quot;upstream_checksum_state&quot;</code> |
| 30 | «malware» «scan» состояние | <code>&quot;malware_scan_state&quot;</code> |
| 31 | Офлайн «open» состояние | <code>&quot;offline_open_state&quot;</code> |
| 32 | «search» «index» состояние | <code>&quot;search_index_state&quot;</code> |
| 33 | «update» класс | <code>&quot;update_class&quot;</code> |
| 34 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 35 | «retention» класс | <code>&quot;retention_class&quot;</code> |
| 36 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 37 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:37 -->
> [!abstract]- Запись 1 из 79 — PKG-KIWIX-READERS — Kiwix Reader and Server
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-KIWIX-READERS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L0&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OFFLINE_READER&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Kiwix Reader and Server&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://get.kiwix.org/en/solutions/applications/download-options/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://get.kiwix.org/en/solutions/applications/download-options/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;BINARIES_SOURCE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;OS_SPECIFIC&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;OPEN_SOURCE_COMPONENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://github.com/kiwix&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_GENERAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Контент каждого ZIM лицензируется отдельно&quot;</code>
>

<!-- record:2 cells:37 -->
> [!abstract]- Запись 2 из 79 — PKG-KIWIX-CATALOG — Kiwix library catalog
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-KIWIX-CATALOG&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CATALOG&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;ZIM_OPDS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Kiwix library catalog&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/catalog/v2/root.xml&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;OPDS_XML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CATALOG_AND_CONTENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://library.kiwix.org/catalog/v2/root.xml&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_GENERAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Каталог не является content review&quot;</code>
>

<!-- record:3 cells:37 -->
> [!abstract]- Запись 3 из 79 — PKG-OPENZIM-LIBZIM — libzim reference implementation
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-OPENZIM-LIBZIM&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;ZIM_RUNTIME_SOURCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;libzim reference implementation&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;openZIM&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://github.com/openzim/libzim&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://github.com/openzim/libzim&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;SOURCE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;CXX_BUILD&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;GPL-2.0-or-later&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://github.com/openzim/libzim/blob/main/COPYING&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_GENERAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:4 cells:37 -->
> [!abstract]- Запись 4 из 79 — PKG-WIKIPEDIA-EN-MINI — Wikipedia English mini or nopic ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-EN-MINI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MINI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia English mini or nopic ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Не operational medical or legal source&quot;</code>
>

<!-- record:5 cells:37 -->
> [!abstract]- Запись 5 из 79 — PKG-WIKIPEDIA-RU-MINI — Wikipedia Russian mini or nopic ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-RU-MINI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MINI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia Russian mini or nopic ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:6 cells:37 -->
> [!abstract]- Запись 6 из 79 — PKG-WIKIPEDIA-PT-MINI — Wikipedia Portuguese mini or nopic ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-PT-MINI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MINI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia Portuguese mini or nopic ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:7 cells:37 -->
> [!abstract]- Запись 7 из 79 — PKG-WIKIPEDIA-EN-MAXI — Wikipedia English full with media ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-EN-MAXI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MAXI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia English full with media ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:8 cells:37 -->
> [!abstract]- Запись 8 из 79 — PKG-WIKIPEDIA-RU-MAXI — Wikipedia Russian full with media ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-RU-MAXI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MAXI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia Russian full with media ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:9 cells:37 -->
> [!abstract]- Запись 9 из 79 — PKG-WIKIPEDIA-PT-MAXI — Wikipedia Portuguese full with media ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIPEDIA-PT-MAXI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENCYCLOPEDIA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIPEDIA_MAXI&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikipedia Portuguese full with media ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_AND_GFDL_MEDIA_PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ENCYCLOPEDIA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_TO_12_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:10 cells:37 -->
> [!abstract]- Запись 10 из 79 — PKG-WIKTIONARY-EN — Wiktionary English ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKTIONARY-EN&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LANGUAGE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;DICTIONARY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wiktionary English ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_GFDL_PER_PROJECT&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_DICTIONARY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:11 cells:37 -->
> [!abstract]- Запись 11 из 79 — PKG-WIKTIONARY-RU — Wiktionary Russian ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKTIONARY-RU&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LANGUAGE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;DICTIONARY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wiktionary Russian ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_GFDL_PER_PROJECT&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_DICTIONARY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:12 cells:37 -->
> [!abstract]- Запись 12 из 79 — PKG-WIKTIONARY-PT — Wiktionary Portuguese ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKTIONARY-PT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LANGUAGE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;DICTIONARY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wiktionary Portuguese ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA_GFDL_PER_PROJECT&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_DICTIONARY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:13 cells:37 -->
> [!abstract]- Запись 13 из 79 — PKG-WIKIBOOKS — Selected Wikibooks RU PT EN
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIBOOKS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EDUCATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKIBOOKS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected Wikibooks RU PT EN&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU|PT|EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM_XML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX_OR_EXTRACTOR&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PROJECT_AND_ITEM_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_EDUCATION&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:14 cells:37 -->
> [!abstract]- Запись 14 из 79 — PKG-WIKISOURCE — Selected Wikisource RU PT EN
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKISOURCE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WIKISOURCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected Wikisource RU PT EN&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU|PT|EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM_XML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX_OR_EXTRACTOR&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;TEXT_AND_SOURCE_WORK_RIGHTS_SEPARATE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_CULTURE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Portugal EU public-domain check per work and translation&quot;</code>
>

<!-- record:15 cells:37 -->
> [!abstract]- Запись 15 из 79 — PKG-WIKIVOYAGE — Wikivoyage RU PT EN ZIM
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIVOYAGE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;NAVIGATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;TRAVEL_REFERENCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikivoyage RU PT EN ZIM&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia via Kiwix&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU|PT|EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://library.kiwix.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ZIM&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;KIWIX&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-SA&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_TRAVEL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DYNAMIC_REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Addresses borders and services can be stale&quot;</code>
>

<!-- record:16 cells:37 -->
> [!abstract]- Запись 16 из 79 — PKG-WIKIDATA-DUMP — Wikidata entity dumps
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIDATA-DUMP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;DATA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;KNOWLEDGE_GRAPH&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikidata entity dumps&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/wikidatawiki/entities/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/wikidatawiki/entities/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;JSON_BZ2&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;CUSTOM_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC0_DATA_WITH_ITEM_EXCEPTIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.wikidata.org/wiki/Wikidata:Licensing&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_DATA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:17 cells:37 -->
> [!abstract]- Запись 17 из 79 — PKG-WIKIMEDIA-DUMPS — Wikimedia database backup dumps
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WIKIMEDIA-DUMPS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;RAW_PROJECT_DUMPS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Wikimedia database backup dumps&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Wikimedia&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/backup-index.html&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://dumps.wikimedia.org/backup-index.html&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;XML_BZ2_GZ_SQL&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;CUSTOM_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PROJECT_AND_MEDIA_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;COMMUNITY_ARCHIVE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:18 cells:37 -->
> [!abstract]- Запись 18 из 79 — PKG-GUTENBERG — Project Gutenberg selected books
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-GUTENBERG&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PUBLIC_DOMAIN_BOOKS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Project Gutenberg selected books&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Project Gutenberg&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_CATALOG_PT_EU_REVIEW&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.gutenberg.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.gutenberg.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;EPUB_HTML_TXT&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;EPUB_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;US_PUBLIC_DOMAIN_ITEM_AND_TRADEMARK_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.gutenberg.org/policy/license&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;CULTURAL_REPOSITORY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_ITEM&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Portugal EU rights check required&quot;</code>
>

<!-- record:19 cells:37 -->
> [!abstract]- Запись 19 из 79 — PKG-STANDARD-EBOOKS — Standard Ebooks selected titles
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-STANDARD-EBOOKS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;CURATED_EBOOKS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Standard Ebooks selected titles&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Standard Ebooks&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_CATALOG_PT_EU_REVIEW&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://standardebooks.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://standardebooks.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;EPUB&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;EPUB_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PUBLIC_DOMAIN_AND_PROJECT_TERMS_PER_TITLE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://standardebooks.org/about/colophon&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;CULTURAL_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_ITEM&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Check author translation illustration rights in Portugal EU&quot;</code>
>

<!-- record:20 cells:37 -->
> [!abstract]- Запись 20 из 79 — PKG-OPENSTAX — Selected OpenStax textbooks
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-OPENSTAX&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EDUCATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;TEXTBOOKS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected OpenStax textbooks&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;OpenStax&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://openstax.org/subjects&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://openstax.org/subjects&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_EPUB&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_EPUB_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_TITLE_OFTEN_CC-BY-NC-SA-4.0&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;EDUCATION_PUBLISHER&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_EDUCATION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_EDITION&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:21 cells:37 -->
> [!abstract]- Запись 21 из 79 — PKG-MIT-OCW — Selected MIT OpenCourseWare
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-MIT-OCW&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EDUCATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;COURSEWARE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected MIT OpenCourseWare&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;MIT&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://ocw.mit.edu/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://ocw.mit.edu/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF_VIDEO&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_MEDIA_PLAYER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-NC-SA-4.0_WITH_EXCLUSIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://ocw.mit.edu/pages/privacy-and-terms-of-use/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;UNIVERSITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_EDUCATION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_COURSE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:22 cells:37 -->
> [!abstract]- Запись 22 из 79 — PKG-PHET — PhET regular HTML5 simulations
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PHET&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EDUCATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;SIMULATIONS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;PhET regular HTML5 simulations&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;University of Colorado Boulder&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://phet.colorado.edu/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://phet.colorado.edu/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML5&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CC-BY-NC-4.0_REGULAR_SIMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://phet.colorado.edu/en/licensing&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;UNIVERSITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_EDUCATION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;PhET-iO and Studio excluded&quot;</code>
>

<!-- record:23 cells:37 -->
> [!abstract]- Запись 23 из 79 — PKG-KOLIBRI — Kolibri offline learning platform
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-KOLIBRI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OFFLINE_LEARNING&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Kolibri offline learning platform&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Learning Equality&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://learningequality.org/kolibri/about-kolibri/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://learningequality.org/kolibri/about-kolibri/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;BINARIES_SOURCE_CHANNELS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;LOCAL_SERVER_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;SOFTWARE_OPEN_SOURCE_CONTENT_PER_CHANNEL&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://github.com/learningequality/kolibri&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_NONPROFIT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_EDUCATION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:24 cells:37 -->
> [!abstract]- Запись 24 из 79 — PKG-WHO-PUBLICATIONS — Selected WHO current publications
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WHO-PUBLICATIONS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WHO_PUBLICATIONS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected WHO current publications&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;WHO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.who.int/publications&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.who.int/publications&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ITEM_OFTEN_CC-BY-NC-SA-3.0-IGO_POST_2016&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.who.int/about/policies/publishing/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Third-party material and translation rules per item&quot;</code>
>

<!-- record:25 cells:37 -->
> [!abstract]- Запись 25 из 79 — PKG-WHO-IRIS — WHO IRIS selected repository packages
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WHO-IRIS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WHO_REPOSITORY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;WHO IRIS selected repository packages&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;WHO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://iris.who.int/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://iris.who.int/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.who.int/about/policies/publishing/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:26 cells:37 -->
> [!abstract]- Запись 26 из 79 — PKG-WHO-EUROPE-RU — WHO Europe official Russian publications
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WHO-EUROPE-RU&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OFFICIAL_RUSSIAN&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;WHO Europe official Russian publications&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;WHO Europe&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EUROPE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.who.int/europe/ru/publications&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.who.int/europe/ru/publications&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.who.int/about/policies/publishing/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:27 cells:37 -->
> [!abstract]- Запись 27 из 79 — PKG-DGS-PT — Selected current DGS guidance
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DGS-PT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PORTUGAL_HEALTH_GUIDANCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected current DGS guidance&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Direção-Geral da Saúde&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.dgs.pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.dgs.pt/normas-orientacoes-e-informacoes/normas-e-circulares-normativas&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;URL_METADATA_ONLY&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_WHEN_NETWORK_RETURNS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;ALL_RIGHTS_RESERVED_PERMISSION_OR_LEGAL_BASIS_REQUIRED&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.dgs.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;YES_IF_AUTHORIZED&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_MEDICAL_CURRENTNESS_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_METADATA_AND_RIGHTS_EVIDENCE&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_METADATA_ONLY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Payload запрещён до сохранённого разрешения или конкретного правового основания&quot;</code>
>

<!-- record:28 cells:37 -->
> [!abstract]- Запись 28 из 79 — PKG-INFARMED — INFARMED medicine and safety information
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-INFARMED&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;MEDICINES_REGULATOR&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;INFARMED medicine and safety information&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;INFARMED&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.infarmed.pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://extranet.infarmed.pt/INFOMED-fo/guia-condicoes-utilizacao.xhtml&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;URL_METADATA_ONLY&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_WHEN_NETWORK_RETURNS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;REPRODUCTION_REQUIRES_WRITTEN_PERMISSION&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://extranet.infarmed.pt/INFOMED-fo/guia-condicoes-utilizacao.xhtml&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;YES_IF_AUTHORIZED&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_REGULATOR&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_MEDICAL_CURRENTNESS_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_METADATA_AND_RIGHTS_EVIDENCE&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_METADATA_ONLY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Infomed terms explicitly prohibit reproduction without written permission; no payload in offline corpus until evidence&quot;</code>
>

<!-- record:29 cells:37 -->
> [!abstract]- Запись 29 из 79 — PKG-ECDC — Selected current ECDC publications and datasets
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-ECDC&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PUBLIC_HEALTH&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected current ECDC publications and datasets&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;ECDC&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.ecdc.europa.eu/en/publications-data&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.ecdc.europa.eu/en/publications-data&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_CSV_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_SPREADSHEET_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;EU_REUSE_WITH_ITEM_EXCEPTIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.ecdc.europa.eu/en/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;EU_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PUBLIC_HEALTH_CURRENTNESS_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:30 cells:37 -->
> [!abstract]- Запись 30 из 79 — PKG-ERC-GUIDELINES — Current European Resuscitation Council guidelines
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-ERC-GUIDELINES&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;RESUSCITATION&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Current European Resuscitation Council guidelines&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;ERC&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.erc.edu/science-research/guidelines/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.erc.edu/science-research/guidelines/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;RIGHTS_REVIEW_REQUIRED&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.erc.edu/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;PROFESSIONAL_BODY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;TRAINING_AND_LOCAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_NEW_GUIDELINE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:31 cells:37 -->
> [!abstract]- Запись 31 из 79 — PKG-CDC-PUBLIC — Selected CDC public guidance
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-CDC-PUBLIC&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MEDICAL&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PUBLIC_GUIDANCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected CDC public guidance&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;CDC&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_REFERENCE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.cdc.gov/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.cdc.gov/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;US_GOV_WITH_THIRD_PARTY_EXCEPTIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.cdc.gov/other/agencymaterials.html&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_APPLICABILITY_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;QUARTERLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:32 cells:37 -->
> [!abstract]- Запись 32 из 79 — PKG-FAO-REPOSITORY — Selected FAO Knowledge Repository publications
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-FAO-REPOSITORY&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRICULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;FAO_KNOWLEDGE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected FAO Knowledge Repository publications&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;FAO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://openknowledge.fao.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://openknowledge.fao.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ITEM_OFTEN_CC-BY-NC-SA-3.0-IGO&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.fao.org/publications/about-fao-publishing/permissions/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_WITH_LOCAL_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:33 cells:37 -->
> [!abstract]- Запись 33 из 79 — PKG-FAO-AGRIS — AGRIS metadata and permitted full-text links
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-FAO-AGRIS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRICULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;BIBLIOGRAPHY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;AGRIS metadata and permitted full-text links&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;FAO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://agris.fao.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://agris.fao.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;METADATA_FULLTEXT_LINKS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_DATABASE&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;METADATA_AND_FULLTEXT_RIGHTS_SEPARATE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.fao.org/knowledge-sharing/en&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_METADATA&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DISCOVERY_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:34 cells:37 -->
> [!abstract]- Запись 34 из 79 — PKG-FAO-GENEBANK — FAO Genebank Standards
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-FAO-GENEBANK&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;AGRICULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;SEEDS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;FAO Genebank Standards&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;FAO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.fao.org/4/i3394e/i3394e.pdf&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.fao.org/4/i3394e/i3394e.pdf&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_PUBLICATION_REVIEW&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.fao.org/publications/about-fao-publishing/permissions/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_NEW_EDITION&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:35 cells:37 -->
> [!abstract]- Запись 35 из 79 — PKG-WHO-WATER-SAFETY — WHO Water Safety Plan Manual second edition
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-WHO-WATER-SAFETY&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;WATER&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WATER_SAFETY_PLAN&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;WHO Water Safety Plan Manual second edition&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;WHO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.who.int/publications/i/item/9789240067691&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.who.int/publications/i/item/9789240067691&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ITEM_WHO&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.who.int/about/policies/publishing/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_LOCAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_NEW_EDITION&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:36 cells:37 -->
> [!abstract]- Запись 36 из 79 — PKG-NCHFP — National Center for Home Food Preservation
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-NCHFP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;FOOD&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;HOME_PRESERVATION&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;National Center for Home Food Preservation&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;University of Georgia USDA partners&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_REFERENCE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://nchfp.uga.edu/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://nchfp.uga.edu/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;RIGHTS_PER_PAGE_PUBLICATION&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://nchfp.uga.edu/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;UNIVERSITY_EXTENSION&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_FOOD_SAFETY_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:37 cells:37 -->
> [!abstract]- Запись 37 из 79 — PKG-HSE-SAFETY — Selected HSE safety guidance
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-HSE-SAFETY&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENGINEERING&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WORK_SAFETY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected HSE safety guidance&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;UK Health and Safety Executive&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;UK_REFERENCE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.hse.gov.uk/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.hse.gov.uk/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;UK_CROWN_COPYRIGHT_WITH_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.hse.gov.uk/help/copyright.htm&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_LAW_AND_COMPETENCE_REVIEW&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:38 cells:37 -->
> [!abstract]- Запись 38 из 79 — PKG-NIST — Selected NIST technical publications and software
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-NIST&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ENGINEERING&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;TECHNICAL_PUBLICATIONS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Selected NIST technical publications and software&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;NIST&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_REFERENCE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.nist.gov/publications&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.nist.gov/publications&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_DATA_SOFTWARE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;MIXED&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;US_GOV_AND_COMPONENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_STANDARDS_BODY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_GENERAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:39 cells:37 -->
> [!abstract]- Запись 39 из 79 — PKG-OSM-PLANET — OpenStreetMap planet or selected extracts
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-OSM-PLANET&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OPENSTREETMAP_DATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;OpenStreetMap planet or selected extracts&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;OpenStreetMap contributors&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://planet.openstreetmap.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://planet.openstreetmap.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PBF_XML_DIFFS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;ODbL-1.0&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.openstreetmap.org/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_DATA_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;MAP_DATA_NOT_ROUTE_PROOF&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Do not bulk mirror standard tile.openstreetmap.org tiles&quot;</code>
>

<!-- record:40 cells:37 -->
> [!abstract]- Запись 40 из 79 — PKG-GEOFABRIK-PT — Portugal OpenStreetMap extract
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-GEOFABRIK-PT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OSM_PORTUGAL_EXTRACT&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Portugal OpenStreetMap extract&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Geofabrik based on OSM&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://download.geofabrik.de/europe/portugal.html&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://download.geofabrik.de/europe/portugal.html&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PBF_SHP&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;ODbL-1.0&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.openstreetmap.org/copyright&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_DATA_DISTRIBUTOR&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;MAP_DATA_NOT_ROUTE_PROOF&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:41 cells:37 -->
> [!abstract]- Запись 41 из 79 — PKG-NATURAL-EARTH — Natural Earth vector and raster data
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-NATURAL-EARTH&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;GLOBAL_BASEMAP&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Natural Earth vector and raster data&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Natural Earth&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.naturalearthdata.com/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.naturalearthdata.com/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;SHP_GEOPACKAGE_RASTER&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PUBLIC_DOMAIN&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.naturalearthdata.com/about/terms-of-use/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_DATA_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;OVERVIEW_NOT_LOCAL_NAVIGATION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:42 cells:37 -->
> [!abstract]- Запись 42 из 79 — PKG-SNIG-RNDG — SNIG RNDG official geodata catalog
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-SNIG-RNDG&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PORTUGAL_GEODATA_CATALOG&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;SNIG RNDG official geodata catalog&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Direção-Geral do Território&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/saber-mais/registo-nacional-de-dados-geograficos&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/saber-mais/registo-nacional-de-dados-geograficos&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;METADATA_OGC_DATASET_SPECIFIC&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_DATASET&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://snig.dgterritorio.gov.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DATASET_AND_LICENSE_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:43 cells:37 -->
> [!abstract]- Запись 43 из 79 — PKG-CAOP — Carta Administrativa Oficial de Portugal
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-CAOP&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;ADMIN_BOUNDARIES&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Carta Administrativa Oficial de Portugal&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;DGT&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.dgterritorio.gov.pt/atividades/cartografia/cartografia-tematica/caop&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.dgterritorio.gov.pt/atividades/cartografia/cartografia-tematica/caop&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;GIS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;OFFICIAL_DATASET_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.dgterritorio.gov.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;MAP_DATA_NOT_HAZARD_STATUS&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:44 cells:37 -->
> [!abstract]- Запись 44 из 79 — PKG-APA-PGRI — Portugal flood risk planning layers
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-APA-PGRI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;FLOOD_RISK&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Portugal flood risk planning layers&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Agência Portuguesa do Ambiente&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT_CONTINENTAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://apambiente.pt/agua/2o-ciclo-de-planeamento-2022-2027&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://apambiente.pt/agua/2o-ciclo-de-planeamento-2022-2027&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;GIS_PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;OFFICIAL_DATASET_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://apambiente.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;HAZARD_MAP_NOT_LIVE_EVENT&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;6_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:45 cells:37 -->
> [!abstract]- Запись 45 из 79 — PKG-ICNF-FIRE — ICNF wildfire and forestry geodata
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-ICNF-FIRE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WILDFIRE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;ICNF wildfire and forestry geodata&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;ICNF&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT_CONTINENTAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://geocatalogo.icnf.pt/catalogo_tema5.html&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://geocatalogo.icnf.pt/catalogo_tema5.html&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;GIS_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_DATASET&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.icnf.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;STRUCTURAL_RISK_NOT_ACTIVE_FIRE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;SEASONAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:46 cells:37 -->
> [!abstract]- Запись 46 из 79 — PKG-IPMA — IPMA selected climate seismic and tsunami materials
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-IPMA&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CLIMATE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;WEATHER_SEISMIC&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;IPMA selected climate seismic and tsunami materials&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;IPMA&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.ipma.pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.ipma.pt/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_DATA_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;MIXED&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;OFFICIAL_SOURCE_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.ipma.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DYNAMIC_SNAPSHOT&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;EVENT_AND_ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:47 cells:37 -->
> [!abstract]- Запись 47 из 79 — PKG-LNEG — LNEG geoscience datasets
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-LNEG&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MAPS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;GEOLOGY_HYDROGEOLOGY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;LNEG geoscience datasets&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;LNEG&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://geoportal.lneg.pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://geoportal.lneg.pt/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;GIS_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;GIS_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_DATASET&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://geoportal.lneg.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_LAB&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REGIONAL_MAP_NOT_SITE_ASSESSMENT&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:48 cells:37 -->
> [!abstract]- Запись 48 из 79 — PKG-COPERNICUS-CLIMATE — Copernicus Climate Data Store selected datasets
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-COPERNICUS-CLIMATE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CLIMATE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;CLIMATE_DATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Copernicus Climate Data Store selected datasets&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;ECMWF Copernicus&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU_GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://cds.climate.copernicus.eu/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://cds.climate.copernicus.eu/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;NETCDF_GRIB_CSV&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;SCIENTIFIC_GIS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;COPERNICUS_LICENSE_PER_DATASET&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://cds.climate.copernicus.eu/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;EU_SERVICE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PROFESSIONAL_INTERPRETATION_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_DATASET_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:49 cells:37 -->
> [!abstract]- Запись 49 из 79 — PKG-IPCC-AR6 — IPCC Sixth Assessment Report
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-IPCC-AR6&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CLIMATE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;ASSESSMENT&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;IPCC Sixth Assessment Report&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;IPCC&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.ipcc.ch/report/sixth-assessment-report-cycle/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.ipcc.ch/report/sixth-assessment-report-cycle/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_DATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;IPCC_COPYRIGHT_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.ipcc.ch/copyright/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_ASSESSMENT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;SCENARIO_NOT_ADDRESS_PREDICTION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_ASSESSMENT&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:50 cells:37 -->
> [!abstract]- Запись 50 из 79 — PKG-EURLEX-BULK — EUR-Lex bulk legal acts and Official Journal packages
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-EURLEX-BULK&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LAW&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;EU_LAW&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;EUR-Lex bulk legal acts and Official Journal packages&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Publications Office of the EU&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://eur-lex.europa.eu/content/help/data-reuse/reuse-contents-eurlex-details.html?locale=en&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://eur-lex.europa.eu/content/help/data-reuse/reuse-contents-eurlex-details.html?locale=en&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;FORMEX_XML_XHTML_PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_XML_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;EU_REUSE_CONDITIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://commission.europa.eu/legal-notice_en&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;EU_OFFICIAL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;CURRENTNESS_REQUIRED_ONLY_OJ_AUTHENTIC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:51 cells:37 -->
> [!abstract]- Запись 51 из 79 — PKG-DRE-PT — Diário da República selected consolidated and official acts
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DRE-PT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LAW&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PORTUGAL_LAW&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Diário da República selected consolidated and official acts&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Diário da República&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://diariodarepublica.pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://diariodarepublica.pt/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;URL_METADATA_ONLY&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_WHEN_NETWORK_RETURNS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PORTUGAL_OFFICIAL_REUSE_REVIEW&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://diariodarepublica.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;NO_UNTIL_AUTHORIZED&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_OFFICIAL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LOCAL_LAW_CURRENTNESS_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;DO_NOT_INGEST&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_METADATA_AND_RIGHTS_EVIDENCE&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_METADATA_ONLY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Payload запрещён до сохранённого разрешения или конкретного правового основания; офлайн-копия не доказывает текущую редакцию&quot;</code>
>

<!-- record:52 cells:37 -->
> [!abstract]- Запись 52 из 79 — PKG-DADOS-PT — dados.gov.pt selected datasets
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DADOS-PT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;DATA&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PORTUGAL_OPEN_DATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;dados.gov.pt selected datasets&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;AMA and dataset publishers&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://dados.gov.pt/pt/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://dados.gov.pt/pt/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;CSV_JSON_API_DATASET_SPECIFIC&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;MIXED&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_DATASET_OPEN_LICENSE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://dados.gov.pt/pt/termos-de-utilizacao&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;GOVERNMENT_PORTAL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DATASET_SPECIFIC&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_DATASET&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:53 cells:37 -->
> [!abstract]- Запись 53 из 79 — PKG-PT-PREDIAL — Portugal property registry and BUPi procedures
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PT-PREDIAL&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LAW&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PROPERTY_REGISTRY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Portugal property registry and BUPi procedures&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Justiça.gov.pt&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;PT&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://justica.gov.pt/Registos/Predial&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://justica.gov.pt/Registos/Predial&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF_FORMS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;OFFICIAL_SITE_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://justica.gov.pt/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_OFFICIAL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;CURRENTNESS_AND_LEGAL_REVIEW_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:54 cells:37 -->
> [!abstract]- Запись 54 из 79 — PKG-EU-EJUSTICE-INHERITANCE — European e-Justice inheritance information
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-EU-EJUSTICE-INHERITANCE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;LAW&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;SUCCESSION&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;European e-Justice inheritance information&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;European Commission&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://e-justice.europa.eu/topics/family-matters-inheritance/inheritance_en&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://e-justice.europa.eu/topics/family-matters-inheritance/inheritance_en&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;EU_REUSE_CONDITIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://commission.europa.eu/legal-notice_en&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;EU_OFFICIAL&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;LEGAL_ADVICE_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:55 cells:37 -->
> [!abstract]- Запись 55 из 79 — PKG-RFC-CORPUS — RFC Editor complete series
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-RFC-CORPUS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;STANDARDS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;INTERNET_RFC&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;RFC Editor complete series&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;RFC Editor IETF Trust&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.rfc-editor.org/series/rfc-download/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.rfc-editor.org/series/rfc-download/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;TXT_XML_PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;TEXT_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;IETF_TRUST_LEGAL_PROVISIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://trustee.ietf.org/documents/trust-legal-provisions/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;STANDARDS_PUBLISHER&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TECHNICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:56 cells:37 -->
> [!abstract]- Запись 56 из 79 — PKG-DEBIAN-ISO — Debian stable installation images and checksums
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DEBIAN-ISO&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OS_INSTALLER&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Debian stable installation images and checksums&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Debian Project&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.debian.org/distrib/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.debian.org/distrib/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;ISO_CHECKSUM_SIGNATURE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BOOTABLE_MEDIA&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;DFSG_AND_PER_PACKAGE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.debian.org/legal/licenses/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;RESTORE_SOFTWARE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_STABLE_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:57 cells:37 -->
> [!abstract]- Запись 57 из 79 — PKG-DEBIAN-MAIN — Debian main selected architecture mirror
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DEBIAN-MAIN&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L3&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PACKAGE_REPOSITORY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Debian main selected architecture mirror&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Debian Project&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.debian.org/mirror/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.debian.org/mirror/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;DEB_SOURCE_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;APT&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;DFSG_PER_PACKAGE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.debian.org/legal/licenses/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;RESTORE_SOFTWARE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;SECURITY_MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:58 cells:37 -->
> [!abstract]- Запись 58 из 79 — PKG-DEBIAN-SNAPSHOT — Debian Snapshot selected reproducible package set
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-DEBIAN-SNAPSHOT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;HISTORICAL_PACKAGES&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Debian Snapshot selected reproducible package set&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Debian Project&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://snapshot.debian.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://snapshot.debian.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;DEB_SOURCE_METADATA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;APT&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_PACKAGE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.debian.org/legal/licenses/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;HISTORICAL_NOT_SECURE_BY_DEFAULT&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PINNED_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:59 cells:37 -->
> [!abstract]- Запись 59 из 79 — PKG-TESSERACT — Tesseract OCR and language data
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-TESSERACT&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OCR&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Tesseract OCR and language data&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Tesseract contributors&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://tesseract-ocr.github.io/tessdoc/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://tesseract-ocr.github.io/tessdoc/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;BINARIES_SOURCE_MODELS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;OS_SPECIFIC&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;APACHE-2.0_COMPONENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TOOL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:60 cells:37 -->
> [!abstract]- Запись 60 из 79 — PKG-APACHE-TIKA — Apache Tika binaries source and docs
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-APACHE-TIKA&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;TEXT_EXTRACTION&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Apache Tika binaries source and docs&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Apache Software Foundation&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://tika.apache.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://tika.apache.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;JAR_SOURCE_DOCS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;JAVA&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;APACHE-2.0&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.apache.org/licenses/LICENSE-2.0&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_FOUNDATION&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TOOL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:61 cells:37 -->
> [!abstract]- Запись 61 из 79 — PKG-CALIBRE — calibre reader and source
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-CALIBRE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;EBOOK_READER&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;calibre reader and source&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;calibre contributors&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://calibre-ebook.com/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://calibre-ebook.com/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;BINARIES_SOURCE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;OS_SPECIFIC&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;GPL-3.0_COMPONENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://github.com/kovidgoyal/calibre&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_PROJECT&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TOOL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:62 cells:37 -->
> [!abstract]- Запись 62 из 79 — PKG-LIBREOFFICE — LibreOffice offline installers help and source
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-LIBREOFFICE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OFFICE_READER&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;LibreOffice offline installers help and source&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;The Document Foundation&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.libreoffice.org/download/download-libreoffice/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.libreoffice.org/download/download-libreoffice/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;BINARIES_HELP_SOURCE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;OS_SPECIFIC&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;MPL-2.0_LGPL_AND_COMPONENT_SPECIFIC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.libreoffice.org/about-us/licenses/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_FOUNDATION&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TOOL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_STABLE_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:63 cells:37 -->
> [!abstract]- Запись 63 из 79 — PKG-PYTHON-DOCS — Python offline documentation and source
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PYTHON-DOCS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PROGRAMMING_DOCS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Python offline documentation and source&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Python Software Foundation&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://docs.python.org/3/download.html&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://docs.python.org/3/download.html&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF_EPUB_SOURCE&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PYTHON&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PSF_LICENSE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://docs.python.org/3/license.html&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;OPEN_SOURCE_FOUNDATION&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_TECHNICAL&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_FEATURE_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:64 cells:37 -->
> [!abstract]- Запись 64 из 79 — PKG-SOFTWARE-HERITAGE — Software Heritage archive identifiers and selected critical source
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-SOFTWARE-HERITAGE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SOFTWARE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;SOURCE_ARCHIVE_REFERENCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Software Heritage archive identifiers and selected critical source&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Software Heritage&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.softwareheritage.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.softwareheritage.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;API_ARCHIVE_SELECTED_BUNDLES&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;CUSTOM_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;SOURCE_LICENSES_PER_PROJECT&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.softwareheritage.org/legal/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NONPROFIT_ARCHIVE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;EXTERNAL_REDUNDANCY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_PROJECT&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:65 cells:37 -->
> [!abstract]- Запись 65 из 79 — PKG-PRONOM — PRONOM technical registry
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PRONOM&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;FORMAT_REGISTRY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;PRONOM technical registry&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;The National Archives UK&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.nationalarchives.gov.uk/pronom/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.nationalarchives.gov.uk/pronom/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;XML_CSV_WEB&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;UK_GOV_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.nationalarchives.gov.uk/legal/copyright/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_ARCHIVE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PRESERVATION_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:66 cells:37 -->
> [!abstract]- Запись 66 из 79 — PKG-LOC-RFS — Library of Congress Recommended Formats Statement
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-LOC-RFS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;FORMAT_GUIDANCE&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Library of Congress Recommended Formats Statement&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Library of Congress&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;US_REFERENCE&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.loc.gov/preservation/resources/rfs/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.loc.gov/preservation/resources/rfs/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;US_GOV_WITH_EXCEPTIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.loc.gov/legal/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_LIBRARY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PRESERVATION_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:67 cells:37 -->
> [!abstract]- Запись 67 из 79 — PKG-NDSA-LEVELS — NDSA Levels of Digital Preservation
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-NDSA-LEVELS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PRESERVATION_LEVELS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;NDSA Levels of Digital Preservation&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;NDSA&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.ndsa.org/publications/levels-of-digital-preservation/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.ndsa.org/publications/levels-of-digital-preservation/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_DOCX_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_PUBLICATION_OPEN_LICENSE_REVIEW&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.ndsa.org/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;PROFESSIONAL_COMMUNITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PRESERVATION_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_RELEASE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:68 cells:37 -->
> [!abstract]- Запись 68 из 79 — PKG-BAGIT-RFC8493 — RFC 8493 The BagIt File Packaging Format
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-BAGIT-RFC8493&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L1&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;PACKAGING_STANDARD&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;RFC 8493 The BagIt File Packaging Format&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;RFC Editor&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.rfc-editor.org/rfc/rfc8493.html&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.rfc-editor.org/rfc/rfc8493.html&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;HTML_TXT_PDF_XML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_TEXT&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;IETF_TRUST_LEGAL_PROVISIONS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://trustee.ietf.org/documents/trust-legal-provisions/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;STANDARDS_PUBLISHER&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PRESERVATION_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_UPDATE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:69 cells:37 -->
> [!abstract]- Запись 69 из 79 — PKG-OAIS — CCSDS OAIS Reference Model Issue 3
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-OAIS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;ARCHIVE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;REFERENCE_MODEL&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;CCSDS OAIS Reference Model Issue 3&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;CCSDS&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://ccsds.org/Pubs/650x0m3.pdf&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://ccsds.org/Pubs/650x0m3.pdf&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;MEDIUM&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;CCSDS_PUBLICATION_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://ccsds.org/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;STANDARDS_BODY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;PRESERVATION_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_REVISION&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:70 cells:37 -->
> [!abstract]- Запись 70 из 79 — PKG-PUBMED — PubMed baseline and updates
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PUBMED&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SCIENCE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;BIOMEDICAL_METADATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;PubMed baseline and updates&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;US National Library of Medicine&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://pubmed.ncbi.nlm.nih.gov/download/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://pubmed.ncbi.nlm.nih.gov/download/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;XML_GZ&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;NLM_DATA_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.nlm.nih.gov/databases/download/terms_and_conditions.html&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_LIBRARY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DISCOVERY_ONLY_NOT_CLINICAL_ACTION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ANNUAL_PLUS_DAILY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:71 cells:37 -->
> [!abstract]- Запись 71 из 79 — PKG-PMC-OA — PubMed Central Open Access subset
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-PMC-OA&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SCIENCE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;OPEN_ACCESS_FULLTEXT&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;PubMed Central Open Access subset&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;US National Library of Medicine&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://pmc.ncbi.nlm.nih.gov/tools/ftp/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://pmc.ncbi.nlm.nih.gov/tools/ftp/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;XML_PDF_MEDIA&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_PDF&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_ARTICLE_LICENSE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://pmc.ncbi.nlm.nih.gov/about/copyright/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;NATIONAL_LIBRARY_REPOSITORY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;RESEARCH_NOT_CLINICAL_ACTION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:72 cells:37 -->
> [!abstract]- Запись 72 из 79 — PKG-EUROPE-PMC — Europe PMC APIs and permitted full text
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-EUROPE-PMC&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SCIENCE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;BIOMEDICAL_DISCOVERY&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Europe PMC APIs and permitted full text&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;EMBL-EBI Europe PMC&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://europepmc.org/developers&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://europepmc.org/developers&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;API_XML_JSON_FULLTEXT_SUBSET&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;METADATA_AND_FULLTEXT_RIGHTS_SEPARATE&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://europepmc.org/Terms&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;RESEARCH_INFRASTRUCTURE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DISCOVERY_ONLY_NOT_CLINICAL_ACTION&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:73 cells:37 -->
> [!abstract]- Запись 73 из 79 — PKG-CROSSREF — Crossref metadata snapshot or API export
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-CROSSREF&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;SCIENCE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;SCHOLARLY_METADATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Crossref metadata snapshot or API export&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Crossref&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.crossref.org/documentation/retrieve-metadata/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.crossref.org/documentation/retrieve-metadata/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;JSON_XML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_TOOLS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;METADATA_LICENSE_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-metadata-license-information/&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;SCHOLARLY_INFRASTRUCTURE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;DISCOVERY_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;MONTHLY&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:74 cells:37 -->
> [!abstract]- Запись 74 из 79 — PKG-EUROPEANA — Europeana metadata and rights-labelled items
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-EUROPEANA&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;CULTURE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;CULTURAL_METADATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Europeana metadata and rights-labelled items&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Europeana&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;EU&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.europeana.eu/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.europeana.eu/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;API_JSON_MEDIA_LINKS&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;METADATA_CC0_ITEMS_RIGHTS_LABELLED&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.europeana.eu/en/rights/europeana-data-sources&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;CULTURAL_INFRASTRUCTURE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;REFERENCE_ONLY&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_ITEM&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:75 cells:37 -->
> [!abstract]- Запись 75 из 79 — PKG-GBIF — GBIF occurrence and species data
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-GBIF&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L4&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;BIOLOGY&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;BIODIVERSITY_DATA&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;GBIF occurrence and species data&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;GBIF&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.gbif.org/&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.gbif.org/&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;DWCA_CSV_API&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;DATABASE_GIS&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VERY_LARGE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;DATASET_CC0_CC-BY_OR_CC-BY-NC&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.gbif.org/terms&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;SCIENTIFIC_INFRASTRUCTURE&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;IDENTIFICATION_NOT_EDIBILITY_PROOF&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;PER_DATASET&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:76 cells:37 -->
> [!abstract]- Запись 76 из 79 — PKG-UNESCO-ED2030 — UNESCO Education 2030 Framework for Action
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-UNESCO-ED2030&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EDUCATION&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;EDUCATION_FRAMEWORK&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;UNESCO Education 2030 Framework for Action&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;UNESCO&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://unesdoc.unesco.org/ark:/48223/pf0000245656&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://unesdoc.unesco.org/ark:/48223/pf0000245656&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_READER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;UNESCO_ITEM_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.unesco.org/en/open-access&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;POLICY_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_REVISION&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:77 cells:37 -->
> [!abstract]- Запись 77 из 79 — PKG-UNDRR-SENDAI — Sendai Framework for Disaster Risk Reduction
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-UNDRR-SENDAI&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L2&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;GOVERNANCE&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;DISASTER_RISK&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Sendai Framework for Disaster Risk Reduction&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;UNDRR&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;MULTI&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;GLOBAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;PDF_BROWSER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;UN_ITEM_TERMS&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;https://www.un.org/en/about-us/terms-of-use&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;INTERNATIONAL_AUTHORITY&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;POLICY_REFERENCE&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_SUCCESSOR_FRAMEWORK&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;&quot;</code>
>

<!-- record:78 cells:37 -->
> [!abstract]- Запись 78 из 79 — PKG-LOCAL-MANUALS — Manuals firmware parts and safety data for owned systems
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-LOCAL-MANUALS&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L0&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;MANUALS&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;EXACT_OWNED_MODELS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Manuals firmware parts and safety data for owned systems&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Exact manufacturers&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU|PT|EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;LOCAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;TBD_PER_ACTUAL_ITEM&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;TBD_PER_ACTUAL_ITEM&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_HTML_BINARIES&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;MODEL_SPECIFIC&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;VARIABLE&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;PER_MANUFACTURER_AND_ITEM&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;TBD_PER_ACTUAL_ITEM&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;MANUFACTURER&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;MANUFACTURER_SPECIFIC_COMPETENCE_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;ON_PURCHASE_OR_UPDATE&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;User input required; highest operational priority&quot;</code>
>

<!-- record:79 cells:37 -->
> [!abstract]- Запись 79 из 79 — PKG-LOCAL-RED-CORE — Address-specific red core and print masters
> - **«package» ID** (<code>&quot;package_id&quot;</code>): <code>&quot;PKG-LOCAL-RED-CORE&quot;</code>
> - **Приоритет** (<code>&quot;priority_tier&quot;</code>): <code>&quot;L0&quot;</code>
> - **«category»** (<code>&quot;category&quot;</code>): <code>&quot;EMERGENCY&quot;</code>
> - **«subcategory»** (<code>&quot;subcategory&quot;</code>): <code>&quot;HOUSEHOLD_RELEASED_CARDS&quot;</code>
> - **Название** (<code>&quot;title&quot;</code>): <code>&quot;Address-specific red core and print masters&quot;</code>
> - **Издатель** (<code>&quot;publisher&quot;</code>): <code>&quot;Household plus official sources&quot;</code>
> - **«languages»** (<code>&quot;languages&quot;</code>): <code>&quot;RU|PT|EN&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;PT_LOCAL&quot;</code>
> - **Канонический адрес в сети** (<code>&quot;canonical_url&quot;</code>): <code>&quot;LOCAL_GENERATED_AFTER_REVIEW&quot;</code>
> - **Адрес получения** (<code>&quot;acquisition_url&quot;</code>): <code>&quot;LOCAL_GENERATED_AFTER_REVIEW&quot;</code>
> - **«distribution» формат** (<code>&quot;distribution_format&quot;</code>): <code>&quot;PDF_A_HTML_TXT_PRINT&quot;</code>
> - **«reader» «or» «runtime»** (<code>&quot;reader_or_runtime&quot;</code>): <code>&quot;BROWSER_PDF_PAPER&quot;</code>
> - **«size» класс** (<code>&quot;size_class&quot;</code>): <code>&quot;SMALL&quot;</code>
> - **Лицензия «expression»** (<code>&quot;license_expression&quot;</code>): <code>&quot;DERIVATIVE_RIGHTS_AND_SOURCE_REVIEW&quot;</code>
> - **Лицензия адрес в сети** (<code>&quot;license_url&quot;</code>): <code>&quot;LOCAL_RIGHTS_LEDGER&quot;</code>
> - **Лицензия проверка состояние** (<code>&quot;license_review_state&quot;</code>): <code>&quot;PRELIMINARY_SOURCE_PAGE_ONLY&quot;</code>
> - **«redistribution» состояние** (<code>&quot;redistribution_state&quot;</code>): <code>&quot;REVIEW_REQUIRED&quot;</code>
> - **«attribution» требуемый** (<code>&quot;attribution_required&quot;</code>): <code>&quot;VERIFY_PER_PACKAGE&quot;</code>
> - **Полномочие класс** (<code>&quot;authority_class&quot;</code>): <code>&quot;LOCAL_REVIEWED&quot;</code>
> - **Класс безопасности** (<code>&quot;safety_class&quot;</code>): <code>&quot;RELEASE_GATES_REQUIRED&quot;</code>
> - **«content» проверка состояние** (<code>&quot;content_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«section» проверка состояние** (<code>&quot;section_review_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«download» состояние** (<code>&quot;download_state&quot;</code>): <code>&quot;NOT_DOWNLOADED&quot;</code>
> - **«downloaded» версия** (<code>&quot;downloaded_version&quot;</code>): <code>&quot;&quot;</code>
> - **«retrieved» время** (<code>&quot;retrieved_at&quot;</code>): <code>&quot;&quot;</code>
> - **Локальный путь** (<code>&quot;local_path&quot;</code>): <code>&quot;&quot;</code>
> - **Размер в байтах** (<code>&quot;byte_size&quot;</code>): <code>&quot;&quot;</code>
> - **Хеш SHA-256** (<code>&quot;sha256&quot;</code>): <code>&quot;&quot;</code>
> - **«upstream» «checksum» состояние** (<code>&quot;upstream_checksum_state&quot;</code>): <code>&quot;NOT_CHECKED&quot;</code>
> - **«malware» «scan» состояние** (<code>&quot;malware_scan_state&quot;</code>): <code>&quot;NOT_SCANNED&quot;</code>
> - **Офлайн «open» состояние** (<code>&quot;offline_open_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«search» «index» состояние** (<code>&quot;search_index_state&quot;</code>): <code>&quot;NOT_INDEXED&quot;</code>
> - **«update» класс** (<code>&quot;update_class&quot;</code>): <code>&quot;EVENT_AND_6_MONTHS&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **«retention» класс** (<code>&quot;retention_class&quot;</code>): <code>&quot;KEEP_LATEST_PLUS_SUPERSEDED_HISTORY&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;PUBLIC_OR_LICENSE_RESTRICTED&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Not created or released in v0.3&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
