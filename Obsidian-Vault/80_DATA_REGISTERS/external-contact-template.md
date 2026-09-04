---
id: "DATA-REGISTER-9db23eb220c62db9"
type: "generated-data-register-view"
title: "Внешние контакты — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "external-contact-template.csv"
source_sha256: "33f958121ae10810e557cb14b514803300e2df99f8a66972c294318e0f364432"
source_bytes: 908
source_row_count: 1
source_column_count: 27
source_cell_count: 27
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: external-contact-template.csv -->

# Внешние контакты — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 1
- **Полей в каждой записи:** 27
- **Ячеек данных, включая пустые:** 27
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `33f958121ae10810e557cb14b514803300e2df99f8a66972c294318e0f364432`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Контакт ID | <code>&quot;contact_id&quot;</code> |
| 2 | «display» «alias» | <code>&quot;display_alias&quot;</code> |
| 3 | «purpose» «codes» | <code>&quot;purpose_codes&quot;</code> |
| 4 | Отношение «or» полномочие | <code>&quot;relationship_or_authority&quot;</code> |
| 5 | Основной «channel» | <code>&quot;primary_channel&quot;</code> |
| 6 | «alternate» «channel» | <code>&quot;alternate_channel&quot;</code> |
| 7 | «contingency» «channel» | <code>&quot;contingency_channel&quot;</code> |
| 8 | Аварийный «channel» | <code>&quot;emergency_channel&quot;</code> |
| 9 | «channel» отказ отрасль доказательство | <code>&quot;channel_failure_domain_evidence&quot;</code> |
| 10 | «pace» испытание состояние | <code>&quot;pace_test_state&quot;</code> |
| 11 | «identity» подтверждение метод | <code>&quot;identity_verification_method&quot;</code> |
| 12 | Подтверждение состояние | <code>&quot;verification_state&quot;</code> |
| 13 | Согласие состояние | <code>&quot;consent_state&quot;</code> |
| 14 | Доступность «window» | <code>&quot;availability_window&quot;</code> |
| 15 | «missed» контакт триггер | <code>&quot;missed_contact_trigger&quot;</code> |
| 16 | «escalation» полномочие | <code>&quot;escalation_authority&quot;</code> |
| 17 | Юрисдикция | <code>&quot;jurisdiction&quot;</code> |
| 18 | «sensitive» контакт ссылка | <code>&quot;sensitive_contact_ref&quot;</code> |
| 19 | «encryption» требуемый | <code>&quot;encryption_required&quot;</code> |
| 20 | «encryption» состояние | <code>&quot;encryption_state&quot;</code> |
| 21 | «access» «control» состояние | <code>&quot;access_control_state&quot;</code> |
| 22 | «retention» «rule» | <code>&quot;retention_rule&quot;</code> |
| 23 | Приватность допуск решение | <code>&quot;privacy_gate_decision&quot;</code> |
| 24 | Операционный статус | <code>&quot;operational_status&quot;</code> |
| 25 | Владелец | <code>&quot;owner&quot;</code> |
| 26 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 27 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:27 -->
> [!abstract]- Запись 1 из 1 — EXT-01
> - **Контакт ID** (<code>&quot;contact_id&quot;</code>): <code>&quot;EXT-01&quot;</code>
> - **«display» «alias»** (<code>&quot;display_alias&quot;</code>): <code>&quot;OUT-OF-AREA-01&quot;</code>
> - **«purpose» «codes»** (<code>&quot;purpose_codes&quot;</code>): <code>&quot;REMOTE_BUDDY|REUNIFICATION|SUCCESSION_ESCALATION&quot;</code>
> - **Отношение «or» полномочие** (<code>&quot;relationship_or_authority&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Основной «channel»** (<code>&quot;primary_channel&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«alternate» «channel»** (<code>&quot;alternate_channel&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«contingency» «channel»** (<code>&quot;contingency_channel&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Аварийный «channel»** (<code>&quot;emergency_channel&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«channel» отказ отрасль доказательство** (<code>&quot;channel_failure_domain_evidence&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«pace» испытание состояние** (<code>&quot;pace_test_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«identity» подтверждение метод** (<code>&quot;identity_verification_method&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Подтверждение состояние** (<code>&quot;verification_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Согласие состояние** (<code>&quot;consent_state&quot;</code>): <code>&quot;UNKNOWN&quot;</code>
> - **Доступность «window»** (<code>&quot;availability_window&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«missed» контакт триггер** (<code>&quot;missed_contact_trigger&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«escalation» полномочие** (<code>&quot;escalation_authority&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Юрисдикция** (<code>&quot;jurisdiction&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«sensitive» контакт ссылка** (<code>&quot;sensitive_contact_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«encryption» требуемый** (<code>&quot;encryption_required&quot;</code>): <code>&quot;YES&quot;</code>
> - **«encryption» состояние** (<code>&quot;encryption_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«access» «control» состояние** (<code>&quot;access_control_state&quot;</code>): <code>&quot;NOT_TESTED&quot;</code>
> - **«retention» «rule»** (<code>&quot;retention_rule&quot;</code>): <code>&quot;TBD_LOCAL_LAW_AND_PURPOSE&quot;</code>
> - **Приватность допуск решение** (<code>&quot;privacy_gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Операционный статус** (<code>&quot;operational_status&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Владелец** (<code>&quot;owner&quot;</code>): <code>&quot;&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Псевдоним; реальный контакт и согласие не внесены&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
