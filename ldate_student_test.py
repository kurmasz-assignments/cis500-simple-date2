####################################################
# LDate
#
# Unit tests for LDate
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################

import unittest
import ldate

class LDateStudentTest(unittest.TestCase):

    #
    # isLeapYear
    #

    def test_a_is_leap_year1(self):
        self.assertTrue(ldate.LDate.is_leap_year(1984))

    def test_a_is_leap_year2(self):
        self.assertFalse(ldate.LDate.is_leap_year(1985))

    #
    # is_valid_date
    #

    def test_b_is_valid_date_month_is_0(self):
        self.assertFalse(ldate.LDate.is_valid_date(2022, 0, 7))

    #
    # equal
    #
    def test_c_is_equal_1(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 == d2)

    def test_c_is_equal_2(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 6, 5)
        self.assertFalse(d1 == d2) 

    #
    # less than
    #
    # IMPORTANT: You need more of these than you think.
    # Think of all the different combinations of month, day, 
    # and year with respect to <


    def test_d_lt_1(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 < d2)

    def test_d_lt_2(self):
        d1 = ldate.LDate(2022, 5, 6)
        d2 = ldate.LDate(2022, 5, 5)
        self.assertFalse(d1 < d2)

    #
    # less than or equal to
    #

    def test_e_le_1(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 6)
        self.assertTrue(d1 <= d2)

    def test_e_le_2(self):
        d1 = ldate.LDate(2022, 5, 5)
        d2 = ldate.LDate(2022, 5, 5)
        self.assertTrue(d1 <= d2)

    #
    #  ordinal_date
    #
    
    def test_f_ordinal_date1(self):
        d = ldate.LDate(1997, 1, 1)
        self.assertEqual(1, d.ordinal_date())

    def test_g_ordinal_date2(self):
        d = ldate.LDate(1995, 2, 1)
        self.assertEqual(32, d.ordinal_date())


    #
    # days_since  
    #
    def test_h_days_since_same_month(self):
        d1 = ldate.LDate(1997, 3, 10)
        d2 = ldate.LDate(1997, 3, 17)
        self.assertEqual(7, d2.days_since(d1))

    def test_g_days_since_next_month(self):
        d1 = ldate.LDate(1997, 3, 10)
        d2 = ldate.LDate(1997, 4, 17)
        self.assertEqual(38, d2.days_since(d1))


    #
    # day_of_week
    #
    def test_i_day_of_week(self):
        d1 = ldate.LDate(2023, 10, 31)
        self.assertEqual('Tuesday', d1.day_of_week())

    #
    # __str__
    #
    def test_j_str1(self):
        d1 = ldate.LDate(2023, 10, 31)
        self.assertEqual('Tuesday, 31 October 2023', d1.__str__())
    

    #
    # constructor
    #
    def test_k_constructor_raises_on_bad_date1(self):
    
        # verify that the constructor raises ValueError
        # when passed values that do not correspond to 
        # a valid date.
        with self.assertRaises(ValueError):
            ldate.LDate(1997, 5, 32)

if __name__ == '__main__':
    unittest.main(failfast=True)    