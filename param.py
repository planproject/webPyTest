import web
        
urls = (
	'/blog', 'blog',
)
app = web.application(urls, globals())

		
class blog:
	def GET(self):
		return web.ctx.env	#获取请求头


if __name__ == "__main__":
    app.run()