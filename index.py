import web
        
urls = (
	'/blog/\d+', 'blog',
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

if __name__ == "__main__":
    app.run()