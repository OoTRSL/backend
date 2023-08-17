# RSLLeaderboard

A full stack app to automatically, efficiently, and reliably update the leaderboard for the Random Settings League in Ocarina of Time Randomizer.

## Installation
To fully set up the python environment, enter the `installation/` directory and run `sudo ./install.sh`

## Required Secrets

The following secrets should be defined:

`keys/spreadsheet_ids.ini`
```
[RatedAsync]
request_form = <google sheets id>
submit_form = <google sheets id>
```

`keys/google_sheets.json`: Google credentials file


## Available Scripts

### `scripts/generate_leaderboard.py`

This script fetches new race data from racetime.gg and computes ratings using all relevant races store in the database.

### `python scripts/fetch_google.py`

This script allows you to download and manipulate rated async data from Google Sheets.
It provides the following functionality:

- Updating existing races
- Adding a new race
- Deleting a race

#### Refresh Existing Races

To refresh the db data for all existing races, use the `--refresh` flag.
By default, the script uses the current season, but you can specify a different season with the (`-s` or `--season`) flag:

```python scripts/fetch_google.py --refresh -s <season_number>```


#### Add a New Race

To add a new race, provide the race number (`-n` or `--number`) and the recorded date (`-d` or `--date`).
By default, the script uses the current season, but you can specify a different season with the (`-s` or `--season`) flag.
If a race already has existing metadata, it will not be replaced unless the `--force` flag is used:

```python scripts/fetch_google.py --new -n <race_number> -d <recorded_date> -s <season_number> [--force]```


#### Delete a Race

To delete a race, provide the race number (`-n` or `--number`).
By default, the script uses the current season, but you can specify a different season with the (`-s` or `--season`) flag.
You can choose to delete only the database entry (`--dbonly`) or both the database entry and metadata:

```python scripts/fetch_google.py --delete -n <race_number> [--dbonly]```