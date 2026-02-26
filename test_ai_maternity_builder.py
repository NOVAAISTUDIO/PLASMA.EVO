import unittest

from ai_maternity_builder import FounderProfile, MaternityCompanyAI


class TestMaternityCompanyAI(unittest.TestCase):
    def setUp(self):
        self.ai = MaternityCompanyAI()
        self.profile = FounderProfile(
            company_name="BloomCare",
            country="Canada",
            core_offer="Prenatal nutrition and postpartum support",
            customer_segment="First-time mothers",
            budget_usd=10000,
            launch_timeline_months=5,
            channels=["Instagram", "Email"],
        )

    def test_budget_split_sums_to_total(self):
        split = self.ai._budget_split(10000)
        self.assertEqual(sum(split.values()), 10000)

    def test_blueprint_contains_core_fields(self):
        blueprint = self.ai.build_blueprint(self.profile)
        self.assertIn("BloomCare", blueprint)
        self.assertIn("Canada", blueprint)
        self.assertIn("Prenatal nutrition and postpartum support", blueprint)
        self.assertIn("$10,000", blueprint)


if __name__ == "__main__":
    unittest.main()
