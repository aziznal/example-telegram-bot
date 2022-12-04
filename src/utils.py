def load_bot_token() -> str:
    with open("./private/bot_access_token.txt") as token_file:
        return token_file.read()
