This repository is created as response to test assignment for Sportradar. 
Requirements:
Design a library for scoreboard that supports the following operations:
1. Start a new match, assuming initial score 0 – 0 and adding it the scoreboard.
This should capture following parameters:
a. Home team
b. Away team
2. Update score. This should receive a pair of absolute scores: home team score and away
team score.
3. Finish match currently in progress. This removes a match from the scoreboard.
4. Get a summary of matches in progress ordered by their total score. The matches with the
same total score will be returned ordered by the most recently started match in the
scoreboard.

Software characteristics:
- Library built on Python 3.11.5
- Pytest library is used for tests
- Test driven development approach
- Simple, contains few assumptions:
    - Validations are simplified, only basic ones (for example score should be integer, country obviously is string, etc. Error messages returned are also simple)
    - Uses Python dictionary to store data in memory
    - No api, database connection, no web frontend
    - Git flow simplified