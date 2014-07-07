import astropy.units as u


class Ticks(object):

    def __init__(self, axes, x, y):
        self._ax = axes
        self.x = x
        self.y = y
        self.x_visible_axes = None
        self.y_visible_axes = None

    def set_xspacing(self, spacing):
        '''
        Set the x-axis tick spacing, in degrees.
        '''
        self._ax.coords[self.x].set_ticks(spacing=spacing * u.degree)

    def set_yspacing(self, spacing):
        '''
        Set the y-axis tick spacing, in degrees.
        '''
        self._ax.coords[self.y].set_ticks(spacing=spacing * u.degree)

    def set_color(self, color):
        '''
        Set the color of the ticks
        '''
        self._ax.coords[self.x].set_ticks(color=color)
        self._ax.coords[self.y].set_ticks(color=color)

    def set_length(self, length, minor_factor=0.5):
        '''
        Set the length of the ticks (in points). Currently minor_factor does
        nothing.
        '''
        self._ax.coords[self.x].set_ticks(size=length)
        self._ax.coords[self.y].set_ticks(size=length)

    def set_linewidth(self, linewidth):
        '''
        Set the linewidth of the ticks (in points)
        '''
        self._ax.coords[self.x].set_ticks(width=linewidth)
        self._ax.coords[self.y].set_ticks(width=linewidth)

    def set_minor_frequency(self, frequency):
        '''
        Set the number of subticks per major tick. Set to one to hide minor
        ticks. Currently WCSAxes does not have minor ticks.
        '''
        #  WCSAxes doesn't have minor ticks
        pass

    def show(self):
        """
        Show the x- and y-axis ticks
        """
        self._ax.coords[self.x].set_ticks_position('all')
        self._ax.coords[self.y].set_ticks_position('all')

    def hide(self):
        """
        Hide the x- and y-axis ticks
        """
        self._ax.coords[self.x].set_ticks_position('')
        self._ax.coords[self.y].set_ticks_position('')

    def show_x(self):
        """
        Show the x-axis ticks
        """
        self._ax.coords[self.x].set_ticks_position('all')

    def hide_x(self):
        """
        Hide the x-axis ticks
        """
        self._ax.coords[self.x].set_ticks_position('')

    def show_y(self):
        """
        Show the y-axis ticks
        """
        self._ax.coords[self.y].set_ticks_position('all')

    def hide_y(self):
        """
        Hide the y-axis ticks
        """
        self._ax.coords[self.y].set_ticks_position('')
