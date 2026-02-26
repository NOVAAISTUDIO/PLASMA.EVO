# Maternity Company AI Builder

A simple Python AI-style planner that generates a practical go-to-market blueprint for a maternity-focused business.

## What it does

`MaternityCompanyAI` takes a structured founder profile and outputs:
- Positioning guidance
- Product ladder roadmap
- Go-to-market sequencing
- Budget split
- Compliance/trust checklist
- KPI framework
- 90-day execution plan

## Quick start

```bash
python3 ai_maternity_builder.py
```

This runs a demo founder profile and prints a full blueprint.

## Customize for your business

Edit the `FounderProfile` in `demo()` or import the module:

```python
from ai_maternity_builder import FounderProfile, MaternityCompanyAI

planner = MaternityCompanyAI()
profile = FounderProfile(
    company_name="Your Brand",
    country="Your Country",
    core_offer="Your maternity offer",
    customer_segment="Your target segment",
    budget_usd=30000,
    launch_timeline_months=6,
    channels=["Instagram", "TikTok", "Partnerships"],
)

blueprint = planner.build_blueprint(profile)
print(blueprint)
```

## Run tests

```bash
python3 -m unittest -v
```
