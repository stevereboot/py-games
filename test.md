# NBA Shot Data Project
## For Day 3 of Bloomberg Coding Workshop 2016

### Files

Filename | Description
---|---
nba_shots.py | Script to load, parse and analyze NBA shot data
kobe.json | Shot data for Kobe's 2015-16 season
lebron.json | Shot data for Lebron's 2015-16 season
steph.json | Shot data for Steph's 2015-16 season

### External Libraries Required
None

### Code Walkthrough


#### Imports
Only Python's native json library is required to parse the player data
``` python
import json		# For json parsing

```

#### Variables
Since there are 3 files to parse, the file names are stored in a list which
we will iterate through next

``` python
players = ['kobe', 'lebron', 'steph']

```

#### Player Shot Data JSON
The player data has 2 major sections:
1. Parameters: non-shot player data
2. resultSets: shot data

The shot data inside resultSets has 2 items:
1. headers: the names of fields in the corresponding data array
2. rowSet: an array of arrays containing shot data

``` python
{
  "resource": "shotchartdetail",
  "parameters": {
    "LeagueID": "00",
    "Season": "2015-16",
    "SeasonType": "Regular Season"
    ...
  },
  "resultSets": [
    {
      "name": "Shot_Chart_Detail",
      "headers": [
        "GRID_TYPE",
        "GAME_ID",
        "GAME_EVENT_ID",
        "PLAYER_ID",
        "PLAYER_NAME",
        ...
      ],
      "rowSet": [
        [
          "Shot Chart Detail",
          "0021500003",
          6,
          201939,
          "Stephen Curry",
          ...
        ],
        ...
      ]
    }
}
```

#### Loop Through Player Data Files
Inside the loop, we open the the player's json file and parse it into a
dictionary called `player_data`.  From this dictionary, we extract
the shot data headers and data and store them into variables.

``` python
for player in players:
	# Open file
	file = open(player + '.json')

	# Parse json data into dictionary
	player_data = json.load(file)

	# Extract shot data
	shot_data = player_data['resultSets'][0]

	# Data headers
	headers = shot_data['headers']

	# Shot data
	shots = shot_data['rowSet']

```

#### Aggregating Data
Continuing inside the loop, we create a new loop to aggregate field goal
statistics for the player.  The `SHOT_TYPE` field is used to distinuguish
field goals from 3 pointers.  We increment all attempts and only shots
that were made by using the `SHOT_MADE_FLAG` field.  Finally, the
field goal percentage is calculated.  Note we want float division to
calculate the percentage to precision: 

`shots_fg_perc = 1.0 * shots_fg_made / shots_fg_att`

``` python
	for shot in shots:
		# Check if shot is 2 pointer
		if shot[headers.index('SHOT_TYPE')] == '2PT Field Goal':
			# Increment attempts
			shots_fg_att += 1

			# Check if shot was made
			if shot[headers.index('SHOT_MADE_FLAG')]:
				# Increment made
				shots_fg_made += 1

		# Calculate percentage made
		shots_fg_perc = 1.0 * shots_fg_made / shots_fg_att
```
