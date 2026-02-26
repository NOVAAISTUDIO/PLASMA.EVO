"""AI-guided planner for building a maternity-focused company.

This module creates practical, founder-ready strategy blueprints from a
structured company profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from textwrap import dedent
from typing import List


@dataclass
class FounderProfile:
    company_name: str
    country: str
    core_offer: str
    customer_segment: str
    budget_usd: int
    launch_timeline_months: int
    channels: List[str]


class MaternityCompanyAI:
    """Lightweight strategic planner for maternity ventures."""

    def build_blueprint(self, profile: FounderProfile) -> str:
        channels = ", ".join(profile.channels) if profile.channels else "organic social"
        budget_split = self._budget_split(profile.budget_usd)

        return dedent(
            f"""
            # {profile.company_name} — AI Company Builder Blueprint
            Generated: {date.today().isoformat()}

            ## 1) Positioning
            - Market: {profile.country}
            - Core offer: {profile.core_offer}
            - Primary customer: {profile.customer_segment}
            - Promise: "Safer, calmer, better-supported motherhood from bump to newborn."

            ## 2) Product Ladder (First 12 Months)
            1. Entry Offer (trust builder): free maternity checklist + weekly tips.
            2. Core Offer: {profile.core_offer} with measurable outcomes.
            3. Premium Offer: concierge support bundle (personalized plans, priority help, partner/family guidance).

            ## 3) Go-To-Market Channels
            Prioritized channels based on your inputs: {channels}.

            Recommended campaign sequence:
            - Month 1-2: audience research interviews + landing page waitlist.
            - Month 3-4: educational content sprint (pain-point tutorials + FAQs).
            - Month 5-6: pilot cohort with testimonials and case studies.
            - Month 7+: referral loop (partner clinics, doulas, OB-GYN communities, parenting groups).

            ## 4) Budget Allocation (${profile.budget_usd:,})
            - Product/service quality & compliance: ${budget_split['quality']:,}
            - Content + brand + website: ${budget_split['marketing_assets']:,}
            - Paid acquisition experiments: ${budget_split['acquisition_tests']:,}
            - Operations + tooling + analytics: ${budget_split['operations']:,}

            ## 5) Compliance & Trust (Non-Negotiables)
            - Distinguish education from medical advice in every customer touchpoint.
            - Add medical reviewer(s) for clinical claims.
            - Implement privacy-by-design for maternal/infant data.
            - Publish clear safety, refund, and escalation policies.

            ## 6) KPI Dashboard
            - Top funnel: waitlist growth, lead conversion rate.
            - Mid funnel: consultation/booked trial rate, cost per qualified lead.
            - Bottom funnel: monthly recurring revenue, retention, referral rate.
            - Experience: NPS, postpartum outcome/self-reported wellbeing trends.

            ## 7) 90-Day Execution Plan
            - Weeks 1-2: 20 customer interviews; validate top 3 painful problems.
            - Weeks 3-4: finalize offer messaging and MVP scope.
            - Weeks 5-8: onboard pilot customers, collect measurable before/after outcomes.
            - Weeks 9-12: optimize onboarding, pricing, and retention sequences.

            ## 8) AI Copilot Workflows You Should Run Weekly
            - Voice-of-customer mining from interview notes.
            - Offer refinement based on objections and churn reasons.
            - Content repurposing (1 expert article -> 5 social posts -> 1 email sequence).
            - KPI anomaly detection and next-week action recommendations.

            ## 9) Launch Target
            You selected a {profile.launch_timeline_months}-month timeline.
            Milestone: reach product-market signal by month {max(2, profile.launch_timeline_months - 1)}
            (>=40% of pilot users say they'd be disappointed if the service disappeared).
            """
        ).strip()

    @staticmethod
    def _budget_split(total_budget: int) -> dict:
        """Split budget across four priorities in founder-friendly proportions."""
        quality = round(total_budget * 0.35)
        marketing_assets = round(total_budget * 0.25)
        acquisition_tests = round(total_budget * 0.2)
        operations = total_budget - quality - marketing_assets - acquisition_tests
        return {
            "quality": quality,
            "marketing_assets": marketing_assets,
            "acquisition_tests": acquisition_tests,
            "operations": operations,
        }


def demo() -> None:
    planner = MaternityCompanyAI()
    profile = FounderProfile(
        company_name="NurtureNest",
        country="United States",
        core_offer="Postpartum recovery coaching + lactation education program",
        customer_segment="First-time mothers aged 26-38 in urban/suburban areas",
        budget_usd=45000,
        launch_timeline_months=6,
        channels=["Instagram", "Email", "Partnerships with doulas"],
    )
    print(planner.build_blueprint(profile))


if __name__ == "__main__":
    demo()
