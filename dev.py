import web
import MySQLdb
import MySQLdb.cursors

render = web.template.render('template')

urls = (
    '/article', 'article',

)