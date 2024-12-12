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
- Test driven development approach
- Simple, contains few assumptions:
    - Validations are simplified, only basic ones (for example score should be positive integer,
            country obviously is string, one country (team) can not play with itself.
            Validations do allow numbers dots and minuses in case if library would be used to reflect Club names,
            not countries, and German football clubs can have numbers and dots.
            Error messages returned are also simple, without dynamic attributes what the source of error is, like team or score.)
    - Uses Python dictionary to store data in memory
    - No api, database connection, no web frontend
    - Git flow simplified (no reviewers in PR etc.)

-Structure of the project:

ScorestreamPy_lib/
│
├── ScorestreamPyb/                  # Main package directory
│   ├── __init__.py                  # Makes it a package
│   ├── Match.py                     # Match class, defines Match object
│   ├── ScoreBoard.py                # ScoreBoard class, defines logic for the Scoreboard
│   └── ScoreManager                 # Utility functions for ScoreBoard class (optional class), provides easier methods 
│
├── tests/                           # Test directory
|   ├── __init___.py                 # Makes it a package
│   ├── TestMatchLogic_.py           # Unit tests for Match class, uses parametrise to unit test output
│   ├── TestBoardLogic.py            # Unit tests for ScoreBoard class, uses fixtures to check logic work
│   └── conftest.py                  # Pytest configuration (need this for better visibility when running a test)
│
├── setup.py                         # Setup script for packaging
├── pyproject.toml                   # Build configuration
├── README.md                        # Project description
├── LICENSE                          # MIT license file
└── requirements.txt                 # Dependency list


