from .regions.MainDeck import (MainElevatorTop, OperationsDeckElevatorTop, HabitationDeckElevatorTop,
                               SectorHubElevator1Top, SectorHubElevator2Top, SectorHubElevator3Top,
                               SectorHubElevator4Top, SectorHubElevator5Top, SectorHubElevator6Top,
                               OperationsDeckElevatorBottom, HabitationDeckElevatorBottom, SectorHubElevatorBottom,
                               RestrictedElevatorBottom)
from .regions.Sector1 import Sector1EntranceElevatorBottom, Sector1TubeLeft, Sector1TubeRight, TourianElevatorTop
from .regions.Sector2 import Sector2EntranceElevatorBottom, Sector2TubeLeft, Sector2TubeRight
from .regions.Sector3 import Sector3EntranceElevatorBottom, Sector3TubeLeft, Sector3TubeRight
from .regions.Sector4 import Sector4EntranceElevatorBottom, Sector4TubeLeft, Sector4TubeRight
from .regions.Sector5 import Sector5EntranceElevatorBottom, Sector5TubeLeft, Sector5TubeRight
from .regions.Sector6 import Sector6EntranceElevatorBottom, Sector6TubeLeft, Sector6TubeRight

default_region_map = {
    Sector1TubeLeft: Sector3TubeRight,
    Sector2TubeLeft: Sector1TubeRight,
    Sector3TubeLeft: Sector5TubeRight,
    Sector4TubeLeft: Sector2TubeRight,
    Sector5TubeLeft: Sector6TubeRight,
    Sector6TubeLeft: Sector4TubeRight,
    SectorHubElevator1Top: Sector1EntranceElevatorBottom,
    SectorHubElevator2Top: Sector2EntranceElevatorBottom,
    SectorHubElevator3Top: Sector3EntranceElevatorBottom,
    SectorHubElevator4Top: Sector4EntranceElevatorBottom,
    SectorHubElevator5Top: Sector5EntranceElevatorBottom,
    SectorHubElevator6Top: Sector6EntranceElevatorBottom,
    OperationsDeckElevatorTop: OperationsDeckElevatorBottom,
    HabitationDeckElevatorTop: HabitationDeckElevatorBottom,
    MainElevatorTop: SectorHubElevatorBottom,
    TourianElevatorTop: RestrictedElevatorBottom
}

reverse_region_map = {v: k for k, v in default_region_map.items()}

full_default_region_map = {
    **default_region_map,
    **reverse_region_map
}