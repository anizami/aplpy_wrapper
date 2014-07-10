from __future__ import absolute_import, print_function, division

from .decorators import auto_refresh


class Frame(object):

    # @auto_refresh
    def __init__(self, parent):

        self.ax = parent.ax
        self._figure = parent._figure

        # Save plotting parameters (required for @auto_refresh)
        self._parameters = parent._parameters

    # @auto_refresh
    def set_linewidth(self, linewidth):
        '''
        Set line width of the frame.

        Parameters
        ----------
        linewidth:
            The linewidth to use for the frame.
        '''
        pass  # Until PR 88 is merged
        # self.ax.coords.set_frame_linewidth(linewidth)

    # @auto_refresh
    def set_color(self, color):
        '''
        Set color of the frame.

        Parameters
        ----------
        color:
            The color to use for the frame.
        '''
        pass  # Until PR 88 is merged
        # self.ax.coords.set_frame_color(color)