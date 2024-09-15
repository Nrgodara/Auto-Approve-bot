from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from telethon.sessions import StringSession
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#-_-_-_-_-_-_-_-_-_-__-__-#

from telethon.sync import TelegramClient
#from telethon.sessions import StringSession

api_id = cfg.API_ID
api_hash = cfg.YOUR_API_HASH
session_string = cfg.SESSION  # Replace with your session string

try:
    print ("checking session validity")
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    client.start()
    print("Session string is valid and client is connected.")
except Exception as e:
    print(f"Error: {e}")
#-_-_-_-__-__-_-_-__-_-_-_-#



app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)
print(f"Session string length: {len(cfg.SESSION)}")
print(f"Session string: {cfg.SESSION}")

# Initialize user client with StringSession
if cfg.SESSION:
    user_client = Client(
        session_name=StringSession(cfg.SESSION),
        api_id=cfg.API_ID,
        api_hash=cfg.API_HASH
    )
else:
    user_client = None  # If session is not set, fallback to None


gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def handle_floodwait(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except FloodWait as e:
            print(f"Sleeping for {e.x} seconds due to FloodWait...")
            await asyncio.sleep(e.x)
            return await wrapper(*args, **kwargs)
    return wrapper




@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
@handle_floodwait
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @Mr_MAHIji__\n\nJoin This Group If you're enthusiastic to watch Movies 👉 @moviesearch_grouptelegram**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/+5orzd-iegcxiYTE1"),
                        InlineKeyboardButton("😉 Movies Group", url="https://t.me/+Pr6FsXJ15t42MTdl")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/Autoaccept_pendingrequests_mbot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/a782e3bbbe40df8a4bb67.jpg", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @Mr_MAHIji**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/Autoaccept_pendingrequests_mbot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/+5orzd-iegcxiYTE1"),
                        InlineKeyboardButton("😉 Movies Group", url="https://t.me/+Pr6FsXJ15t42MTdl")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/Autoaccept_pendingrequests_mbot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @SdBotz__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

    #_-_-_-_-__-_-_-_-_-_-__--__-_-#

@app.on_message(filters.command("approve"))
@handle_floodwait
async def approve_all_requests(_, m: Message):
    if not user_client:
        await m.reply_text("User session is not configured.")
        return
    
    user_session_username = cfg.SESSION_USERNAME  # Username of the StringSession user (for messages)

    if m.chat.type == enums.ChatType.PRIVATE:
        # Private chat: Inform the user to promote the user account to admin with a button to go to chat
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"Promote {user_session_username} to Admin", 
                        url=f"https://t.me/{user_session_username}?startgroup=true"
                    )
                ]
            ]
        )
        await m.reply_text(
            f"Hi {m.from_user.mention}, please promote [{user_session_username}](https://t.me/{user_session_username}) to admin with 'Add Members' permission in your group/channel. "
            "Make sure the 'Add Members' permission is enabled when promoting. After that, use this command in the group/channel where you want to approve pending requests.",
            reply_markup=keyboard
        )
    else:
        # Group or Channel: Check if user session has the right permissions
        try:
            if not user_client.is_connected:
                await user_client.start()

            user_chat_member = await user_client.get_chat_member(m.chat.id, user_session_username)

            if user_chat_member.status != enums.ChatMemberStatus.ADMINISTRATOR or not user_chat_member.can_invite_users:
                bot_chat_member = await app.get_chat_member(m.chat.id, 'me')

                if bot_chat_member.status == enums.ChatMemberStatus.ADMINISTRATOR and bot_chat_member.can_promote_members:
                    await app.promote_chat_member(
                        chat_id=m.chat.id,
                        user_id=user_session_username,
                        can_invite_users=True  # Grant "Add Members" permission
                    )
                    await m.reply_text(f"Promoted {user_session_username} to admin with 'Add Members' permission. Now approving pending requests...")
                else:
                    keyboard = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"Promote {user_session_username} to Admin", 
                                    url=f"https://t.me/{user_session_username}?startgroup=true"
                                )
                            ]
                        ]
                    )
                    await m.reply_text(
                        f"Hi {m.from_user.mention}, please promote [{user_session_username}](https://t.me/{user_session_username}) to admin with 'Add Members' permission and then use this command again.",
                        reply_markup=keyboard
                    )
                    return

            pending_requests = user_client.get_chat_join_requests(m.chat.id)
            approved_count = 0

            async for request in pending_requests:
                try:
                    await user_client.approve_chat_join_request(m.chat.id, request.user.id)
                    approved_count += 1

                    await app.send_message(request.user.id, f"Hello {request.user.mention}, your join request to {m.chat.title} has been approved!")
                except Exception as e:
                    logger.error(f"Failed to approve {request.user.id}: {str(e)}")

            if approved_count == 0:
                await m.reply_text("No pending join requests to approve.")
            else:
                await m.reply_text(f"✅ Approved `{approved_count}` pending requests.")

        except Exception as e:
            logger.error(f"Error while approving requests: {str(e)}")
            await m.reply_text(f"An error occurred while processing the command: {str(e)}")



#_-_-_-__-_-__-_-_-_--__-_--_-_-_-_--

print("I'm Alive Now!")
app.run()
