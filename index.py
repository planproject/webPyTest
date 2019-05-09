import web
        
urls = (
	'/blog/\d+', 'blog',
	'/rape/(.*)', 'rape',
	'/paramss', 'accepts',
	'/(.*)', 'hello',
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
		
class blog:
	def GET(self):
		return 'number:'

class rape:
	def GET(self, query):
		if not query:
			query = 'no'
		return 'Freeze' + query
		
class accepts:
	def GET(self):
		query = web.input()
		return query

if __name__ == "__main__":
    app.run()