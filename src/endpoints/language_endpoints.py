from fastapi import APIRouter
from service.language_service import LanguageService

router = APIRouter()
languagetag = ['languagecountrycode']

@router.get('/get_language_by_countrycode', tags=languagetag)

def get_language_by_countrycode(countrycode):
    return LanguageService.get_language_by_countrycode(countrycode)