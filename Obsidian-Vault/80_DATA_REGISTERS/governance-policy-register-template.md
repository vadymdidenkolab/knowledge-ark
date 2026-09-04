---
id: "DATA-REGISTER-cbd0cd44be3f7376"
type: "generated-data-register-view"
title: "Политики управления — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "governance-policy-register-template.csv"
source_sha256: "2984440849d696e5858c36d4c875cbe26aab8e15aa401b9512de5ed35149f9c8"
source_bytes: 718
source_row_count: 1
source_column_count: 24
source_cell_count: 24
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: governance-policy-register-template.csv -->

# Политики управления — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 1
- **Полей в каждой записи:** 24
- **Ячеек данных, включая пустые:** 24
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `2984440849d696e5858c36d4c875cbe26aab8e15aa401b9512de5ed35149f9c8`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Правило ID | <code>&quot;policy_id&quot;</code> |
| 2 | «institution» ID | <code>&quot;institution_id&quot;</code> |
| 3 | Решение класс | <code>&quot;decision_class&quot;</code> |
| 4 | «ordinary» решение «rule» | <code>&quot;ordinary_decision_rule&quot;</code> |
| 5 | «quorum» «rule» | <code>&quot;quorum_rule&quot;</code> |
| 6 | «supermajority» «rule» | <code>&quot;supermajority_rule&quot;</code> |
| 7 | «conflict» «of» «interest» «rule» | <code>&quot;conflict_of_interest_rule&quot;</code> |
| 8 | «recusal» «rule» | <code>&quot;recusal_rule&quot;</code> |
| 9 | «minority» «protection» «rule» | <code>&quot;minority_protection_rule&quot;</code> |
| 10 | «child» «and» «dependent» «safeguarding» «rule» | <code>&quot;child_and_dependent_safeguarding_rule&quot;</code> |
| 11 | Аварийный полномочие роль | <code>&quot;emergency_authority_role&quot;</code> |
| 12 | Аварийный полномочие область | <code>&quot;emergency_authority_scope&quot;</code> |
| 13 | Аварийный полномочие «expires» «after» | <code>&quot;emergency_authority_expires_after&quot;</code> |
| 14 | Аварийный проверка требуемый | <code>&quot;emergency_review_required&quot;</code> |
| 15 | «grievance» «process» ссылка | <code>&quot;grievance_process_ref&quot;</code> |
| 16 | «removal» «or» «recall» «rule» | <code>&quot;removal_or_recall_rule&quot;</code> |
| 17 | «appeal» «rule» | <code>&quot;appeal_rule&quot;</code> |
| 18 | Правило версия | <code>&quot;policy_version&quot;</code> |
| 19 | «approval» доказательство ссылка | <code>&quot;approval_evidence_ref&quot;</code> |
| 20 | «effective» из | <code>&quot;effective_from&quot;</code> |
| 21 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 22 | Правило состояние | <code>&quot;policy_state&quot;</code> |
| 23 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 24 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:24 -->
> [!abstract]- Запись 1 из 1 — GOVPOL-EXAMPLE-001
> - **Правило ID** (<code>&quot;policy_id&quot;</code>): <code>&quot;GOVPOL-EXAMPLE-001&quot;</code>
> - **«institution» ID** (<code>&quot;institution_id&quot;</code>): <code>&quot;INST-EXAMPLE-001&quot;</code>
> - **Решение класс** (<code>&quot;decision_class&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«ordinary» решение «rule»** (<code>&quot;ordinary_decision_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«quorum» «rule»** (<code>&quot;quorum_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«supermajority» «rule»** (<code>&quot;supermajority_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«conflict» «of» «interest» «rule»** (<code>&quot;conflict_of_interest_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«recusal» «rule»** (<code>&quot;recusal_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«minority» «protection» «rule»** (<code>&quot;minority_protection_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«child» «and» «dependent» «safeguarding» «rule»** (<code>&quot;child_and_dependent_safeguarding_rule&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный полномочие роль** (<code>&quot;emergency_authority_role&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный полномочие область** (<code>&quot;emergency_authority_scope&quot;</code>): <code>&quot;&quot;</code>
> - **Аварийный полномочие «expires» «after»** (<code>&quot;emergency_authority_expires_after&quot;</code>): <code>&quot;TBD_NONZERO&quot;</code>
> - **Аварийный проверка требуемый** (<code>&quot;emergency_review_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«grievance» «process» ссылка** (<code>&quot;grievance_process_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«removal» «or» «recall» «rule»** (<code>&quot;removal_or_recall_rule&quot;</code>): <code>&quot;&quot;</code>
> - **«appeal» «rule»** (<code>&quot;appeal_rule&quot;</code>): <code>&quot;&quot;</code>
> - **Правило версия** (<code>&quot;policy_version&quot;</code>): <code>&quot;0.0-DRAFT&quot;</code>
> - **«approval» доказательство ссылка** (<code>&quot;approval_evidence_ref&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Правило состояние** (<code>&quot;policy_state&quot;</code>): <code>&quot;NOT_ADOPTED&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Emergency authority без scope и expiry запрещена&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
