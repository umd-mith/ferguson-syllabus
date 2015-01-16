This repository contains 8,067 tweets that used the #FergusonSyllabus tag 
between August 17th 2014 and January 7th, 2015. The data was collected with
[twarc](http://github.com/edsu/twarc). Twitter's Terms of Service do not allow
sharing the original JSON data retrieved by twarc, but the Tweet IDs are
included, as well as a derivative CSV file.

If you would like to *hydrate* the Tweet IDs you can use twarc to pull down the
JSON for the tweets:

    pip install twarc
    twarc --hydrate tweet-ids.txt > tweets.json

You can also find some scripts we used for analyzing the data here.
