const database = {
	['index.html']: '<html>Hello there from the database!</html>',
};

module.exports.get = (key, callback) => {
	setTimeout(() => {
		callback(database[key]);
	}, 1000);
};
