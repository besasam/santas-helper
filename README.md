# Santa's Helper
Discord bot for Advent of Code

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
This is my first bot so it's probably kinda bad, but if you want to help, 
you can find me on Discord at [The Code Café](https://discord.gg/QjNX9sMYAC) :coffee: