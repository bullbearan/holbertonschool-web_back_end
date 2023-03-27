const updateStudentGradeByCity = (listStudents, city, newGrades) => {
  const h = listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter((grade) => grade.studentId === student.id);
      const a = student;

      if (grade.length === 1) a.grade = grade[0].grade;
      else a.grade = 'N/A';

      return student;
    });
  return h;
};
export default updateStudentGradeByCity;
