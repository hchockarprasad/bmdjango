from django.db import connection


# Sale Watcher that filters possible duplicates
class SaleWatcher(object):

    def __init__(self, voucher_id):

        self.voucher_id = voucher_id

        a = voucher_id

        # Most duplicates are created on successive vouchers so nearby vouchers are scanned
        self.possible_duplicates = [a-2, a-1, a, a+1, a+2]

    '''
    Finds possible duplicates of inventory transaction transactions
    '''
    def find_dupes(self):

        sql = (
            """SELECT outward, amount_value, batch_id, inventory_id """
            """FROM tbl_inv_tran WHERE voucher_id = ANY(ARRAY{0})"""
            """GROUP BY outward, amount_value, batch_id, inventory_id """
            """HAVING count(*) > 1;"""
        ).format(self.possible_duplicates)

        cursor = connection.cursor()

        cursor.execute(sql)

        if cursor.fetchone() is None:

            return {'status': False, 'message': 'No duplicates for found for voucher with id {0}'.format(self.voucher_id)}

        return {'status': True, 'message': 'Duplicates found for this voucher with id {0}'.format_map(self.voucher_id)}
