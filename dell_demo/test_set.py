from base_entity import BaseEntity


class TestSet(BaseEntity):
    CUSTOM_NAMES = {}
    def __init__(self, name):
        super(TestSet,self).__init__()
        self.customNames = self.CUSTOM_NAMES
        # Mandatory fields
        self.name = name
        self.subtypeId = 'hp.qc.test-set.default'
