from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND
from user import User

start_time = dt.now()


@access_control
def get_statistics(player: User, *args, **kwargs) -> None:
    game_time = dt.now() - start_time
    print(
        f'Общее время игры: {game_time}, '
        f'текущая игра - №{player.total_games_count}')


@access_control
def get_right_answer(number: int, *args, **kwargs) -> None:
    print(f'Правильный ответ: {number}')


def check_number(player: User, guess: int, number: int) -> bool:
    # Если число угадано...
    if guess == number:
        print(f'Отличная интуиция, {player.name}! Вы угадали число :)')
        # ...возвращаем True
        return True

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    else:
        print('Ваше число больше того, что загадано.')
    return False


def game(player: User) -> None:
    # Получаем случайное число в диапазоне от 1 до 100.
    number = randint(1, 100)
    print(
        '\nУгадайте число от 1 до 100.\n'
        'Для выхода из текущей игры введите команду "stop"'
    )
    while True:
        # Получаем пользовательский ввод,
        # отрезаем лишние пробелы и переводим в нижний регистр.
        user_input = input('Введите число или команду: ').strip().lower()

        match user_input:
            case 'stop':
                break
            case 'stat':
                get_statistics(player, username=player.name)
            case 'answer':
                get_right_answer(number, username=player.name)
            case _:
                try:
                    guess = int(user_input)
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue

                if check_number(player, guess, number):
                    break


def get_username() -> str:
    username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
    if username == ADMIN_USERNAME:
        print(
            '\nДобро пожаловать, создатель! '
            'Во время игры вам доступны команды "stat", "answer"'
        )
    else:
        print(f'\n{username}, добро пожаловать в игру!')
    return username


def guess_number() -> None:
    while True:
        player.increase_games_count_by_one()
        game(player)
        play_again = input('\nХотите сыграть ещё? (yes/no) ')
        if play_again.strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    try:
        print(
            'Вас приветствует игра "Угадай число"!\n'
            'Для выхода нажмите Ctrl+C'
        )
        player: User = User(get_username())
        guess_number()
    except KeyboardInterrupt:
        print("\n\nИгра прервана. До свидания!")
