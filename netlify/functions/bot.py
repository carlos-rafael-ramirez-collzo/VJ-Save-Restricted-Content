const { spawn } = require('child_process');
const path = require('path');

exports.handler = async (event) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python3', [
      path.join(__dirname, '../../bot.py'),
      event.body
    ]);

    let output = '';
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code === 0) {
        resolve({
          statusCode: 200,
          body: output
        });
      } else {
        reject({
          statusCode: 500,
          body: 'Error ejecutando el bot'
        });
      }
    });
  });
};
