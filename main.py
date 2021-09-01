from views.base import View
from controllers.base import Controller


def main():
    view = View()
    controller = Controller(view)
    controller.run()


if __name__ == "__main__":
    main()
