export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) !== 'string') throw TypeError('Name must be a string');
    if (typeof (length) !== 'number') throw TypeError('Length must be a number');
    if (Array.isArray(students) !== true) throw TypeError('Students must be an array');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(nameValue) {
    if (typeof (nameValue) !== 'string') throw TypeError('Name must be a string');
    this._name = nameValue;
  }

  get length() {
    return this._length;
  }

  set length(lengthValue) {
    if (typeof (lengthValue) !== 'number') throw TypeError('Length must be a number');
    this._length = lengthValue;
  }

  get students() {
    return this._students;
  }

  set students(studentsValue) {
    if (Array.isArray(studentsValue) !== true) throw TypeError('Students must be an array');
    this._students = studentsValue;
  }
}
