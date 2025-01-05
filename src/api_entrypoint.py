from endpoints.city_endpoints import router as city_router
from endpoints.country_endpoints import router as country_router
from endpoints.countrycode_endpoints import router as countrycode_router
from endpoints.continent_endpoints import router as continent_router
from endpoints.language_endpoints import router as language_router


class ApiEntrypoint:

    def __init__(self, app):
        self.app = app
        self.setup_endpoints()

    def setup_endpoints(self):
        self.app.include_router(city_router)
        self.app.include_router(country_router)
        self.app.include_router(countrycode_router)
        self.app.include_router(continent_router)
        self.app.include_router(language_router)
