from utils.db_utils import DatabaseManager

class PopulationService:

    @staticmethod

    def get_population_by_language(language):
        sql_string = f"SELECT SUM(a.Population) AS TotalPopulation, b.Language FROM world.country AS a LEFT JOIN world.countrylanguage AS b ON a.Code = b.CountryCode WHERE Language = '{language}' GROUP BY Language"
        data = DatabaseManager.execute_sql(sql_string)
        a = list(map(lambda x: x[0], data))
        return a
