def describe_city(city, country='Pakistan'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Islamabad')
describe_city('Mumbai', 'India')
describe_city('Murre')