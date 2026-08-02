import unittest

from server import (
    build_chat_response,
    build_ux_bot_response,
    calculate_student_eligibility,
    get_daily_loan_metrics,
    get_ux_bot_instructions,
)


class ServerTests(unittest.TestCase):
    def test_daily_metrics_returns_integer(self):
        value = get_daily_loan_metrics()
        self.assertIsInstance(value, int)
        self.assertGreater(value, 0)

    def test_eligibility_uses_basic_risk_rules(self):
        result = calculate_student_eligibility("engineering", 35000, "US")
        self.assertEqual(result["max_amount"], 120000)
        self.assertEqual(result["baseline_interest_rate"], 6.8)

    def test_eligibility_adjusts_for_high_income(self):
        result = calculate_student_eligibility("arts", 95000, "GB")
        self.assertEqual(result["max_amount"], 65000)
        self.assertEqual(result["baseline_interest_rate"], 7.3)

    def test_ux_bot_instructions_include_principles(self):
        instructions = get_ux_bot_instructions("checkout")
        self.assertIn("clarity", instructions["focus_areas"])
        self.assertIn("reduce friction", instructions["guidance"])

    def test_build_ux_bot_response_formats_output(self):
        response = build_ux_bot_response("eligibility")
        self.assertIn("UX Bot guidance", response)
        self.assertIn("student-loan", response)
        self.assertIn("eligibility", response)

    def test_build_chat_response_returns_faq_suggestions(self):
        response = build_chat_response("What does this bot do?")
        self.assertIn("FAQ suggestions", response["reply"])
        self.assertIn("How much can I borrow for a student loan?", response["suggestions"])


if __name__ == "__main__":
    unittest.main()
