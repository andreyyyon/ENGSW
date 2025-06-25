const express = require('express');
const app = express();
const port = 3000;

let itens = [
    { id: 1, name: "Engenharia de Software"},
    { id: 2, name: "Sistemas de Informacao"}
];

app.get('/items', (req, res) => {
 res.status(200).json(itens);
});

app.listen(port, () => {
    console.log(`Servidor está rodando em http://localhost:${port}`);
});
