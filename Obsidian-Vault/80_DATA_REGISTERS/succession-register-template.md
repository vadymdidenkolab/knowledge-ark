---
id: "DATA-REGISTER-54161152870bfc45"
type: "generated-data-register-view"
title: "Передача полномочий — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "succession-register-template.csv"
source_sha256: "5c0c0ace7de8f369c1e34564dff373c308325d6084b8a74923b3079b8b2c7817"
source_bytes: 837
source_row_count: 1
source_column_count: 26
source_cell_count: 26
ignored_blank_row_count: 0
semantic_group: "CENTURY_CONTINUITY"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: succession-register-template.csv -->

# Передача полномочий — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Преемственность и столетний горизонт
- **Записей:** 1
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 26
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `5c0c0ace7de8f369c1e34564dff373c308325d6084b8a74923b3079b8b2c7817`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Преемственность ID | <code>&quot;succession_id&quot;</code> |
| 2 | Область тип | <code>&quot;scope_type&quot;</code> |
| 3 | Область ID | <code>&quot;scope_id&quot;</code> |
| 4 | «outgoing» полномочие ID | <code>&quot;outgoing_authority_id&quot;</code> |
| 5 | «incoming» полномочие ID | <code>&quot;incoming_authority_id&quot;</code> |
| 6 | «successor» роль ID | <code>&quot;successor_role_id&quot;</code> |
| 7 | Триггер класс | <code>&quot;trigger_class&quot;</code> |
| 8 | Триггер доказательство ссылка | <code>&quot;trigger_evidence_ref&quot;</code> |
| 9 | «identity» подтверждение состояние | <code>&quot;identity_verification_state&quot;</code> |
| 10 | Приёмка запись ссылка | <code>&quot;acceptance_record_ref&quot;</code> |
| 11 | Приёмка состояние | <code>&quot;acceptance_state&quot;</code> |
| 12 | Полномочие доказательство ссылка | <code>&quot;authority_evidence_ref&quot;</code> |
| 13 | Правовой валидация состояние | <code>&quot;legal_validation_state&quot;</code> |
| 14 | «access» «package» ID | <code>&quot;access_package_id&quot;</code> |
| 15 | Знания «package» ID | <code>&quot;knowledge_package_id&quot;</code> |
| 16 | Имущество «handover» ID | <code>&quot;asset_handover_ids&quot;</code> |
| 17 | «credential» «gap» ID | <code>&quot;credential_gap_ids&quot;</code> |
| 18 | «supervision» требование | <code>&quot;supervision_requirement&quot;</code> |
| 19 | «handoff» испытание время | <code>&quot;handoff_test_at&quot;</code> |
| 20 | «handoff» испытание результат | <code>&quot;handoff_test_result&quot;</code> |
| 21 | «effective» время «utc» | <code>&quot;effective_at_utc&quot;</code> |
| 22 | «revocation» «or» «reversal» «rule» | <code>&quot;revocation_or_reversal_rule&quot;</code> |
| 23 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 24 | Преемственность допуск состояние | <code>&quot;succession_gate_state&quot;</code> |
| 25 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 1 — SUCC-EXAMPLE-001
> - **Преемственность ID** (<code>&quot;succession_id&quot;</code>): <code>&quot;SUCC-EXAMPLE-001&quot;</code>
> - **Область тип** (<code>&quot;scope_type&quot;</code>): <code>&quot;CAPABILITY&quot;</code>
> - **Область ID** (<code>&quot;scope_id&quot;</code>): <code>&quot;CAP-GOV-SUCCESSION&quot;</code>
> - **«outgoing» полномочие ID** (<code>&quot;outgoing_authority_id&quot;</code>): <code>&quot;&quot;</code>
> - **«incoming» полномочие ID** (<code>&quot;incoming_authority_id&quot;</code>): <code>&quot;&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;&quot;</code>
> - **Триггер класс** (<code>&quot;trigger_class&quot;</code>): <code>&quot;&quot;</code>
> - **Триггер доказательство ссылка** (<code>&quot;trigger_evidence_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«identity» подтверждение состояние** (<code>&quot;identity_verification_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Приёмка запись ссылка** (<code>&quot;acceptance_record_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Полномочие доказательство ссылка** (<code>&quot;authority_evidence_ref&quot;</code>): <code>&quot;&quot;</code>
> - **Правовой валидация состояние** (<code>&quot;legal_validation_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«access» «package» ID** (<code>&quot;access_package_id&quot;</code>): <code>&quot;&quot;</code>
> - **Знания «package» ID** (<code>&quot;knowledge_package_id&quot;</code>): <code>&quot;&quot;</code>
> - **Имущество «handover» ID** (<code>&quot;asset_handover_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«credential» «gap» ID** (<code>&quot;credential_gap_ids&quot;</code>): <code>&quot;&quot;</code>
> - **«supervision» требование** (<code>&quot;supervision_requirement&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» испытание время** (<code>&quot;handoff_test_at&quot;</code>): <code>&quot;&quot;</code>
> - **«handoff» испытание результат** (<code>&quot;handoff_test_result&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«effective» время «utc»** (<code>&quot;effective_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«revocation» «or» «reversal» «rule»** (<code>&quot;revocation_or_reversal_rule&quot;</code>): <code>&quot;&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Преемственность допуск состояние** (<code>&quot;succession_gate_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Названный successor без согласия права доступа и теста не активен&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
