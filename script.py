class Script(object):
    START_TXT = """<b>Hello {},

My Name is <a href=https://t.me/{}>{}</a>. A Smart RoBot With Many Amazing Features. I Can Provide Movies & Help You To Manage Your Groups, Just Add Me To Your Group And Enjoy.π₯°</b>"""

    HELP_TXT = """<b>Hey {}
Here Is The Help For My Commands π.</b>"""

    HACKER_TXT = """<b>Here Is The Help For My Commands.</b>"""

    HELLP_TXT = """<b>Here Is The Help For My Commands.</b>"""

    BOTSTATUS_TXT = """Send /status for getting bot and heroku status"""

    ABOUT_TXT = """<b>HEY {} DUDE πββοΈ
π π’α΄α΄α΄α΄Ι΄α΄ Κα΄Κα΄ π</b>"""
    ABOUT_TXT = """
<b>π€ Κα΄α΄ Ι΄α΄α΄α΄: <a href='https://t.me/mcmoviesData2_Bot'>Κα΄Ι΄Ι΄Κα΄.</a>

π Κα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href='https://www.python.org/'>α΄Κα΄Κα΄Ι΄</a>

π κ°Κα΄α΄α΄α΄‘α΄Κα΄ : <a href='https://github.com/pyrogram/pyrogram'>α΄ΚΚα΄Ι’Κα΄α΄</a>

π‘ Κα΄sα΄α΄α΄ α΄Ι΄ : <a href='http://heroku.com/'>Κα΄Κα΄α΄α΄</a>

π¨βπ» α΄α΄α΄ α΄Κα΄α΄α΄Κ : <a href='https://t.me/iAmLiKu1'>α΄s ΚΙͺα΄α΄ β₯οΈ</a>

π‘ sα΄α΄Κα΄α΄ α΄α΄α΄α΄ : <a href='https://t.me/cs_cloud'>α΄ΚΙͺα΄α΄ Κα΄Κα΄</a>

π₯ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ : <a href='https://t.me/+oMiWi94WoAQ0MmY5'>Mα΄α΄ Ιͺα΄s α΄Κα΄Κ</a>

π’ α΄α΄α΄α΄α΄α΄s α΄Κα΄Ι΄Ι΄α΄Κ : <a href='https://t.me/+qdq5ZO_xDytkYzJl'>α΄α΄ α΄Κα΄Κ</a>
\n\nπ πΈππππ : <code>plz bro credit de dena</code></b>"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Nancy should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - add a filter in chat.
β’ /filters - list all the filters of a chat.
β’ /del - delete a specific filter in chat.
β’ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Nancy support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Nancy supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    JSON_TXT ="""<b>JSON</b>

Bot Send Json For All Replied Messages Using A Simple Command.

<b>Command and Usage:</b>

β /json :- Reply To Any Message To Get Json
β You Can Use This Command In Pm And Groups."""

    IPADD_TXT = """β’ /ip [text] Address Name"""

    COUNTRY_TXT = """Help: <b>COUNTRY</b>

Here is the help for County information module.

I am a country information finder.

/country [countryname] 
I can find information of any country of the world"""

    LOGO_TXT = """Help: <b>LOGO</b>

Create awesome cool logo with your name!

USAGE:
β’ /logo [text] - Create logo with given text.
β’ /logo [reply][colour] - Create logo with replied text.
β’ /logo [text]|[colour] - Create logo with text & colour.

<b>NOTE</b>:
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    CARBON_TXT = """HELP: <b>CARBON</b>

Beautify your code using carbon.now.sh!

USAGE:
β’ /carbon [text] - Create carbon from the given text.
β’ /carbon [reply] - Create carbon from the replied text.

<b>NOTE</b>:
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    IMG_TXT = """HELP: <b>TEXT-IMAGE</b>

If You Want To Make A Image Of Text Send.

USAGE:
β’ /text [text] to Get the Photo.

<b>NOTE</b>:
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    FONTS_TXT = """HELP: <b>FONTS</b>

Want Some Stylish Fonts Send.

USAGE:
β’ /font [text] Create Font with given text..

<b>NOTE</b>:
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    LOCK_TXT = """Here is the help for the <b>Locks</b> module:

<b>Admin only</b>:
Γ /lock <permission>: Lock Chat permission..
Γ /unlock <permission>: Unlock Chat permission.
Γ /locks: View Chat permission.
Γ /locktypes: Check available lock types!
Locks can be used to restrict a group's users.
Locking urls will auto-delete all messages with urls, locking stickers will delete all stickers, etc.
Locking bots will stop non-admins from adding bots to the chat.

Example:
/lock media: this locks all the media messages in the chat."""

    REPORT_TEXT = """π§πΎππ: <b><u>π±πΎππππ</u></b>

Report something wrong to group admins for review!

<b><u>π’ππππΊππ½π:</u></b>
β’ /report [reply] - Report a message to admins for review.
β’ /report [reason] - Report a message to admins with reason.
β’ @admins - Same as report command, but not a command.

<b><u>NOTE:</u></b>
β’ Nancy should have admin privillage.
β’ These commands can be used only in group.
β’ These commands can be used by any group member."""

    SONG_TXT = """Help: <b>πΌSong DownloadπΌ</b>

