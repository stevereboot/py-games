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
The main steps are

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
