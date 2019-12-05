import configparser


def test_readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/URL_Bro.cfg')
    return config.get(section, key)


# readConfigData ('Details','Application_URL')
# print(readConfigData('Details','Application_URL'))

def test_homeloc(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/Homepage.cfg')
    return config.get(section, key)


def test_searchlocal(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/SearchPage.cfg')
    return config.get(section, key)


def test_PopUpmodal(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/Alert_Modal.cfg')
    return config.get(section, key)
