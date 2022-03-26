# API Deployment

+ *In this app I fully deploy an API using the Django REST Framework, Docker as an image container, and ElephantSQL for the database using an AWS EC2 server.*

## Feature Tasks and Requirements

### Create a CookieStand App

+ The CookieStand model must contain
  + location = models.CharField(max_length=256)
  + owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
  + description = models.TextField(blank=True)
  + hourly_sales = models.JSONField(default=list, null=True)
  + minimum_customers_per_hour = models.IntegerField(default=0)
  + maximum_customers_per_hour = models.IntegerField(default=0)
  + average_cookies_per_sale = models.FloatField(default=0)
+ Update str method to return the stand’s location.

### Database Deployment Requirements

+ Database hosted by ElephantSQL

### Deployed URLs

+ **Running Server:** N/A
+ **Running Clients:** N/A

### Pull Request

+ [cookie-stand-api/pull/1](URL 'https://github.com/micgreene/cookie-stand-api/pull/1')

### README

+ [README.md](URL 'https://github.com/micgreene/cookie-stand-api/blob/master/README.md')
