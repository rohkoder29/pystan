from time import sleep

print("\n\tWELCOME TO THE COUNTDOWN APP\n")


def countdown(seconds: int) -> None:
    """ countdown(seconds)\n
    Count down from a given amount of seconds to 0. """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        sleep(1)
        seconds -= 1

    print("Countdown done!")


while 1:
    try:
        t = int(input("Enter number of seconds to countdown from: "))
        assert t > 0
    except ValueError:
        print("Please input an integer value.")
    except AssertionError:
        print("Maybe something > 0.")
    else:
        countdown(t)
        break
