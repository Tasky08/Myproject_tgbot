from aiogram import F, Bot, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import classes as cl
from aiogram.filters import Command
import keyboards
import functions

router = Router()
bot = Bot(token="6353580222:AAEwKxAQCwsajFFltpsMv_h-Gi_5DLUBm5w")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Добро пожаловать в бота", reply_markup=keyboards.hello_kb)

@router.callback_query(F.data == 'balance')
async def give_balance(callback: CallbackQuery):
    await bot.edit_message_text(text=f"Текущий баланс: {functions.balance}", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.balance_kb)

@router.callback_query(F.data == "back")
async def go_to_start(callback: CallbackQuery):
    await bot.edit_message_text(text="Выберите что вам нужно", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.hello_kb)

@router.callback_query(F.data == "inp_balance")
async def enter_balance(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите целое число", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.Enter_st.enter_st)

@router.message(cl.Enter_st.enter_st)
async def get_balance(message: Message, state: FSMContext):
    cur_balance = message.text

    if functions.input_balance(cur_balance) == "wrong input":
        await message.answer("Указано некорректное число", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Баланс успешно обновлен", reply_markup=keyboards.hello_kb)

    await state.clear()

@router.callback_query(F.data == "ch_categories")
async def choose_cat(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Выберите категорию", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.ch_categories_kb)

@router.callback_query(F.data == "entert")
async def enter_balance_enterteiment(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите трату(название траты и количество потраченных денег)", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.EnterString_st.cat1_st)

@router.message(cl.EnterString_st.cat1_st)
async def get_balance(message: Message, state: FSMContext):
    cur_spending = message.text

    fun_res = functions.add_categories_budget(cur_spending,0)
    if fun_res == "wrong input":
        await message.answer("Введены некорректные данные", reply_markup=keyboards.hello_kb)
    elif fun_res == "no money":
        await message.answer("Недостаточно средств", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Траты за данную категорию успешно обновлены", reply_markup=keyboards.hello_kb)

    await state.clear()


@router.callback_query(F.data == "eat")
async def enter_balance_eat(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите трату(название траты и количество потраченных денег)", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.EnterString_st.cat2_st)

@router.message(cl.EnterString_st.cat2_st)
async def get_balance(message: Message, state: FSMContext):
    cur_spending = message.text

    fun_res = functions.add_categories_budget(cur_spending, 0)
    if fun_res == "wrong input":
        await message.answer("Введены некорректные данные", reply_markup=keyboards.hello_kb)
    elif fun_res == "no money":
        await message.answer("Недостаточно средств", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Траты за данную категорию успешно обновлены", reply_markup=keyboards.hello_kb)

    await state.clear()


@router.callback_query(F.data == "transport")
async def enter_transpert_eat(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите трату(название траты и количество потраченных денег)", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.EnterString_st.cat3_st)

@router.message(cl.EnterString_st.cat3_st)
async def get_balance(message: Message, state: FSMContext):
    cur_spending = message.text

    fun_res = functions.add_categories_budget(cur_spending, 0)
    if fun_res == "wrong input":
        await message.answer("Введены некорректные данные", reply_markup=keyboards.hello_kb)
    elif fun_res == "no money":
        await message.answer("Недостаточно средств", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Траты за данную категорию успешно обновлены", reply_markup=keyboards.hello_kb)

    await state.clear()


@router.callback_query(F.data == "mont_expen")
async def enter_mont_expen_eat(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите трату(название траты и количество потраченных денег)", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.EnterString_st.cat4_st)

@router.message(cl.EnterString_st.cat4_st)
async def get_balance(message: Message, state: FSMContext):
    cur_spending = message.text

    fun_res = functions.add_categories_budget(cur_spending, 0)
    if fun_res == "wrong input":
        await message.answer("Введены некорректные данные", reply_markup=keyboards.hello_kb)
    elif fun_res == "no money":
        await message.answer("Недостаточно средств", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Траты за данную категорию успешно обновлены", reply_markup=keyboards.hello_kb)

    await state.clear()


@router.callback_query(F.data == "once_expence")
async def enter_once_expence(callback: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(text="Укажите трату(название траты и количество потраченных денег)", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

    await state.set_state(cl.EnterString_st.cat5_st)

@router.message(cl.EnterString_st.cat5_st)
async def get_balance(message: Message, state: FSMContext):
    cur_spending = message.text

    fun_res = functions.add_categories_budget(cur_spending, 0)
    if fun_res == "wrong input":
        await message.answer("Введены некорректные данные", reply_markup=keyboards.hello_kb)
    elif fun_res == "no money":
        await message.answer("Недостаточно средств", reply_markup=keyboards.hello_kb)
    else:
        await message.answer("Траты за данную категорию успешно обновлены", reply_markup=keyboards.hello_kb)

    await state.clear()

@router.callback_query(F.data == 'statistics')
async def give_stat(callback: CallbackQuery):
    await bot.edit_message_text(text=f"Статистика \n На развлечения было потрачено - {functions.categories[0]} \n на еду - {functions.categories[1]} \n на транспорт - {functions.categories[2]} \n на ежемесячные расходы - {functions.categories[3]} \n на разовые траты - {functions.categories[4]}", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=keyboards.back_kb)

