class Teacher():
    def teacher_actions(self):
        print('I teach')
class Student():
    def student_actions(self):
        print('I can code')
class you_tuber():
    def you_tuber_actions(self):
        print('I can edit videos')

class person(Teacher,Student,you_tuber):
    pass

codify=person()
codify.teacher_actions()
codify.student_actions()
codify.you_tuber_actions()