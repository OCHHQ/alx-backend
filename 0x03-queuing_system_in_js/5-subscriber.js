import { createClient } from "redis";

//Create Redis Client
const client = createClient();

//Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

//Handle connection Error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the "Holberton school channel"
client.subscribe('holberton school channel');

// Listen for message
client.on('message', (channel, message) => {
    console.log(`Recieved message: ${message}`);

    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
