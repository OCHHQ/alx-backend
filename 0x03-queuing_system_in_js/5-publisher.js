import { createClient } from "redis";

//Create Redis client
const client = createClient();


//Handle successful connection
client.on('connect', () => {
    console.log('Redis client connection to the server');
});

//Handle connection errors
client.on('error', (err) => {
    console.log(`Redis client ot connected to the server: ${err.message}`);
});

/**
 * This publish a message to "Holberton school chennnel"after a delay
 * @param {string} message - The message sent.
 * @param {number} time - The delay in milliseconds
 */
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('Holberton school chennnel', message);

    }, time);
}

//Call the function with specified message and delays
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);