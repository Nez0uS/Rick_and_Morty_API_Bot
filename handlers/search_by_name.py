from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.main_menu import main_menu

from services.Rick_and_Morty_API import Rick_And_Morty
from keyboards.main_menu import main_menu

api = Rick_And_Morty()
router = Router()

class SearchByName(StatesGroup):
    waiting_for_search = State()


@router.callback_query(F.data == "search_by_name")
async def search_by_name(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(SearchByName.waiting_for_search)
    await callback_query.message.answer("Введите имя персонажа (пример: Rick, Morty):")

@router.message(SearchByName.waiting_for_search)
async def search_result(message: Message, state: FSMContext):
    result = await api.search_by_name(message.text)

    text = f"Результат поиска:\n\n"

    for index, character in enumerate(result):
        text += f"{index + 1}. {character['name']}\n"

    await message.answer(text, reply_markup=main_menu())
    await state.clear()
