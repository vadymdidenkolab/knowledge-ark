# QA интерактивной схемы v0.3

**Проверено:** 2026-08-29  
**Объект:** [framework-visualization.html](framework-visualization.html)  
**SHA-256:** `cc82e15397a62b9bf36347dc98e3f2acb0f5436e1cdd0cae595dc95b1dda673d`

Проверка выполнена headless Chromium через Playwright на самостоятельной HTML-копии. Основная матрица содержит 24 случая:

- viewport: 360, 736 и 1 024 px;
- theme: light и dark;
- размер группы: N=1 и N=7;
- дальний горизонт: E4 и E5.

Дополнительно программно переключены все шесть горизонтов E0–E5.

## Результаты матрицы

Во всех 24 случаях:

- select содержит ровно 6 options;
- timeline содержит ровно 6 dots;
- первый и последний dots совпадают с концами track;
- DOM summary соответствует выбранному горизонту и размеру группы;
- N=1 показывает 2 role nodes, N=7 — 7 role nodes;
- при E5 видна строка `CELL → SITE → INSTITUTION`, при E4 она скрыта;
- `rootScrollWidth = rootClientWidth` и `bodyScrollWidth = bodyClientWidth`;
- page errors: 0.

| Representative viewport/theme | Horizon | N | SVG viewBox | Role nodes | Horizontal overflow | Track endpoints |
|---:|---|---:|---|---:|---|---|
| 360 px / light | E5 | 7 | `0 0 328 875` | 7 | нет: `328 = 328` | `28…300`, dots `28…300` |
| 736 px / dark | E5 | 7 | `0 0 704 875` | 7 | нет: `704 = 704` | `28…676`, dots `28…676` |
| 1 024 px / light | E5 | 7 | `0 0 992 445` | 7 | нет: `992 = 992` | `48…944`, dots `48…944` |

## Визуальная проверка

Три representative screenshots просмотрены вручную:

- 360 px / light / N=7 / E5;
- 736 px / dark / N=7 / E5;
- 1 024 px / light / N=7 / E5.

Ключевой текст E5, timeline, functional chain, role nodes и stewardship row читаются; наложений и горизонтальной обрезки не обнаружено. На узком viewport документ закономерно прокручивается по вертикали.

## Граница доказанности

Проверка доказывает корректность отображения и программного переключения в протестированной среде. Она не доказывает физическую готовность аптечки, запасов, карт, офлайн-корпуса, action cards, людей или столетних capability outcomes.

Нативное клавиатурное взаимодействие с select в headless Chrome не включено в доказанный объём: тест использовал программное изменение select и проверку DOM. Семантика нативного элемента сохранена, но отдельный assistive-technology/keyboard audit ещё требуется.
