import random
# Класс для создания участника игры
class Player:
    def __init__(self, pid, name):
        self.id = pid  # Уникальный номер участника
        self.name = name  # Имя участника

    def __str__(self):
        # Как будет отображаться участник при печати (например: "1:Маша1")
        return f"{self.id}:{self.name}"

# Класс для управления игрой
class Game:
    def __init__(self, n, k):
        self.k = k  # Шаг считалки - каждого k-го участника удаляем

        # Список возможных имен для участников
        names = ["Маша", "Петя", "Аня", "Саша", "Коля", "Оля", "Дима", "Игорь", "Катя"]

        # Создаем n участников со случайными именами
        # Для i от 1 до n: создаем участника с номером i и случайным именем + номер
        self.players = [Player(i, random.choice(names) + str(i)) for i in range(1, n + 1)]

    def play(self):
        # Открываем файл для записи лога игры
        with open("game_log.txt", "w", encoding="utf-8") as f:
            # Записываем начальные условия
            f.write(f"Начинаем игру: N={len(self.players)}, k={self.k}\n")
            f.write("Участники: " + ", ".join(str(p) for p in self.players) + "\n\n")

            index = 0  # Начинаем отсчет с первого участника

            # Игра продолжается, пока не останется 1 участник
            while len(self.players) > 1:
                # Вычисляем индекс участника, который выбывает:
                # % - это деление с остатком, чтобы "ходить по кругу"
                index = (index + self.k - 1) % len(self.players)

                # Удаляем участника с вычисленным индексом
                removed = self.players.pop(index)

                # запись в лог с измененными данными
                f.write(f"Удалён: {removed}\n")
                f.write("Остались: " + ", ".join(str(p) for p in self.players) + "\n\n")

            # Запись победителя
            f.write(f"Победитель: {self.players[0]}\n")

        # Возвращаем победителя
        return self.players[0]
if __name__ == "__main__":
    winner = Game(n=5, k=2).play() #n = количество участников k= шаг
    print("Победитель:", winner)