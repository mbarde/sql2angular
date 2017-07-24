# Generates CRUD Service for AngularJS from SQL table

from stringBuilder import StringBuilder

def insert_function(name, parameter, query, queryParameter, stringBuilder):
	if parameter:
		stringBuilder.addLine('function ' + name + '(' + parameter + ') {')
	else:
		stringBuilder.addLine('function ' + name + '() {')

	stringBuilder.increaseIndentation()
	stringBuilder.addLine('var deferred = $q.defer();')
	stringBuilder.addLine('var query = "' + query + '";')

	if queryParameter:
		stringBuilder.addLine('connection.query(query, [' + queryParameter + '], function(err, res) {')
	else:
		stringBuilder.addLine('connection.query(query, function(err, res) {')

	stringBuilder.increaseIndentation()
	stringBuilder.addLine('if (err) deferred.reject(err);')
	stringBuilder.addLine('deferred.resolve(res.insertId);}')
	stringBuilder.decreaseIndentation()
	stringBuilder.addLine('});')
	stringBuilder.addLine('return deferred.promise;')
	stringBuilder.decreaseIndentation()
	stringBuilder.addLine('}')
	stringBuilder.addLine('')

def generate_service(table):
	sb = StringBuilder()
	sb.addLine('(function () {')
	sb.increaseIndentation()
	sb.addLine('\'use strict\';')
	sb.addLine('var mysql = require(\'mysql\');')
	sb.addLine('')
	sb.addLine('angular.module(\'app\')')
	sb.addLine('.service(\'' + table.name + 'Service\', [\'$q\', \'DatabaseConnector\', ' + table.name.title() + 'Service]);')
	sb.addLine('')
	sb.addLine('function ' + table.name.title() + 'Service($q, DatabaseConnector) {')
	sb.addLine('')
	sb.increaseIndentation()
	sb.addLine('var dbConnector = new DatabaseConnector();')
	sb.addLine('var connection = dbConnector.getConnection();')
	sb.addLine('')

	sb.setIndentation(2)
	sb.addLine('return {')
	sb.increaseIndentation()
	sb.addLine('create: create' + table.name.title() + ',')
	sb.addLine('destroy: destroy' + table.name.title() + ',')
	sb.addLine('update: update' + table.name.title() + ',')
	sb.addLine('getAll: get' + table.name.title() + 's,')
	sb.addLine('getById: get' + table.name.title() + 'byId,')
	sb.decreaseIndentation()
	sb.addLine('};')
	sb.addLine('')

	insert_function('create' + table.name.title(), table.name, 'INSERT INTO ' + table.sqlName + ' SET ?', table.name, sb)
	insert_function('destroy' + table.name.title(), 'id', 'DELETE FROM ' + table.sqlName + ' WHERE id = ?', 'id', sb)
	insert_function('get' + table.name.title() + 's', False, 'SELECT * FROM ' + table.sqlName, False, sb)
	insert_function('get' + table.name.title() + 'ById', 'id', 'SELECT * FROM ' + table.sqlName + ' WHERE id = ?', 'id', sb)

	hName = 'update' + table.name.title()
	hQuery = 'UPDATE ' + table.sqlName + ' SET '
	hQueryParameter = ''
	for field in table.fields:
		hQuery += field + ' = ?, '
		hQueryParameter += table.name + '.' + field + ', '
	hQuery = hQuery[:-2]
	hQuery += ' WHERE id = ?'
	hQueryParameter += table.name + '.' + 'id'
	insert_function(hName, table.name, hQuery, hQueryParameter, sb)

	sb.decreaseIndentation()
	sb.addLine('}')
	sb.decreaseIndentation()
	sb.addLine('})();')

	f = open('output/' + table.name + 'Service.js', 'w')
	f.write(sb.getString())
	f.closed
