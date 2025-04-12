const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  res.json({ service: 'product', status: 'ok' });
});

app.get('/products', (req, res) => {
  res.json([
    { id: 1, name: 'Laptop', price: 1500 },
    { id: 2, name: 'Phone', price: 800 },
    { id: 3, name: 'Headphones', price: 150 }
  ]);
});

app.listen(5003, () => {
  console.log('Product service running on port 5003');
});