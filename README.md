# Premier League Picture Scraping
A personal project scraping football player data

## Purpose
For a long time I have used the application [Anki](https://apps.ankiweb.net/) for learning and memorising new things. It started off as a tool to learn and pass Spanish GCSE and A Levels, but then became a bit of a hobby. 

I have always wanted to learn every footballer in the Premier League, which is their preferred foot, their position and so on.

**There are a number of public datasets, but the tricky thing is finding consistent looking images for each of players. This is where pl_pics.py comes in.**

## Methodology

#### Finding Consistent Pictures
Since I play [Fantasy Premier League](https://www.premierleague.com/), I noticed that they have a picture for almost every single player on their website. So I learnt a bit about *BeautifulSoup* and figured out how I could extract the image source for each player.

#### The Code Steps
I determined a [root url](https://www.premierleague.com/clubs) to start my script in, and then built the following steps:
 1. Pull all the team names
 2. Pull back the link to each team
 3. For each team, go to the link, pull each player, and download their image.
 
## Result
The result was that instead of me manually clicking through to each player on the Premier League website, and clicking "save image as", about ~500 times, I instead have a script that can do this for me!

## Future Development Ideas
 * Pulling other player attributes such as age, position, nationality
 * Automating the insertion / update into an Anki deck 
 * Creating functions to enable selection of player attributes, or specific players, teams


