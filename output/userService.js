(function () {
	'use strict';
	var mysql = require('mysql');
	
	angular.module('app')
	.service('userService', ['$q', 'DatabaseConnector', UserService]);
	
	function UserService($q, DatabaseConnector) {
	
		var dbConnector = new DatabaseConnector();
		var connection = dbConnector.getConnection();
		
		return {
			create: createUser,
			destroy: destroyUser,
			update: updateUser,
			getAll: getUsers,
			getById: getUserbyId,
		};
		
		function createUser(user) {
			var deferred = $q.defer();
			var query = "INSERT INTO users SET ?";
			connection.query(query, [user], function(err, res) {
				if (err) deferred.reject(err);
				deferred.resolve(res.insertId);}
			});
			return deferred.promise;
		}
		
		function destroyUser(id) {
			var deferred = $q.defer();
			var query = "DELETE FROM users WHERE id = ?";
			connection.query(query, [id], function(err, res) {
				if (err) deferred.reject(err);
				deferred.resolve(res.insertId);}
			});
			return deferred.promise;
		}
		
		function getUsers() {
			var deferred = $q.defer();
			var query = "SELECT * FROM users";
			connection.query(query, function(err, res) {
				if (err) deferred.reject(err);
				deferred.resolve(res.insertId);}
			});
			return deferred.promise;
		}
		
		function getUserById(id) {
			var deferred = $q.defer();
			var query = "SELECT * FROM users WHERE id = ?";
			connection.query(query, [id], function(err, res) {
				if (err) deferred.reject(err);
				deferred.resolve(res.insertId);}
			});
			return deferred.promise;
		}
		
		function updateUser(user) {
			var deferred = $q.defer();
			var query = "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?";
			connection.query(query, [user.username, user.email, user.password, user.id], function(err, res) {
				if (err) deferred.reject(err);
				deferred.resolve(res.insertId);}
			});
			return deferred.promise;
		}
		
	}
})();
