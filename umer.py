import synk

target_url = "https://example.com"

# Define a test suite
class MyTestSuite(synk.TestSuite):

    # Define a test case
    def test_sql_injection(self):
        payloads = ["' OR 1=1; --", "1' OR '1'='1"]
        for payload in payloads:
            response = self.client.get(target_url, params={"user_id": payload})
            self.assertNotContains("SQL error", response.content)

# Run the test suite
synk.run(MyTestSuite)