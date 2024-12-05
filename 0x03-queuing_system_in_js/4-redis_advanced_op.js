// import the redis library
const redis = require('redis');

const client = redis.createClient();

//here check the connection status
client.on('connect', () => {
    console.log('Redis client connection to server')
});

// Error handing is very import to understand where to handle constrains
client.on(`error`, (err) => {
    console.log(`Error: ${err}`)
});

// Data storing in hash
const hashKey = 'HolbertonSchools';
const data = {
    Portland:50,
    Seattle:80,
    'New York':20,
    Bogota:20,
    Cali:40,
    Paris:2,
};

//Store the hash
for (const[city, value] of Object.entries(data)) {
    client.hset(hashKey, city, value, (err, reply) => {
        if (err) {
            console.log(`Error setting ${city}: ${err}`);
        } else {
            console.log(`Reply for ${city}: ${reply}`)
        }
    });
}

client.hgetall(hashKey, (err, object) => {
    if (err) {
        console.log(`Error retrieving hash: ${err}`);
    } else {
        console.log(object);
    }

    // ensure to close redis connection after operation
    client.quit();
})