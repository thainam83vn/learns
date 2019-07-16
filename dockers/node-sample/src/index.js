const express = require('express');
const app = express();
const PORT = process.env.PORT || 80;

app.get('/', (req, res) => {
  console.log('API GET /: 200OK');
  res.send('Great. API is working');
});

app.listen(PORT, () => console.log(`Listen ${PORT}`));
