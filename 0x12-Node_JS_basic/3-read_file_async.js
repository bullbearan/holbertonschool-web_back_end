const fs = require('fs').promises;

const countStudents = (path) => {
  const promise = async (resolve, reject) => {
    try {
      let a = null;
      const final = [];
      let data = await fs.readFile(path);
      data = data.toString().split('\n');
      data = data.slice(1, data.length - 1);
      const fields = {};
      data.forEach((row) => {
        if (row.length > 0) {
          const info = row.split(',');
          if (info[3] in fields) fields[info[3]].push(info[0]);
          else fields[info[3]] = [info[0]];
        }
      });
      a = `Number of students: ${data.length}`;
      console.log(a);
      final.push(a);
      for (const [key, value] of Object.entries(fields)) {
        if (key) {
          a = `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`;
          console.log(a);
          final.push(a);
        }
      }
      resolve(final);
    } catch (error) {
      reject(Error('Cannot load the database'));
    }
  };
  return new Promise(promise);
};
module.exports = countStudents;
