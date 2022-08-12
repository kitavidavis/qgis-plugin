# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeopsyCollect
                                 A QGIS plugin
 This plugin fetches geometrical data from the GeoPsy Collect platform and visualizes it as points, polylines or polygons
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-12
        copyright            : (C) 2022 by David Kitavi
        email                : daviskitavi@geopsyresearch.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeopsyCollect class from file GeopsyCollect.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geopsy_collect import GeopsyCollect
    return GeopsyCollect(iface)
