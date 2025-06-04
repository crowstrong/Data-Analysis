from datetime import datetime
from collections import defaultdict

class Visit:
    _registry = []

    def __init__(self, user_id: int, device: str, country: str, page: str, duration: float, timestamp: datetime = None):
        self.user_id = user_id
        self.device = device
        self.country = country
        self.page = page
        self.duration = duration
        self.timestamp = datetime.now()
        Visit._registry.append(self)

    @property
    def is_mobile_user(self) -> bool:
        return self.device.lower() in ["mobile", "phone", "smartphone", "tablet"]

    @staticmethod
    def is_mobile(device: str) -> bool:
        return device.lower() in ["mobile", "phone", "smartphone", "tablet"]

    @classmethod
    def total_visits(cls) -> int:
        return len(cls._registry)

    @classmethod
    def avg_duration(cls) -> float:
        if not cls._registry:
            return 0
        return round(sum(v.duration for v in cls._registry) / len(cls._registry), 2)

    @classmethod
    def visits_by_country(cls) -> dict:
        result = defaultdict(int)
        for v in cls._registry:
            result[v.country] += 1
        return dict(result)

    @classmethod
    def top_pages(cls, n=3) -> list:
        totals = defaultdict(float)
        for v in cls._registry:
            totals[v.page] += v.duration
        return sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]

    @classmethod
    def clear_registry(cls):
        cls._registry.clear()

    def __str__(self) -> str:
        return (
            f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
            f"User {self.user_id} from {self.country} visited '{self.page}' "
            f"using {self.device} for {self.duration}s"
        )

    def __repr__(self):
        return f"Visit(user_id={self.user_id}, page={self.page}, duration={self.duration})"


if __name__ == "__main__":
    Visit.clear_registry()

    visit1 = Visit(1, "Mobile", "Ukraine", "/home", 120)
    visit2 = Visit(2, "Desktop", "USA", "/about", 240)
    visit3 = Visit(3, "Tablet", "Ukraine", "/home", 180)
    visit4 = Visit(4, "Mobile", "Germany", "/contact", 300)
    visit5 = Visit(5, "Desktop", "Ukraine", "/home", 150)
    visit6 = Visit(6, "Smartphone", "USA", "/home", 90)

    print(f"Total visits: {Visit.total_visits()}")
    print(f"Average duration: {Visit.avg_duration()} seconds")
    print(f"Visits by country: {Visit.visits_by_country()}")
    print(f"Top pages: {Visit.top_pages()}")

    for visit in Visit._registry:
        print(visit)
