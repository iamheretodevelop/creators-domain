class StudentRecord:
  student_record = []

  def __init__(self):
    self.student_dict = {}

  def create_info(self, name, id, classification, number_of_credit):
    self.student_dict['name'] = name
    self.student_dict['id'] = id
    self.student_dict['classification'] = classification
    self.student_dict['number_of_credit'] = number_of_credit

  def add_info(self):
    StudentRecord.student_record.append(self.student_dict)

# robert = StudentRecord()
# robert.create_info("Robert", "0123", "Freshman", 50)
# robert.add_info()
# print(StudentRecord.student_record)

# bon = StudentRecord()
# bon.create_info("Bon", "2322", "Junior", 115)
# bon.add_info()
# print(StudentRecord.student_record)

class StudentResult(StudentRecord):
  student_records = [{"name":"James Anderson", "id":"02228211", "classification":"Sophomore", "number_of_credit":30},{'name': 'Sam Barnes', 'classification': "Freshman", 'id': "03258411", 'number_of_credit': 20},{'name': 'Ashley Summers', 'classification': "Senior", 'id': "01429895", 'number_of_credit': 110}]
  def student_finder(self, name):
    for student in self.student_records:
      if student["name"] == name:
        return student
      return "Student does not exist"

  def credits_left(self, name):
    student_dictionary = self.student_finder(name)
    current_credits = student_dictionary['number_of_credit']
    credits_remaining = 120 - current_credits
    return credits_remaining

  def courses_left(self, name):
    credits = self.credits_left(name)
    if credits % 4 == 0:
      courses_remaining = credits/4
    else:
      courses_remaining = credits//4
      credits -= courses_remaining * 4
      if credits % 2 == 0:
        courses_remaining += credits/2
      else:
        courses_remaining = credits//2
        credits -= courses_remaining * 2
        courses_remaining += credits
    return int(courses_remaining)

  def return_message(self, name):
    message = name + " needs " + str(self.credits_left(name))+ " credits and "+ str(self.courses_left(name))+ " courses to graduate."
    return message
  
  def remove(self, name):
    student = self.student_finder(name)
    self.student_records.remove(student)
    return self.student_records

james = StudentResult()
james.student_finder("James Anderson")
james.credits_left("James Anderson")
james.courses_left("James Anderson")
print(james.return_message("James Anderson"))

