# Машинная модель E5: площадка, институт, преемственность и gates

## 1. Три уровня субъекта

Столетний горизонт нельзя моделировать только числом людей.

| Уровень | Код | Что это | Что не доказывает |
|---|---|---|---|
| оперативная ячейка | `CELL` | текущая группа `N=1…7`, реагирующая на событие | существование того же состава через поколение |
| площадка/имущество | `SITE` | жильё, земля, вода, энергия, мастерская, архив | законное право, пригодность или работающую организацию |
| институт stewardship | `INSTITUTION` | люди, устав, активы, succession, аудит, право и внешние связи | бессрочность, легитимность без review или гарантию результата |

Несколько `CELL` могут обслуживать один `SITE`; несколько площадок могут принадлежать или быть доступны одной `INSTITUTION`. Связи фиксируются явными IDs и revision snapshots.

## 2. Подгоризонты E5

Для аудита, а не для обещания длительности поколения:

- `E5A 15–30 лет` — первый устойчивый successor и замена ключевых технологий;
- `E5B 30–60 лет` — смена поколения, собственников/управления и нескольких media/platform cycles;
- `E5C 60–100 лет` — система должна быть понятна людям, не знавшим первоначальных создателей.

Основной код в сценариях остаётся `E5`, чтобы не размножать карточки. `E5A/B/C` используются в stewardship-аудитах.

## 3. Общий контракт revisioned-записи

Любая E5-запись, где применимо, хранит:

```text
record_id
logical_object_id
revision_id
previous_revision_id
horizon_code
jurisdiction
effective_from_utc
effective_until_utc
owner_role_id
steward_person_or_cell_id
successor_role_id
source_ids
evidence_refs
content_sha256
last_verified_at_utc
review_due_utc
privacy_class
record_state
gate_decision
notes
```

Правила:

- старые ревизии не перезаписываются;
- `record_state` не равен `gate_decision`;
- owner, steward и successor — разные сущности;
- имя преемника без согласия, компетенции, доступа и права не считается succession;
- обязательное пустое/`UNKNOWN`, просрочка, hash mismatch или неразрешённый FK дают `DENY`;
- допустимое утверждение — `ALLOW_FOR_CURRENT_REVIEW_PERIOD`, не `100_YEAR_READY`.

## 4. Обязательные реестры v0.3

### 4.1. Горизонты и capabilities

- [horizon-register.csv](horizon-register.csv) — E0–E5 и допустимые утверждения.
- [century-capability-register.csv](century-capability-register.csv) — измеримый service outcome, зависимости, maximum safe outage, владелец, преемник, evidence и текущий gate.
- [century-gate-snapshot-template.csv](century-gate-snapshot-template.csv) — агрегат всех обязательных E5-gates.

Агрегат вычисляется по худшему обязательному gate. Один критический `UNKNOWN/DENY` не превращается в «95% готовности».

### 4.2. Институт и решения

- [institution-register-template.csv](institution-register-template.csv) — цель, legal status, assets, governing document, audit/amendment/dissolution.
- [governance-policy-register-template.csv](governance-policy-register-template.csv) — quorum, supermajority, conflict/recusal, minority protection, safeguarding, grievance и emergency authority expiry.
- [succession-register-template.csv](succession-register-template.csv) — outgoing/incoming authority, acceptance, legal validation, access/knowledge package и handoff test.

Emergency authority обязана иметь точный scope, автоматическое окончание и последующий review. Внутренний устав не отменяет закон и не разрешает насилие, дискриминацию или принуждение.

### 4.3. Земля, вода, почва и семена

- [land-parcel-register-template.csv](land-parcel-register-template.csv) — кадастр/registry, title/tenure, easements, zoning, constraints и legal review.
- [water-source-capacity-template.csv](water-source-capacity-template.csv) — право доступа, сезонный yield, legal limit, quality/treatment, dependencies и failover.
- [soil-monitoring-template.csv](soil-monitoring-template.csv) — sampling protocol, laboratory, fertility/contamination и next due.
- [seed-accession-template.csv](seed-accession-template.csv) — вид/сорт, provenance, rights, storage behavior, germination, regeneration и safety duplicate.

Земельный титул не создаёт автоматически право неограниченного водозабора. Пакет семян не является семенным банком: срок и regeneration species-specific.

### 4.4. Техника и навыки

- [asset-component-lifecycle-template.csv](asset-component-lifecycle-template.csv) — модель/серия, опасности, safe isolation, BOM, repairability, firmware, tools/skills, replacement и recycling.
- [competency-lineage-template.csv](competency-lineage-template.csv) — legal/prohibited scope, theory, supervised practice, assessment, currency, primary/backup/learner.
- [population-capacity-snapshot-template.csv](population-capacity-snapshot-template.csv) — состав, care demand/capacity и service capacities без репродуктивного принуждения.
- [climate-pathway-register-template.csv](climate-pathway-register-template.csv) — источник/сценарий/неопределённость, impacts, adaptation, lock-in, retreat triggers.

