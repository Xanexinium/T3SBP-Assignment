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
- Pytest library is used for tests, pytest 7.4.0
- SOLID approach. Thread safety implemented
- Test driven development approach

Assumptions:
- Simple, contains few assumptions:
    - Validations are simplified, only basic ones (for example score should be positive integer,
            country obviously is string, one country (team) can not play with itself.
            Validations do allow numbers dots and minuses in case if library would be used to reflect Club names,
            not countries, and German football clubs can have numbers and dots.
            Error messages returned are also simple, without dynamic attributes what the source of error is, like team or score.)
    - Uses Python dictionary to store data in memory
    - No methods to purge the scoreboard (mass close matches), mass update scores
    - No api, database connection, no web frontend
    - Git flow intentionally simplified ! (no reviewers in PR etc., one branch per functionality)

Brief usage guide: 

```
# First, import the BoardManager class from your package and can create a BoardManager instance.

# The BoardManager will automatically manage a ScoreBoard internally. 

# Use BoardManager.add_match_to_board(match.home_team, match.away_team, ID: match.match_id)
 to create a new match with the home and away teams. A unique match_id can also be optionally provided.

# Use BoardManager.update_match_score(match.match_id, home_score=3, away_score=2) to update the scores of an existing match using its match_id.

# Use finish_match(match.match_id) to finish match.

# Use BoardManager.get_scoreboard_summary() to get formatted numbered list of matches.

```

-Structure of the project:
```
ScorestreamPy_lib/
│
├── ScorestreamPyb/                  # Main package directory
│   ├── __init__.py                  # Makes it a package
│   ├── Match.py                     # Match class, defines Match object
│   ├── ScoreBoard.py                # ScoreBoard class, purpose to reflect the scoreboard
│   └── ScoreManager.py              # Manager class, methods to operate matches on the scoreboard
│
├── tests/                           # Test directory
│   ├── __init__.py                  # Makes it a package
│   ├── test_Match_Logic.py          # Unit tests for Match class
│   ├── test_Board_Logic.py          # Unit tests for ScoreBoard class
│   ├── test_Board_Manager_Logic.py  # Unit tests for BoardManager class
│   ├── test_Board_Manager_TreadSafety.py  # Thread safety tests for BoardManager
│   ├── test_Board_Thread_Safety.py  # Thread safety tests for ScoreBoard
│   └── conftest.py                  # Pytest configuration
│
├── setup.py                         # Setup script for packaging
├── pyproject.toml                   # Build configuration
├── README.md                        # Project description
├── LICENSE                          # MIT License
└── requirements.txt                 # Dependency list
```

Test coverage report
```
Name                                                           Stmts   Miss  Cover
----------------------------------------------------------------------------------
/Users/markiianprysukhin/T3SBP/ScoreStreamPy/BoardManager.py      33      8    76%
/Users/markiianprysukhin/T3SBP/ScoreStreamPy/Match.py             40      0   100%
/Users/markiianprysukhin/T3SBP/ScoreStreamPy/ScoreBoard.py        29      0   100%
/Users/markiianprysukhin/T3SBP/ScoreStreamPy/__init__.py           3      0   100%
__init__.py                                                        0      0   100%
conftest.py                                                        8      1    88%
test_Board_Logic.py                                               75      0   100%
test_Board_Manager_Logic.py                                       29      2    93%
test_Board_Manager_TreadSafety.py                                 81      4    95%
test_Board_Thread_Safety.py                                       69      2    97%
test_Match_Logic.py                                               41      0   100%
----------------------------------------------------------------------------------
TOTAL                                                            408     17    96%
```
