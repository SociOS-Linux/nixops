import nixops.statefile
from nixops.util import ImmutableValidatedObject
from typing import Type


class MemoryBackendOptions(ImmutableValidatedObject):
    pass


class MemoryBackend:
    @staticmethod
    def options() -> Type[MemoryBackendOptions]:
        return MemoryBackendOptions

    def __init__(self, args: MemoryBackendOptions) -> None:
        pass

    # fetchToFile: acquire a lock and download the state file to
    # the local disk. Note: no arguments will be passed over kwargs.
    # Making it part of the type definition allows adding new
    # arguments later.
    def fetchToFile(self, path: str, **kwargs) -> None:
        pass

    def onOpen(self, sf: nixops.statefile.StateFile, **kwargs) -> None:
        sf.create_deployment()

    # uploadFromFile: upload the new state file and release any locks
    # Note: no arguments will be passed over kwargs. Making it part of
    # the type definition allows adding new arguments later.
    def uploadFromFile(self, path: str, **kwargs) -> None:
        pass