import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        let output = 'This is the list of our students';

        const sortedFields = Object.keys(fields).sort(
          (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
        );

        sortedFields.forEach((field) => {
          const names = fields[field];
          output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        });

        response.status(200).send(output);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const databasePath = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(databasePath)
      .then((fields) => {
        const names = fields[major] || [];
        response.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
