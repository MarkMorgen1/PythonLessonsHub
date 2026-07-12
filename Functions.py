# create user-defined functions
name = "  JosepH  "
print(
    name.strip().lower()
)  # remove blank spaces from front and rear and convert to lowercase


# define a function
def strip_lower(
    x, country="USA"
):  # sets default value of country, in case it's not included in the call
    print(x.strip().lower(), "from:", country)


# call that function
strip_lower(name, "France")  # name is defined as global variable
strip_lower("   KaiSER     Wilhelm   ")


def mult_by_2(x, y):
    print(x * 2, " ", y)


mult_by_2(4.8, "billy")


# how to return a value from function to program
def clean_the_name(name):
    return name.strip().lower()


print(clean_the_name("   PhillY MCKaviTy    "))
