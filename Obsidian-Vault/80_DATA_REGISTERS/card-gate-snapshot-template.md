---
id: "DATA-REGISTER-f010b1c77062080d"
type: "generated-data-register-view"
title: "Снимок допуска карточки — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "card-gate-snapshot-template.csv"
source_sha256: "fa0ac466e81eba4d67339a30804b2096b5afa4a21efb5d003bbc3d4cb2e0802f"
source_bytes: 1155
source_row_count: 1
source_column_count: 30
source_cell_count: 30
ignored_blank_row_count: 0
semantic_group: "SYSTEM_READINESS"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: card-gate-snapshot-template.csv -->

# Снимок допуска карточки — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Архитектура системы, готовность и сценарии
- **Записей:** 1
- **Полей в каждой записи:** 30
- **Ячеек данных, включая пустые:** 30
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `fa0ac466e81eba4d67339a30804b2096b5afa4a21efb5d003bbc3d4cb2e0802f`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Снимок ID | <code>&quot;snapshot_id&quot;</code> |
| 2 | «card» ID | <code>&quot;card_id&quot;</code> |
| 3 | «card» версия | <code>&quot;card_version&quot;</code> |
| 4 | «event» ID | <code>&quot;event_id&quot;</code> |
| 5 | Назначение ID | <code>&quot;assignment_id&quot;</code> |
| 6 | Человек ID | <code>&quot;person_id&quot;</code> |
| 7 | Роль допуск состояние | <code>&quot;role_gate_state&quot;</code> |
| 8 | «credential» допуск состояние | <code>&quot;credential_gate_state&quot;</code> |
| 9 | «currency» допуск состояние | <code>&quot;currency_gate_state&quot;</code> |
| 10 | Область допуск состояние | <code>&quot;scope_gate_state&quot;</code> |
| 11 | Протокол допуск состояние | <code>&quot;protocol_gate_state&quot;</code> |
| 12 | Юрисдикция допуск состояние | <code>&quot;jurisdiction_gate_state&quot;</code> |
| 13 | Медицинский «direction» допуск состояние | <code>&quot;medical_direction_gate_state&quot;</code> |
| 14 | «facility» допуск состояние | <code>&quot;facility_gate_state&quot;</code> |
| 15 | Оборудование допуск состояние | <code>&quot;equipment_gate_state&quot;</code> |
| 16 | «patient» «specific» «order» допуск состояние | <code>&quot;patient_specific_order_gate_state&quot;</code> |
| 17 | Источник «provenance» допуск состояние | <code>&quot;source_provenance_gate_state&quot;</code> |
| 18 | «translation» допуск состояние | <code>&quot;translation_gate_state&quot;</code> |
| 19 | Профессиональный проверка допуск состояние | <code>&quot;professional_review_gate_state&quot;</code> |
| 20 | Приватность допуск состояние | <code>&quot;privacy_gate_state&quot;</code> |
| 21 | «all» требуемый «gates» состояние | <code>&quot;all_required_gates_state&quot;</code> |
| 22 | «computed» выпуск решение | <code>&quot;computed_release_decision&quot;</code> |
| 23 | «computed» время | <code>&quot;computed_at&quot;</code> |
| 24 | «computed» кем | <code>&quot;computed_by&quot;</code> |
| 25 | Доказательство ссылки | <code>&quot;evidence_refs&quot;</code> |
| 26 | «immutable» запись хеш | <code>&quot;immutable_record_hash&quot;</code> |
| 27 | Примечания | <code>&quot;notes&quot;</code> |
| 28 | «card» «content» SHA-256 | <code>&quot;card_content_sha256&quot;</code> |
| 29 | «card» «content» хеш «match» состояние | <code>&quot;card_content_hash_match_state&quot;</code> |
| 30 | Роль допуск запись ID | <code>&quot;role_gate_record_id&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:30 -->
> [!abstract]- Запись 1 из 1 — TBD
> - **Снимок ID** (<code>&quot;snapshot_id&quot;</code>): <code>&quot;SNAP-EXAMPLE-001&quot;</code>
> - **«card» ID** (<code>&quot;card_id&quot;</code>): <code>&quot;CARD-EXAMPLE-001&quot;</code>
> - **«card» версия** (<code>&quot;card_version&quot;</code>): <code>&quot;0.0-DRAFT&quot;</code>
> - **«event» ID** (<code>&quot;event_id&quot;</code>): <code>&quot;EVT-YYYYMMDD-001&quot;</code>
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Роль допуск состояние** (<code>&quot;role_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«credential» допуск состояние** (<code>&quot;credential_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«currency» допуск состояние** (<code>&quot;currency_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Область допуск состояние** (<code>&quot;scope_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Протокол допуск состояние** (<code>&quot;protocol_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Юрисдикция допуск состояние** (<code>&quot;jurisdiction_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Медицинский «direction» допуск состояние** (<code>&quot;medical_direction_gate_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **«facility» допуск состояние** (<code>&quot;facility_gate_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **Оборудование допуск состояние** (<code>&quot;equipment_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«patient» «specific» «order» допуск состояние** (<code>&quot;patient_specific_order_gate_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **Источник «provenance» допуск состояние** (<code>&quot;source_provenance_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«translation» допуск состояние** (<code>&quot;translation_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Профессиональный проверка допуск состояние** (<code>&quot;professional_review_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Приватность допуск состояние** (<code>&quot;privacy_gate_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **«all» требуемый «gates» состояние** (<code>&quot;all_required_gates_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
> - **«computed» выпуск решение** (<code>&quot;computed_release_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«computed» время** (<code>&quot;computed_at&quot;</code>): <code>&quot;&quot;</code>
> - **«computed» кем** (<code>&quot;computed_by&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство ссылки** (<code>&quot;evidence_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«immutable» запись хеш** (<code>&quot;immutable_record_hash&quot;</code>): <code>&quot;&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример fail-closed snapshot; NOT_APPLICABLE требует доказанной политики, а не свободного текста&quot;</code>
> - **«card» «content» SHA-256** (<code>&quot;card_content_sha256&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«card» «content» хеш «match» состояние** (<code>&quot;card_content_hash_match_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Роль допуск запись ID** (<code>&quot;role_gate_record_id&quot;</code>): <code>&quot;TBD&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
