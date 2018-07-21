from base_entity import BaseEntity


class Test(BaseEntity):
    CUSTOM_NAMES = {
        'numExecutionToPass': 'user-16',
        'productcomp': 'user-12'
    }

    def __init__(self, dictionar):
        super(Test,self).__init__()
        self.customNames = self.CUSTOM_NAMES
        dictionary = dict(dictionar)
        # Mandatory fields
        self.name = dictionary.get('name')
        self.parentId = dictionary.get('parent-id')
        self.subtypeId = dictionary.get('subtype-id')
        self.user01 = dictionary.get('user-01')
        self.user03 = dictionary.get('user-03')
        self.user04 = dictionary.get('user-04')
        self.user16 = 'link'
        self.user12 = 'product350'
