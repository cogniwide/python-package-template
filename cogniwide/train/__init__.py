from cogniwide.component import Component


class BaseAnnotator(Component):
    def __init__(self, component_config=None):
        super().__init__(component_config)
