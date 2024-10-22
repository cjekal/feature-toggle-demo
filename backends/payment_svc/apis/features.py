from UnleashClient import UnleashClient

class FeaturesClient:
    _instance = None
    _unleash_client = None

    def __new__(cls):
        if not cls._instance:
            unleash_client = UnleashClient(
                url="http://unleash:4242/api/",
                app_name="payment_svc",
                custom_headers={'Authorization': '*:development.e2bb1dea54ce0c2a63151e7483d1bef0d87503385744bedef597dfe6'}
            )
            unleash_client.initialize_client()
            _unleash_client = unleash_client
            cls._instance = super(FeaturesClient, cls).__new__(cls)
        return cls._instance

    def is_enabled(self, feature_name):
        return self._unleash_client.is_enabled(feature_name)
