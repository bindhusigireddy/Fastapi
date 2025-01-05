from utils.db_utils import DatabaseManager

class LanguageService:

    @staticmethod

    def get_language_by_countrycode(country_code):
        sql_string = f"select language from world.countrylanguage where CountryCode='{country_code}'"
        data = DatabaseManager.execute_sql(sql_string)
        a = list(map(lambda x: x[0], data))
        return a
