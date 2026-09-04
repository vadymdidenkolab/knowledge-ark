---
id: "GAP-006"
kind: "known-gap"
title: "Непрерывность назначенных лекарств, рецептов, расходников и холодовой цепи"
priority_tier: "P0_RED"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "UNASSIGNED"
safety_class: "UNASSIGNED"
execution_gate: "DENY_UNTIL_PRESCRIBED_MEDICATION_CONTINUITY_VERIFIED"
status: "OPEN_NO_PERSONAL_MEDICATION_PLAN"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Непрерывность назначенных лекарств, рецептов, расходников и холодовой цепи

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `GAP-006`
- **Статус:** `OPEN_NO_PERSONAL_MEDICATION_PLAN`
- **Приоритет:** `P0_RED`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_PRESCRIBED_MEDICATION_CONTINUITY_VERIFIED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: known-gap-register.csv -->
- **gap_id:** GAP-006
- **domain:** HEALTH
- **scope_layer:** PERSON
- **priority_tier:** P0_RED
- **earliest_service_level:** SL1
- **gap_ru:** Непрерывность назначенных лекарств, рецептов, расходников и холодовой цепи
- **blocks_service_level:** SL1|SL2|SL3|SL4|SL5
- **blocker:** YES
- **required_evidence:** Персональный medication list; назначивший врач; законный запас и ротация; температурный журнал где нужен; резервный план; противопоказания; контакт аптеки/врача
- **current_evidence:** Персональных лекарственных данных и подтверждённого запаса 0
- **status:** OPEN_NO_PERSONAL_MEDICATION_PLAN
- **owner:** UNASSIGNED
- **due:** TBD_NOT_SCHEDULED
- **release_gate:** DENY_UNTIL_PRESCRIBED_MEDICATION_CONTINUITY_VERIFIED
- **release_version:** 0.5-draft
- **notes:** Не предлагать самостоятельную замену дозы, препарата или синтез лекарства

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
