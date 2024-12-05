const kue  = require('kue')

//create queue
const queue = kue.createQueue();


//function for handig notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}. with message: ${message}`)
}

//process
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});