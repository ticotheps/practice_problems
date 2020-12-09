const database = require('./database');
const express = require('express');
const app = express();

app.listen(5000, () => console.log('Listening on port 5000'));

// Keep a hash table of the previous access time for each user
const accesses = {};

app.get('/index.html', (req, res) => {
	const { user } = req.headers;

	// User is in the DB so check their previous access time to
	// see if they've exceeded their rate limit.
	if (user in accesses) {
		const previousAccessTime = accesses[user];

		// Limit to 1 request every 3 seconds.
		if (Date.now() - previousAccessTime < 3000) {
			res.status(429).send(
				"You've exceeded your rate limit of 1 request per 3 seconds.\n"
			);
			return;
		}
	}

	// User is NOT in the DB so serve the page and store
	// this access time.
	database.get('index.html', (page) => {
		accesses[user] = Date.now();
		res.send(page + '\n');
	});
});
