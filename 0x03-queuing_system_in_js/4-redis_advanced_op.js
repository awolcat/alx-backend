import { createClient, print } from 'redis';

const client = createClient() // Defaults to localhost on port 6sth
client.on('error', (error) => {
  console.log('Redis client not connected to the server:', error.toString());
});

client.on('connect', (err, response) => {
  console.log('Redis client connected to the server');
});

function setFieldValue(key, field, value) {
  client.hset(key, field, value, print);
}

const fieldValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [field, value] of Object.entries(fieldValues)) {
  setFieldValue('HolbertonSchools', field, value);
}

client.hgetall('HolbertonSchools', (error, response) => console.log(response));
