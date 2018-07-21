from base_entity import BaseEntity


class TestRun(BaseEntity):
    CUSTOM_NAMES = {}
    def __init__(self, dictionar):
        super(TestRun,self).__init__()
        dictionary = dict(dictionar)
        self.customNames = self.CUSTOM_NAMES
        # Mandatory fields
        self.name = dictionary.get('name')
        self.testId = dictionary.get('testId')
        self.testcyclId = dictionary.get('testcycl-id')
        self.owner = dictionary.get('owner')
