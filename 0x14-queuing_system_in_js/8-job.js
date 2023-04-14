export default function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) throw Error("Jobs is not an array");
	jobs.forEach((job) => {
		const currentJob = queue.create("push_notification_code_3", job).save((err) => {
			if (!err) console.log(`Notification job created: ${currentJob.id}`);
		});
		currentJob.on("complete", () => console.log(`Notification job ${currentJob.id} completed`));
		currentJob.on("failed", (err) =>
			console.log(`Notification job ${currentJob.id} failed: ${err}`),
		);
		currentJob.on("progress", (progress) =>
			console.log(`Notification job ${currentJob.id} ${progress}% complete`),
		);
	});
}
