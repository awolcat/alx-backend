const kue = require('kue');

export default function createPushNotificationJobs(jobs, queue) {
  if ( !Array.isArray(jobs) ) {
    throw new Error('Jobs is not an array');
  } else {
    const queue = kue.createQueue();
    for ( const jobData of jobs ) {
      const job = queue.create('push_notification_code_3', jobData).save((err) => {
        if ( !err ) console.log('Notification job created', job.id);
      });
      job.on('complete', (result) => {
        console.log(`Notification job ${job.id} completed`);
      }).on('failed', (result) => {
        console.log(`Notification job ${job.id} failed:`, result);
      }).on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    }
  }
}
