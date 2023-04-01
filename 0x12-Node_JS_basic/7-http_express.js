const express = require('express');
const countStudents = require('./3-read_file_async');

const port = 1245;
const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  const intro = 'This is the list of our students\n';
  try {
    const data = await countStudents(process.argv[2]);
    res.send(`${intro}${data.join('\n')}`);
  } catch (error) {
    res.send(`${intro}${error.message}`);
  }
});
app.listen(port);
module.exports = app;
