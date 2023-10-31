
#######################################################
# LDate
#
# A simple date class for *L*earning to write classes
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################

class LDate:

    # **class** method
    def is_leap_year(year: int) -> bool:
        """Return True if year is a leap year, False otherwise
           This should be a **class** method"""
        pass
        #  
 
    # **class** method
    def days_in_month(year,  month):
        """ Return the number of days in the requested month"""
        pass
        #  

    # **class** method
    def is_valid_date(year, month, day):
        """ Return whether year-month-day represents a valid date.
            This should be a **class** method """
        pass
        #  

    #  

    def __init__(self, year: int, month: int, day: int):
        """ Constructor 
            Raise a ValueError if year-month-day is not a valid date (e.g., 2022-15-27)
        """
        pass
        #  


    def ordinal_date(self) -> int:
        """ Return the number of days elapsed since the beginning of the year, including any partial days.
            For example, the ordinal date for 1 January is 1."""
        pass
        #  

    def __eq__(self, other) -> bool:
        """ return whether the two objects represent the same date.
            return False if other is not an LDate. """
        pass
        #  

    def __lt__(self, other) -> bool:
        """ return whether self < other.  
            Raise a ValueError of other is not an LDate """
        pass
        #  

    def __le__(self, other) -> bool:
        """ return whether self <= other.  
            Raise a ValueError of other is not an LDate
            Use the methods above.  Don't re-implement the < algorithm! """
        pass
        #  


    def days_since(self, other) -> bool:
        """ Return the number of days that have elapsed since other.
            (In other words, when other < self, the result should be positive.)
        """
        pass
        #  

    _DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    def day_of_week(self) -> str:
        """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
            Hint 1: 1 January 1753 was a Monday.
            Hint 2: Use the methods you've already written."""
        pass
        #  


    def __str__(self) -> str:
        """ Return this date as string of the form "Wednesday, 07 March 1833"."""
        pass
        #  

    def __add__(self, days):
        """ Return a new LDate object that is the requested number of days after self. """
        pass
        #  

    
if __name__ == '__main__':
    d1 = LDate(1941, 12, 7)
    d2 = LDate(2023, 11, 1)
    print(d1)
    print(d2)
    print(d2.days_since(d1))    