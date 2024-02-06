/*
import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log('Redis client not connected to the server:', error.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
*/

import redisClient from './redisClient.js';

const client = redisClient();

client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
