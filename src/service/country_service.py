from utils.db_utils import DatabaseManager

class CountryService:

    @staticmethod
    def get_population_by_countrynames(country_name):
        sql_string = f"select population from world.country where name='{country_name}'"
        data = DatabaseManager.execute_sql(sql_string)
        a = list(map(lambda x : x[0], data))
        return a
