"""Every Person is Unique

    https://py.checkio.org/en/mission/every-person-is-unique/

    Every year, the number of your friends is increasing and monitoring
    information about their lives is becoming more difficult.
    Let's simplify and slightly automate this process.
    Indeed, the simplification of routine processes is one of the key
    programming tasks.

    You have to create a class ‘Person’ and a few methods to work with
    its instances. See the class description below.

    class Person(first_name, last_name, birth_date, job, working_years,
                salary, country, city, gender='unknown')

    It returns a new instance of the ‘Person’ class with
    the name and surname [first_name, last_name],
    date of birth - birth_date (in 'dd.mm.yyyy' format),
    current job - job, number of working years - working_years,
    average salary - salary (per month),
    current country and city - [country, city] and gender - gender.
    The gender parameter could be 'male' or 'female'.
    If this parameter is undefined, the default value is - 'unknown'.

    Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
            ‘Canada’, ‘Vancouver’, ‘male’) ==
    Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
            ‘Canada’, ‘Vancouver’, ‘male’)

    Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2,
            2150, ‘Austria’, ‘Vienna’) ==
    Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2,
            2150, ‘Austria’, ‘Vienna’, ‘unknown’)

    name()
    Returns the full name (name and surname, separated by a whitespace).

    Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’,
            ‘Vancouver’, ‘male’).name() == ‘John Smith’

    age()
    Returns the person’s age - the number of fully lived years.
    (The current date is 01.01.2018)

    Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
            ‘Canada’, ‘Vancouver’, ‘male’).age() == 38

    work()
    Returns the person’s job in a sentence as follows: ‘He is a ...’ (if male)
    ‘She is a ...’ (if female) ‘Is a ...’ (if unknown)

    Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150,
            ‘Austria’, ‘Vienna’).work() == ‘Is a designer’

    money()
    Returns an amount of money, earned during the working years.
    It should be returned in format xx xxx … - every 3 decimal
    places should be separated by a whitespace.
    For example: ‘10 568’ ‘1 051 422’

    Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600,
            ‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648 000’

    home()
    Returns the country and the city where a person lives: ‘Lives in the city, country’

    Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2,
            2150, ‘Austria’, ‘Vienna’).home() == ‘Lives in Vienna, Austria’

    In this mission all data will be correct and you won't need
    to implement the value checking.

    Input: Statements and expressions that use the ‘Person’ class.
    Output: The behavior of an instance as described above.

    Precondition: All data is correct.
"""

from dataclasses import dataclass, field
import datetime


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: str  # DD.MM.YYYY format
    job: str
    working_years: float
    salary: int
    country: str
    city: str
    gender: str = "unknown"
    _prefix: str = field(init=False)
    _birth_date: datetime.date = field(init=False)
    _today: datetime.date = field(init=False)

    def __post_init__(self):
        if self.gender == "male":
            self._prefix = "He is"
        elif self.gender == "female":
            self._prefix = "She is"
        else:
            self._prefix = "Is"
        self._birth_date = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y")
        self._today = datetime.date(2018, 1, 1)

    def name(self):
        """Returns the full name (name and surname, separated by a whitespace)"""
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """Returns the person’s age - the number of fully lived years"""
        dob = self._birth_date
        return (
            self._today.year
            - dob.year
            - ((self._today.month, self._today.day) < (dob.month, dob.day))
        )

    def work(self):
        """Returns the person’s job in a sentence as follows:
            ‘He is a ...’ (if male) ‘She is a ...’ (if female) ‘Is a ...’ (if unknown)
        """
        return f"{self._prefix} a {self.job}"

    def money(self):
        """Returns an amount of money, earned during the working years.
            It should be returned in format xx xxx … -
            every 3 decimal places should be separated by a whitespace.
            For example: ‘10 568’ ‘1 051 422’
        """
        return f"{self.working_years * self.salary * 12:,}".replace(",", " ")

    def home(self):
        """Returns the country and the city where a person lives:
            ‘Lives in the city, country’
        """
        return f"Lives in {self.city}, {self.country}"


if __name__ == "__main__":
    p1 = Person(
        "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
    )
    p2 = Person(
        "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
    )
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("PASSED!")
