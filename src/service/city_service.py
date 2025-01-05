from utils.db_utils import DatabaseManager

class CityService:

    
    @staticmethod
    def get_district_names():
        sql_string = "select distinct district from world.city" 
        data = DatabaseManager.execute_sql(sql_string)
        datacollector=list(map(lambda row: row[0],data))
        return datacollector



