from database.database_functions import *


class Payment:
    """
    a class that represent payment which is responsible for validating data before commiting to the database
    """
    def __init__(self, payment_id, camper_id = '', camp_id = '', payment_date = '', paid_amount = ''):
        """
        initialize a payment object, you can only define a payment id
        """
        self.__payment_id__ = payment_id
        self.__camper_id__ = camper_id
        self.__camp_id__ = camp_id
        self.__payment_date__ = payment_date
        self.__paid_amount__ = paid_amount

    def insert_payment(self):
        """
        insert a payment record into the db after validating
        """
        insert_payment_into_db(self.__camper_id__, self.__camp_id__, self.__payment_date__, self.__paid_amount__)

    def update_payment(self):
        """
        update a payment record to the db after validating
        """
        update_payment_to_db(self.__payment_id__, self.__camper_id__, self.__camp_id__, self.__payment_date__, self.__paid_amount__)

    def select_payment(self):
        """
        select a payment record from the db after validating
        returns a payment object
        """
        return select_payment_by_id(self.__payment_id__)

    def delete_payment(self):
        """
        delete a payment record from the db after validating
        """
        return delete_payment_by_id(self.__payment_id__)

    def get_camp_id(self):
        return self.__camper_id__

    def get_payment_date(self):
        return self.__payment_date__

    @staticmethod
    def get_all_ids():
        return get_all_payments_ids()
