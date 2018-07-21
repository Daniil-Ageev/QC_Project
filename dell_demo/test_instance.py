from base_entity import BaseEntity


class TestInstance(BaseEntity):
    CUSTOM_NAMES = {}
    def __init__(self, dictionar):
        super(TestInstance,self).__init__()
        dictionary = dict(dictionar)
        self.customNames = self.CUSTOM_NAMES
        # Mandatory fields
        self.testId = dictionary.get('test-id')
        self.cycleId = dictionary.get('cycle-id')
        self.subtypeId = 'hp.qc.test-instance.MANUAL'