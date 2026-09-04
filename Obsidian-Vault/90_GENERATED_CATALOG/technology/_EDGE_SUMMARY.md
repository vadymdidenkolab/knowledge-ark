---
kind: MOC_TECHNOLOGY_EDGES
generated: true
instruction_state: CATALOG_ONLY_NOT_EXECUTABLE
---

# Семантика технологических зависимостей

Типизированных рёбер: **2808**. Человекочитаемый обзор: [[20 — Рабочие разделы/07 — Области знаний и систем|области знаний и систем]].

> [!warning] Роли и service levels пока PROVISIONAL_AUTO_REVIEW_REQUIRED и не являются разрешением на работу.

## По роли

- **ALTERNATIVE:** 24
- **CONDITIONAL:** 231
- **HAZARD_ONLY:** 64
- **OPTIONAL:** 6
- **REQUIRED:** 2483

## По service level

- **SL0:** 27
- **SL1:** 2091
- **SL2:** 166
- **SL3:** 334
- **SL4:** 79
- **SL5:** 75
- **SL6:** 36

## Корневые зависимости

- **REQUIRED / SL0:** [[TEC TD-BASE|TD-BASE]]
- **REQUIRED / SL0:** [[TEC TD-WATER|TD-WATER]]
- **REQUIRED / SL1:** [[TEC TD-FOOD|TD-FOOD]]
- **REQUIRED / SL0:** [[TEC TD-SHELTER|TD-SHELTER]]
- **REQUIRED / SL1:** [[TEC TD-ENERGY|TD-ENERGY]]
- **REQUIRED / SL0:** [[TEC TD-HEALTH|TD-HEALTH]]
- **REQUIRED / SL0:** [[TEC TD-MAPS-COMMS|TD-MAPS-COMMS]]
- **REQUIRED / SL2:** [[TEC TD-KNOWLEDGE|TD-KNOWLEDGE]]
- **REQUIRED / SL0:** [[TEC TD-GOV|TD-GOV]]
- **REQUIRED / SL3:** [[TEC TD-WORKSHOP|TD-WORKSHOP]]
- **CONDITIONAL / SL2:** [[TEC TD-FUELS|TD-FUELS]] — fuel_dependent_service_present
- **REQUIRED / SL0:** [[TEC TD-PEOPLE|TD-PEOPLE]]
- **REQUIRED / SL2:** [[TEC TD-TRANSPORT|TD-TRANSPORT]]
- **REQUIRED / SL0:** [[TEC TD-SECURITY|TD-SECURITY]]
- **REQUIRED / SL3:** [[TEC TD-EDUCATION|TD-EDUCATION]]
- **CONDITIONAL / SL5:** [[TEC TD-MATERIALS-PRODUCTION|TD-MATERIALS-PRODUCTION]] — household_repair_or_intergroup_production_path_selected
- **CONDITIONAL / SL3:** [[TEC TD-CONSTRUCTION|TD-CONSTRUCTION]] — construction_or_structural_work_present
- **CONDITIONAL / SL3:** [[TEC TD-ANIMALS|TD-ANIMALS]] — animals_present
- **REQUIRED / SL2:** [[TEC TD-ENVIRONMENT|TD-ENVIRONMENT]]
- **REQUIRED / SL0:** [[TEC TD-PORTUGAL|TD-PORTUGAL]]
- **HAZARD_ONLY / SL0:** [[TEC TD-HAZARDS|TD-HAZARDS]] — always_visible_as_stop_boundary
