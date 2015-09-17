# Copyright (C) 2015  Ouachita Hills Ministries
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest

from classes import Database


class databaseTestCase(unittest.TestCase):
	def setUp(self):
		testDatabase = Database()

# ToDo:
#
# test getStudent
# test every table exists
#
# tableList = ['inventoryRecord', 'student', 'vehicle',
#			 'mileageRecord', 'fuelRecord', 'expense',
#			 'cashOnHandRecord', 'bankTransaction',
#			 'advance', 'dailyStudentRecord', 'book',
#			 'bookSaleRecord']

class testInventoryRecordTableExistence(databaseTestCase):
	def runTest(self):
		self.assertEqual(testDatabase.testTablePresent('inventoryRecord'), 1,
			'inventoryRecord table missing')

runner = unittest.TextTestRunner()
runner.run(testInventoryRecordTableExistence)