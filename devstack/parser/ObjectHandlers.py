import zope.interface

class IObjectHandler(zope.interface.Interface):
    """Common interface for handling parsing of different objects"""

    def parse(yamlObject, objectContainer):
        """parses a particular type of object, extracts all relevant information and appends to container"""


@zope.interface.implementer(IObjectHandler)
class ServiceObjectHandler(IObjectHandler):
    
    def parse(self, yamlObject, objectContainer):
        pass

@zope.interface.implementer(IObjectHandler)
class VolumeObjectHandler(IObjectHandler):
    
    def parse(self, yamlObject, objectContainer):
        pass


handlers = {
    "volumes" : VolumeObjectHandler(),
    "services": ServiceObjectHandler()
}