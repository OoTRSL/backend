import unittest
import os
import data_access as dba
import settings

class TestDataAccess(unittest.TestCase):

    sampledb_path = os.path.join(settings.project_root, 'tests', 'testdata', 'smallsample.db')

    def test_create_connection(self):
        import sqlite3
        conn = dba.create_connection(self.sampledb_path)
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_build_column_list(self):
        t1 = dba._build_column_list(None)
        self.assertIsInstance(t1, str)
        self.assertEqual(t1, '*')

        t2 = dba._build_column_list(['1', '2', '3', '4'])
        self.assertIsInstance(t2, str)
        self.assertEqual(t2, '1, 2, 3, 4')

        t3 = dba._build_column_list(['1'])
        self.assertIsInstance(t3, str)
        self.assertEqual(t3, '1')

    # =============================
    # Table: racelist
    # =============================
    def test_race_exists(self):
        conn = dba.create_connection(self.sampledb_path)
        self.assertFalse(dba.race_exists(conn, None))
        self.assertFalse(dba.race_exists(conn, ''))
        self.assertFalse(dba.race_exists(conn, 'sad-mido-1234'))
        self.assertTrue(dba.race_exists(conn, 'artful-dekutree-1773'))
        conn.close()

    def test_select_racelist(self):
        conn = dba.create_connection(self.sampledb_path)
        self.assertListEqual(dba.select_racelist_by_slug(conn, 'artful-dekutree-1773'),
                             [('artful-dekutree-1773', '/ootr/artful-dekutree-1773',
                              '2023-05-27T00:32:39.177Z', 6)]
                            )
        self.assertListEqual(dba.select_racelist_by_slug(conn, 'artful-dekutree-1773', ['season']), [(6,)])
        self.assertListEqual(dba.select_racelist_by_slug(conn, 'artful-dekutree-1773', ['season', 'season']), [(6,6)])
        self.assertListEqual(dba.select_racelist_by_slug(conn, ''), [])
        conn.close()

    @unittest.skip("Not implemented")
    def test_select_all_racelist(self):
        pass

    @unittest.skip("Not implemented")
    def test_insert_racelist(self):
        pass

    # =============================
    # Table: players
    # =============================
    @unittest.skip("Not implemented")
    def test_select_player(self):
        pass

    @unittest.skip("Not implemented")
    def test_select_all_players(self):
        pass

    @unittest.skip("Not implemented")
    def test_insert_player(self):
        pass

    @unittest.skip("Not implemented")
    def test_update_players(self):
        pass

    # =============================
    # Table: entrants
    # =============================
    @unittest.skip("Not implemented")
    def test_select_entrants_by_race(self):
        pass

    @unittest.skip("Not implemented")
    def test_insert_entrant(self):
        pass

    @unittest.skip("Not implemented")
    def test_update_entrants(self):
        pass

    # =============================
    # Edit all data for a race
    # =============================
    @unittest.skip("Not implemented")
    def test_insert_new_race(self):
        pass

    @unittest.skip("Not implemented")
    def test_delete_race(self):
        pass

    # =============================
    # Table: discord_users
    # =============================
    @unittest.skip("Not implemented")
    def test_select_discord_user(self):
        pass

    @unittest.skip("Not implemented")
    def test_insert_insert_discord_user(self):
        pass

    @unittest.skip("Not implemented")
    def test_update_discord_user(self):
        pass

    # =============================
    # Table: seedlog
    # =============================
    @unittest.skip("Not implemented")
    def test_select_seedid(self):
        pass

    @unittest.skip("Not implemented")
    def test_insert_seedid(self):
        pass

    @unittest.skip("Not implemented")
    def test_delete_seedid(self):
        pass

    # self.assertIn(settings.environment, ['dev', 'prod'])
    # self.assertTrue(os.path.isdir(settings.data_dir))
    # self.assertIsInstance(settings._config, ConfigParser)