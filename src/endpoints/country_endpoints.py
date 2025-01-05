from fastapi import APIRouter
from service.country_service import CountryService

router = APIRouter()
countrytag = ['country']

@router.get('/get_population_by_country_name', tags=countrytag)
def get_population(country_name):
    return CountryService.get_population_by_countrynames(country_name)

