from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self.__hummer_level} level")

    def get_rating(self) -> int:
        return self.__hummer_level + 4
