import pkg_resources


class Version:
    """A class for retrieving the version of Malbench."""

    @staticmethod
    def version():
        """
        Read the version number from the project's version.txt file.

        Returns:
            The version number as a string.
        """

        with pkg_resources.resource_stream("malbench", "../data/version.txt") as f:
            return f.read().decode("utf-8")
