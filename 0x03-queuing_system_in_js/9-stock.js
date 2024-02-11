import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const listProducts = [ 
  { id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 }, 
  { id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 3 },
];

function getItemById(id) {
  for ( const product of listProducts ) {
    if ( product.id === id ) return product;
  }
}

const client = createClient();
client.on('error', (error) => {
  console.log('Redis client not connected to the server:', error.toString());
});

client.on('connect', (err, response) => {
  console.log('Redis client connected to the server');
});


function reserveStockById(itemId, stock) {
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

app.get('/list_products/:itemId', async (request, response) => {
  const id = parseInt(request.params.itemId);
  const item = getItemById(id);
  if ( !item ) {
    response.json({'status': 'Product not found'});
  } else {
    const reserved = await getCurrentReservedStockById(item.id) ||  0;
    const reservedStock = parseInt(reserved);
    item.currentQuantity = item.initialAvailableQuantity - reservedStock;
    response.json(item);
  }
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const id = parseInt(request.params.itemId);
  const item = getItemById(id);
  if ( !item ) {
    response.json({'status' : 'Product not found'});
    return;
  } else if ( item ) {
    const reserved = await getCurrentReservedStockById(item.id) ||  0;
    const stockReserved = parseInt(reserved);
    item.currentQuantity = item.initialAvailableQuantity - stockReserved;
    if ( item.currentQuantity < 1 ) {
      response.json({'status': 'Not enough stock available', 'itemID': item.id});
      return;
    } else {
      await reserveStockById(item.id, stockReserved + 1);
      response.json({'status': 'Reservation confirmed','itemId':1, 'remaining': item.currentQuantity});
    }
  }
});

app.listen(port);
