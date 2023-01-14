from fastapi import APIRouter, status

from schemas.bands import BandRead

router = APIRouter()

fake_db = [
    {"name": "Foo Fighters", "song": "My Hero"},
    {"name": "Metallica", "song": "Hero of the Day"}
]


@router.get(
    "",
    response_model=list[BandRead],
    status_code=status.HTTP_200_OK,
    name="get_bands"
)
async def get_bands() -> list[BandRead]:
    return [BandRead(**band)for band in fake_db]