Запрещены поля и практики вроде `required_births`, `approved_partner`, fertility quota или «генетического качества». Демография нужна для жилья, ухода, образования и мощности систем, а не для управления репродуктивными решениями.

### 4.5. Офлайн-архив

- [offline-corpus-manifest.csv](offline-corpus-manifest.csv) — queue и evidence внешних пакетов;
- [offline-storage-plan-template.csv](offline-storage-plan-template.csv) — копии и failure domains;
- [archive-media-register-template.csv](archive-media-register-template.csv) — устройства, состояние, чтение и retirement;
- [format-migration-register-template.csv](format-migration-register-template.csv) — before/after hashes, validation и information loss;
- [offline-restore-test-template.csv](offline-restore-test-template.csv) — blank-device restore и поиск другим человеком;
- [knowledge-succession-register-template.csv](knowledge-succession-register-template.csv) — designated community, преемник и demonstration.

## 5. Domain-gates E5

### Governance

`ALLOW` возможно, только если:

- charter versioned и известен участникам;
- полномочия, quorum, conflict/recusal, grievance и safeguarding записаны;
- emergency powers истекают автоматически;
- successor согласился и прошёл handoff;
- активы не могут быть присвоены одним человеком при dissolution.

### Право/tenure

- registry/cadastral refs разрешаются;
- holder, burdens, easements, zoning, taxes и permitted use перепроверены;
- вода и строительство проверены отдельными правовыми gates;
- succession/estate documents проверены квалифицированно в применимой юрисдикции.

### Вода

- законный доступ не `UNKNOWN`;
- спрос и подтверждённая capacity измеряются в одной единице;
- качество имеет sampling/laboratory plan;
- просроченный анализ блокирует quality gate;
- резервный законный источник/поставка не зависит от того же отказа;
- failover реально испытан.

### Почва/пища/семена

- soil baseline и протокол повторного sampling;
- contamination не выводится из запаха/цвета;
- основные культуры имеют provenance, права и локальные циклы;
- safety duplicate хранится вне общей площадки;
- рацион оценивает не только калории;
- есть внешние агрономические/лабораторные связи.

### Энергия/ремонт

- минимум полный сезон измеренных данных до `CYCLE_PROVEN`;
- критические нагрузки отделены;
- failover прошёл load-test;
- каждый опасный узел имеет isolation, manual и границу квалификации;
- replacement budget включает электронику, батареи, насосы и измерители;
- successor выполнил routine maintenance по документации.

### Здоровье/care

- проверены primary/emergency/pharmacy/referral paths;
- continuity для regular medicines, cold chain и critical devices;
- care-hour demand не превышает доказанную capacity без внешнего плана;
- medical role/scope/currency/jurisdiction разделены;
- домашнее производство рецептурных лекарств не считается capability.

### Образование/компетенции

- primary + backup/внешний специалист + learner для критической функции;
- теория, supervised practice и assessment разделены;
- assessor authority и currency записаны;
- successor находит материал и выполняет безопасную тестовую задачу;
- внутренний тест не присваивает государственную профессию.

### Архив

- package manifest, rights, edition, SHA-256 и status;
- original и derivative различаются;
- копии находятся в разных failure domains;
- fixity без unresolved mismatch;
- blank-device restore и successor recovery успешны;
- readers/installers находятся офлайн;
- obsolete/quarantined исключены из operational search.

### Климат/переезд

- несколько официальных pathways, а не одна линия;
- неопределённость сохранена;
- heat/fire/drought/flood/coastal/water triggers;
- lock-in и reversibility крупных инвестиций;
- заранее записанный relocation threshold и route.

## 6. Медленные каскады

Столетний слой обязан моделировать:

```text
потеря владельца
→ потеря ключа/полномочия
→ недоступный архив или актив
→ невозможность ремонта
→ потеря воды/энергии/жилья
```

```text
засуха
→ юридическое/физическое ограничение воды
→ деградация почвы
→ неурожай
→ питание/доход/здоровье
→ миграция
```

```text
потеря навыка
→ пропущенное обслуживание
→ скрытый дефект
→ отказ критического компонента
→ длительный outage
```

```text
захват управления
→ непрозрачный учёт
→ неравный доступ к ресурсам
→ safeguarding failure
→ конфликт/уход участников
→ институциональный распад
```

## 7. Допустимые proof states

```text
E5_ARCHITECTED
E5_BASELINE_VERIFIED
E5_CYCLE_PROVEN
E5_HANDOFF_TESTED
E5_INSTITUTIONALLY_EFFECTIVE
E5_BLOCKED
```

`E5_COMPLETE`, `PERMANENTLY_AUTONOMOUS` и `GUARANTEED_SELF_SUFFICIENT` запрещены. Даже `E5_INSTITUTIONALLY_EFFECTIVE` означает лишь, что на дату проверки действуют механизмы воспроизводства, передачи и адаптации.
