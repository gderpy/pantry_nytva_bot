import logging

from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from admin_panel.excel_parser import ExcelParser


class ExcelParserMiddleware(BaseMiddleware):
    def __init__(self):
        self.excel_parser = ExcelParser()

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        data["excel_parser"] = self.excel_parser
        self.excel_parser.bot = data.get("bot")
        self.excel_parser.chat_id = data.get("event_chat").id

        return await handler(event, data)


# {'dispatcher': <Dispatcher '0x1eca57b1f10'>,
#  'bots': (<aiogram.client.bot.Bot object at 0x000001EC9C1F8290>,),
#  'bot': <aiogram.client.bot.Bot object at 0x000001EC9C1F8290>,

#  'event_from_user': User(id=228931634, is_bot=False, first_name='Юрий', last_name=None,
#                          username='gderpov', language_code='ru', is_premium=None,
#                          added_to_attachment_menu=None, can_join_groups=None,
#                          can_read_all_group_messages=None, supports_inline_queries=None),

#  'event_chat': Chat(id=228931634, type='private', title=None, username='gderpov', first_name='Юрий',
#                     last_name=None, is_forum=None, photo=None, active_usernames=None,
#                     available_reactions=None, accent_color_id=None, background_custom_emoji_id=None,
#                     profile_accent_color_id=None, profile_background_custom_emoji_id=None,
#                     emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None,
#                     bio=None, has_private_forwards=None, has_restricted_voice_and_video_messages=None,
#                     join_to_send_messages=None, join_by_request=None, description=None,
#                     invite_link=None, pinned_message=None, permissions=None,
#                     slow_mode_delay=None, message_auto_delete_time=None,
#                     has_aggressive_anti_spam_enabled=None, has_hidden_members=None,
#                     has_protected_content=None, has_visible_history=None,
#                     sticker_set_name=None, can_set_sticker_set=None,
#                     linked_chat_id=None, location=None),

# 'fsm_storage': <aiogram.fsm.storage.memory.MemoryStorage object at 0x000001ECA57B3890>,

# 'state': <aiogram.fsm.context.FSMContext object at 0x000001ECA5A13140>,

# 'raw_state': None,

# 'handler': HandlerObject(callback=<bound method Dispatcher._listen_update of <Dispatcher
#                                   '0x1eca57b1f10'>>,
#                          awaitable=True,
#                          params={'update', 'self'},
#                          varkw=True,
#                          filters=[],
#                          flags={}),

# 'base_function': <handlers.base_functions.base_functions_engine.BaseFunctionsEngine
#                  object at 0x000001ECA57C43B0>,

# 'message_engine': <message_engine.MessageEngine object at 0x000001ECA5A10DA0>,
# 'sql_engine': <sql.sql_engine.SQLEngine object at 0x000001ECA56F1910>}