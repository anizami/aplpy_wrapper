# -*- coding: utf-8 -*-

from matplotlib.ticker import Formatter

position_map = {'bottom': 'b', 'top': 't', 'right': 'r', 'left': 'l'}


class TickLabels(object):
    def __init__(self, axes, x, y):
        self._ax = axes
        self.x = x
        self.y = y

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
            self._ax.coords[self.x].set_major_formatter(formatter)

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
            self._ax.coords[self.y].set_major_formatter(formatter)

    # @auto_refresh
    def set_style(self, style):
        """
        Set the format of the x-axis tick labels.

        This can be 'colons' or 'plain':

            * 'colons' uses colons as separators, for example 31:41:59.26 +27:18:28.1
            * 'plain' uses letters and symbols as separators, for example 31h41m59.26s +27º18'28.1"
        """
        # TODO: Remove pass once PR 90 in WCSAxes is merged
        if style == 'latex':
            warnings.warn("latex has now been merged with plain - whether or not to use LaTeX is controled through set_system_latex")
            style = 'plain'
        if style not in ['colons', 'plain']:
            raise Exception("Label style should be one of colons/plain")

        if style == 'colons':
            x_sep = (':', ':', '')
            y_sep = (':', ':', '')

        else:
            x_sep = ('d', 'm', 's')
            y_sep = ('d', 'm', 's')
            x_format = self._ax.coords[self.x]._formatter_locator.format
            if (x_format is not None) and 'h' in x_format:
                x_sep = ('h', 'm', 's')
            y_format = self._ax.coords[self.y]._formatter_locator.format
            if (y_format is not None) and 'h' in y_format:
                y_sep = ('h', 'm', 's')

        try:
            self._ax.coords[self.x].set_separator(x_sep)
            self._ax.coords[self.y].set_separator(y_sep)
        except:
            pass

    def set_font(self, **kwargs):
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
        self._ax.coords[self.x].set_ticklabel(**kwargs)
        self._ax.coords[self.y].set_ticklabel(**kwargs)

    def show(self):
        """
        Show the x- and y-axis tick labels.
        """
        self._ax.coords[self.x].set_ticklabel_position('b')
        self._ax.coords[self.y].set_ticklabel_position('l')

    def hide(self):
        """
        Hide the x- and y-axis tick labels.
        """
        self._ax.coords[self.x].set_ticklabel_position('')
        self._ax.coords[self.y].set_ticklabel_position('')

    def show_x(self):
        """
        Show the x-axis tick labels.
        """
        self._ax.coords[self.x].set_ticklabel_position('b')

    def hide_x(self):
        """
        Hide the x-axis tick labels.
        """
        self._ax.coords[self.x].set_ticklabel_position('')

    def show_y(self):
        """
        Show the y-axis tick labels.
        """
        self._ax.coords[self.y].set_ticklabel_position('l')

    def hide_y(self):
        """
        Hide the y-axis tick labels.
        """
        self._ax.coords[self.y].set_ticklabel_position('')

    def set_xposition(self, position):
        """
        Set the position of the x-axis tick labels ('top' or 'bottom')
        """
        position = position_map[position]
        self._ax.coords[self.x].set_ticklabel_position(position)

    def set_yposition(self, position):
        """
        Set the position of the y-axis tick labels ('left' or 'right')
        """
        position = position_map[position]
        self._ax.coords[self.y].set_ticklabel_position(position)
