from create_bot import bot
import __init__
__init__.reg_handlers()
bot.polling(none_stop=True)