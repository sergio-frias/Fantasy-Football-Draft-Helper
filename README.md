# Fantasy-Football-Draft-Helper

## Brief Background
I am a sports loving person who has been playing fantasy football for about 10 years. I also enjoy programming. This project has been a perfect marriage of the two.

## What is Fantasy Football
- A standard fantasy football league is made up of 10 teams
- Each team is composed of players from the NFL
- The teams build their rosters through the draft
- What is the draft?
  - The draft consists of about 17 rounds, depending on the league rules
  - Each round, every team selects one player to add to their roster
  - The 4 main positions that make up a fantasy football team are the Quarterback (QB), Running Back (RB), Wide Receiver (WR), and Tight End (TE)
- Each week, teams face off in head-to-head matches
- The teams with the most wins are admitted to the playoff tournament
- The winner of the single-elimination tournament is crowned champion of the season

## What Inspired this Project?
The main sites used for hosting fantasy football leagues and live drafts are ESPN and Yahoo! During the draft, the only tool they provide is a fixed list of the "best remaining available players". I find their rankings to be poorly determined, so I generally write up my own lists and cross off the players as they are selected. I rate each player based on career statistics, injury history, and their projected role on their current team. There are only 60 seconds or less for each pick, so fumbling around with these lists can be costly. For that reason I decided to write a program to manage these lists and compile a ranking of the best available players at any given time.

## Description of the Project - Big Picture
- I have created a list of the best available players
- The top 10 available players are constantly being displayed throughout the draft to keep the user updated
- The player rankings and draft advice are adjusted throughout the draft based on a few factors
  - Strategy
    - Example: I find the QB position to be the least important, so QB ratings are decreased during the early rounds of the draft
  - Scarcity
    - Example: I have also grouped players into tiers. Players at the same position with similar ratings are placed in the same tier. When a certain tier becomes scarce, the user is alerted about how many players are left available at that tier. This helps prevent the user from missing out on elite talent at a certain position.
  - Team Needs
    - Example: If the user team selects 2 RBs in the first 2 rounds, the rest of the available RBs receive a ratings decrease. This essentially boosts the ratings for the other positions in an effort to draft a well-balanced team.


