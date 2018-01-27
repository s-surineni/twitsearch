# Twitsearch

The twitsearch app can be used to search recent trending tweets.

Here are the steps to use the twitsearch. 
Search tweets by tweet text: trending/search_tweets?text=<text>
Ex: trending/search_tweets?text=shri

Search tweets by screen name: trending/search_tweets?name=<screen name>
Ex: trending/search_tweets?name=ipraypatel

You can also sort the search results.
To combine search with sort by date: trending/search_tweets?text=<tweet text>&sortBy=created_at_in_sec
Ex: trending/search_tweets?text=shri&sortBy=created_at_in_sec

You can also search tweets by username or screen name.
To get all tweets whose username start with **Ja**: trending/search_tweets?textSearch=user_name&textSearch=Ja&textSearch=starts with

To get all tweets whose username ends with **33**: trending/search_tweets?textSearch=user_name&textSearch=33&textSearch=ends with

To get all tweets whose username contains **in**: trending/search_tweets?textSearch=user_name&textSearch=in&textSearch=contains

Just replace user_name with screen_name to do the previous 3 searches with screen_name.

To search tweets in a date range use: localhost:8000/trending/search_tweets?date=2018-01-27&date=2018-01-30

To search tweets whose retweet count is less than 100: trending/search_tweets?retweetCount=100&values=lte

To search tweets whose retweet count is greater than 100: trending/search_tweets?retweetCount=100&values=gte

