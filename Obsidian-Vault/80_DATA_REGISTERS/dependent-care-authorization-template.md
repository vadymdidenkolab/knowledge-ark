---
id: "DATA-REGISTER-1b726705182016cf"
type: "generated-data-register-view"
title: "Полномочия по уходу за зависимым человеком — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "dependent-care-authorization-template.csv"
source_sha256: "b10cb4fd5805b177e5e3336ec79ab086a95553a0ddd653bb5d644099e1291a68"
source_bytes: 803
source_row_count: 1
source_column_count: 22
source_cell_count: 22
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: dependent-care-authorization-template.csv -->

# Полномочия по уходу за зависимым человеком — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 1
- **Полей в каждой записи:** 22
- **Ячеек данных, включая пустые:** 22
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `b10cb4fd5805b177e5e3336ec79ab086a95553a0ddd653bb5d644099e1291a68`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Разрешение ID | <code>&quot;authorization_id&quot;</code> |
| 2 | «dependent» человек ID | <code>&quot;dependent_person_id&quot;</code> |
| 3 | «authorized» человек ID | <code>&quot;authorized_person_id&quot;</code> |
| 4 | Резервный «authorized» человек ID | <code>&quot;backup_authorized_person_id&quot;</code> |
| 5 | Отношение | <code>&quot;relationship&quot;</code> |
| 6 | Полномочие тип | <code>&quot;authority_type&quot;</code> |
| 7 | Полномочие доказательство ссылка | <code>&quot;authority_evidence_ref&quot;</code> |
| 8 | Полномочие подтверждение состояние | <code>&quot;authority_verification_state&quot;</code> |
| 9 | «identity» подтверждение метод | <code>&quot;identity_verification_method&quot;</code> |
| 10 | «handoff» «conditions» | <code>&quot;handoff_conditions&quot;</code> |
| 11 | Запрещённый «handoff» «conditions» | <code>&quot;prohibited_handoff_conditions&quot;</code> |
| 12 | Согласие «or» «best» «interest» «basis» | <code>&quot;consent_or_best_interest_basis&quot;</code> |
| 13 | «effective» из | <code>&quot;effective_from&quot;</code> |
| 14 | «effective» до | <code>&quot;effective_until&quot;</code> |
| 15 | Приёмка запись ID | <code>&quot;acceptance_record_id&quot;</code> |
| 16 | «sensitive» запись ссылка | <code>&quot;sensitive_record_ref&quot;</code> |
| 17 | Приватность класс | <code>&quot;privacy_class&quot;</code> |
| 18 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |
| 19 | Разрешение статус | <code>&quot;authorization_status&quot;</code> |
| 20 | Владелец | <code>&quot;owner&quot;</code> |
| 21 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 22 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:22 -->
> [!abstract]- Запись 1 из 1 — CARE-AUTH-001
> - **Разрешение ID** (<code>&quot;authorization_id&quot;</code>): <code>&quot;CARE-AUTH-001&quot;</code>
> - **«dependent» человек ID** (<code>&quot;dependent_person_id&quot;</code>): <code>&quot;P07&quot;</code>
> - **«authorized» человек ID** (<code>&quot;authorized_person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Резервный «authorized» человек ID** (<code>&quot;backup_authorized_person_id&quot;</code>): <code>&quot;P02&quot;</code>
> - **Отношение** (<code>&quot;relationship&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Полномочие тип** (<code>&quot;authority_type&quot;</code>): <code>&quot;TBD_LOCAL_LAW&quot;</code>
> - **Полномочие доказательство ссылка** (<code>&quot;authority_evidence_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Полномочие подтверждение состояние** (<code>&quot;authority_verification_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«identity» подтверждение метод** (<code>&quot;identity_verification_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«handoff» «conditions»** (<code>&quot;handoff_conditions&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Запрещённый «handoff» «conditions»** (<code>&quot;prohibited_handoff_conditions&quot;</code>): <code>&quot;Не передавать неподтверждённому лицу&quot;</code>
> - **Согласие «or» «best» «interest» «basis»** (<code>&quot;consent_or_best_interest_basis&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«effective» из** (<code>&quot;effective_from&quot;</code>): <code>&quot;&quot;</code>
> - **«effective» до** (<code>&quot;effective_until&quot;</code>): <code>&quot;&quot;</code>
> - **Приёмка запись ID** (<code>&quot;acceptance_record_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«sensitive» запись ссылка** (<code>&quot;sensitive_record_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Приватность класс** (<code>&quot;privacy_class&quot;</code>): <code>&quot;RESTRICTED&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Разрешение статус** (<code>&quot;authorization_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Только схема; P07 не означает реального зависимого человека&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
