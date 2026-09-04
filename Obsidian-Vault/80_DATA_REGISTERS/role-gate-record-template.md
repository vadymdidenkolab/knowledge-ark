---
id: "DATA-REGISTER-10dd82ea3cfa8fdc"
type: "generated-data-register-view"
title: "Допуск роли к действию — шаблон"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "role-gate-record-template.csv"
source_sha256: "b9236ca6a47b9d8d654442c2756befb58ae0e87becd3a113e3ce50377aa40d67"
source_bytes: 971
source_row_count: 1
source_column_count: 26
source_cell_count: 26
ignored_blank_row_count: 0
semantic_group: "PEOPLE_GOVERNANCE"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: role-gate-record-template.csv -->

# Допуск роли к действию — шаблон

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Люди, роли, операции и управление
- **Записей:** 1
- **Полей в каждой записи:** 26
- **Ячеек данных, включая пустые:** 26
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `b9236ca6a47b9d8d654442c2756befb58ae0e87becd3a113e3ce50377aa40d67`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Роль допуск запись ID | <code>&quot;role_gate_record_id&quot;</code> |
| 2 | Назначение ID | <code>&quot;assignment_id&quot;</code> |
| 3 | Группа профиль ID | <code>&quot;group_profile_id&quot;</code> |
| 4 | Функция код | <code>&quot;function_code&quot;</code> |
| 5 | Человек ID | <code>&quot;person_id&quot;</code> |
| 6 | Допуск правило ссылка | <code>&quot;gate_policy_ref&quot;</code> |
| 7 | «identity» подтверждение состояние | <code>&quot;identity_verification_state&quot;</code> |
| 8 | Навык «or» «credential» ссылка | <code>&quot;skill_or_credential_ref&quot;</code> |
| 9 | «credential» состояние | <code>&quot;credential_state&quot;</code> |
| 10 | «currency» состояние | <code>&quot;currency_state&quot;</code> |
| 11 | Область состояние | <code>&quot;scope_state&quot;</code> |
| 12 | Юрисдикция состояние | <code>&quot;jurisdiction_state&quot;</code> |
| 13 | Доступность состояние | <code>&quot;availability_state&quot;</code> |
| 14 | «fitness» «self» проверка состояние | <code>&quot;fitness_self_check_state&quot;</code> |
| 15 | Приёмка состояние | <code>&quot;acceptance_state&quot;</code> |
| 16 | «conflict» «of» «interest» состояние | <code>&quot;conflict_of_interest_state&quot;</code> |
| 17 | «limitations» | <code>&quot;limitations&quot;</code> |
| 18 | Подтверждённый время «utc» | <code>&quot;verified_at_utc&quot;</code> |
| 19 | «valid» до «utc» | <code>&quot;valid_until_utc&quot;</code> |
| 20 | Доказательство ссылки | <code>&quot;evidence_refs&quot;</code> |
| 21 | «all» требуемый «gates» состояние | <code>&quot;all_required_gates_state&quot;</code> |
| 22 | «computed» решение | <code>&quot;computed_decision&quot;</code> |
| 23 | «computed» кем | <code>&quot;computed_by&quot;</code> |
| 24 | «immutable» запись хеш | <code>&quot;immutable_record_hash&quot;</code> |
| 25 | Запись статус | <code>&quot;record_status&quot;</code> |
| 26 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:26 -->
> [!abstract]- Запись 1 из 1 — P01
> - **Роль допуск запись ID** (<code>&quot;role_gate_record_id&quot;</code>): <code>&quot;RGATE-EXAMPLE-001&quot;</code>
> - **Назначение ID** (<code>&quot;assignment_id&quot;</code>): <code>&quot;ASG-N1-INCIDENT&quot;</code>
> - **Группа профиль ID** (<code>&quot;group_profile_id&quot;</code>): <code>&quot;GP-N1&quot;</code>
> - **Функция код** (<code>&quot;function_code&quot;</code>): <code>&quot;INCIDENT_COORDINATION&quot;</code>
> - **Человек ID** (<code>&quot;person_id&quot;</code>): <code>&quot;P01&quot;</code>
> - **Допуск правило ссылка** (<code>&quot;gate_policy_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«identity» подтверждение состояние** (<code>&quot;identity_verification_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **Навык «or» «credential» ссылка** (<code>&quot;skill_or_credential_ref&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«credential» состояние** (<code>&quot;credential_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **«currency» состояние** (<code>&quot;currency_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **Область состояние** (<code>&quot;scope_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Юрисдикция состояние** (<code>&quot;jurisdiction_state&quot;</code>): <code>&quot;MISSING_OR_NOT_APPLICABLE_UNREVIEWED&quot;</code>
> - **Доступность состояние** (<code>&quot;availability_state&quot;</code>): <code>&quot;NOT_VERIFIED&quot;</code>
> - **«fitness» «self» проверка состояние** (<code>&quot;fitness_self_check_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **Приёмка состояние** (<code>&quot;acceptance_state&quot;</code>): <code>&quot;NOT_RECORDED&quot;</code>
> - **«conflict» «of» «interest» состояние** (<code>&quot;conflict_of_interest_state&quot;</code>): <code>&quot;NOT_REVIEWED&quot;</code>
> - **«limitations»** (<code>&quot;limitations&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Подтверждённый время «utc»** (<code>&quot;verified_at_utc&quot;</code>): <code>&quot;&quot;</code>
> - **«valid» до «utc»** (<code>&quot;valid_until_utc&quot;</code>): <code>&quot;&quot;</code>
> - **Доказательство ссылки** (<code>&quot;evidence_refs&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«all» требуемый «gates» состояние** (<code>&quot;all_required_gates_state&quot;</code>): <code>&quot;BLOCKED&quot;</code>
> - **«computed» решение** (<code>&quot;computed_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **«computed» кем** (<code>&quot;computed_by&quot;</code>): <code>&quot;&quot;</code>
> - **«immutable» запись хеш** (<code>&quot;immutable_record_hash&quot;</code>): <code>&quot;&quot;</code>
> - **Запись статус** (<code>&quot;record_status&quot;</code>): <code>&quot;DRAFT_NOT_EFFECTIVE&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Пример структуры; NOT_APPLICABLE допустим только по проверенной policy&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
