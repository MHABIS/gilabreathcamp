from database.database_functions import *


class Bunkhouse(object):
    """docstring for bunkhouse."""
    def __init__(self, campers_gender, camp_id, num_campers = 12):
        self.__campers_gender__ = campers_gender
        self.__camp_id__ = camp_id
        self.__num_campers__ = num_campers

    def insert_bunkhouse(self):
        insert_bunkhouse_db(self.__campers_gender__, self.__camp_id__, self.__num_campers__)

    @staticmethod
    def get_available_bunkgouses(gender, camp_id):
        return select_available_bunkhouse(gender, camp_id)

    @staticmethod
    def insert_check_in(camper_id,camp_id,team_id,bunk_house_id):
        insert_check_in_record(camper_id,camp_id,team_id,bunk_house_id)

    @staticmethod
    def increment_checked_in(bunkhouse_id):
        increment_checked_in_num_bunkhouse(bunkhouse_id)

    @staticmethod
    def decrement_checked_in(bunkhouse_id):
        decrement_checked_in_num_bunkhouse(bunkhouse_id)

    @staticmethod
    def select_camp_team_bunkhouse(camper_id):
        data = select_camp_team_bunkhouse_db(camper_id)
        camps = ''
        teams = ''
        bunkhouses = ''
        for camp_id, team_id, bunk_house_id in data:
            camps += str(camp_id) + ', '
            teams += str(team_id) + ', '
            bunkhouses += str(bunk_house_id) + ', '
        return camps, teams, bunkhouses

    @staticmethod
    def update_bunkhouses_num(num):
        update_bunkhouses_num_db(num)

    @staticmethod
    def get_all_ids():
        return get_all_bunkhouses_id_db()

    @staticmethod
    def select_bunkhouse(bunkhouse_id):
        return select_bunkhouse_by_id(bunkhouse_id)

    @staticmethod
    def update_bunkhouse_id(camper_id, camp_id, bunkhouse_id):
        update_bunkhouse_id_checked_in(camper_id, camp_id, bunkhouse_id)
