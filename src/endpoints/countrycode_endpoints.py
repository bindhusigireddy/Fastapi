from fastapi import APIRouter
from service.countrycode_service import CountryCodeService

router = APIRouter()
countrycodetag=['countrycode']

@router.get('/get_population_by_countrycode', tags=countrycodetag)
def get_population_by_countrycode(country_code):
    return CountryCodeService.get_population_by_countrycode(country_code)
