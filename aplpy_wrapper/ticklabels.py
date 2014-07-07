from matplotlib.ticker import Formatter

position_map = {'bottom': 'b', 'top': 't', 'right': 'r', 'left': 'l'}


class TickLabels(object):
    def __init__(self, axes):
        self._ax = axes

    def set_xformat(self, formatter):
        '''
        Set the format of the x-axis tick labels.

        If the x-axis type is ``longitude`` or ``latitude``, then the options
        are:

            * ``ddd.ddddd`` - decimal degrees, where the number of decimal places can be varied
            * ``hh`` or ``dd`` - hours (or degrees)
            * ``hh:mm`` or ``dd:mm`` - hours and minutes (or degrees and arcminutes)
            * ``hh:mm:ss`` or ``dd:mm:ss`` - hours, minutes, and seconds (or degrees, arcminutes, and arcseconds)
            * ``hh:mm:ss.ss`` or ``dd:mm:ss.ss`` - hours, minutes, and seconds (or degrees, arcminutes, and arcseconds), where the number of decimal places can be varied.

        If the x-axis type is ``scalar``, then the format should a string such
        as 'x.xx'.
        '''
        if isinstance(formatter, Formatter):
            raise NotImplementedError()
        else:  # Change this to elif isinstance(formatter, six.string_types) later
            self._ax.coords[0].set_major_formatter(formatter)

    def set_yformat(self, formatter):
        '''
        Set the format of the y-axis tick labels.

        If the x-axis type is ``longitude`` or ``latitude``, then the options
        are:

            * ``ddd.ddddd`` - decimal degrees, where the number of decimal places can be varied
            * ``hh`` or ``dd`` - hours (or degrees)
            * ``hh:mm`` or ``dd:mm`` - hours and minutes (or degrees and arcminutes)
            * ``hh:mm:ss`` or ``dd:mm:ss`` - hours, minutes, and seconds (or degrees, arcminutes, and arcseconds)
            * ``hh:mm:ss.ss`` or ``dd:mm:ss.ss`` - hours, minutes, and seconds (or degrees, arcminutes, and arcseconds), where the number of decimal places can be varied.

        If the x-axis type is ``scalar``, then the format should a string such
        as 'x.xx'.
        '''
        if isinstance(formatter, Formatter):
            raise NotImplementedError()
        else:
            self._ax.coords[1].set_major_formatter(formatter)

    def set_font(self, family=None, style=None, variant=None, stretch=None, weight=None, size=None, fontproperties=None):
        """
        Set the font of the tick labels.

        Parameters
        ----------

        common: family, style, variant, stretch, weight, size, fontproperties

        Notes
        -----

        Default values are set by matplotlib or previously set values if
        set_font has already been called. Global default values can be set by
        editing the matplotlibrc file.
        """
        # TODO: Ask Tom to confirm that there is currently no way to set
        # tick label font properties.
        pass
        # ax.coords[0].set_axislabel(family=family, style=style, variant=variant,
        #                            weight=weight, size=size,
        #                            fontproperties=fontproperties)
        # ax.coords[1].set_axislabel(family=family, style=style, variant=variant,
        #                            weight=weight, size=size,
        #                            fontproperties=fontproperties)

    def show(self):
        """
        Show the x- and y-axis tick labels.
        """
        self._ax.coords[0].set_ticklabel_position('b')
        self._ax.coords[1].set_ticklabel_position('l')

    def hide(self):
        """
        Hide the x- and y-axis tick labels.
        """
        self._ax.coords[0].set_ticklabel_position('')
        self._ax.coords[1].set_ticklabel_position('')

    def show_x(self):
        """
        Show the x-axis tick labels.
        """
        self._ax.coords[0].set_ticklabel_position('b')

    def hide_x(self):
        """
        Hide the x-axis tick labels.
        """
        self._ax.coords[0].set_ticklabel_position('')

    def show_y(self):
        """
        Show the y-axis tick labels.
        """
        self._ax.coords[1].set_ticklabel_position('l')

    def hide_y(self):
        """
        Hide the y-axis tick labels.
        """
        self._ax.coords[1].set_ticklabel_position('')

    def set_xposition(self, position):
        """
        Set the position of the x-axis tick labels ('top' or 'bottom')
        """
        position = position_map[position]
        self._ax.coords[0].set_ticklabel_position(position)

    def set_yposition(self, position):
        """
        Set the position of the y-axis tick labels ('left' or 'right')
        """
        position = position_map[position]
        self._ax.coords[1].set_ticklabel_position(position)
