import sqlite3
import praw
import sys

r = praw.Reddit(user_agent="RedditLinks bot")
popSubReds = r.get_popular_subreddits(limit=10)
frontPageReds = r.get_front_page(limit=20)
techSubRed = r.get_subreddit('technology').get_hot(limit=20)
results = [a for a in popSubReds]
results1 = [b for b in frontPageReds]
results2 = [c for c in techSubRed]
res = []
res1 = []
res2 = []
#print dir(results[0])
for item in results:
	res.append({'title': item.title, 'link' : item.url})
for item in results1:
	res1.append({'title': item.title, 'link' : item.url})
for item in results2:
	res2.append({'title': item.title, 'link' : item.permalink})
#print(res)
conn = sqlite3.connect('RLinks.db')
with conn:
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS links")
	cur.execute("CREATE TABLE links(Id INT, Title TEXT,Link TEXT)")
	for i in range(len(res)):
		cur.execute("INSERT INTO links VALUES (?,?,?)", (i, res[i]['title'], res[i]['link']))

	#def printDb(someTable): #prints out db for testing
	#	cur.execute("SELECT * FROM someTable")
	#	rows = cur.fetchall()
	#	for row in rows:
	#		print row
	#printDb(links)

	cur.execute("DROP TABLE IF EXISTS links1")
	cur.execute("CREATE TABLE links1(Id INT, Title TEXT, Link TEXT)")
	for i in range(len(res1)):
		cur.execute("INSERT INTO links1 VALUES (?,?,?)",(i,res1[i]['title'],res1[i]['link']))

	cur.execute("DROP TABLE IF EXISTS links2")
	cur.execute("CREATE TABLE links2(Id INT, Title TEXT, Link TEXT)")
	for i in range(len(res2)):
		cur.execute("INSERT INTO links2 VALUES (?,?,?)",(i,res2[i]['title'],res2[i]['link']))

	cur.execute("SELECT * FROM links1")
	rows = cur.fetchall()
	for row in rows:
		print row
