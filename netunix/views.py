
from datetime import *


def dotnet_unix(unix=None, dotnet=None, real_date=None):
	if(unix, dotnet, real_date is None):
		dotnet = datetime(1,1,1)
		g = datetime.now()
		unix = g - dotnet
		dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
		return dotnettimestamp
	elif(real_date):
		dotnet = datetime(1,1,1)
		f = "%d/%m/%Y %H:%M:%S"
		times = datetime.strptime(real_date, f)
		unix = times - dotnet
		dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
		return dotnettimestamp
# Create your views here.
