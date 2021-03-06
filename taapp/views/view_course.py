from . import setup
from .cmd_interface import CmdInterface
from .file_io import FileIO
from ..models import Course


class ViewCourse(CmdInterface):
    def action(self, command_input):
        # Checks that there is user currently logged in
        if setup.current_user is None:
            return "Failed. No user currently logged in"

        # Shouldnt need to check the permission: should be accessible to everyone

        # Verify legal parameters
        command_items = command_input.split()
        valid_params = self.validateInputParameters(command_items)
        if not valid_params:
            return "Failed. Invalid parameters"

        # Check for course existence
        file = FileIO()
        course_item = file.readData(command_items[1], "Course")
        if course_item is None:
            return "Failed. Course does not exists"

        # Print out course information
        print("Course ID: " + course_item.courseID)
        print("Name: " + course_item.courseName)
        print("# of Lectures: " + course_item.lectureSectionCount)
        print("# of Labs: " + course_item.labSectionCount)


    def validateInputParameters(self, parameters):
        # Need to check that the courseID is a 5 digit positive integer (> 99999)
        if len(parameters) != 2:
            return False

        return True
