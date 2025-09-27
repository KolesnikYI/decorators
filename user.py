class User:
    """Содержит имя пользователя и его количество сыгранных партий"""

    def __init__(self,
                 name: str,
                 ) -> None:
        self.name = name
        self.total_games: int = 0

    @property
    def total_games_count(self) -> int:
        return self.total_games

    def increase_games_count_by_one(self) -> None:
        self.total_games += 1
