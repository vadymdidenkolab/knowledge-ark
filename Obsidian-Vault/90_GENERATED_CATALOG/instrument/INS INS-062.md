---
id: "INS-062"
kind: "instrument"
title: "GNSS receiver"
priority_tier: "P1_ORANGE"
priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED
audience: "LAY_OR_TRAINED_AS_NOTED"
safety_class: "S1_LOW_RISK_HOUSEHOLD"
execution_gate: "DENY_UNTIL_REVIEWED"
status: "CANDIDATE_NOT_INVENTORIED"
backend_provenance: INTERNAL_MANIFEST_ONLY
generated_on: "2026-09-04"
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# GNSS receiver

> [!warning] Каталожная карточка
> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.

## Краткий статус

- **ID:** `INS-062`
- **Статус:** `CANDIDATE_NOT_INVENTORIED`
- **Приоритет:** `P1_ORANGE`
- **Аудитория:** `LAY_OR_TRAINED_AS_NOTED`
- **Класс безопасности:** `S1_LOW_RISK_HOUSEHOLD`
- **Допуск:** `DENY_UNTIL_REVIEWED`

<details>
<summary>Технические данные backend (для аудита)</summary>

<!-- backend-source: practical-science-instrument-register.csv -->
- **instrument_id:** INS-062
- **category:** NAVIGATION
- **instrument_ru:** GNSS receiver
- **measures:** координаты/время
- **unit:** lat/lon/height/time
- **range_hint:** TBD_PER_EXACT_TASK_AND_METHOD; не закупать/не применять по этой общей строке и не работать у края диапазона.
- **resolution_hint:** TBD_PER_EXACT_TASK_AND_METHOD; правило 10:1 — только planning hint, не универсальная спецификация точности.
- **calibration_method:** known control point and multi-fix comparison
- **reference_required:** TBD_PER_EXACT_INSTRUMENT: документированный эталон, контрольная точка или официальный сервис выбираются по методу/классу.
- **interval:** BEFORE_CRITICAL_USE|AFTER_DAMAGE|ANNUAL_OR_MANUFACTURER
- **storage:** чисто, сухо, защищено от удара/магнитов/температуры по manual
- **maintenance:** визуальный осмотр, батарея/расходник, очистка, журнал offset и следующей проверки
- **failure_signs:** нестабильный ноль, дрейф, повреждение, невозможный результат, расхождение с контрольной точкой
- **safety_class:** S1_LOW_RISK_HOUSEHOLD
- **prohibited_use:** координата не доказывает проходимость/безопасность
- **spare_strategy:** phone + standalone + paper
- **manual_package_id:** [[PKG PSP-116|PSP-116]]
- **status:** CANDIDATE_NOT_INVENTORIED
- **release_version:** 0.4

</details>

## Связи и наполнение

- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.
- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.
