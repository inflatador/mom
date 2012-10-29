#!/usr/bin/env python
# Memory Overcommitment Manager
# Copyright (C) 2010 Adam Litke, IBM Corporation
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from distutils.core import setup

setup(name='mom',
      version='0.3.0',
      description='Memory Overcommitment Manager',
      author='Adam Litke',
      author_email='agl@us.ibm.com',
      url='http://www.ovirt.org',
      packages=['mom', 'mom.Collectors', 'mom.Controllers', 'mom.HypervisorInterfaces', 'mom.Policy',
                'mom.debug' ],
      keywords=['Requires: libvirt'],
      data_files=[('/usr/sbin', ['momd']),
                  ('/usr/share/doc/mom/examples',
                   ['doc/mom-balloon.conf', 'doc/balloon.rules',
                    'doc/mom-balloon+ksm.conf', 'doc/ksm.rules']
                  )],
     )

