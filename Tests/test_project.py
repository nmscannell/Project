from unittest import TestCase
from main.models import UI
from django.test import testcases
"""
TODO: 
add permission denied tests 
add password field to edit and editInfo
finish login command 
"""
class TestProject(TestCase):

    def setUp(self):
        self.UI = UI()
        self.UI.command("createAccount accountName title")
        self.UI.command("editAccount accountName password newPassword")
        self.UI.command("login accountName newPassword")



    """
        login command
        When the login command is entered, it takes two arguments
        -user name
        -password
    
    """
    def test_command_login_success(self):
        self.assertEqual(self.UI.command("login userName password"), "Login success")

    def test_command_login_failure(self):
        self.assertEqual(self.UI.command("login userName password"), "Login failed")

    """ 
        createAccount command
        When the createAccount command is entered, it takes 3 arguments:
        -User name 
        -Title
        -Email 
    
        If arguments are missing from the command, an error message is displayed and the command is not executed.  
    """

    def test_command_createAccount_success(self):
        self.assertEqual(self.UI.command("createAccount username title email"), "Account successfully created")

    def test_command_createAccount_missingArguments(self):
        self.asserEqual(self.UI.command("createAccount username"),
                        "Your command is missing arguments, please enter your command in the following format: "
                        "createAccount username title email")

    def test_command_createAccount_missingArguments2(self):
        self.asserEqual(self.UI.command("createAccount username title"),
                        "Your command is missing arguments, please enter your command in the following format: "
                        "createAccount username title email")

    def test_command_createAccount_invalidTitle(self):
        self.assertEqual(self.UI.command("createAccount accountName cashier"), "Please enter a valid title")

    def test_command_createAccount_no_args(self):
        self.assertEqual(self.UI.command("createAccount"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createAccount username title email")

    def test_command_createAccount_already_exists(self):
        self.assertEqual(self.UI.command("createAccount accountName title email"), "Account already exists")

    """
        createCourse command 
        When the createCourse command is entered, it takes five arguments:
        -Course Name 
        -Course Number 
        -Meetings days or "online" for an online class
        -Start time 
        -End time
           
        If the course name matches a database entry a then the course is not created 
        and an error message is displayed and some other stuff
           
        If a command argument is missing, an error message is displayed. 
            
    """

    def test_command_createCourse_success(self):
        self.assertEqual(self.UI.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course successfully created")

    def test_command_createCourse_missingArguments(self):
        self.assertEqual(self.UI.command("createCourse courseNumber daysOfWeek start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments2(self):
        self.assertEqual(self.UI.command("createCourse courseName daysOfWeek start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments3(self):
        self.assertEqual(self.UI.command("createCourse courseName courseNumber start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments4(self):
        self.assertEqual(self.UI.command("createCourse courseName courseNumber daysOfWeek end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments5(self):
        self.assertEqual(self.UI.command("createCourse courseName courseNumber daysOfWeek start"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_no_args(self):
        self.assertEqual(self.UI.command("createCourse"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_course_exists(self):
        self.assertEqual(self.UI.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course already exists, course not added.")


    """
        When the createLab command is entered, it takes the following arguments:
        -Course number associated with the lab 
        -Lab section number
        -Day(s) of week
        -Begin time
        -End time
        If the lab already exists, a new lab is not created. If arguments are missing, return error. If the 
        associated course is online, a lab cannot be created for it.
    """

    def test_command_createLab_success(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection day begin end"),
                         "Course successfully created")

    def test_command_createLab_no_args(self):
        self.assertEqual(self.UI.command("createLab"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_lab_exists(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection day begin end"),
                         "Lab already exists, lab not added")

    def test_command_createLab_missing_course(self):
        self.assertEqual(self.UI.command("createLab labSection day begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_section(self):
        self.assertEqual(self.UI.command("createLab courseNumber day begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_day(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_begin(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection day end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_end(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection day begin"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_invalid_lab(self):
        self.assertEqual(self.UI.command("createLab courseNumber labSection day begin end"),
                         "Lab cannot be created for an online course.")

    """
        When the edit command is entered, it takes 4 arguments.
        Only supervisors and administrators can utilize this command
        -Username
        -Field that needs editing 
            - Home phone
            - Email 
            - Office hours (a start time, an end time and days of office hours) 
            - Address 
            - Office Number
            - Office phone Number
            - Password 
        -The new information to replace the current information 
        
        If the user does not exist, an error message is displayed.
        If command arguments are missing, an error message is displayed. 
    
       """

    def test_command_edit_homePhone_success(self):
        self.asserEqual(self.UI.command("edit username homephone 262-555-7134"),
                        "Home phone successfully updated")

    def test_command_edit_email_success(self):
        self.assertEqual(self.UI.command("edit username email timmy345@uwm.edu"),
                         "Email successfully updated")

    def test_command_edit_office_hours_success(self):
        self.assertEqual(self.UI.command("edit username officehours 1500 1600 MW"),
                         "Office hours successfully updated")

    def test_command_edit_address_success(self):
        self.assertEqual(self.UI.command("edit username address 6789 Hilly Avenue Milwaukee WI 53218"),
                         "Address successfully updated")

    def test_command_edit_officeNumber_success(self):
        self.assertEqual(self.UI.command("edit username officeNumber 5679"),
                         "Office number successfully updated")

    def test_command_edit_officePhone_success(self):
        self.assertEqual(self.UI.command("edit username officePhone 262-789-5476"),
                         "Office phone successfully updated")

    def test_command_edit_password_success(self):
        self.assertEqual(self.UI.command("edit username password newPassword"), "Password successfully changed")

    def test_command_edit_error_missing_args1(self):
        self.assertEqual(self.UI.command("edit"),
                         "There are missing arguments in your command. Please enter your command in the following "
                         "format: edit username field newInformation")

    def test_command_edit_error_missing_args2(self):
        self.assertEqual(self.UI.command("edit username"),
                         "There are missing arguments in your command, Please enter you command in the following "
                         "format: edit username field newInformation")

    def test_command_edit_error_missing_args3(self):
        self.assertEqual(self.UI.command("edit username homePhone"),
                         "There are missing arguments in your command, Please enter you command in the following "
                         "format: edit username field newInformation")

    def test_command_edit_error_user_does_not_exist(self):
        self.assertEqual(self.UI.command("edit username homePhone 262-555-7134"),
                         "The user you specified does not exist in the system, please try again")

    """
        send command 
        Only supervisors and administrators can utilize this command 
        When the sendOutNotification command is entered it takes 2-3 arguments: 

        -send -a
        To send notification to all users.

        -send accountNames -s
        To send notification to specific users.

        -send  accountName
        to send notification to one person
    """

    def test_command_send_success(self):
        self.assertEqual(self.UI.command("sendNotification accountName"), "Notification was sent successfully")

    def test_command_send_all_success(self):
        self.assertEqual(self.UI.command("sendNotification -a"),
                         "Notification was sent to all users successfully")

    def test_command_send_specific_success(self):
        self.assertEqual(self.UI.command("sendNotification accountName(s) -s"),
                         "Notification was sent to specific people successfully")

    def test_command_send_error(self):
        self.assertEqual(self.UI.command("sendNotification accountName"),
                         "We weren't able to send a notification")

    def test_command_send_all_error(self):
        self.assertEqual(self.UI.command("sendNotification accountName -a"),
                         "We weren't able to send a notification to all")

    def test_command_send_specific_error(self):
        self.assertEqual(self.UI.command("sendNotification accountNames -s"),
                         "We weren't able to send a notification to specific people")

    def test_command_send_no_argument(self):
        self.assertEqual(self.UI.command("sendNotification -s"),
                         "Please type the user names that you want to sent")

    def test_command_send_no_argument_2(self):
            self.assertEqual(self.UI.command("sendNotification -a"),
                             "Please type the user names  that you want to sent")

    def test_command_send_no_argument_3(self):
        self.assertEqual(self.UI.command("sendNotification"), "Please type the username that you want to sent")


    """
        sendTA command
        The sendTA command takes one argument 
        -classNumber
    """

    def test_command_sendTA_success(self):
        self.assertEqual(self.UI.command("sendTA courseNumber"), "Email sent successfully to all TAs associated"
                                                                      "with the specified course")

    def test_command_sendTA_error_course_does_not_exist(self):
        self.assertEqual(self.UI.command("sendTA courseNumber"), "Error, course does not exist, email not sent")

    def test_command_sendTA_missingArguments(self):
        self.assertEqual(self.UI.command("sendTA"),
                         "Your command is missing arguments, please enter the command in the following format: "
                         "sendTA courseNumber")

    """
        When the deleteAccount command is entered, it takes two arguments, 
        -name 
        -title
        If a name or title is missing, an error message is displayed
        If the account that the user is trying to delete does not exist, an error 
           message is displayed.          
    """

    def test_command_deleteAccount(self):
            self.assertEqual(self.UI.command("deleteAccount userName"), "Account successfully deleted")

    def test_command_deleteAccount_no_name(self):
            self.assertEqual(self.UI.command("deleteAccount"),
                             "There are arguments missing, please enter your command in the following format: "
                             "deleteAccount userName")

    def test_command_deleteAccount_doesNotExist(self):
            self.assertEqual(self.UI.command("deleteAccount userName"), "Error, Account does not exist")



    """
        When the assignInstructorCourse command is entered it takes 2 arguments: 
        - class Number
        - Instructor user Name
    """

    def test_command_assignInstructorCourse_missingArguments(self):
        self.assertEqual(self.UI.command("assignInstructorCourse classNumber"),
                         "There are arguments missing, Please enter your command in the following format: "
                         "assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_missingArguments2(self):
        self.assertEqual(self.UI.command("assignInstructorCourse userName"),
                         "There are arguments missing, Please enter your command in the following format: "
                         "assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_no_args(self):
        self.assertEqual(self.UI.command("assignInstructorCourse"),
                         "There are arguments missing, Please enter your command in the following format: "
                         "assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_conflict(self):
        self.assertEqual(self.UI.command("assignInstructorCourse classNumber userName"),
                         "This class was already assigned")

    def test_command_assignInstructorCourse_success(self):
        self.assertEqual(self.UI.command("assignInstructorCourse classNumber userName"),
                         "Assignment was successful")

    """
        When assignTACourse command is entered, it takes two arguments:
        --TA username
        --Course number
        Assignment may fail if:
        --Scheduling conflict for TA
        --Max TAs assigned to course
        --TA username is invalid or missing
        --Course number is invalid or missing
        --No arguments    
    """

    def test_command_assignTACourse_success(self):
        self.assertEqual(self.UI.command("assignTACourse userName courseNumber"), "Assignment successful")

    def test_command_assignTACourse_missingTA(self):
        self.assertEqual(self.UI.command("assignTACourse courseNumber"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "assignTACourse userName classNumber")

    def test_command_assignTACourse_invalidTA(self):
        self.assertEqual(self.UI.command("assignTACourse userName courseNumber"), "Invalid TA username.")

    def test_command_assignTACourse_missingCourse(self):
        self.assertEqual(self.UI.command("assignTACourse accountName"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "assignTACourse userName classNumber")

    def test_command_assignTACourse_invalidCourse(self):
        self.assertEqual(self.UI.command("assignTACourse accountName courseNumber"), "Invalid course number.")

    def test_command_assignTACourse_Maximum(self):
        self.assertEqual(self.UI.command("assignTACourse userName courseNumber"),
                         "TA has exceeded assignment limit, TA not assigned")

    def test_command_assignTACourse_schedulingConflict(self):
        self.assertEqual(self.UI.command("assignTACourse userName courseNumber"),
                         "Scheduling conflict encounterd, TA not assigned.")

    def test_command_assignTACourse_noArgs(self):
        self.assertEqual(self.UI.command("assignTACourse"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "assignTACourse userName classNumber")


    """
        assignTALab
        -When the assignTALab command is entered, it takes three arguments
        -userName of TA to be assigned
        -classNumber
        -Lab section number 
    """

    def test_command_assignTALab_success(self):
        self.assertEqual(self.UI.command("assignTALab userName classNumber labSectionNumber"),
                         "TA successfully assigned")

    def test_command_assignTALab_argumentsMissing(self):
        self.assertEqual(self.UI.command("assignTALab username classNumber"),
                         "Your argument is missing commands, please enter your command in the following format: "
                         "assignTALab username classNumber labSectionNumber")

    def test_command_assignTALab_argumentsMissing(self):
        self.assertEqual(self.UI.command("assignTALab userName"),
                         "Your argument is missing commands, please enter your command in the following format: "
                         "assignTALab username classNumber labSectionNumber")

    def test_command_assignTALab_TAMax(self):
        self.assertEqual(self.UI.command("assignTALab userName classNumber labSectionNumber"),
                         "TA has been reached maximum assignment limit, TA not assigned")

    def test_command_assignTALab_grader(self):
        self.assertEqual(self.UI.command("assignTALAb userName classNumber labSectionNumber"),
                         "The specified TA is a grader, TA not assigned")


    """
        When the viewInfo command is entered it takes one argument: 
        -accountName 
        
        If the account does not exist, an error message is displayed, otherwise, public data is displayed   
    """

    def test_command_viewInfo_success(self):
        self.asserEqual(self.UI.command("viewInfo userName"), "")

    def test_command_viewInfo_user_does_not_exist(self):
        self.asserEqual(self.UI.command("viewInfo userName"), "Account does not exist")

    def test_command_viewInfo_no_accountName(self):
        self.assertEqual(self.UI.command("viewInfo"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "viewInfo userName")

    """
        editInfo command
        The editInfo command does not take a userName because it is implied that the user will be editing his/her 
        own information when he/she is logged into the system. 
        When the editInfo command is entered it takes two arguments: 
        -Field that needs editing, can include: 
            -homePhone
            -email
            -officeHours (start time, end time and day(s) of week entered as a string)
            -Address (entered as a string)
            -Password 
        -What the field should be changed to. 
    
    """

    def test_command_editInfo_homePhone_success(self):
        self.assertEqual(self.UI.command("editInfo homePhone 262-777-8888"), "Home phone successfully updated")

    def test_command_editInfo_email_success(self):
        self.assertEqual(self.UI.command("editInfo email timmy123@uwm.edu"), "Email successfully updated")

    def test_command_editInfo_officeHours(self):
        self.assertEqual(self.UI.command("editInfo officeHours ""start end daysOfWeek"),
                         "Office hours successfully updated")

    def test_command_editInfo_address(self):
        self.assertEqual(self.UI.command("editInfo address ""6785 Holly Lane Milwaukee WI 54389"),
                         "Address successfully updated")

    def test_command_editInfo_password(self):
        self.assertEqual(self.UI.command("editInfo password newPassword"), "Password successfully changed.")

    def test_command_editInfo_missingArgument(self):
        self.assertEqual(self.UI.command("editInfo homePhone"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "editInfo field newInformation")

    """
        viewCourseAssignments
        When the viewCourseAssignments command is entered, it takes no arguments 
        It is implied that the viewCourseAssignments will display the course assignments 
        for the instructor who is currently logged in to the system. 
    
    """

    def test_command_viewCourseAssignments(self):
        self.assertEqual(self.UI.command("viewCourseAssignments"), "")


    """
       When the viewTAAssignments command is entered, it takes one argument
       - class Number 

       If the class Number is not entered, an error message is displayed
       If the class does not exist, an error message is displayed 
       
    """

    def test_command_viewTAAssignments_success(self):
        self.assertEqual(self.UI.command("viewTAAssignments classNumber"), "The TA Assignments are: ")

    def test_command_viewTAAssignments_noClassNum(self):
        self.assertEqual(self.UI.command("viewTAAssignments"),
                         "Your command is missing arguments, please enter the command in the following format: "
                         "viewTAAssignments classNumber")

    def test_command_viewTAAssignments_classDoesNotExist(self):
        self.assertEqual(self.UI.command("viewTAAssignments classNumber"), "Class does not exist")
