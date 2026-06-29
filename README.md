# Bob AI

Bob AI is a Discord self bot built around an unfiltered AI chat experience. You can modify the default personality, swap models, change join DMs, and control private blocklists from `.env`.


## Features

- **Personality-based AI chat**: Bob replies with configurable system messages and channel-level personalities.
- **Normal and insane modes**: Switch between the default chat model (filtered) and the higher-intensity model with commands.
- **Custom personalities**: Use bot commands to make Bob act in different styles per channel.
- **Image understanding**: Attached images can be described by a vision model before the chat model replies.
- **Image generation**: Generate images from prompts.
- **Image editing**: Edit an attached image from a prompt.
- **TTS voice messages**: Generate voice messages from AI responses or direct TTS commands.
- **Server owner join DM**: When Bob joins a server, it can DM the owner or highest-role fallback with information about the bot.
- **Random replies and background engagement**: Configurable random response chances and background message tasks.
- **Blocklists**: User and server blocklists are controlled from `.env`.
- **Public command list**: Use `!.!help` in Discord.

## Important Warning

This is a Discord self bot. Self bots may violate Discord's Terms of Service. Use at your own risk.

You also **cannot have `discord.py` and `discord.py-self` installed in the same Python environment**. If imports or Discord client startup fail, this is one of the first things to check.
**PLEASE DO NOT ASK ME FOR HELP SETTING THIS UP!!!!**

If needed:

```bash
pip3 uninstall discord.py
pip3 install discord.py-self
```

## Installation

Make sure Python is installed. Python 3.12 or newer is recommended.

Install the Python dependencies:

```bash
pip3 install -r requirements.txt
```

Or install them manually:

```bash
pip3 install discord.py-self aiohttp psutil
```

TTS voice messages require `ffmpeg`, because the bot converts generated MP3 audio into Discord-compatible Opus OGG.

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install -y ffmpeg
```

Check that `ffmpeg` works:

```bash
ffmpeg -version
```

On Windows or macOS, install `ffmpeg` and make sure the `ffmpeg` command is available on your PATH.

## Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` and add your tokens etc.

Required values:

- `DISCORD_BOT_TOKEN`
- `NANO_GPT_API_KEY`
- `DEZGO_API_KEY`
- `ADMIN_USER_ID`

Important optional values:

- `DEFAULT_CHAT_MODEL`
- `INSANE_CHAT_MODEL`
- `IMAGE_VISION_MODEL`
- `IMAGE_ENABLED`
- `TTS_ENABLED`
- `TTS_MODEL`
- `TTS_VOICE`
- `GUILD_OWNER_JOIN_DM_TEMPLATE`
- `GUILD_HIGHEST_ROLE_JOIN_DM_TEMPLATE`
- `BLOCKLIST_USER_IDS`
- `SERVER_BLACKLIST_IDS`
- `BYPASS_USER_IDS`
- `STATUS_ROTATION`

## API Keys And Tokens

- **Discord token**: Put your Discord token in `DISCORD_BOT_TOKEN`.
- **NanoGPT API key**: Put your NanoGPT key in `NANO_GPT_API_KEY`. This is used for chat, vision, usage checks, and TTS. https://nano-gpt.com
- **Dezgo API key**: Put your Dezgo key in `DEZGO_API_KEY`. This is used for image generation and image editing. https://dezgo.com/

The old ZukiJourney setup is no longer relevant for this version.

## Running The Bot

Run the public bot file:

```bash
python3 bot_public.py
```

On Windows, depending on your Python install:

```powershell
python bot_public.py
```

You can also run the supervisor if you want the bot process restarted after crashes:

```bash
python3 supervisor.py
```

## Commands

Use this in Discord to see the current command list:

```text
!.!help
```

Common commands include:

- `!.!help`
- `!.!personalities`
- `!.!personality [name]`
- `!.!type [text|tts]`
- `!.!short`
- `!.!long`
- `!.!insane`
- `!.!normal`
- `!.!reset`
- `!.!tts [text]`
- `!.!image [prompt]`
- `!.!edit [prompt]` with an image attachment

Admin-only commands use `ADMIN_USER_ID` from `.env`.
- `!.!send [channel ID] [instructions to AI]`
- `!.!dm [user ID] [ instructions to AI]`

## Dependencies

`requirements.txt` is correct for the current imports:

- `aiohttp`
- `discord.py-self`
- `psutil`

The bot uses only standard-library modules besides those packages. It also loads `.env` by itself, so `python-dotenv` is not required.
