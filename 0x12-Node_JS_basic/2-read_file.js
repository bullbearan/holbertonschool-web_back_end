const fs = require('fs');

const countStudents = (path) => {
  try {
    let data = fs.readFileSync(path).toString().split('\n');
    data = data.slice(1, data.length - 1);
    const fields = {};
    data.forEach((row) => {
      if (row.length > 0) {
        const info = row.split(',');
        if (info[3] in fields) fields[info[3]].push(info[0]);
        else fields[info[3]] = [info[0]];
      }
    });
    console.log(`Number of students: ${data.length}`);
    for (const [key, value] of Object.entries(fields)) {
      if (key) console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
