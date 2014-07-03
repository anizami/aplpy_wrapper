import matplotlib.pyplot as plt
import os
from astropy.io import fits
from astropy.wcs import WCS
from wcsaxes import WCSAxes
from ticks import APLpyTicks as Ticks
from ticklabels import APLplyTickLabels as TickLabels
from axis_labels import APLpyAxisLabels as AxisLabels
from colorbar import Colorbar


class FITSFigure(object):

    def __init__(self, data, hdu=0, figure=None, subplot=(1, 1, 1),
                 downsample=False, north=False, convention=None,
                 dimensions=[0, 1], slices=[], auto_refresh=True,
                 **kwargs):

        '''
        Create a FITSFigure instance.

        Parameters
        ----------

        data : see below

            The FITS file to open. The following data types can be passed:

                 string
                 astropy.io.fits.PrimaryHDU
                 astropy.io.fits.ImageHDU
                 pyfits.PrimaryHDU
                 pyfits.ImageHDU
                 astropy.wcs.WCS
                 np.ndarray
                 RGB image with AVM meta-data

        hdu : int, optional
            By default, the image in the primary HDU is read in. If a
            different HDU is required, use this argument.

        figure : ~matplotlib.figure.Figure, optional
            If specified, a subplot will be added to this existing
            matplotlib figure() instance, rather than a new figure
            being created from scratch.

        subplot : tuple or list, optional
            If specified, a subplot will be added at this position. If a tuple
            of three values, the tuple should contain the standard matplotlib
            subplot parameters, i.e. (ny, nx, subplot). If a list of four
            values, the list should contain [xmin, ymin, dx, dy] where xmin
            and ymin are the position of the bottom left corner of the
            subplot, and dx and dy are the width and height of the subplot
            respectively. These should all be given in units of the figure
            width and height. For example, [0.1, 0.1, 0.8, 0.8] will almost
            fill the entire figure, leaving a 10 percent margin on all sides.

        downsample : int, optional
            If this option is specified, the image will be downsampled
            by a factor *downsample* when reading in the data.

        north : str, optional
            Whether to rotate the image so that the North Celestial
            Pole is up. Note that this option requires Montage to be
            installed.

        convention : str, optional
            This is used in cases where a FITS header can be interpreted
            in multiple ways. For example, for files with a -CAR
            projection and CRVAL2=0, this can be set to 'wells' or
            'calabretta' to choose the appropriate convention.

        dimensions : tuple or list, optional
            The index of the axes to use if the data has more than three
            dimensions.

        slices : tuple or list, optional
            If a FITS file with more than two dimensions is specified,
            then these are the slices to extract. If all extra dimensions
            only have size 1, then this is not required.

        auto_refresh : str, optional
            Whether to refresh the figure automatically every time a
            plotting method is called. This can also be set using the
            set_auto_refresh method.

        kwargs
            Any additional arguments are passed on to matplotlib's Figure() class.
            For example, to set the figure size, use the figsize=(xsize, ysize)
            argument (where xsize and ysize are in inches). For more information
            on these additional arguments, see the *Optional keyword arguments*
            section in the documentation for `Figure
            <http://matplotlib.sourceforge.net/api/figure_api.html?
            #matplotlib.figure.Figure>`_
        '''
        self._data = data
        if hdu is not None:
            self._hdu_int = hdu
        # Don't know what to do with this matplotlib figure
        if figure is not None:
            self._figure = figure
        # TODO: figure out what to do with subplot parameter
        self._subplot = subplot
        self._downsample = downsample
        self._north = north
        self._convention = convention
        self._dimensions = dimensions
        self._slices = slices
        # TODO: ask about auto_refresh
        self._auto_refresh = auto_refresh
        self._kwargs = kwargs
        if 'figsize' not in kwargs:
            self._kwargs['figsize'] = (10, 9)

        # TODO: Currently only assumes files are fits files, fix so it also
        # works with HDU objects

        # Start plotting the matplotlib figure
        self.fig = plt.figure(figsize=self._kwargs['figsize'])
        # self.fig = fig  # Different from self._figure

        # Get the HDU data from the file
        self.hdu = fits.open(data)[hdu]
        self.wcs = WCS(self.hdu.header)
        self.ax = WCSAxes(self.fig, [0.1, 0.1, 0.8, 0.8], wcs=self.wcs)
        # Initialize Ticks, TickLabels and AxisLabels
        self.ticks = Ticks(self.ax)
        self.axis_labels = AxisLabels(self.ax)
        self.tick_labels = TickLabels(self.ax)

    def show_colorscale(self, vmin=None, vmid=None, vmax=None,
                        pmin=0.25, pmax=99.75, stretch='linear', exponent=2,
                        cmap='default', smooth=None, kernel='gauss',
                        aspect='equal', interpolation='nearest'):
        '''
        Show a colorscale image of the FITS file.

        Parameters
        ----------

        vmin : None or float, optional
            Minimum pixel value to use for the colorscale. If set to None,
            the minimum pixel value is determined using pmin (default).

        vmax : None or float, optional
            Maximum pixel value to use for the colorscale. If set to None,
            the maximum pixel value is determined using pmax (default).

        pmin : float, optional
            Percentile value used to determine the minimum pixel value to
            use for the colorscale if vmin is set to None. The default
            value is 0.25%.

        pmax : float, optional
            Percentile value used to determine the maximum pixel value to
            use for the colorscale if vmax is set to None. The default
            value is 99.75%.

        stretch : { 'linear', 'log', 'sqrt', 'arcsinh', 'power' }, optional
            The stretch function to use

        vmid : None or float, optional
            Baseline value used for the log and arcsinh stretches. If
            set to None, this is set to zero for log stretches and to
            vmin - (vmax - vmin) / 30. for arcsinh stretches

        exponent : float, optional
            If stretch is set to 'power', this is the exponent to use

        cmap : str, optional
            The name of the colormap to use

        smooth : int or tuple, optional
            Default smoothing scale is 3 pixels across. User can define
            whether they want an NxN kernel (integer), or NxM kernel
            (tuple). This argument corresponds to the 'gauss' and 'box'
            smoothing kernels.

        kernel : { 'gauss', 'box', numpy.array }, optional
            Default kernel used for smoothing is 'gauss'. The user can
            specify if they would prefer 'gauss', 'box', or a custom
            kernel. All kernels are normalized to ensure flux retention.

        aspect : { 'auto', 'equal' }, optional
            Whether to change the aspect ratio of the image to match that
            of the axes ('auto') or to change the aspect ratio of the axes
            to match that of the data ('equal'; default)

        interpolation : str, optional
            The type of interpolation to use for the image. The default is
            'nearest'. Other options include 'none' (no interpolation,
            meaning that if exported to a postscript file, the colorscale
            will be output at native resolution irrespective of the dpi
            setting), 'bilinear', 'bicubic', and many more (see the
            matplotlib documentation for imshow).
        '''

        self.fig.add_axes(self.ax)

        self.image = self.ax.imshow(self.hdu.data, cmap=None, aspect=aspect,
                       interpolation=interpolation,
                       vmin=vmin, vmax=vmax, origin='lower')
        # self.fig.canvas.draw()
        # TODO: figure out what to do with the following parameters
        # * pmin
        # * pmax
        # * stretch
        # * vmid
        # * exponent
        # * smooth
        # TODO: make my own Normalizer class?

    def hide_colorscale(self):
        pass
        # self.image.set_visible(False)

    def show_grayscale(self, vmin=None, vmid=None, vmax=None,
                       pmin=0.25, pmax=99.75,
                       stretch='linear', exponent=2, invert='default',
                       smooth=None, kernel='gauss', aspect='equal',
                       interpolation='nearest'):
        '''
        Show a grayscale image of the FITS file.

        Parameters
        ----------

        vmin : None or float, optional
            Minimum pixel value to use for the grayscale. If set to None,
            the minimum pixel value is determined using pmin (default).

        vmax : None or float, optional
            Maximum pixel value to use for the grayscale. If set to None,
            the maximum pixel value is determined using pmax (default).

        pmin : float, optional
            Percentile value used to determine the minimum pixel value to
            use for the grayscale if vmin is set to None. The default
            value is 0.25%.

        pmax : float, optional
            Percentile value used to determine the maximum pixel value to
            use for the grayscale if vmax is set to None. The default
            value is 99.75%.

        stretch : { 'linear', 'log', 'sqrt', 'arcsinh', 'power' }, optional
            The stretch function to use

        vmid : None or float, optional
            Baseline value used for the log and arcsinh stretches. If
            set to None, this is set to zero for log stretches and to
            vmin - (vmax - vmin) / 30. for arcsinh stretches

        exponent : float, optional
            If stretch is set to 'power', this is the exponent to use

        invert : str, optional
            Whether to invert the grayscale or not. The default is False,
            unless set_theme is used, in which case the default depends on
            the theme.

        smooth : int or tuple, optional
            Default smoothing scale is 3 pixels across. User can define
            whether they want an NxN kernel (integer), or NxM kernel
            (tuple). This argument corresponds to the 'gauss' and 'box'
            smoothing kernels.

        kernel : { 'gauss', 'box', numpy.array }, optional
            Default kernel used for smoothing is 'gauss'. The user can
            specify if they would prefer 'gauss', 'box', or a custom
            kernel. All kernels are normalized to ensure flux retention.

        aspect : { 'auto', 'equal' }, optional
            Whether to change the aspect ratio of the image to match that
            of the axes ('auto') or to change the aspect ratio of the axes
            to match that of the data ('equal'; default)

        interpolation : str, optional
            The type of interpolation to use for the image. The default is
            'nearest'. Other options include 'none' (no interpolation,
            meaning that if exported to a postscript file, the grayscale
            will be output at native resolution irrespective of the dpi
            setting), 'bilinear', 'bicubic', and many more (see the
            matplotlib documentation for imshow).
        '''

        if invert == 'default':
            invert = self.fig.apl_grayscale_invert_default

        if invert:
            cmap = 'gist_yarg'
        else:
            cmap = 'gray'

        self.image = self.ax.imshow(self.hdu.data, cmap=cmap, aspect=aspect,
                                    interpolation=interpolation,
                                    vmin=vmin, vmax=vmax, origin='lower')

    def return_image(self):
        return self.image

    def hide_grayscale(self, *args, **kwargs):
        pass
        # self.hide_colorscale(*args, **kwargs)

    def show_contour(self, data=None, hdu=0, layer=None, levels=5,
                     filled=False, cmap=None, colors=None, returnlevels=False,
                     convention=None, dimensions=[0, 1], slices=[],
                     smooth=None, kernel='gauss', overlap=False, **kwargs):
        pass

    def save(self, filename, dpi=None, transparent=False, adjust_bbox=True,
             max_dpi=300, format=None):
        self.fig.savefig(filename)
        # self.fig.savefig(filename, transparent=transparent, dpi=dpi, format=format)
        # if isinstance(filename, basestring) and format is None:
        #         format = os.path.splitext(filename)[1].lower()[1:]
        # if adjust_bbox:
        #     self.fig.savefig(filename, transparent=transparent, dpi=dpi,
        #                      bbox_inches='tight', format=format)
        # else:
        #     self.fig.savefig(filename, transparent=transparent, dpi=dpi,
        #                      format=format)

    def set_xaxis_coord_type(self, coord_type):
        '''
        Set the type of x coordinate.

        Options are:

        * ``scalar``: treat the values are normal decimal scalar values
        * ``longitude``: treat the values as a longitude in the 0 to 360 range
        * ``latitude``: treat the values as a latitude in the -90 to 90 range
        '''
        self.ax.coords[0].set_coord_type(coord_type)

    def set_yaxis_coord_type(self, coord_type):
        '''
        Set the type of y coordinate.

        Options are:

        * ``scalar``: treat the values are normal decimal scalar values
        * ``longitude``: treat the values as a longitude in the 0 to 360 range
        * ``latitude``: treat the values as a latitude in the -90 to 90 range
        '''
        self.ax.coords[1].set_coord_type(coord_type)

    def set_system_latex(self, usetex):
        pass

    def recenter(self, x, y, radius=None, width=None, height=None):
        pass

    def add_label(self, x, y, text, relative=False, color='black',
                  family=None, style=None, variant=None, stretch=None,
                  weight=None, size=None, fontproperties=None,
                  horizontalalignment='center', verticalalignment='center',
                  layer=None, **kwargs):
        # TODO: Should I do all the checking for parameters?
        if relative:
            self.ax.text(x, y, text, color=color, family=family, style=style,
                         variant=variant, stretch=stretch, weight=weight,
                         size=size, horizontalalignment=horizontalalignment,
                         verticalalignment=verticalalignment,
                         transform=self._ax1.transAxes, **kwargs)
        else:
            # Do a world2pix transformation
            # xp, yp = ...
            # Should I use the world2pix transformation from WCSAxes?
            xp, yp = WCS.wcs_world2pix(self.wcs, x, y)  # This doesn't feel right
            self._ax1.text(xp, yp, text, color=color, family=family,
                           style=style, variant=variant, stretch=stretch,
                           weight=weight, size=size,
                           horizontalalignment=horizontalalignment,
                           verticalalignment=verticalalignment, **kwargs)

    def set_auto_refresh(self, refresh):
        pass

    def refresh(self, force=True):
        pass

    def set_theme(self, theme):
        pass

    def add_grid(self, *args, **kwargs):
        pass

    def remove_grid(self):
        pass

    def add_beam(self, *args, **kwargs):
        pass

    def remove_beam(self, beam_index=None):
        pass

    def add_scalebar(self, length, *args, **kwargs):
        pass

    def remove_scalebar(self):
        pass

    def add_colorbar(self, *args, **kwargs):
        '''
        Add a colorbar to the current figure.

        Once this method has been run, a colorbar attribute becomes
        available, and can be used to control the aspect of the colorbar::

            >>> f = aplpy.FITSFigure(...)
            >>> ...
            >>> f.add_colorbar()
            >>> f.colorbar.set_width(0.3)
            >>> f.colorbar.set_location('top')
            >>> ...
        '''
        if hasattr(self, 'colorbar'):
            raise Exception("Colorbar already exists")
        if self.image is None:
            raise Exception("No image is shown, so a colorbar cannot be displayed")
        # try:
        self.colorbar = Colorbar(self)
        # self.colorbar.show(*args, **kwargs)
        # except:
        #     del self.colorbar
        #     raise

    def remove_colorbar(self):
        pass

    def show_rgb(self, filename=None, interpolation='nearest',
                 vertical_flip=False, horizontal_flip=False, flip=False):
        # Can WCSAxes show rgb images?
        pass

    def close(self):
        plt.close(self.fig)
