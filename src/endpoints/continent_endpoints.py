from fastapi import APIRouter
from service.continent_service import ContinentService

router = APIRouter()
continenttag=['Continent']

@router.get('/get_population_by_continent', tags=continenttag)
def get_population_by_continent(continent):
    return ContinentService.get_population_by_continent(continent)


