from aiogram import F, Router
from aiogram.types import CallbackQuery

from api import Rick_And_Morty


router = Router()
api = Rick_And_Morty()

@router.callback_query(F.data == "random")
async def random_charachter():
    pass