Song Download Module, For Those Who Love Music.

<b>π’ππππΊππ½π</b>
- /song [Song Name] - To Download Music π.

<b>Usage</b>
- Can Be Used By Everyone
- Works in bot pm."""

    VIDEO_TXT = """Help: <b>VIDEO</b>

Help You To Download Video From YouTube.

<b><u>π’ππππΊππ½π:</u></b>
β’ Type /video or /MP4 And [YouTube Link]
β’ Example:- <code>/video https://youtu.be/8FAUEv_E_xQ</code> 

<b>USAGE:</b>
β’ You Can Download Any Video From YouTube"""

    YTTHUMB_TXT = """Help: <b>YouTube Thumbnail</b>

Help To Download Any YouTube Video Thumbnail.

<b><u>π’ππππΊππ½π:</u></b>
β’ Type /ytthumb And [YouTube Link]
β’ Example:- <code>/ytthumb https://youtu.be/8FAUEv_E_xQ</code> 

<b>USAGE:</b>
β’ You Can Download From YouTube Thumbnail"""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
β’ /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
β’ Only Digits Are Allowed
β’ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    AFK_TXT = """Help: <b>AFK</b>

Away From Keyboard is to tell that you're not available!

<b>Commands and Usage:</b>
β’ /afk - Mark yourself as afk.
β’ /afk [reason] - Mark yourself as afk with reason.

NOTE:
β’ Nancy should have admin privillage.
β’ These commands can be used only in group.
β’ These commands can be used by any group member."""

    FILLINGS_TXT = """Help: <b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Replied Message.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - connect a particular chat to your PM.
β’ /disconnect  - disconnect from a chat.
β’ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
β’ /paste [text] - paste the given text on Pasty
β’ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
β’ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
β’ /id - get id of a specified user.
β’ /info  - get information about a user.
β’ /json - get the json details of a message.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage:</b>
β’ /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
β’ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
β’ /imdb  - get the film information from IMDb source.
β’ /search  - get the film information from various sources.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ More search tools can be found on inline.
β’ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
β’ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
β’ /ban - ban a user.
β’ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /mute - mute a user.
β’ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
β’ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
β’ /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works only group.
β’ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - to get the rescent errors.
β’ /stats - to get status of files in db.
β’ /delete - to delete a specific file from db.
β’ /users - to get list of my users and ids.
β’ /chats - to get list of the my chats and ids.
β’ /leave - to leave from a chat.
β’ /disable - do disable a chat.
β’ /ban_users - to ban a user.
β’ /unban_users - to unban a user.
β’ /channel - to get list of total connected channels.
β’ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**β¦οΈ READ THIS INSTRUCTION β¦οΈ**

__π£ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately π__

**π JOIN THIS CHANNEL & TRY AGAIN π**"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
β’ /throw or /dart - tπ mπΊππΎ drat 
β’ /roll or /dice - roll the dice 
β’ /goal or /shoot - to make a goal or shoot
β’ /luck or /cownd - Spin the Lucky
β’ /runs strings

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
β’ /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
β’ /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    ABOOK_TXT = """β€ πππ₯π©: π ππ½πππ»πππ
πππ πππ πππππππ π πΏπ³π΅ ππππ ππ π πππππ ππππ π πππ ππππ πππππππ β―
β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:
βͺ /audiobook: π±πΎπππ ππππ πΌππππΊππ½ ππ πΊππ π―π£π₯ ππ ππΎππΎππΊππΎ πππΎ πΊππ½ππ"""

    FILE_TXT = """β€ πππ₯π©: π₯πππΎ π²ππππΎ
ππππ ππππ πππππππ π πππ πππππ πππππ πππ ππππ π’ππ π πππππππππ ππππ π πππ ππππ ππππ π πππ πππππ ππππ πππππ π’ππ ππππ ππ ππππ πππ’ πππππππ π ππππππ ππππππ ππ
β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:
βͺ /plink - π±πΎπππ ππ πΊππ ππΎπ½ππΊ ππ ππΎπ ππππ
βͺ /pbatch - π΄ππΎ ππππ ππΊπ½ππΊ ππππ ππππ ππππ πΌππππΊππ½
βͺ /batch - To create link for multiple post
βπ€ππΊππππΎ:
/pbatch <code>https://t.me/c/1508000334/555 https://t.me/c/1508000334/557</code>"""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
β’ /song or /mp3 (songname) - download song from yt servers.
β’ /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
β’ /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    STICKER_TXT = """<b>ππ²πΉπ½ ππΌπΏ π¦ππΆπ°πΈπ²πΏ πΆπ±

β’ π¨ππ?π΄π²
To Get Sticker ID

β’ ππΌπ π§πΌ π¨ππ²
β Reply To Any Sticker [<code>/stickerid</code>]</b>"""

    CORONA_TXT ="""Help: <b>Corona</b>

<b>Here is the help for the coron information module</b>

β’ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

β’ <b>Example</b> : - /covid India"""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
β’ /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
β’ Only Digits Are Allowed
β’ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
β’ /share (text or reply to message)

<b>NOTE:</b>
β’ Nancy should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """βYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """π? Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """βI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

