from __future__ import absolute_import, print_function, division

import warnings

import numpy as np
from matplotlib.collections import LineCollection
import astropy.units as u


# from . import math_util
# from . import wcs_util
# from . import angle_util as au
# from .ticks import tick_positions, default_spacing
# from .decorators import auto_refresh

# import math_util
# import wcs_util
# import angle_util as au
# from ticks import tick_positions, default_spacing
from .decorators import auto_refresh


class Grid(object):

    # @auto_refresh
    def __init__(self, parent, x, y):

        # Save axes and wcs information
        self.ax = parent.ax
        self._wcs = parent._wcs
        self._figure = parent._figure
        self.x = x
        self.y = y

        # Save plotting parameters (required for @auto_refresh)
        self._parameters = parent._parameters

        # Initialize grid container
        # self._grid = None
        # self._active = False

        # Set defaults
        # self.x_auto_spacing = True
        # self.y_auto_spacing = True
        # self.default_color = 'white'
        # self.default_alpha = 0.5

        # Set grid event handler
        # TODO: Ask Tom about grid event handlers for WCSAxes..
        # self.ax.callbacks.connect('xlim_changed', self._update_norefresh)
        # self.ax.callbacks.connect('ylim_changed', self._update_norefresh)

    # @auto_refresh
    # def _remove(self):
    #     self._grid.remove()

    # @auto_refresh
    def set_xspacing(self, xspacing):
        '''
        Set the grid line spacing in the longitudinal direction

        Parameters
        ----------
        xspacing : { float, str }
            The spacing in the longitudinal direction. To set the spacing
            to be the same as the ticks, set this to 'tick'
        '''
        # TODO: Assumes unit is degrees
        if xspacing != 'tick':
            self.ax.coords[self.x].set_ticks(spacing=xspacing * u.deg)
        else:
            self.ax.coords[self.x].grid()

        # TODO: Ask Tom how to implement this because in WCSAxes, grid spacing
        # can only be changed with ticks spacing
        # if xspacing == 'tick':
        #     self.x_auto_spacing = True
        # elif np.isreal(xspacing):
        #     self.x_auto_spacing = False
        #     if self._wcs.xaxis_coord_type in ['longitude', 'latitude']:
        #         self.x_grid_spacing = au.Angle(
        #             degrees=xspacing,
        #             latitude=self._wcs.xaxis_coord_type == 'latitude')
        #     else:
        #         self.x_grid_spacing = xspacing
        # else:
        #     raise ValueError("Grid spacing should be a scalar or 'tick'")

        # self._update()

    # @auto_refresh
    def set_yspacing(self, yspacing):
        '''
        Set the grid line spacing in the latitudinal direction

        Parameters
        ----------
        yspacing : { float, str }
            The spacing in the latitudinal direction. To set the spacing
            to be the same as the ticks, set this to 'tick'
        '''
        # TODO: Assumes coords[1] is the y-axis
        # TODO: Assumes unit is degrees
        if yspacing != 'tick':
            self.ax.coords[self.y].set_ticks(spacing=yspacing * u.deg)
        else:
            self.ax.coords[self.y].grid()

    # @auto_refresh
    def set_color(self, color):
        '''
        Set the color of the grid lines

        Parameters
        ----------
        color : str
            The color of the grid lines
        '''
        self.ax.coords.grid(color=color)

        # if self._grid:
        #     self._grid.set_edgecolor(color)
        # else:
        #     self.default_color = color

    # @auto_refresh
    def set_alpha(self, alpha):
        '''
        Set the alpha (transparency) of the grid lines

        Parameters
        ----------
        alpha : float
            The alpha value of the grid. This should be a floating
            point value between 0 and 1, where 0 is completely
            transparent, and 1 is completely opaque.
        '''
        self.ax.coords.grid(alpha=alpha)

        # if self._grid:
        #     self._grid.set_alpha(alpha)
        # else:
        #     self.default_alpha = alpha

    # @auto_refresh
    def set_linewidth(self, linewidth):
        self.ax.coords.grid(linewidth=linewidth)

    # @auto_refresh
    def set_linestyle(self, linestyle):
        self.ax.coords.grid(linestyle=linestyle)

    # @auto_refresh
    def show(self):
        self.ax.grid()

        # if self._grid:
        #     self._grid.set_visible(True)
        # else:
        #     self._active = True
        #     self._update()
        #     self.set_color(self.default_color)
        #     self.set_alpha(self.default_alpha)

    # @auto_refresh
    def hide(self):
        # TODO: implement
        pass
        # self._grid.set_visible(False)
