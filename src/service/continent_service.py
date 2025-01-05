from utils.db_utils import DatabaseManager

class ContinentService:

    @staticmethod
    def get_population_by_continent(continent):
        sql_string = f"select continent, SUM(population) AS total_population from world.country where continent ='{continent}' GROUP BY continent"
        data = DatabaseManager.execute_sql(sql_string)
        a = list(map(lambda x: x[1], data))
        return a[0]

