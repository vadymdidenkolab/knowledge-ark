---
id: "GAP-019"
kind: "known-gap"
title: "Аудит критических электрических и тепловых нагрузок по времени и пусковой мощности"
priority_tier: "P1_ORANGE"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "UNASSIGNED"
safety_class: "UNASSIGNED"
execution_gate: "DENY_UNTIL_CRITICAL_LOADS_MEASURED_AND_BACKED_UP"
status: "OPEN_NO_ENERGY_LOAD_AUDIT"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Аудит критических электрических и тепловых нагрузок по времени и пусковой мощности

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `GAP-019`
- **Статус:** `OPEN_NO_ENERGY_LOAD_AUDIT`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_CRITICAL_LOADS_MEASURED_AND_BACKED_UP`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: known-gap-register.csv -->
- **gap_id:** GAP-019
- **domain:** ENERGY
- **scope_layer:** SITE_PERSON
- **priority_tier:** P1_ORANGE
- **earliest_service_level:** SL1
- **gap_ru:** Аудит критических электрических и тепловых нагрузок по времени и пусковой мощности
- **blocks_service_level:** SL1|SL2|SL3|SL4
- **blocker:** YES
- **required_evidence:** Перечень нагрузок; W/Wh; пуск; режим; приоритет отключения; профиль 24 часа; измерение; автономия; потери; защита; второй путь
- **current_evidence:** Каталог систем есть; измеренного load profile 0
- **status:** OPEN_NO_ENERGY_LOAD_AUDIT
- **owner:** UNASSIGNED
- **due:** TBD_NOT_SCHEDULED
- **release_gate:** DENY_UNTIL_CRITICAL_LOADS_MEASURED_AND_BACKED_UP
- **release_version:** 0.5-draft
- **notes:** Выбор генерации и батарей до измерения нагрузки недостоверен

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
