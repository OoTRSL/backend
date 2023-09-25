import unittest
import settings
import os
from configparser import ConfigParser

class TestSettings(unittest.TestCase):

    def test_load_environment(self):
        self.assertIn(settings.environment, ['dev', 'prod'])

    def test_valid_paths(self):
        self.assertTrue(os.path.isdir(settings.project_root))
        self.assertTrue(os.path.isdir(settings.data_dir))

    def test_config_loads(self):
        self.assertIsInstance(settings._config, ConfigParser)

    def test_config_contents(self):
        self.assertIsInstance(settings.current_season, int)
        self.assertTrue(settings.racelist_db_path.endswith('racelist.db'))
        self.assertTrue(settings.racelist_schema_path.endswith('create_racelist.sql'))
        self.assertTrue(settings.leaderboard_file_path.endswith('leaderboard.json'))
        self.assertTrue(settings.google_sheets_key_path.endswith('keys/google_sheets.json'))
        self.assertTrue(settings.spreadsheet_ids_path.endswith('keys/spreadsheet_ids.ini'))
        self.assertTrue(settings.rated_async_info_path.endswith('data/rated_async_info.json'))

    def test_rated_async_forms(self):
        self.assertIsInstance(settings._idconfig, ConfigParser)
        self.assertIsInstance(settings.sheets_id_ra_request, str)
        self.assertIsInstance(settings.sheets_id_ra_submit, str)

    def test_season_dates(self):
        self.assertTrue(os.path.isfile(os.path.join(settings.data_dir, 'season_dates.json')))
        self.assertIsInstance(settings.season_dates, dict)
        self.assertIsInstance(settings.season_dates[settings.current_season], tuple)