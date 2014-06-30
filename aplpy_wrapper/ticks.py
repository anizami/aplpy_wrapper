from wcsaxes.ticks import Ticks
import astropy.units as u


class APLpyTicks(object):

    def __init__(self, axes):
        self._ax = axes

    def set_xspacing(self, spacing):
        #  TODO: Assumes coords indices are 0 and 1 - not true for cube data
        self._ax.coords[0].set_ticks(spacing=spacing * u.degree)

    def set_yspacing(self, spacing):
        #  TODO: Assumes coords indices are 0 and 1 - not true for cube data
        self._ax.coords[1].set_ticks(spacing=spacing * u.degree)

    def set_color(self, color):
        # Can only set this in WCSAxes through set_ticks(values, spacing, color=...)
        pass

    def set_length(self, length, minor_factor=0.5):
        #  Minor factor is irrelevant for WCSAxes
        # Can only set this in WCSAxes through set_ticks(values, spacing, width=...)        
        # self._ax.coords[0].set_ticksize(length)
        # self._ax.coords[1].set_ticksize(length)
        pass

    def set_linewidth(self, linewidth):
        # Can only set this in WCSAxes through set_ticks(values, spacing, size=...)
        pass

    def set_minor_frequency(self, frequency):
        #  WCSAxes doesn't have minor ticks
        pass

    def show(self):
        self._ax.coords[0].set_visible_axes('all')
        self._ax.coords[1].set_visible_axes('all')
        pass

    def hide(self):
        #  WCSAxes doesn't allow removing from _visible_axes
        pass

    def show_x(self):
        self._ax.coords[0].set_visible_axes('all')

    def hide_x(self):
        #  WCSAxes doesn't allow removing from _visible_axes
        pass

    def show_y(self):
        self._ax.coords[1].set_visible_axes('all')

    def hide_y(self):
        #  WCSAxes doesn't allow removing from _visible_axes
        pass

