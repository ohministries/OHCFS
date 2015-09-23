import unittest
from classes import StudentCli
from mock import Mock, ReturnValues


class TestStudentCli(unittest.TestCase):
    def _initWithAddSubCommand(self):
        self.mockedDatabase = Mock()
        self.studentCli = StudentCli.StudentCli(self.mockedDatabase,'student','add',['john doe'])

    def _initWithConvertSubCommand(self):
        self.mockedDatabase = Mock()
        self.studentCli = StudentCli.StudentCli(self.mockedDatabase, 'leader', 'convert', ['joh doe'])

    def testAddsStudent(self):
        self._initWithAddSubCommand()
        self.mockedDatabase.mockCheckCall(0,'addStudent','john','doe')

    def testGetsAllStudentsWhenConverting(self):
        self._initWithConvertSubCommand()
        self.mockedDatabase.mockCheckCall(0,'getStudentsFromFilters',['joh doe'])

    def PASStestConvertsStudent(self):
        self._initWithConvertSubCommand()
        self.mockedDatabase.mockCheckCall(1,'convertStudentToLeader','John','Doe')