class WatsonAccountSettings:
    """
        Uncomment the return lines, place your own values and remove raise ValueErrors.
        Login to your IBM watson services to see your settings.
    """
    def __init__(self):
        __file = open("API-key.txt", "r")
        __lines = __file.readlines()
        self.__username = __lines[1].split()
        self.__password = __lines[2].split()
        self.__env_id = __lines[3].split()
        self.__coll_id = __lines[4].split()
        self.__conf_id = __lines[5].split()

    def username(self):
        #raise ValueError('You need to add your own username to ibm_settings.py file')
        return self.__username

    def password(self):
        #raise ValueError('You need to add your own password to ibm_settings.py file')
        return self.__password

    def environment_id(self):
        """
            Not necessary for DiscoveryNews
        """
        # raise ValueError('You need to add your own enviroment_id to ibm_settings.py file')
        return self.__env_id

    def collection_id(self):
        """
            Not necessary for DiscoveryNews
        """
        #raise ValueError('You need to add your own collection_id to ibm_settings.py file')
        return self.__coll_id

    def configuration_id(self):
        """
            Not necessary for DiscoveryNews
        """
        #raise ValueError('You need to add your own configuration_id to ibm_settings.py file')
        return self.__conf_id