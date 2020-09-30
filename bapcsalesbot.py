import discord
import praw
from discord.ext import commands
# a simple bot with the function to produce the most recent post in the sub r/bapcsalescanada given a search query.

TOKEN = ""
reddit_ID = ""
reddit_secret = ""
reddit_username = ""
reddit_password = ""

reddit = praw.Reddit(client_id = reddit_ID,
                     client_secret = reddit_secret = "",
                     username = reddit_username,
                     password = reddit_password,
                     user_agent = "")

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def bapcsales(ctx, search_query, sort_by, num_posts):
    subreddit = reddit.subreddit("bapcsalescanada")
    submission_list = []
    for submission in subreddit.search(query = search_query,
                                       limit = int(num_posts),
                                       sort = sort_by,
                                       time_filter = 'all'):
        post = discord.Embed(title = submission.title)
        if hasattr(submission, 'preview') == True:
            post.set_thumbnail(url = submission.preview['images'][0]['source']['url'])
        post.url = submission.url
        post.set_author(name = '{} Upvotes, {} Comments'.format(submission.score, submission.num_comments),
                        url='https://www.reddit.com{}'.format(submission.permalink),
                        icon_url = 'https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png')
        post.set_footer(text ='r/bapcsalescanada')
        await ctx.send(embed = post)

client.run(TOKEN)
