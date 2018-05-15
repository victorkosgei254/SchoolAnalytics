class Courses():
    #this class creates a course object,table,
    course_name = models.CharField(max_length = 60)
    #course_id = to be generated automatically
    #TODO Create a function to register new courses

    
class RegisterCourse():
    #this class regsters student to a course,by adding student id
    #this class updates the table with new rows


class ExaminationID():
    #this class is to update a table with new columns

class GenerateReport():
    #this class generates a report based on user request
    #generate pass list,fail list,English Pass,
    #student individual report

class SendReport():
    #send report to recepient{Student,Teacher,Administator}
    #

#--------------The below classes does the task of filtering data based on school --------
#No school should view another schools data in any way,no mixing of student results,
