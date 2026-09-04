---
id: "GAP-025"
kind: "known-gap"
title: "Независимые резервные копии и доказанное восстановление всего кита без сети"
priority_tier: "P1_ORANGE"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "UNASSIGNED"
safety_class: "UNASSIGNED"
execution_gate: "DENY_UNTIL_BACKUP_RESTORE_DRILL_PASSED"
status: "OPEN_NO_RESTORE_EVIDENCE"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Независимые резервные копии и доказанное восстановление всего кита без сети

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `GAP-025`
- **Статус:** `OPEN_NO_RESTORE_EVIDENCE`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `UNASSIGNED`
- **Класс безопасности:** `UNASSIGNED`
- **Допуск:** `DENY_UNTIL_BACKUP_RESTORE_DRILL_PASSED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: known-gap-register.csv -->
- **gap_id:** GAP-025
- **domain:** KNOWLEDGE
- **scope_layer:** SITE
- **priority_tier:** P1_ORANGE
- **earliest_service_level:** SL2
- **gap_ru:** Независимые резервные копии и доказанное восстановление всего кита без сети
- **blocks_service_level:** SL2|SL3|SL4|SL5|SL6
- **blocker:** YES
- **required_evidence:** Минимум две независимые копии; одна географически отделена; manifest/hash; зашифрованные приватные данные; restore drill; время восстановления; журнал ошибок
- **current_evidence:** Фактический restore drill и независимые носители не подтверждены
- **status:** OPEN_NO_RESTORE_EVIDENCE
- **owner:** UNASSIGNED
- **due:** TBD_NOT_SCHEDULED
- **release_gate:** DENY_UNTIL_BACKUP_RESTORE_DRILL_PASSED
- **release_version:** 0.5-draft
- **notes:** Копия считается резервной только после восстановления

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
