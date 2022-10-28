from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1",
    tags=["Scraping"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get(path="/scraping")
def scraping():
    return 'aqui desde scraping'

