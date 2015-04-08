#
#   Copyright (c) 2013-2014, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
# Make sure we import the local openbandparams version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from openbandparams import *

AlInAs_InP = AlInAs(a=InP.a())
GaInAs_InP = GaInAs(a=InP.a())

AlGaInAs_InP = IIIVZincBlendeTernary(
    name='AlGaInAs/InP',
    elements=('Al', 'Ga', 'InAs'),
    binaries=(AlInAs_InP, GaInAs_InP),
    parameters=[])

print AlGaInAs_InP.latex()
print 'Eg =', AlGaInAs_InP(Al=0).Eg()

# Change a parameter in this instance, but no other instances
GaInAs_InP.set_parameter(ValueParameter('Eg_Gamma', 2., 'eV'))
print 'Customized Eg =', AlGaInAs_InP(Al=0).Eg()