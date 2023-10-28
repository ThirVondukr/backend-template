import dataclasses


@dataclasses.dataclass(slots=True, kw_only=True)
class Dataloaders:
    pass


def create_dataloaders() -> Dataloaders:
    return Dataloaders()
