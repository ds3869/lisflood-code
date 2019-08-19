"""

Copyright 2019 European Union

Licensed under the EUPL, Version 1.2 or as soon they will be approved by the European Commission  subsequent versions of the EUPL (the "Licence");

You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence at:

https://joinup.ec.europa.eu/sites/default/files/inline-files/EUPL%20v1_2%20EN(1).txt

Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the Licence for the specific language governing permissions and limitations under the Licence.

"""
from __future__ import absolute_import

# defining global variables

# global maskinfo         #Definition of compressed mask array and info how to blow it up again
# maskinfo = {}

# global MMaskMap, maskmapAttr, bigmapAttr, cutmap, metadataNCDF
global MMaskMap         #mask for checking maps
MMaskMap = 0

global maskmapAttr      #attributes of masking map (clonemap) - dictionary
maskmapAttr = {}


global cutmap           #defines the MaskMap inside the forcing maps
cutmap = [0, 1, 0, 1]

global metadataNCDF     #store map metadata from netcdf default file (or e0.nc)
metadataNCDF = {}

global timestepInit     #if initial conditions are stored as netCDF with different time steps this variable indicates which time step to use either as date e.g. 1/1/2010 or as number e.g. 5
timestepInit =[]

# global timeMes,TimeMesString, timeMesSum
global timeMes          # time measure - filled in dynamic
timeMes=[]

global TimeMesString    # name of the time measure - filled in dynamic
timeMesString = []

global timeMesSum       # time measure of hydrological modules
timeMesSum = []
