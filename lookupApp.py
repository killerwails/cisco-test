import web
import re
import MySQLdb

db = web.database(
    dbn='mysql',
    host='127.0.0.1',
    user='lookupService',
    pw='q8776G~2BYf67',
    db='cisco',
)


urls = (
    '/urlinfo/1/(.+?):(\d+)/(.+)', 'lookup'
)

class lookup: 
    def GET(self, hostname, port, original_path_and_query_string): 
        from pprint import pprint
        vars = dict(hostname=hostname,port=port,url=original_path_and_query_string+"?"+ web.ctx.environ['QUERY_STRING'])
        results = db.query('select count(*) as matches from mockData where hostname=$hostname and port=$port and url=$url', vars=vars)
        matches = results[0].matches
#        print env['QUERY_STRING']
        return matches

if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()



#	curl http://urlinfo.com/{hostname_and_port}/{original_path_and_query_string} 


