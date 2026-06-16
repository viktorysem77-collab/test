# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
previous = 0
increase = 20

if previous == 0:
    percent = float('inf')
    print(f"Абсолютный прирост: +{increase} баллов")
    print("Относительный прирост: ∞% (невозможно рассчитать, так как исходный рейтинг равен 0)")
else:
    percent = increase / previous * 100
    print(f"Абсолютный прирост: +{increase} баллов")
    print(f"Относительный прирост: {percent:.2f}%")