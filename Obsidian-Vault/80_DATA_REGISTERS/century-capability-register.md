---
id: "DATA-REGISTER-cd648eaa55384eb4"
type: "generated-data-register-view"
title: "Возможности столетней непрерывности"
generated: true
generated_by: "build_obsidian_data_views.py"
generator_version: "1"
source_path: "century-capability-register.csv"
source_sha256: "c58fd490d2ce6ae84fcae115fa06b2d617327dc063dc36543a4af4c4e5b1d630"
source_bytes: 17105
source_row_count: 32
source_column_count: 20
source_cell_count: 640
ignored_blank_row_count: 0
semantic_group: "CENTURY_CONTINUITY"
instruction_state: "CATALOG_ONLY_NOT_EXECUTABLE"
release_gate: "DENY"
---

<!-- backend-source: century-capability-register.csv -->

# Возможности столетней непрерывности

[[80_DATA_REGISTERS/INDEX|← Все реестры]]

> [!warning] Доказательная граница
> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.
> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.

## Сводка

- **Смысловая группа:** Преемственность и столетний горизонт
- **Записей:** 32
- **Полей в каждой записи:** 20
- **Ячеек данных, включая пустые:** 640
- **Пустых физических строк пропущено:** 0
- **Целостность источника:** SHA-256 `c58fd490d2ce6ae84fcae115fa06b2d617327dc063dc36543a4af4c4e5b1d630`
- **Состояние:** каталог; не исполнимая инструкция

