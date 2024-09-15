from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait

from telethon.sessions import StringSession
from telethon import TelegramClient
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

import logging

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#-_-_-_-_-_-_-_-_-_-__-__-#

#from telethon.sync import TelegramClient
#from telethon.sessions import StringSession

API_ID = cfg.API_ID
API_HASH = cfg.API_HASH
session = cfg.SESSION
#print(f"Session string length: {len(session_string)}")
#print(f"Session string: '{session_string}'")
try:
    print ("checking session validity")
    client = TelegramClient(StringSession(session), API_ID, API_HASH)
    client.connect()
    print("Session string is valid and client is connected.")
except Exception as e:
    print(f"method 1st failed :{e}")
    print("Trying method 2")
    print(".")
    print(".")
    print(".")
    print(".")
   
#add pyrogram method here if required



    

      
 
        
#-_-_-_-__-__-_-_-__-_-_-_-_#



app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)
    
    
UserM = Client(name="AcceptUser", session_string="BQF60A4ARev2RW62XHl4Fpml-7v65zFYEge-FXS1R4ZRSeWL1jCtaNXHZc6K1sMNPKPRm5afFky7zP7v-yt1Y2-cE9iol789_8GQwFxcgx_E7EUg95a8XlKpJCXrlICA021IbUlV-Rq6lEyyc6_DzoRnZ34Oo2B5dQiOLgouxA8UTFv9thpBOt0P3buH6jQdvhTjPxztI-x4F852flZ9NM2yfjm_Cp89timCg33-hN_WEnLfIA8ArIiIKiW7FIukqP0lRlu-jPPOIkPedW5_4NSeB0EdBD8-01PiwBw7UhXM_lmGOXGVVLINYbevIypT7Th2dviICSV2Iydhe1NLsQeEJzRQAAAAGPi72fAA")
        
    
    

 #Initialize user client with StringSession
if cfg.SESSION:
    user_client = TelegramClient(
        StringSession(cfg.SESSION),
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
        if m.chat.type == enums.ChatType.PRIVATE:
            await app.get_chat_member(cfg.CHID, m.from_user.id)
        #if m.chat.type == enums.ChatType.PRIVATE:
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
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/Autoaccept_pendingrequests_mbot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.mention if m.from_user else m.chat.title), reply_markup=keyboard)
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
        logger.warning("User session is not configured.")
        await m.reply_text("User session is not configured.")
        return

    user_session_username = cfg.SESSION_USERNAME  # Assistant account username
    logger.info(f"Command received from user {m.from_user.id} in chat {m.chat.id}.")

    if m.chat.type == enums.ChatType.PRIVATE:
        logger.info(f"Private chat detected, informing user {m.from_user.id}.")
        await m.reply_text(
            f"Hi {m.from_user.mention}, use this command in your channel or group to approve pending requests."
        )
        return

    try:
        # Check if assistant has the right permissions
        user_chat_member = await app.get_chat_member(m.chat.id, user_session_username)

        if user_chat_member is None:
            logger.error(f"Could not retrieve chat member info for {user_session_username}.")
            await m.reply_text(
                f"⚠️ The assistant account @{user_session_username} could not be found in this chat. Please make sure the assistant is a member."
            )
            return

        # Check if the assistant is an admin
        if user_chat_member.status != enums.ChatMemberStatus.ADMINISTRATOR:
            logger.error(f"{user_session_username} is not an admin in {m.chat.id}.")
            await m.reply_text(
                f"⚠️ The assistant account @{user_session_username} is not an admin.\n"
                f"Please make sure the assistant has the necessary admin rights."
            )
            return

        # Check if the assistant has the 'Add Members' permission
        if not hasattr(user_chat_member, 'privileges') or not user_chat_member.privileges.can_invite_users:
            logger.error(f"{user_session_username} does not have 'Add Members' permission in {m.chat.id}.")
            await m.reply_text(
                f"⚠️ The assistant account @{user_session_username} does not have the 'Add Members' permission.\n"
                f"Please grant the assistant this permission."
            )
            return

        # Check if the bot itself is an admin with 'Add Members' permission
        bot_chat_member = await app.get_chat_member(m.chat.id, 'me')

        if bot_chat_member is None:
            logger.error("Could not retrieve bot's chat member info.")
            await m.reply_text("⚠️ I couldn't retrieve my permissions. Please ensure I'm in the chat and an admin.")
            return
        
        if bot_chat_member.status != enums.ChatMemberStatus.ADMINISTRATOR or not bot_chat_member.privileges.can_invite_users:
            logger.error(f"Bot lacks 'Add Members' permission in {m.chat.id}.")
            await m.reply_text("⚠️ I need 'Add Members' permission to approve join requests. Please grant me this permission.")
            return

        # If both bot and assistant have permissions, proceed with approval
        if not user_client:
            logger.warning("User client is not initialized.")
            await m.reply_text("User client is not available to process join requests.")
            return

        # Retrieve and process pending join requests using user_client
        pending_requests = userM.get_chat_join_requests(m.chat.id)  # This returns an async generator

        approved_count = 0

        async for request in pending_requests:
            try:
                await user_client.approve_chat_join_request(m.chat.id, request.user.id)
                approved_count += 1
                logger.info(f"Approved join request for user {request.user.id} in chat {m.chat.id}.")
                await app.send_message(request.user.id, f"Hello {request.user.mention}, your join request to {m.chat.title} has been approved!")
            except Exception as e:
                logger.error(f"Failed to approve request for user {request.user.id}: {str(e)}")

        if approved_count == 0:
            logger.info("No pending join requests to approve.")
            await m.reply_text("No pending join requests to approve.")
        else:
            logger.info(f"Approved {approved_count} pending requests.")
            await m.reply_text(f"✅ Approved `{approved_count}` pending requests.")

    except Exception as e:
        logger.error(f"Error while approving requests: {str(e)}")
        await m.reply_text(f"An error occurred while processing the command: {str(e)}")






#_-_-_-__-_-__-_-_-_--__-_--_-_-_-_--

print("I'm Alive Now!")
app.run()
