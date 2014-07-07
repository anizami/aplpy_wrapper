position_map = {'bottom': 'b', 'top': 't', 'right': 'r', 'left': 'l'}


class AxisLabels(object):
    def __init__(self, axes):
        self._ax = axes

    def set_xtext(self, label):
        """
        Set the x-axis label text.
        """
        self._x_text = label
        self._ax.coords[0].set_axislabel(label)

    def set_ytext(self, label):
        """
        Set the y-axis label text.
        """
        self._y_text = label
        self._ax.coords[1].set_axislabel(label)

    def set_xpad(self, pad):
        """
        Set the x-axis label displacement, in points.
        """
        self._ax.coords[0].set_axislabel(self._x_text, minpad=pad)

    def set_ypad(self, pad):
        """
        Set the y-axis label displacement, in points.
        """
        self._ax.coords[1].set_axislabel(self._y_text, minpad=pad)

    def set_font(self, **kwargs):
        """
        Set the font of the axis labels.

        Parameters
        ----------

        common: family, style, variant, stretch, weight, size, fontproperties

        Notes
        -----

        Default values are set by matplotlib or previously set values if
        set_font has already been called. Global default values can be set by
        editing the matplotlibrc file.
        """
        self._ax.coords[0].set_axislabel(self._x_text, **kwargs)
        self._ax.coords[1].set_axislabel(self._y_text, **kwargs)

    def show(self):
        """
        Show the x- and y-axis labels.
        """
        self._ax.coords[0].set_axislabel_position('b')
        self._ax.coords[0].set_axislabel_position('l')

    def hide(self):
        """
        Hide the x- and y-axis labels.
        """
        self._ax.coords[0].set_axislabel_position('')
        self._ax.coords[0].set_axislabel_position('')

    def show_x(self):
        """
        Show the x-axis label.
        """
        self._ax.coords[0].set_axislabel_position('b')

    def hide_x(self):
        """
        Hide the x-axis label.
        """
        self._ax.coords[0].set_axislabel_position('')

    def show_y(self):
        """
        Show the y-axis label.
        """
        self._ax.coords[1].set_axislabel_position('l')

    def hide_y(self):
        """
        Hide the y-axis label.
        """
        self._ax.coords[0].set_axislabel_position('')

    def set_xposition(self, position):
        """
        Set the position of the x-axis label ('top' or 'bottom')
        """
        position = position_map[position]
        self._ax.coords[0].set_axislabel_position(position)

    def set_yposition(self, position):
        """
        Set the position of the y-axis label ('left' or 'right')
        """
        position = position_map[position]
        self._ax.coords[1].set_axislabel_position(position)