## Структура полей

Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\n`, `\r`, `\t` — часть точного текстового представления.

| № | Русское пояснение | Имя backend-поля |
|---:|---|---|
| 1 | Возможность ID | <code>&quot;capability_id&quot;</code> |
| 2 | Код отрасли | <code>&quot;domain_code&quot;</code> |
| 3 | «subject» уровень | <code>&quot;subject_level&quot;</code> |
| 4 | Сервис «outcome» | <code>&quot;service_outcome&quot;</code> |
| 5 | «beneficiary» область | <code>&quot;beneficiary_scope&quot;</code> |
| 6 | Сервис единица | <code>&quot;service_unit&quot;</code> |
| 7 | «demand» «formula» | <code>&quot;demand_formula&quot;</code> |
| 8 | Минимальный сервис уровень | <code>&quot;minimum_service_level&quot;</code> |
| 9 | Зависимость возможность ID | <code>&quot;dependency_capability_ids&quot;</code> |
| 10 | Внешний зависимость класс | <code>&quot;external_dependency_class&quot;</code> |
| 11 | Максимальный «safe» «outage» | <code>&quot;maximum_safe_outage&quot;</code> |
| 12 | «regeneration» «or» замена метод | <code>&quot;regeneration_or_replacement_method&quot;</code> |
| 13 | Владелец роль ID | <code>&quot;owner_role_id&quot;</code> |
| 14 | «successor» роль ID | <code>&quot;successor_role_id&quot;</code> |
| 15 | Доказательство требуемый | <code>&quot;evidence_required&quot;</code> |
| 16 | Состояние доказательств | <code>&quot;evidence_state&quot;</code> |
| 17 | Жизненный цикл состояние | <code>&quot;lifecycle_state&quot;</code> |
| 18 | Проверка срок | <code>&quot;review_due&quot;</code> |
| 19 | Допуск решение | <code>&quot;gate_decision&quot;</code> |
| 20 | Примечания | <code>&quot;notes&quot;</code> |

## Полное содержимое

Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются.

<!-- record:1 cells:20 -->
> [!abstract]- Запись 1 из 32 — CAP-GOV-SUCCESSION — законная передача полномочий и доступа
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-GOV-SUCCESSION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;GOV&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;законная передача полномочий и доступа&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;CELL|SITE|INSTITUTION&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;SUCCESSFUL_HANDOFF&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;ONE_CURRENT_OWNER_PLUS_ACCEPTED_SUCCESSOR&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;handoff без помощи автора&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE|CAP-LAW-TENURE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;LEGAL_AND_EXTERNAL_REVIEW&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ZERO_UNOWNED_PERIOD_FOR_CRITICAL_ASSET&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;versioned charter acceptance access test&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:2 cells:20 -->
> [!abstract]- Запись 2 из 32 — CAP-GOV-SAFEGUARD — защита прав согласия и уязвимых участников
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-GOV-SAFEGUARD&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;GOV&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;защита прав согласия и уязвимых участников&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;POLICY_AND_CASE_RESPONSE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;APPLICABLE_RISKS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;grievance recusal emergency expiry&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-GOV-SUCCESSION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;LEGAL_SOCIAL_SERVICES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ZERO_TOLERANCE_FOR_ACTIVE_ABUSE&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;independent review and corrective action&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:3 cells:20 -->
> [!abstract]- Запись 3 из 32 — CAP-LAW-TENURE — действующее право владения или пользования
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-LAW-TENURE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;LEG&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;действующее право владения или пользования&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;SITE_AND_BENEFICIARIES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;VALID_RIGHT&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;EACH_CRITICAL_ASSET&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;registry title burdens reviewed&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-DOC-IDENTITY|CAP-GOV-SUCCESSION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;REGISTRY_LEGAL_COUNSEL&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_ANY_RIGHT_DEPENDENT_ACTION&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;renew verify transfer or lawfully relocate&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:4 cells:20 -->
> [!abstract]- Запись 4 из 32 — CAP-FIN-LIFECYCLE — финансирование обслуживания замены и аудита
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-FIN-LIFECYCLE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;FIN&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;финансирование обслуживания замены и аудита&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CRITICAL_CAPABILITIES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;FUNDED_REPLACEMENT_CYCLE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;LIFECYCLE_COST_PLUS_CONTINGENCY&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;no unfunded critical replacement&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;ALL_CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MARKETS_BANKS_INSURANCE&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_MAINTENANCE_DEFAULT&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;income reserve insurance and reprioritization&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:5 cells:20 -->
> [!abstract]- Запись 5 из 32 — CAP-DOC-IDENTITY — восстановимая идентичность права и записи
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-DOC-IDENTITY&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;DOC&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;восстановимая идентичность права и записи&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS_AND_ENTITY&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RESTORABLE_RECORD_SET&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;ONE_CURRENT_SET_PER_SUBJECT&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;verified copy plus lawful recovery route&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE|CAP-LAW-TENURE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;STATE_REGISTRIES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_ADMINISTRATIVE_LOSS&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;renew copies and official reissue&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:6 cells:20 -->
> [!abstract]- Запись 6 из 32 — CAP-POP-CARE — достаточная и добровольная мощность ухода
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-POP-CARE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;CARE&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;достаточная и добровольная мощность ухода&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;DEPENDENTS_AND_CAREGIVERS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;CARE_HOURS_PER_WEEK&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PROFILE_BASED_DEMAND&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;demand not above proven capacity&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-MED-PRIMARY|CAP-SHELTER&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;HEALTH_SOCIAL_NETWORK&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;PROFILE_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;train rotate recruit and external care&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:7 cells:20 -->
> [!abstract]- Запись 7 из 32 — CAP-MED-PRIMARY — непрерывный доступ к лицензированной первичной и срочной помощи
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-MED-PRIMARY&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;MED&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;непрерывный доступ к лицензированной первичной и срочной помощи&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;VERIFIED_CARE_PATH&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PERSON_CONTINUITY_PLANS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;primary emergency pharmacy referral paths&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-TRANSPORT|CAP-COMMS|CAP-DOC-IDENTITY&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;HEALTH_SYSTEM&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;PERSON_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;provider network transport and lawful supply&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:8 cells:20 -->
> [!abstract]- Запись 8 из 32 — CAP-MED-PUBLIC-HEALTH — общественное здоровье и профилактика
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-MED-PUBLIC-HEALTH&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;MED&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;общественное здоровье и профилактика&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;CONTROL_MEASURES_CURRENT&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;RISK_AND_POPULATION_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;water sanitation ventilation vaccination guidance&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE|CAP-SANITATION|CAP-AIR&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;PUBLIC_HEALTH_AUTHORITY&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;RISK_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;monitor update and external response&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:9 cells:20 -->
> [!abstract]- Запись 9 из 32 — CAP-WATER-SAFE — безопасная вода в требуемом объёме
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-WATER-SAFE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;WAT&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;безопасная вода в требуемом объёме&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;PEOPLE_ANIMALS_CRITICAL_USE&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;L_PER_DAY_VERIFIED&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PROFILE_DEMAND_PLUS_LOSSES&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;legal source quality treatment failover&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL|CAP-REPAIR|CAP-LAW-TENURE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;LAB_PERMIT_SUPPLY&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;PROFILE_AND_CLIMATE_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;protect source treat test repair alternate supply&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:10 cells:20 -->
> [!abstract]- Запись 10 из 32 — CAP-SANITATION — безопасное удаление отходов и гигиена
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-SANITATION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;SAN&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;безопасное удаление отходов и гигиена&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS_AND_ANIMALS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;PERSON_DAYS_SERVICE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PROFILE_AND_WATER_CONTEXT&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;hand hygiene toilet waste vectors&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE|CAP-ENERGY-CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MUNICIPAL_WASTE_LAB&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;LESS_THAN_ONE_DAY_FOR_CRITICAL_FAILURE&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;repair alternate containment lawful disposal&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:11 cells:20 -->
> [!abstract]- Запись 11 из 32 — CAP-FOOD-NUTRITION — питательно достаточная и безопасная пища
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-FOOD-NUTRITION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;FOOD&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;питательно достаточная и безопасная пища&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;PERSON_DAYS_BALANCED&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PERSON_PROFILE_X_DAYS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;energy protein fat micronutrients special diets&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-AGR-SOIL|CAP-AGR-SEED|CAP-WATER-SAFE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MARKET_LAB_AGRONOMY&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;PROFILE_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;rotate produce preserve trade and external supply&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:12 cells:20 -->
> [!abstract]- Запись 12 из 32 — CAP-AGR-SOIL — поддерживаемая плодородная и безопасная почва
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-AGR-SOIL&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;AGR&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;поддерживаемая плодородная и безопасная почва&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;FOOD_SYSTEM&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;PRODUCTIVE_AREA_AND_TEST&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;CROP_PLAN_AND_LOCAL_CONDITIONS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;baseline monitoring erosion contamination controls&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE|CAP-TOOLS&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;LAB_AGRONOMIST&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ONE_SEASON_WITHOUT_PLAN&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;amend protect rotate and remediate professionally&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:13 cells:20 -->
> [!abstract]- Запись 13 из 32 — CAP-AGR-SEED — жизнеспособный законный и разнообразный семенной фонд
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-AGR-SEED&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;AGR&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;жизнеспособный законный и разнообразный семенной фонд&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;FOOD_SYSTEM&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;ACCESSIONS_WITH_VIABILITY&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;CROP_PLAN_PLUS_RESEED_MARGIN&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;provenance germination regeneration safety duplicate&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-AGR-SOIL|CAP-ARCHIVE-RESTORE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;GENEBANK_SUPPLIERS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_PLANTING_WINDOW&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;test regenerate exchange and safety duplicate&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:14 cells:20 -->
> [!abstract]- Запись 14 из 32 — CAP-ANIMAL-CARE — welfare и непрерывный уход за животными
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-ANIMAL-CARE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;PET&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;welfare и непрерывный уход за животными&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;REGISTERED_ANIMALS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;ANIMAL_DAYS_SERVICE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;SPECIES_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;water feed medicine shelter transport vet&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE|CAP-FOOD-NUTRITION|CAP-MED-PRIMARY&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;VETERINARY_SYSTEM&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;SPECIES_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;rotate supplies alternate caregiver and veterinary network&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:15 cells:20 -->
> [!abstract]- Запись 15 из 32 — CAP-SHELTER — безопасное климатически пригодное жильё
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-SHELTER&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;SHEL&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;безопасное климатически пригодное жильё&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS_AND_ANIMALS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;SAFE_OCCUPANCY_CAPACITY&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PROFILE_AND_CLIMATE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;structure envelope exits temperature accessibility&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-FIRE|CAP-AIR|CAP-ENERGY-CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;ENGINEERS_REGULATORS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;CONDITION_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;maintain repair relocate&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:16 cells:20 -->
> [!abstract]- Запись 16 из 32 — CAP-FIRE — раннее обнаружение выход и пожарная безопасность
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-FIRE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;FIRE&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;раннее обнаружение выход и пожарная безопасность&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_OCCUPANTS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;VERIFIED_ESCAPE_AND_DETECTION&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;BUILDING_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;alarms exits drills professional systems&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-SHELTER|CAP-COMMS&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;FIRE_SERVICE_INSPECTOR&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ZERO_FOR_BLOCKED_EXIT&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;detect exit call service and repair&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:17 cells:20 -->
> [!abstract]- Запись 17 из 32 — CAP-AIR — приемлемый воздух вентиляция и защита от дыма/плесени
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-AIR&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;AIR&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;приемлемый воздух вентиляция и защита от дыма/плесени&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_OCCUPANTS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;VERIFIED_AIR_CONTROL&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;BUILDING_AND_HEALTH_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;ventilation filtration moisture and exposure limits&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL|CAP-SHELTER&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;LAB_HVAC_PUBLIC_HEALTH&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;HEALTH_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;ventilate filter repair leave unsafe site&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:18 cells:20 -->
> [!abstract]- Запись 18 из 32 — CAP-ENERGY-CRITICAL — энергия для измеренных критических нагрузок
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;ENE&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;энергия для измеренных критических нагрузок&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;CRITICAL_SYSTEMS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;WH_PER_DAY_AND_PEAK_W&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;MEASURED_LOAD_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;load test failover isolation replacement budget&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-REPAIR|CAP-FIN-LIFECYCLE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;GRID_FUEL_INSTALLER&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;LOAD_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;diverse sources storage manual alternatives replace components&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:19 cells:20 -->
> [!abstract]- Запись 19 из 32 — CAP-COMMS — PACE-связь и внешний check-in
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-COMMS&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;COM&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;PACE-связь и внешний check-in&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CELLS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;SUCCESSFUL_MESSAGE_PATHS&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PRIMARY_ALT_CONTINGENCY_EMERGENCY&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;different failure domains and lawful operation&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL|CAP-DOC-IDENTITY&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;TELECOM_RADIO_AUTHORITY&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;EVENT_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;change devices operators licenses and channels&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:20 cells:20 -->
> [!abstract]- Запись 20 из 32 — CAP-NAV — офлайн-навигация и проверенные маршруты
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-NAV&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;NAV&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;офлайн-навигация и проверенные маршруты&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CELLS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;CURRENT_MAP_ROUTE_SET&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;LOCATIONS_AND_SCENARIOS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;digital plus print field checks and stop criteria&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE|CAP-TRANSPORT&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MAPPING_AUTHORITIES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ROUTE_VALIDITY_WINDOW&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;update data print and field verify&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:21 cells:20 -->
> [!abstract]- Запись 21 из 32 — CAP-INFO-TRUST — достоверная информация и разделение current/history
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-INFO-TRUST&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;INFO&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;достоверная информация и разделение current/history&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_USERS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RELEASED_SOURCE_COVERAGE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;CRITICAL_DECISIONS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;issuer version jurisdiction review and gates&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE|CAP-EDUCATION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;PRIMARY_AUTHORITIES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;SOURCE_CLASS_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;review replace preserve provenance&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:22 cells:20 -->
> [!abstract]- Запись 22 из 32 — CAP-ARCHIVE-RESTORE — восстановление критического корпуса без сети
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;INFO&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;восстановление критического корпуса без сети&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;DESIGNATED_COMMUNITY&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RESTORE_SUCCESS_AND_RTO&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;L0_L1_COMPLETE_PLUS_SAMPLED_DEEP&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;fixity readers copies blank-device successor test&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ENERGY-CRITICAL|CAP-SOFTWARE-READ&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MEDIA_SOFTWARE_SUPPLIERS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ANNUAL_FOR_CRITICAL&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;replicate verify migrate and print core&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:23 cells:20 -->
> [!abstract]- Запись 23 из 32 — CAP-SOFTWARE-READ — открытие форматов и восстановление вычислительной среды
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-SOFTWARE-READ&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;CYB&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;открытие форматов и восстановление вычислительной среды&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ARCHIVE_USERS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;FORMATS_WITH_TWO_READ_PATHS&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;ALL_PRESERVATION_FORMATS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;installers licenses source build notes test files&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-ARCHIVE-RESTORE|CAP-ENERGY-CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;OPEN_SOURCE_AND_HARDWARE&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_FORMAT_OBSOLESCENCE&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;portable readers open formats emulation and migration&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:24 cells:20 -->
> [!abstract]- Запись 24 из 32 — CAP-EDUCATION — базовое и профессиональное обучение через поколения
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-EDUCATION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;базовое и профессиональное обучение через поколения&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_LEARNERS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;LEARNING_OUTCOMES_ASSESSED&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;AGE_ROLE_LANGUAGE_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;curriculum materials teacher accessibility assessment&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-INFO-TRUST|CAP-SKILL-SUCCESSION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;SCHOOLS_CERTIFIERS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;LEARNING_STAGE_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;teach assess update and external recognition&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:25 cells:20 -->
> [!abstract]- Запись 25 из 32 — CAP-SKILL-SUCCESSION — передача критических практических компетенций
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-SKILL-SUCCESSION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;EDU&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;передача критических практических компетенций&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;CRITICAL_ROLES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;DEMONSTRATED_SUCCESSOR_COVERAGE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;ONE_PER_CRITICAL_ROLE_OR_EXTERNAL_BACKUP&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;theory supervised practice assessment currency&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-EDUCATION|CAP-GOV-SUCCESSION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;CERTIFIERS_SPECIALISTS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;BEFORE_HOLDER_LOSS&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;apprenticeship assessment and repeat practice&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:26 cells:20 -->
> [!abstract]- Запись 26 из 32 — CAP-REPAIR — безопасный ремонт или замена критических систем
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-REPAIR&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;TOOL&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;безопасный ремонт или замена критических систем&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CRITICAL_ASSETS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RECOVERY_WITHIN_RTO&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;ASSET_FAILURE_MODES&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;manual BOM tools parts competence isolation&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-TOOLS|CAP-SKILL-SUCCESSION|CAP-FIN-LIFECYCLE&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;MANUFACTURERS_WORKSHOPS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;ASSET_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;standardize repair fabricate permitted parts or replace&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:27 cells:20 -->
> [!abstract]- Запись 27 из 32 — CAP-TOOLS — исправные инструменты и измерения
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-TOOLS&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;TOOL&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;исправные инструменты и измерения&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;MAINTENANCE_ROLES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;AVAILABLE_CALIBRATED_FUNCTIONS&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;TASK_AND_RISK_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;condition calibration consumables safe storage&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-REPAIR|CAP-ENERGY-CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;CALIBRATION_SUPPLIERS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;TASK_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;maintain calibrate substitute and retire&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:28 cells:20 -->
> [!abstract]- Запись 28 из 32 — CAP-TRANSPORT — законное перемещение людей и критических ресурсов
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-TRANSPORT&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;TRANS&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|SITE&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;законное перемещение людей и критических ресурсов&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_PERSONS_AND_DEPENDENTS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;PEOPLE_AND_LOAD_ROUTE_CAPACITY&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;PROFILE_ROUTE_AND_LOAD&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;vehicle walk cycle accessible alternatives&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-NAV|CAP-ENERGY-CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;ROADS_TRANSIT_REPAIR&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;EVENT_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;maintain diversify and relocate early&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:29 cells:20 -->
> [!abstract]- Запись 29 из 32 — CAP-CLIMATE-ADAPT — адаптация к измеренным климатическим траекториям
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-CLIMATE-ADAPT&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;ENV&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;SITE|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;адаптация к измеренным климатическим траекториям&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;SITE_AND_BENEFICIARIES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;TRIGGERS_WITH_ACTION_PATHS&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;MULTIPLE_OFFICIAL_PATHWAYS&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;uncertainty lock-in reversibility retreat thresholds&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-WATER-SAFE|CAP-SHELTER|CAP-RELOCATION&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;CLIMATE_AUTHORITIES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;REVIEW_AT_LEAST_5Y&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;monitor stage adaptations and relocate&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:30 cells:20 -->
> [!abstract]- Запись 30 из 32 — CAP-COMMUNITY — внешняя сеть взаимопомощи специалистов и институтов
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-COMMUNITY&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;COMM&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;внешняя сеть взаимопомощи специалистов и институтов&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CELLS&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;VERIFIED_MUTUAL_PATHS&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;CRITICAL_EXTERNAL_DEPENDENCIES&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;consent contacts capabilities exercises&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-GOV-SAFEGUARD|CAP-COMMS&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;PUBLIC_SERVICES_NEIGHBORS&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;CONTEXT_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;maintain relationships diversify and reciprocate lawfully&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:31 cells:20 -->
> [!abstract]- Запись 31 из 32 — CAP-RECOVERY — восстановление после событий и обучение на ошибках
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-RECOVERY&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;REC&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;восстановление после событий и обучение на ошибках&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_CAPABILITIES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RTO_AND_CORRECTIVE_ACTION_CLOSURE&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;IMPACT_AND_CRITICALITY&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;logs evidence AAR owners due dates&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;ALL_CRITICAL&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;INSURANCE_PUBLIC_SERVICES&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;EVENT_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;repair rebuild relocate and update baseline&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

<!-- record:32 cells:20 -->
> [!abstract]- Запись 32 из 32 — CAP-RELOCATION — безопасный законный перенос людей знаний и функций
> - **Возможность ID** (<code>&quot;capability_id&quot;</code>): <code>&quot;CAP-RELOCATION&quot;</code>
> - **Код отрасли** (<code>&quot;domain_code&quot;</code>): <code>&quot;REC&quot;</code>
> - **«subject» уровень** (<code>&quot;subject_level&quot;</code>): <code>&quot;CELL|INSTITUTION&quot;</code>
> - **Сервис «outcome»** (<code>&quot;service_outcome&quot;</code>): <code>&quot;безопасный законный перенос людей знаний и функций&quot;</code>
> - **«beneficiary» область** (<code>&quot;beneficiary_scope&quot;</code>): <code>&quot;ALL_BENEFICIARIES&quot;</code>
> - **Сервис единица** (<code>&quot;service_unit&quot;</code>): <code>&quot;RELOCATION_PATH_READY&quot;</code>
> - **«demand» «formula»** (<code>&quot;demand_formula&quot;</code>): <code>&quot;TRIGGER_AND_PROFILE&quot;</code>
> - **Минимальный сервис уровень** (<code>&quot;minimum_service_level&quot;</code>): <code>&quot;threshold authority route destination records&quot;</code>
> - **Зависимость возможность ID** (<code>&quot;dependency_capability_ids&quot;</code>): <code>&quot;CAP-TRANSPORT|CAP-NAV|CAP-DOC-IDENTITY&quot;</code>
> - **Внешний зависимость класс** (<code>&quot;external_dependency_class&quot;</code>): <code>&quot;HOST_JURISDICTION_HOUSING&quot;</code>
> - **Максимальный «safe» «outage»** (<code>&quot;maximum_safe_outage&quot;</code>): <code>&quot;TRIGGER_SPECIFIC&quot;</code>
> - **«regeneration» «or» замена метод** (<code>&quot;regeneration_or_replacement_method&quot;</code>): <code>&quot;stage move preserve rights and rebaseline&quot;</code>
> - **Владелец роль ID** (<code>&quot;owner_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **«successor» роль ID** (<code>&quot;successor_role_id&quot;</code>): <code>&quot;TBD&quot;</code>
> - **Доказательство требуемый** (<code>&quot;evidence_required&quot;</code>): <code>&quot;SEE_16_AND_18&quot;</code>
> - **Состояние доказательств** (<code>&quot;evidence_state&quot;</code>): <code>&quot;MISSING&quot;</code>
> - **Жизненный цикл состояние** (<code>&quot;lifecycle_state&quot;</code>): <code>&quot;PLANNED&quot;</code>
> - **Проверка срок** (<code>&quot;review_due&quot;</code>): <code>&quot;&quot;</code>
> - **Допуск решение** (<code>&quot;gate_decision&quot;</code>): <code>&quot;DENY&quot;</code>
> - **Примечания** (<code>&quot;notes&quot;</code>): <code>&quot;Архитектурная строка; не доказанная способность&quot;</code>
>

---

Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.
