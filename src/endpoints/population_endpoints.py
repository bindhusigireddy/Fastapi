from fastapi import APIRouter
from service.population_service import PopulationService

router = APIRouter()
Populationtag=['Population']

@router.get('/get_population_by_language',tags=Populationtag)
def get_population_by_language(language):
    return PopulationService.get_population_by_language(language)