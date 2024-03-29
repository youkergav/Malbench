from datetime import date, timedelta


class Celebrations:
    """
    Represents a class for calculating and managing celebrations.

    This class provides functionality to calculate and manage various celebrations based on the given year.

    Attributes:
        year (int): The year for which celebrations are calculated.

    Methods:
        new_years(): Calculates and returns the date of New Year's Day for the given year.
    """

    def __init__(self, year: int):
        """
        Initializes a new instance of the Celebrations class.

        Args:
            year (int): The year for which celebrations are calculated.
        """

        self.year = year

    @property
    def new_years(self) -> date:
        """
        Gets the date of New Year's Day for the given year.

        Returns:
            A date object representing the date of New Year's Day.
        """

        return date(self.year, 1, 1)

    @property
    def valentines_day(self) -> date:
        """
        Gets the date of Valentine's Day Day for the given year.

        Returns:
            A date object representing the date of Valentine's Day Day.
        """

        return date(self.year, 2, 14)

    @property
    def st_patricks_day(self) -> date:
        """
        Gets the date of St. Patrick's Day for the given year.

        Returns:
            A date object representing the date of St. Patrick's Day.
        """

        return date(self.year, 3, 17)

    @property
    def birthday(self) -> date:
        """
        Gets the date of Malbench's birthday for the given year.

        Returns:
            A date object representing the date of Malbench's birthday.
        """

        return date(self.year, 4, 1)

    @property
    def easter(self) -> date:
        """
        Gets the dates of Easter for the given year.

        Returns:
            A date object representing the date of Easter.
        """

        # Calculate Easter based on Meeus/Jones/Butcher algorithm.
        a = self.year % 19
        b = self.year // 100
        c = self.year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        m = (32 + 2 * e + 2 * i - h - k) % 7
        n = (a + 11 * h + 22 * m) // 451
        p = (h + m - 7 * n + 114) // 31
        q = (h + m - 7 * n + 114) % 31

        easter_day = q + 1
        easter_month = p

        return date(self.year, easter_month, easter_day)

    @property
    def star_wars_day(self) -> date:
        """
        Get the date of Star Wars Day for the given year.

        Returns:
            A date object representing the date of Star Wars Day.
        """

        return date(self.year, 5, 4)

    @property
    def cinco_de_mayo(self) -> date:
        """
        Gets the date of Cinco de Mayo for the given year.

        Returns:
            A date object representing the date of Cinco de Mayo.
        """

        return date(self.year, 5, 5)

    @property
    def mothers_day(self):
        """
        Gets the date of Mother's Day for the given year.

        Returns:
            A date object representing the date of Mother's Day.
        """

        # Calculate the second Sunday of May (Mother's date).
        may_1st = date(self.year, 5, 1)
        may_1st_weekday = may_1st.weekday()
        days_to_second_sunday = (6 - may_1st_weekday) % 7 + 7  # Adding 7 to ensure it goes to the next week
        mothers_day = may_1st + timedelta(days=days_to_second_sunday)

        return mothers_day

    @property
    def fathers_day(self):
        """
        Gets the date of Father's Day for the given year.

        Returns:
            A date object representing the date of Father's Day.
        """

        # Calculate the third Sunday of June (Father's date).
        june_1st = date(self.year, 6, 1)
        june_1st_weekday = june_1st.weekday()
        days_to_third_sunday = (6 - june_1st_weekday) % 7 + 14  # Adding 14 to ensure it goes to the third week
        fathers_day = june_1st + timedelta(days=days_to_third_sunday)

        return fathers_day

    @property
    def labor_day(self) -> date:
        """
        Gets the date of Labor Day for the given year.

        Returns:
            A date object representing the date of Labor Day.
        """

        september_1st = date(self.year, 9, 1)
        september_1st_weekday = september_1st.weekday()
        days_to_labor_day = (7 - september_1st_weekday) % 7
        labor_day = september_1st + timedelta(days=days_to_labor_day)

        return labor_day

    @property
    def independence_day(self) -> date:
        """
        Gets the date of Independence Day for the given year.

        Returns:
            A date object representing the date of Independence Day.
        """

        return date(self.year, 7, 4)

    @property
    def halloween(self) -> date:
        """
        Gets the date of Halloween for the given year.

        Returns:
            A date object representing the date of Halloween.
        """

        return date(self.year, 10, 31)

    @property
    def thanksgiving(self) -> date:
        """
        Gets the date of Thanksgiving for the given year.

        Returns:
            A date object representing the date of Thanksgiving.
        """

        # Calculate the fourth Thursday of November (Thanksgiving date).
        november_1st = date(self.year, 11, 1)
        november_1st_weekday = november_1st.weekday()
        days_to_first_thursday = (3 - november_1st_weekday) % 7
        days_to_thanksgiving = 21 + days_to_first_thursday
        thanksgiving = november_1st + timedelta(days=days_to_thanksgiving)

        return thanksgiving

    @property
    def christmas_eve(self) -> date:
        """
        Gets the date of Christmas Eve for the given year.

        Returns:
            A date object representing the date of Christmas Eve.
        """

        return date(self.year, 12, 24)

    @property
    def christmas(self) -> date:
        """
        Gets the date of Christmas for the given year.

        Returns:
            A date object representing the date of Christmas.
        """

        return date(self.year, 12, 25)

    @property
    def new_years_eve(self) -> date:
        """
        Gets the date of New Year's Eve for the given year.

        Returns:
            A date object representing the date of New Year's Eve.
        """

        return date(self.year, 12, 31)
