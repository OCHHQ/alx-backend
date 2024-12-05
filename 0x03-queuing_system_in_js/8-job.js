/**
 * Creates push notification jobs and adds them to a Kue queue.
 *
 * @param {Array} jobs - Array of job objects containing phoneNumber and message.
 * @param {object} queue - Kue queue instance.
 * @throws {Error} If jobs is not an array.
 */
const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    jobs.forEach((jobData) => {
      const job = queue.create('push_notification_code_3', jobData);
  
      job
        .on('enqueue', () => {
          console.log(`Notification job created: ${job.id}`);
        })
        .on('complete', () => {
          console.log(`Notification job ${job.id} completed`);
        })
        .on('failed', (error) => {
          console.log(`Notification job ${job.id} failed: ${error}`);
        })
        .on('progress', (progress) => {
          console.log(`Notification job ${job.id} ${progress}% complete`);
        });
  
      job.save();
    });
  };
  
  export default createPushNotificationsJobs;  