import unittest

from slimebot_routing import build_roast_request


class RoastRoutingTests(unittest.TestCase):
    def test_mentioned_target_becomes_roast_target_not_teller(self):
        request = build_roast_request(
            text="<@UBOT> roast <@UTARGET>",
            teller_user_id="UTELLER",
            bot_user_id="UBOT",
        )

        self.assertEqual(request.target_user_ids, ["UTARGET"])
        self.assertIn("UTARGET", request.prompt)
        self.assertIn("target", request.prompt.lower())
        self.assertNotIn("UTELLER", request.prompt)

    def test_explicit_target_prompt_does_not_roast_the_request_itself(self):
        request = build_roast_request(
            text="<@UBOT> roast <@UTARGET>",
            teller_user_id="UTELLER",
            bot_user_id="UBOT",
        )

        prompt = request.prompt.lower()
        self.assertNotIn("request context", prompt)
        self.assertNotIn("requester", prompt)
        self.assertNotIn("the request", prompt)

    def test_roast_without_target_falls_back_to_teller(self):
        request = build_roast_request(
            text="<@UBOT> roast me",
            teller_user_id="UTELLER",
            bot_user_id="UBOT",
        )

        self.assertEqual(request.target_user_ids, ["UTELLER"])
        self.assertIn("UTELLER", request.prompt)


if __name__ == "__main__":
    unittest.main()
