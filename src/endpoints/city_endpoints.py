from fastapi import APIRouter
from service.city_service import CityService


router = APIRouter()
citytag = ['City']

@router.get('/get_district_names', tags = citytag)
def get_district_names():
    return CityService.get_district_names()


