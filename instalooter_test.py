from instalooter.looters import ProfileLooter
import datetime
import dateutil.relativedelta

# instalooter_test downloads videos posted by postleg__ in the last month

# Instanciate 
looter = ProfileLooter("postleg__", videos_only=True, template="{id}-{username}-{width}-{height}")
looter.login("bigshaq6bih", "mmm12345")

today = datetime.date.today()
thismonth = (today, today - dateutil.relativedelta.relativedelta(days=28))

looter.download('./Memes_December_4', media_count=50, timeframe=thismonth)