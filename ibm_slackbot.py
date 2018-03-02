import os
import time
import re
from slackclient import SlackClient
import finance


# instantiate Slack client
file = open("API-key.txt", "r")
key = file.readlines()[0]
slack_client = SlackClient(key)
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "search"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def parse_search(command):
    """
    Parses a market and a stock from command
    :param command:
    :return:
    """
    market_and_stock = command.split(" ")[1].split(":")
    if len(market_and_stock) != 2:
        raise ValueError("The command should be in format Market:Stock")
    return market_and_stock[0], market_and_stock[1]


def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *help* or *search*."

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(EXAMPLE_COMMAND):
        try:
            market, stock = parse_search(command)
            response = finance.getStockQuote(market, stock)
        except (IndexError, ValueError, TypeError) as e:
            response = str(e)

    if command.startswith('help'):
        response = "This is a bot for stock price and news search. You " + \
            "can search for stock price from specified market and you " + \
            "will get a price, a list of some news about it and sentiment " + \
            "analysis on the news. If you want to know Nokia price and news " + \
            " on Nokia, you can use this bot by: " + \
            "@ibm_discovery_bot search HEL:Nokia"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")