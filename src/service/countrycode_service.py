from utils.db_utils import DatabaseManager

class CountryCodeService:

    @staticmethod
    def get_population_by_countrycode(country_code):
        sql_string = f"select population from world.country where code='{country_code}'"
        data = DatabaseManager.execute_sql(sql_string)
        a = list(map(lambda x: x[0], data))
        return a

