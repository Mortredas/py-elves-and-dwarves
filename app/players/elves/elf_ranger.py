from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
                f"{self.__bow_level} level")

    def get_rating(self) -> int:
        return 3 * self.__bow_level
