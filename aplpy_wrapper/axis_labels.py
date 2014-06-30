position_map = {'bottom': 'b', 'top': 't', 'right': 'r', 'left': 'l'}


class APLpyAxisLabels(object):
    def __init__(self, axes):
        self._ax = axes

    def set_xtext(self, label):
        self._ax.coords[0].set_axislabel(label)

    def set_ytext(self, label):
        self._ax.coords[1].set_axislabel(label)

    def set_xpad(self, pad):
        # Can't do it directly in WCSAxes
        pass

    def set_ypad(self, pad):
        # Can't do it directly in WCSAxes
        pass

    def set_font(self, family=None, style=None, variant=None, stretch=None, weight=None, size=None, fontproperties=None):
        # Can't do it directly in WCSAxes
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
        self._ax.coords[0].set_axislabel_position(position)

    def set_yposition(self, position):
        position = position_map[position]
        self._ax.coords[1].set_axislabel_position(position)





