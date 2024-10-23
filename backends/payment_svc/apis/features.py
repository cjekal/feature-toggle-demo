from UnleashClient import UnleashClient

class FeaturesClient:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FeaturesClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.unleash_client = UnleashClient(
            url="http://unleash:4242/api/",
            app_name="payment_svc",
            custom_headers={'Authorization': 'default:development.fa3a8e6c5719535e800341eaed00f444dfc5dddc807ce5f4bc8e25fd'}
        )
        self.unleash_client.initialize_client()

    def is_enabled(self, feature_name):
        return self.unleash_client.is_enabled(feature_name)
