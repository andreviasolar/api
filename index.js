const express = require('express');
const app = express();
const port = 3000;

app.get('/api/saudacao', (req, res) => {
  res.send('Olá, mundo! Esta é uma API simples de saudação.');
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
