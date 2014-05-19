#Database code
#list1 = []
#list1.append({1:"one"})
#list1.append({2:"two"})
#if __name__ == "__main__":
#	print(list1)
#	#print(Second item in list is: %(two)s %list1[1])
#	print ("the first number is " + list1[0][1] )
import sqlite3
import praw
import sys

r = praw.Reddit(user_agent="TopRedditLinks")
submissions = r.get_subreddit("technology").get_hot(limit=5)
results = [a for a in submissions]
res = []
for item in results:
	res.append({'title': item.title, 'link' : item.permalink})
#print(res)
conn = sqlite3.connect('example.db')
with conn:
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS links")
	cur.execute("CREATE TABLE links(Id INT, Title TEXT,Link TEXT)")
	for i in range(len(res)):
		cur.execute("INSERT INTO links VALUES (?,?,?)", (i, res[i]['title'], res[i]['link']))
	#sqlite> .mode column
	#sqlite> .headers on
	#sqlite> SELECT * FROM links;
	cur.execute("SELECT * FROM links")
	rows = cur.fetchall()
	for row in rows:
		print row