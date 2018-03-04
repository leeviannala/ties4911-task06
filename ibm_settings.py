class WatsonAccountSettings:
    """
        Uncomment the return lines, place your own values and remove raise ValueErrors.
        Login to your IBM watson services to see your settings.
    """
    def username(self):
        raise ValueError('You need to add your own username to ibm_settings.py file')
        #return "username-here"
    def password(self):
        raise ValueError('You need to add your own password to ibm_settings.py file')
        #return "password-here"
    def environment_id(self):
        """
            Not necessary for DiscoveryNews
        """
        raise ValueError('You need to add your own enviroment_id to ibm_settings.py file')
        #return "enviroment_id-here"
    def collection_id(self):
        """
            Not necessary for DiscoveryNews
        """
        raise ValueError('You need to add your own collection_id to ibm_settings.py file')
        #return "collection-here"
    def configuration_id(self):
        """
            Not necessary for DiscoveryNews
        """
        raise ValueError('You need to add your own configuration_id to ibm_settings.py file')
        #return "configuration_id-here"