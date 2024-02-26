from forms import Forms


class ProjectClass:
    """
    ProjectClass is the class to demonstrate concepts
    """
    def __init__(self):
        """
        The constructor
        """
        self.id = 0
        self.forms = Forms()

    def get_available_forms(self):
        return self.forms.__class__
