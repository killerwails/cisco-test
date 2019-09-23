import web
import re

urls = (
    '/urlinfo/1/(.+?):(\d+)/(.+)', 'lookup'
)

class lookup: 
    def GET(self, hostname, port, original_path_and_query_string): 
        print hostname + " " + port + original_path_and_query_string
        return 1
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()



#	curl http://urlinfo.com/{hostname_and_port}/{original_path_and_query_string} 


