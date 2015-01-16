This repository contains 8,067 tweets that used the #FergusonSyllabus tag between August 17th 2014 and January 7th, 2015. The data was collected with [twarc](http://github.com/edsu/twarc).

Twitter's [Terms of Service](https://dev.twitter.com/overview/terms/policy#6._Be_a_Good_Partner_to_Twitter) do not allow sharing the original JSON data retrieved from Twitter's API. But they do allow the Tweet IDs to be shared, as well as a derivative CSV file (if less than 50,000 tweets). You can find tweet-ids.txt and tweets.csv here in this repository.

If you would like to *hydrate* the Tweet IDs you can use twarc to pull down the
JSON for the tweets:

    pip install twarc
    twarc --hydrate tweet-ids.txt > tweets.json

You can also find some scripts we used for analyzing the data here. You will
need the original JSON data to run them.
