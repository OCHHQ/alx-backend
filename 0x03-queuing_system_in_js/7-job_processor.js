import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Function to process a notification job
 * @param {string} phoneNumber - The recipient's phone number
 * @param {string} message - The notification message
 * @param {object} job - The job instance
 * @param {function} done - The callback to signal completion
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Initial progress set to 0%

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Simulate job progress and processing
  job.progress(50, 100); // Midway progress set to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done(); // Mark the job as completed
};

// Process jobs in the `push_notification_code_2` queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});