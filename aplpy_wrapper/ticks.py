import astropy.units as u


class APLpyTicks(object):

    def __init__(self, axes):
        self._ax = axes
        self.x_visible_axes = None
        self.y_visible_axes = None

    def set_xspacing(self, spacing):
        '''
        Set the x-axis tick spacing, in degrees.
        '''
        #  TODO: Assumes coords indices are 0 and 1 - not true for cube data
        self._ax.coords[0].set_ticks(spacing=spacing * u.degree)

    def set_yspacing(self, spacing):
        '''
        Set the y-axis tick spacing, in degrees.
        '''
        #  TODO: Assumes coords indices are 0 and 1 - not true for cube data
        self._ax.coords[1].set_ticks(spacing=spacing * u.degree)

    def set_color(self, color):
        self._ax.coords[0].set_ticks(color=color)
        self._ax.coords[1].set_ticks(color=color)

    def set_length(self, length, minor_factor=0.5):
        self._ax.coords[0].set_ticks(size=length)
        self._ax.coords[1].set_ticks(size=length)

    def set_linewidth(self, linewidth):
        self._ax.coords[0].set_ticks(width=linewidth)
        self._ax.coords[1].set_ticks(width=linewidth)

    def set_minor_frequency(self, frequency):
        #  WCSAxes doesn't have minor ticks
        pass

    def show(self):
        self._ax.coords[0].set_ticks_position('all')
        self._ax.coords[1].set_ticks_position('all')

    def hide(self):
        self._ax.coords[0].set_ticks_position('')
        self._ax.coords[1].set_ticks_position('')

    def show_x(self):
        self._ax.coords[0].set_ticks_position('all')

    def hide_x(self):
        self._ax.coords[0].set_ticks_position('')

    def show_y(self):
        self._ax.coords[1].set_ticks_position('all')

    def hide_y(self):
        self._ax.coords[1].set_ticks_position('')
