from unittest import TestCase
from unittest.mock import Mock
import numpy


class TestRdmPlot(TestCase):

    def test_nrow_ncolumn(self):
        from rsatoolbox.vis.rdm_plot import MultiRdmPlot
        rdms = Mock()
        rdms.n_cond = 3
        rdms.n_rdm = 10
        rdms.get_matrices.return_value = numpy.zeros([10, 3, 3])
        conf = MultiRdmPlot.from_show_rdm_args(
            rdms,
            pattern_descriptor = None,
            cmap = 'bone',
            rdm_descriptor=None,
            n_column = None,
            n_row = None,
            show_colorbar = 'figure',
            gridlines = None,
            num_pattern_groups = None,
            figsize = None,
            nanmask = "diagonal",
            style = None,
            vmin = None,
            vmax = None,
            icon_spacing = 1.0,
            linewidth = 0.5,
            overlay = None,
            overlay_color='#00ff0050',
            contour = None,
            contour_color = 'red'
        )
        self.assertEqual(conf.n_column, 4)
        self.assertEqual(conf.n_row, 3)
