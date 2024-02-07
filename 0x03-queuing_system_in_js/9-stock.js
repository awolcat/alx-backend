import { createClient } from 'redis';
import {promisify } from 'util';

const express = require('express');

const listProducts = [ 
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 }, 
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  for ( const product of listProducts ) {
    if ( product.id === id ) return product;
  }
}

const client = createClient();

function reserveStockById(itemID, stock) {
  client.SET(`item.${itemId}`, stock);
}

function getCurrentReservedStockById(itemId) {
  return promisify(client.GET).bind(client)(`item.${itemId}`);
}

const app = express();
const port = 1245;

app.get('/list_products', (request, response) => {
  response.json(listProducts);
});

app.get('/list_products/:itemId', (request, response) => {
  const id = parseInt(request.params.itemId);
  const item = getItemById(id);
  if ( !item ) {
    response.json({'status': 'Product not found'});
  } else {
    response.json(item);
  }
});

app.listen(port);


