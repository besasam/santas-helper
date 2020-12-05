# Santa's Helper
Discord bot for Advent of Code

## Usage
While the core features are still being developed, the bot will not be available publicly yet.

To run it locally: Clone this repo, create a `.env` file in the root directory 
containing `DISCORD_TOKEN=your_bot_token`, make sure you have all packages installed
and run `bot.py`. 

But please keep in mind that some commands are not fully implemented yet
and might lead to errors or undesired behavior.

## Commands Reference
* __Levels__
  * `aoc!level`: Get link to today's level
  * `aoc!level <day>`: Get link to level in current year
  * `aoc!level <year> <day>`: Get link to level in previous year
* __Leaderboard__
  * `aoc!init <id>`: Initialize leaderboard for this server (`id` is user id of leaderboard owner on AoC)
  * `aoc!setcode <code>`: Set join code for leaderboard
  * `aoc!code`: Get join code
  * `aoc!join <id>`: Join server's leaderboard (`id` is your own user id on AoC)

## To Do
- [x] Get link to level
- [ ] Get level name/description
- [ ] Get server leaderboard (via AoC API)
- [ ] Get user's scores
- [ ] Limit commands (like `code` or `join`) to specific roles
- [ ] Connect GitHub
- [ ] Get user's solutions for level (if they have a GitHub connection)
- [ ] Find a way to cache leaderboard (AoC limits API requests)
- [ ] Figure out a better way to save and access data in general lol
- [ ] Hosting? Deployment? What's that?

## Contributing
This is my first bot so it's probably kinda bad, but feel free to report any issue 
you might find or even make a pull request. Check open issues or look for `TODO`s 
in the code to see what still needs to be done. And if you want to chat, you can 
find me on Discord at [The Code Café](https://discord.gg/QjNX9sMYAC) :coffee: