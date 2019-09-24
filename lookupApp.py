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

success_msg = "DANGEROUS\n"
fail_msg = "OK\n"

def getUrl(original_path_and_query_string): 
    if web.ctx.env.get('QUERY_STRING'):
        return original_path_and_query_string+"?"+ web.ctx.environ['QUERY_STRING']
    else: 
        return original_path_and_query_string

def askDB(hostname,port,url):
        vars = dict(hostname=hostname,port=port,url=url)
        results = db.query('select count(*) as matches from mockData where hostname=$hostname and port=$port and url=$url', vars=vars)
        matches = results[0].matches
        return matches

class lookup: 
    def GET(self, hostname, port, original_path_and_query_string): 
        url = getUrl(original_path_and_query_string)
        if askDB(hostname,port,url):
        	return success_msg
        else: 
        	return fail_msg

if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()



#	curl http://urlinfo.com/{hostname_and_port}/{original_path_and_query_string} 


