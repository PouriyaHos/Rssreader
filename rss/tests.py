from django.test import TestCase

from django.urls import reverse

from rss.models import Feed

import json

class RssIndexViewTests(TestCase):
    def test_no_feed(self):
        pass

    def test_user_feed(self):
        pass

def test_no_feed(self):
    response = self.client.get(reverse("index"))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["feed"], None)

def test_user_feed(self):
    response = self.client.get(reverse("index") + "?url=http://www.24sata.hr/feeds/aktualno.xml")

    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(response.context["feed"], None)




class RssFeedModelTests(TestCase):
    
    def setUp(self):
        Feed.objects.create(
        url="http://www.24sata.hr/feeds/aktualno.xml"
    )

    def test_model_has_url(self):
        django_feed = Feed.objects.get(
        url="http://www.24sata.hr/feeds/aktualno.xml"
    )

        self.assertEqual(
        django_feed.url,
        "http://www.24sata.hr/feeds/aktualno.xml"
    )



class RssRestFeedsViewTests(TestCase):

    def test_create_feed(self):
        url = "http://www.24sata.hr/feeds/aktualno.xml"
        json_data = json.dumps({ "url": url })

        response = self.client.post(
            reverse("rest-feeds"),
            json_data,
            content_type="application/json"
        )

        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 201)
        self.assertQuerysetEqual(
            feeds,
            ["<Feed '{}'>".format(url)]
        )

    def test_get_feeds(self):
        url = "http://www.24sata.hr/feeds/aktualno.xml"

        Feed.objects.create(
            url=url
        )

        response = self.client.get(reverse('rest-feeds'))
        feed = response.json()[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(feed["url"], url)

    def test_update_feed(self):
        url = "http://www.24sata.hr/feeds/aktualno.xml"
        new_url = "https://utan.io/?feed=rss2"

        Feed.objects.create(
            url=url
        )

        json_data = json.dumps({
            "url": new_url
        })

        response = self.client.put(
            "/rss/feeds/1/",
            json_data,
            content_type="application/json"
        )


        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            feeds,
            ["<Feed '{}'>".format(new_url)]
        )

    def test_delete_feed(self):
        Feed.objects.create(
            url="http://www.24sata.hr/feeds/aktualno.xml"
        )

        response = self.client.delete("/rss/feeds/1/")

        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            feeds,
            []
        )

class RssRestItemsViewTests(TestCase):

    def test_get_items(self):
        Feed.objects.create(
            url="http://www.24sata.hr/feeds/aktualno.xml"
        )

        response = self.client.get(reverse("rest-items"))

        self.assertEqual(response.status_code, 200)





