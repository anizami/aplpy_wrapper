from matplotlib.ticker import Formatter

position_map = {'bottom': 'b', 'top': 't', 'right': 'r', 'left': 'l'}


class APLplyTickLabels(object):
    def __init__(self, axes):
        self._ax = axes

    def set_xformat(self, formatter):
        if isinstance(formatter, Formatter):
            raise NotImplementedError()
        else:  # Change this to elif isinstance(formatter, six.string_types) later
            self._ax.coords[0].set_major_formatter(formatter)

    def set_yformat(self, formatter):
        if isinstance(formatter, Formatter):
            raise NotImplementedError()
        else:
            self._ax.coords[1].set_major_formatter(formatter)

    def set_style(self, style):
        pass

    def set_font(self, family=None, style=None, variant=None, stretch=None, weight=None, size=None, fontproperties=None):
        pass

    def show(self):
        pass

    def hide(self):
        pass

    def show_x(self):
        pass

    def hide_x(self):
        pass

    def show_y(self):
        pass

    def hide_y(self):
        pass

    def set_xposition(self, position):
        position = position_map[position]
        self._ax.coords[0].set_ticklabel_position(position)

    def set_yposition(self, position):
        position = position_map[position]
        self._ax.coords[1].set_ticklabel_position(position)
