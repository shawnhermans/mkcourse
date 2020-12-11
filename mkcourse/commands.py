import fire


class MkCourse(object):
    """Markdown based course builder."""

    def __init__(self, config=None):
        self._config = config

    def build(self):
        pass


if __name__ == '__main__':
    fire.Fire(MkCourse)
